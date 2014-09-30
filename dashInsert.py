#!/usr/bin/python
import re

def dashInsert(num):
	num_str = str(num)
	num_str = re.sub(r'([13579])([13579])',r'\1-\2',num_str)
	return num_str
