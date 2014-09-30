#!/usr/bin/python
import re
def ABCheck(str):
	x = re.search(r"a.{3}b", str, flags=0)
	return x != None
