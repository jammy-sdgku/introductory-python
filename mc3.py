#challenge: Compare two values

# This code takes two integer inputs.
x=int(input("Enter your first value: "))
y=int(input("Enter your second value: "))

#function to compare two values
def compare_values(x, y):
    if x<0 or y<0:
        print("Please enter only positive values")
    else:
        if x==y:
            print("They are the same")
        else:
            print("They are different")

# Call the function to compare the values        
compare_values(x, y)