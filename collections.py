#python collections
#group of data elements that allow us to store multiple values in a single variable.
#list, tuple, set, dictionary

#list: ordered, changeable, allows duplicate values
#defined with square brackets []
print(f"---------------------Lists---------------------")

fruits= ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'banana']
print(fruits)

print(fruits[1]) #accessing an element

print(fruits[-1]) #accessing the last element

print(fruits[2:5]) #accessing a range of elements

print(fruits[2:]) #accessing from the 2nd element to the end

print(fruits[:4]) #accessing from the beginning to the 4th element (not included)

fruits.append('mango') #adding an element to the end of the list
print(fruits)

fruits.pop(5) #removing an element by index
print(f"using pop to remove element: {fruits}")   

fruits.insert(2, 'grape') #inserting an element at a specific index
print(f"using insert to add element at point: {fruits}")

#----------------------------------------------------------------------------------
#tuple: ordered, unchangeable, allows duplicate values
#defined with parentheses ()
print(f"---------------------Tuples---------------------")

thistuple= ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'banana')
print(f"Printing the tuple: {thistuple}") #printing the whole tuple

print(thistuple[1]) #accessing an element

print(thistuple[-1]) #accessing the last element

print(thistuple[2:5]) #accessing a range of elements. last number is not included

#----------------------------------------------------------------------------------
#set: unordered, unindexed, unchangeable, no duplicate values
#defined with curly braces {}
print(f"---------------------Sets---------------------")

thisset= {'apple', 'banana', 'cherry', 'orange', 'kiwi'}
print(thisset)
#accessing elements in a set is not possible because sets are unordered and unindexed

#------------------------------------------------------------------------------------
#dictionary: preserves order, changeable, no duplicate values
#defined with curly braces {} and key:value pairs
print(f"---------------------Dictionary---------------")

thisdict= {'brand': 'Ford', 
           'model': 'Mustang', 
           'year': 1964,
           'colors': ['orange', 'blue', 'green']
           }
             
print(f"Printing the dictionary:  {thisdict}") #printing the whole dictionary


print(f"printing brands: {thisdict['brand']}") #accessing an element

print(thisdict.get('model')) #accessing an element with get method

thisdict['year']= 2020 #changing the value of an element
print(thisdict)

thisdict['color']= 'red' #adding an element
print(thisdict)

thisdict.pop('model') #removing an element
print(thisdict)

print(len(thisdict)) #length of the dictionary 

print(f"accessing the items using get method: {thisdict.get('colors')}") #accessing the value of a key

thisdict.update({'engine': 'V8'}) #adding a new key-value pair
print(f"adding a new key-value pair: {thisdict}")   

print(f"-----------Looping through a dictionary------------")

#looping through a dictionary
for x in thisdict:
    print(x) #prints the keys   
    
for x in thisdict:
    print(thisdict[x]) #prints the values
    
for x in thisdict.values():
    print(x) #prints the values
    
for x, y in thisdict.items():
    print(x, y) #prints the key and value pairs
    

