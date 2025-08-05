print("Hello world from Python!")
print(True)
print(5+3)

x=10
y=20
print(x+y)

first_name = "James"
last_name = "Jones"
age = 30
found= False
print("My name is " + first_name +" "+ last_name + " and I am " + str(age) + " years old.")

print("Did he show up to class? " + str(found))

print(f"My name is {first_name} {last_name} and I am {age} years old.")

#type function helps to identify type of variable 
print(type(first_name))

#casting
#helps us to convert different types of variables
#srt() converts to string
#int() converts to integer
#float() converts to float
print(20+int("20"))
print(20+age)
print(20+float("20.5"))

#input function
#input() function takes input from user
#input() returns a string
name = input("What is your name? ")
print("Hello " + name)
alert = input("Enter an alert message: ")
print("Alert: " + alert)
#input() can also be used to take numbers, but they will be strings

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
print("The sum of the two numbers is: " + str(x+y))