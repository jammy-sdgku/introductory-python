#keyword continue
#continue is used to skip the current iteration of a loop and continue with the next iteration

#keyword break
#break is used to exit a loop prematurely

#keyword pass
#pass is a null operation; it is used when a statement is required syntactically but no action is desired


print(f"-----------Looping through a dictionary------------")

thisdict= {'brand': 'Ford', 
           'model': 'Mustang', 
           'year': 1964,
           'colors': ['orange', 'blue', 'green']
           }

print(f"-----------Looping through a dictionary for the keys------------")

#looping through a dictionary
for x in thisdict:
    print(x) #prints the keys   
    
print(f"-----------Looping through a dictionary for values------------")
    
for x in thisdict:
    print(thisdict[x]) #prints the values


    
for x in thisdict.values():
    print(x) #prints the values
    
print(f"-----------Looping through a dictionary for key/value pairs------------")   
    
for x, y in thisdict.items():
    print(x, y) #prints the key and value pairs
    

print(f"-----------Looping through a list------------")
#looping through a list
fruits= ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'banana']

for i in fruits:
    print(i) #prints each element in the list

print(f"-----------Looping through a list to get index and value ------------")
    
index=0
for i in fruits:
    print(index)
    print(i) #prints each element in the list with index
    index = index+1    
    
print(f"-----------Looping through a string ------------")

for x in "banana":
    print(x) #prints each character in the string   
    
    
print(f"-----------Looping using range ------------")

for number in range(0,11):
    print(number) #prints numbers from 0 to 10
    
 #looping through a range of numbers. start value, end value, increment value   
for number in range(0,1):
    print(fruits) #prints fruits list  

#Create a function called total that receives a list as a parameter and returns the total value.
print(f"-----------Looping function to return total value ------------")   
product_cart=[100,200,300,400,500]

def get_total(product_cart):
    total = 0
    for product in product_cart:
        total = total + product   
    return total 
print(get_total(product_cart)) #prints the total value of the product cart


print(f"-----------built-in sum to return total value ------------")  
def total(product_cart):
    return sum(product_cart) #using built-in sum function to get total value    
print(total(product_cart)) #prints the total value of the product cart using built-in sum function

