#!/usr/bin/env python3

# return_text_value() function
# Author ID: [your_seneca_id]

def return_text_value():
    # Return a string value that matches the test expectations
    return "Good Morning Terry"

# return_number_value() function

def return_number_value():
    # Return a number value that matches the test expectations
    return 15

# print_out_text() function
def print_out_text():
    # Call return_text_value() and print its result
    print(return_text_value())

# Main Program

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
    print_out_text()
