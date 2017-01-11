#!/usr/bin/env python2

# use nice python3 printyness
from __future__ import print_function

from sys import stdin
from ast import literal_eval


def evalidate(input):
	"""
	Evaluate input and return None if type of input is not acceptable; else return input with evaluated type
	"""
	valid_types = {
		int,
		float,
		str,
		tuple,
		list,
		bool
	}
		
	
        # try to evaluate input
        try:
	    evil_input = literal_eval(input)
        except (ValueError, SyntaxError):
            evil_input = str(input)

	if type(evil_input) in valid_types:
	    return evil_input
        else:
            print('Input of type', type(evil_input), 'is not acceptable. Please enter something else.')

def prompt(promptstr):
    print(promptstr, end=": ")
    return stdin.readline().strip('\r\n')

def get_inputs():
	"""
	Prompt user and collect input
	"""
	input_a = prompt('Enter a value')
	input_b = prompt('Enter another value')
	
	return evalidate(input_a), evalidate(input_b)

def additionify(a, b):
	return a + b


def subtractionify(a, b):
        pass

while True:
        a, b = get_inputs()

        if a and b:
            if type(a) == type(b):
                result = additionify(a, b)
                print('Result:', result)
            else:
                print('Types', type(a), 'and', type(b), 'are not the same. Please enter two values of the same type')


