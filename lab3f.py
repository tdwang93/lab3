#!/usr/bin/env python3

import os

# Create a global list to hold items
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(lst):
    """Adds the next sequential number to the provided list."""
    next_item = max(lst) + 1  # Get the next number
    lst.append(next_item)      # Append it to the list
    return lst

def remove_items_from_list(lst, items):
    """Removes specified items from the provided list."""
    for item in items:
        if item in lst:
            lst.remove(item)
    return lst

if __name__ == '__main__':
    # You can test your functions here or call unittest.main()
    print("Current list:", my_list)
    add_item_to_list(my_list)
    print("After adding an item:", my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print("After removing items:", my_list)
