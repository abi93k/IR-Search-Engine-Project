#!/usr/bin/env python
from __future__ import print_function
from sys import argv
import re
import json
import simplejson

removeChars = ["(",")", "#",":", "-", "!"]
regexPatterns = ["RT","@.*","htt.*"]
tweets = []
def processTweet(text):
    global removeChars, regexPatterns
    line = text.split()
    for i in range(0,len(line)):
	line[i]
	for pattern in regexPatterns:
	    if re.match(pattern,line[i]):
		line[i] = ''
		continue
	for ch in removeChars:
	    line[i] = line[i].replace(ch,'')
    return ' '.join(line).strip()

def writeToFile():
    global tweets
    filename = argv[1].split('.')[0] +"_modified.json"
    try:
	jsondata = simplejson.dumps(tweets, indent=4, skipkeys=True, sort_keys=True)
	fd = open(filename, 'w')
	fd.write(jsondata)
	fd.close()
    except:
	print('ERROR writing',filename)
	pass

def main():
    global tweets
    text = open(argv[1],'r').read()
    text = json.loads(text)
    for twt in text:
	twt['topic'] = argv[2].strip()
	if twt.get('text_en'):
	    twt['text_en_modified'] = processTweet(twt['text_en'])
	tweets.append(twt)
	writeToFile()

if __name__ == '__main__':
 	main()
