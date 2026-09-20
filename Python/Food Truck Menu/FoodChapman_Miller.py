#nicholas chapman-miller
#Food Truck App

#function to find cost of an item
def findCost(itemNum):

	#match/switch instead of if and elifs
	match itemNum:
		
		case 1:
			return 20.0
		case 2: 
			return 15.0
		case 3:
			return 15.0
		case 4:
			return 20.0
		case 5:
			return 18.0

	
	#if user input does not match menu print error msg

	print("*** NO MATCH. PLEASE TRY AGAIN")
	return -1

#function to display food truck menu
def menu():
	print("*************************************")
	print("*         BILLYS FOOD TRUCK         *")
	print("*         -----------------         *")
	print("*       #1 Wings              $20   *")
	print("*       #2 Chicken Strips     $15   *")
	print("*       #3 Fish Basket        $15   *")
	print("*       #4 Shrimp Po Boy      $20   *")
	print("*       #5 Pork Chop Basket   $18   *")
	print("*         _________________         *")
	print("*************************************")


programChoice = "y"


while(programChoice.lower() == "y"):

	#variables that reset with every customer
	cartCount = 0
	subTot = 0.0
	tax = 0.0
	tip = 0.0
	total = 0.0
	custChoice = "y"


	while(custChoice.lower() == "y"):
		cartCount = cartCount + 1

		menu()
		itemNum = int(input("Enter plate # "+format(cartCount)+": "))

		
		#determine cost of plate ordered
		cost = findCost(itemNum)

		#if user input is not valid function returns -1 so we continue if = -1
		if(cost == -1):
			cartCount = cartCount - 1
			continue

		#if valid add to sub total
		subTot += cost

		#prompt user to add another order or checkout
		custChoice = input("Would you like to add another plate to your order? y/n  \n")

	#calculate tax and total before tip
	tax = subTot * .09
	total = subTot + tax

	#order info before tip
	print("****************************")
	print("        YOUR ORDER        ")
	print("    Subtotal: $"+format(subTot, ".2f"))
	print("    Tax: $"+format(tax, ".2f"))
	print("****************************")
	
	#prompt user for tip
	tipChoice = input("Would you like to tip? y/n \n")

	if(tipChoice.lower() == "y"):
		tip = float(input("Enter tip amount: $"))

		#stop user from subtracting from total with a negative tip
		if(tip > 0):
			#add tip to total if input valid
			total += tip
		else:
			#set tip to 0 if not valid
			tip = 0.0

	#final info for order
	print("****************************")
	print("        YOUR ORDER        ")
	print("    Subtotal: $"+format(subTot, ".2f"))
	print("    Tax: $"+format(tax, ".2f"))
	print("    Tip: $"+format(tip, ".2f"))
	print("    Total: $"+format(total, ".2f"))
	print("****************************")

	print()

	#prompt to continue the loop for another customer
	programChoice = input("Is there another customer? y/n \n")

#thank user after program is done
print("*** THANK YOU ***")

