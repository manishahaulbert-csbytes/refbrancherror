#define a function
def hello_world():
    print("Hello, World!")

def add_numbers(a, b):
    break # This is a syntax error, but we are ignoring it for this example.
    return a + b
    

def random_function(param1, param2):
    print(f"Random function called with parameters: {param1} and {param2}")
    if param2 > 40:
        break # This is a syntax error, but we are ignoring it for this example.
    return param1.upper()


def main():
    some_variable = "Hello, World!"
    some_random_number = 42
    random_function(some_variable, some_random_number)
    hello_world()
    print("This is a random print statement.")
    add_numbers(5, 10)


if __name__ == "__main__":    
    main()
    