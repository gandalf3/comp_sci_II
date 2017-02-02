#!/usr/bin/env python2

# use nice python3 printyness
from __future__ import print_function

from sys import stdin
from ast import literal_eval

def prompt(promptstr):
    """
    Print promptstr and read next line from stdin
    """
    print(promptstr, end=": ")
    return stdin.readline().strip('\r\n')

def interpret(input_string):
    """
    Return typed version of input string
    """
    
    # try to evaluate input to determine type, fall back to str if nothing works
    try:
        evil_input = literal_eval(input_string)
    except (ValueError, SyntaxError):
        evil_input = str(input_string)
        
    return evil_input

def get_input(promptstr, valid_types=None, valid_values=None):
    """
    Repeatedly prompt user with promptstr until a response c
    """
    
    while True:
        value = interpret(prompt(promptstr))
        
        if valid_types is None or type(value) in valid_types:
            if valid_values is None or value in valid_values:
                return value
            else:
                print('Input not one of', valid_values, '. Please enter one of these.')
        else:
            print('Input of type', type(value), 'is not one of', valid_types, '. Please enter one of these.')

def get_inputs():
    """
    Collect all user values needed to perform calculation
    """
    
    op = get_input(
            "In the spirit of Reverse Reverse Polish Style..\nPlease specify an operation (a[dd]|s[ubtract])",
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
            if type(a) is bool:
                result = a and b
            print('Result:', result)
        else:
            print('Types', type(a), 'and', type(b), 'are not the same. Please enter two values of the same type')
