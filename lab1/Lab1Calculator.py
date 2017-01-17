#!/usr/bin/env python2

# use nice python3 printyness
from __future__ import print_function

from sys import stdin
from ast import literal_eval


def interpret(input_string):
    # try to evaluate input to determine type, fall back to str if nothing works
    try:
        evil_input = literal_eval(input_string)
    except (ValueError, SyntaxError):
        evil_input = str(input_string)
        
    return evil_input

def get_input(promptstr, valid_types=None, valid_values=None):
    while True:
        value = interpret(prompt(promptstr))
        
        if valid_types is None or type(value) in valid_types:
            if valid_values is None or value in valid_values:
                return value
            else:
                print('Input not one of', valid_values, '. Please enter one of these.')
        else:
            print('Input of type', type(value), 'is not one of', valid_types, '. Please enter one of these.')

def prompt(promptstr):
    print(promptstr, end=": ")
    return stdin.readline().strip('\r\n')

def get_inputs():
    """
    Prompt user and collect input
    """
    
    op = get_input(
            "In the spirit of Reverse Polish Style..\nPlease specify an operation (a[dd]|s[ubtract])",
            valid_types=[str],
            valid_values=["a", "add", "s", "subtract"]
        )

    if op is not None:
        inputs = []
        for i, promptstr in enumerate(['Enter a value', 'Enter another value']):
            # get an input of correct type depending on selected operation
            inputs.append(
                get_input(
                    promptstr,
                    valid_types=[int, float, str, tuple, list, bool] if op.startswith('a') else [int, float]
                ))
        
    return op, inputs[0], inputs[1]

while True:
        op, a, b = get_inputs()

        if type(a) == type(b):
            if op.startswith('a'):
                result = a + b
            else:
                result = a - b
            print('Result:', result)
        else:
            print('Types', type(a), 'and', type(b), 'are not the same. Please enter two values of the same type')
