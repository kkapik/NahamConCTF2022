#!/usr/bin/env python3

ct = open('out', 'r').read()
flag=''
d= ord(ct[0])-ord('f') #first letter should be 'f' for the flag
for c in ct:
	flag += chr(ord(c) - d)

print(flag)