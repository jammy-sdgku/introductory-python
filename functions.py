#functions is a block of code which only runs when it is called. 
# We can pass data, known parameters and the function can return data as a result.

#functions without parameters
def greet():
    print("Hello, welcome to the program!") 
    
#calling the function
greet()
    
#functions with parameters
def greet_user(name):   
    print("Hello, " + name + "! Welcome to the program!")
    
#calling the function with an argument
greet_user("Alice")

def print_full_name(first_name, last_name):
    print(f"The full name is {first_name} {last_name}.")
    
#calling the function with two arguments
print_full_name("John", "Doe")

#functions that return values
def add_numbers(a, b):
    return a + b

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

#calling the function and storing the result
get_full_name_result = get_full_name("Jane", "Smith")

print (get_full_name_result)

#Challenge 
def subtract(a, b):
    return a - b
result = subtract(10, 3)
print(f"The result equals: {result}")


   
