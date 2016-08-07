#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
dict = {'3':0, '4':1, '5':2, '6':3, '7':4, '8':5, '9':6, '10':7, 'J':8, 'Q':9, 'K':10, 'A':11, '2':12, 'joker':13, 'JOKER':14}
for line in sys.stdin:
	first = line.split('-')[0]
	second = line.split('-')[1].strip('\n')
	firstList = first.split(' ')
	secondList = second.split(' ')
	#no 'JOKER' or 'joker'
	if len(firstList) == 2 and (firstList[0] == 'JOKER' or firstList[0] == 'joker'):
		print (firstList[0], firstList[1])
		sys.exit(0)
	if len(secondList) == 2 and (secondList[0] == 'JOKER' or secondList[0] == 'joker'):
		print (secondList[0], secondList[1])
		sys.exit(0)
	#valid
	if len(firstList) == len(secondList):
		if dict[firstList[0]] > dict[secondList[0]]:
			print (' '.join(firstList))
		else:
			print (' '.join(secondList))
		sys.exit(0)
	#invalid or bomb
	else:
		if len(firstList) == 4:
			print (' '.join(firstList))
		elif len(secondList) == 4:
			print (' '.join(secondList))
		else:
			print ('ERROR')
		sys.exit(0)