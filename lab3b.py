#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: twangmo12

def sum_numbers(number1, number2):
    """This function adds number1 and number2 and returns the value"""
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    """This function subtracts number2 from number1 and returns the value"""
    return int(number1) - int(number2)

def multiply_numbers(number1, number2):
    """This function multiplies number1 and number2 and returns the value"""
    return int(number1) * int(number2)

if __name__ == '__main__':
    print(sum_numbers(10, 5))       # Should return 15
    print(subtract_numbers(10, 5))  # Should return 5
    print(multiply_numbers(10, 5))  # Should return 50
