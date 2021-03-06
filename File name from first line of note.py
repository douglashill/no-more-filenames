#! /usr/bin/python
# coding=utf-8

# http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python

import sys, os, os.path, re

max_length = 100

def getTitle(file_path):
	with open(file_path) as text_file:
		first_line = text_file.readline()
		title = first_line.rstrip()
		
		# Blacklist: / :
		title = re.sub('[/:]+', '', title)
		title = title.strip('#') # Markdown title marks
		if len(title) > max_length:
			title = title[:max_length]
		title = re.sub('\s{2,}', ' ', title)
		title = title.strip()
		
		return title

def refreshFileName(file_path):
	title = getTitle(file_path)

	# Don’t want to rename new files to .txt, which makes them hard to fine.
	if len(title) == 0:
		return
	
	file_name = os.path.basename(file_path)
	old_base_name = os.path.splitext(file_name)[0]
	extension = os.path.splitext(file_name)[1]

	# Don’t write if the name already matches.
	if old_base_name == title:
		return

	# Add numbers to avoid the same name.
	counter = 1
	while os.path.exists(os.path.join(os.path.dirname(file_path), title + extension)):
		++counter
		title = title + ' ' + str(counter)
	
	os.rename(file_path, os.path.join(os.path.dirname(file_path), title + extension))

for path in sys.argv[1:]:
	refreshFileName(path)
