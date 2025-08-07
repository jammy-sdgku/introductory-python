#Calculate the total product cart list and calculate the average of the product cart. 

#Create a function called total that receives a list as a parameter and returns the total value.
#Create an average function that receives two parameters: total and length and return the average value.
#Print the total and average variables using f formatting that says "The total is: {total} and the average is: {average}"

product_cart=[100,200,300,400,500]

def get_total(product_cart):
    total = 0
    for product in product_cart:
        total = total + product   
    return total 

def get_average(total, length):
    return total / length

total= get_total(product_cart)
avg= get_average(total, len(product_cart))

print(f" The total is: {total} and average is: {avg} ")
    