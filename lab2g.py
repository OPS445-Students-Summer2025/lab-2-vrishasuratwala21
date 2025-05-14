#!/usr/bin/env python3

#Author: Vrisha Suratwala 
#Author id: vvsuratwala@myseneca.ca
#Date created: 2025/05/14

import sys
if len(sys.argv) == 2:
	timer = int(sys.argv[1])
else:
	timer = 3
while timer > 0:
        print(timer)
        timer = timer - 1
print("blast off!")
