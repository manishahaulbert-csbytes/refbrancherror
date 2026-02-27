

import os
import sys

#define a function
def random_function(param1, param2):
    """This function prints parameters but has code quality issues"""
    unused_variable = "this is unused"  # S1481: Unused variable
    print(f"Parameter 1: {param1}")
    print(f"Parameter 2: {param2}")
    return param1 + param2  # Return something

def main():
    some_variable = "Hello, World!"
    some_random_number = 42
    random_function(some_variable, some_random_number)
    random_function("Another string", 3.14)
    print("This is a random print statement.")
    # TODO: This is a TODO comment that should be flagged
    
    # Some code smells
    if True:  # S1940: Boolean literals should not be redundant 
        pass
    
    x = 1
    if x == 1:  # Duplicate condition
        print("x is 1")
    elif x == 1:  # S1862: Duplicated conditions
        print("x is still 1")

if __name__ == "__main__":
    main()
