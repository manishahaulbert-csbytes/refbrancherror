#define a function
def hello_world():
    print("Hello, World!")

def random_function(param1, param2):
    print(f"Random function called with parameters: {param1} and {param2}")
    if param2 > 40:
        break
    return param1.upper()

def another_random_function():
    print("This is another random function.")
    return "Random Result"


def main():
    some_variable = "Hello, World!"
    some_random_number = 42
    random_function(some_variable, some_random_number)
    hello_world()
    print("This is a random print statement.")


if __name__ == "__main__":    
    main()