#! /usr/bin/python
# coding=utf-8

import sys, os.path

file_name = sys.argv[1]

with open(file_name, 'r') as text_file:
	contents = text_file.read()

with open(file_name, 'w') as text_file:
	base_name = os.path.splitext(file_name)[0]
	text_file.write(base_name + '\n\n' + contents)
