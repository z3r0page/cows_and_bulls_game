#!/usr/bin/python
'''
Cows and bulls game
'''
__author__ = 'amar sarvepalli'
__email__ = 'errrlog@gmail.com'

import random

def cal_cows(n, i):
	c = 0
	for k in range(0,4):
		if n[k] == i[k]:
			c += 1
	return c

def cal_bulls(n, i):
	b = 0 
	for j in range(0, 4):
		if n[j] in i and n[j] != i[j]:
			b += 1
	return b

def gen_rand():
	num = str(random.randrange(1000, 10000))
	while len(set(num)) != 4:
		num = str(random.randrange(1000, 10000))
	return num

def mail():
	cows = 0
	bulls = 0
	num = gen_rand()

	while True:
		input = raw_input("Enter your 4 digit num: ")
		c = 0
		b = 0

		if num == input: 
			print "You cracked it. Random: %s Input: %s" %(num, input)
			print "Total Cows: ", cows
			print "Total Bulls: ", bulls
			break
		else:
			c = cal_cows(num, input)
			b = cal_bulls(num, input)
			cows += c
			bulls += b

		r = raw_input("Continue: y/n?: ")
		if r != 'y':
			print "Exiting. Random: %s Input: %s" %(num, input)
			print "Cows: ", c
			print "Bulls: ", b
			print "Total Cows: ", cows
			print "Total Bulls: ", bulls
			break
		else:
			print "Cows: ", c
			print "Bulls: ", b
	
if __name__ == "__main__":
	mail()
