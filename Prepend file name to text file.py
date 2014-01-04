#! /usr/bin/python
# coding=utf-8

import sys, os.path

def prependName(file_path):
	with open(file_path, 'r') as text_file:
		contents = text_file.read()
	
	with open(file_path, 'w') as text_file:
		file_name = os.path.basename(file_path)
		base_name = os.path.splitext(file_name)[0]
		text_file.write(base_name + '\n\n' + contents)

for path in sys.argv[1:]:
	prependName(path)
