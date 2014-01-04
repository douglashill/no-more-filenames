#! /usr/bin/python
# coding=utf-8

# http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python

import os, os.path, re

max_length = 100

file_name = 'Untitled.txt'

with open(file_name) as text_file:
	first_line = text_file.readline()
	
	# Blacklist: [ ] / \ = + < > : ; " , * .
	# https://forums.dropbox.com/topic.php?id=23023
	title = re.sub('[\[\]/\\=\+<>:;",\*\.]+', '', first_line)
	title = title.strip('#') # Markdown title marks
	if len(title) > max_length:
		title = title[:max_length]
	title = re.sub('\s{2,}', ' ', title)
	title = title.strip()
	print('The title is: “' + title + '”.')

extension = os.path.splitext(file_name)[1]
new_file_name = title + extension
print('The new file name is ' + new_file_name)
os.rename(file_name, new_file_name)
