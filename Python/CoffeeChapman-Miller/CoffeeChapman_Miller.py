#Nicholas Chapman-Miller CPT-127-A01H
#this program calculates the total of an order for west end coffee roasters company
#the program takes in user name and order weight to calculate cost

import time

#get user name
name = input('Please enter your name \n')

#get order weight
weight = input('Enter weight of your order \n')


#calculate how much the coffee costs according to inputted weight
itemTot = float(weight) * 10.5

#calculate how much shipping costs according to inputted weight
shipping = (float(weight) * .86) + 1.5

#calculate subtotal
subTot = itemTot + shipping

#calculate tax
tax = subTot * .07

#calculate total
total = subTot + tax

#display costs with user name
print(name +"'s order totals: ")
print("***************************")
print("Coffee Price: $"+ format(itemTot,",.2f"))
print("Shipping Fee: $"+ format(shipping, ",.2f"))
print("Subtotal: $"+ format(subTot,",.2f"))
print("Tax: $"+ format( tax,",.2f"))
print("Total: $"+format(total, ",.2f"))

#pause before close
time.sleep(3)