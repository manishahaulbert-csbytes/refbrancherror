#define a function
def hello_world():
    print("Hello, World!")

def random_function(param1, param2):
    print(f"Parameter 1: {param1}")
    print(f"Parameter 2: {param2}")
    int c=param1<>param2    # checking if the parameters are not equal and assigning the result to variable c    
    return param1<>param2 #checking if the parameters are not equal


def main():
    some_variable = "Hello, World!"
    some_random_number = 42
    random_function(some_variable, some_random_number)
    hello_world()
    print("This is a random print statement.")


if __name__ == "__main__":    
    main()
    