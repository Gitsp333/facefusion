import json
from json import JSONDecodeError
from typing import Optional

from facefusion.filesystem import is_file
from facefusion.types import Content


def read_json(json_path : str) -> Optional[Content]:
	if is_file(json_path):
		try:
			if '..' in json_path:
				raise Exception('Invalid file path')
			with open(json_path) as json_file:
				return json.load(json_file)
		except JSONDecodeError:
			pass
	return None


def write_json(json_path : str, content : Content) -> bool:
	if '..' in json_path:
		raise Exception('Invalid file path')
	with open(json_path, 'w') as json_file:
		json.dump(content, json_file, indent = 4)
	return is_file(json_path)
