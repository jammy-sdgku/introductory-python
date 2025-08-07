#if else statements. Execute logic instructions if the condition is correct. 
# we can catch with if else statements the errors in the code and execute the logic instructions if the condition is correct.
#comparative operators: < less than, > greater than, <= less than or equal to, >= greater than or equal to, == equal, != not equal to

age= 106

if age < 100:   
    if age < 18:
        print("You are a child")
    else:
        print("You are a young person")
elif age ==100:  #else if statement
    print("You are an old fart")
else:
    print("You are a dinosaur")


#remember that python is case sensitive.

x='Hello'
y='hello'

if x==y:
    print("They are equal")
else:
    print("They are not equal")
    
    
# Write Python code that evaluates if a is greater than b and assign to result variable
a = 5
b = 3

result = True

# Assign the opposite of 'result'
inverse_result = False

