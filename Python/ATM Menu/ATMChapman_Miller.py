#ATM Withdrawal Program
#Nicholas Chapman-Miller

import time

#function to check if user input is valid
def checkInput():
    tenCheck = False

    #ask for user input until it is valid
    while(tenCheck == False):
        wAmt = float(input("Please enter an amount to withdrawal (multiple of 10 only): \n $"))
    
        if(wAmt < 0 or wAmt % 10 != 0): #if user input is not divisble by 10 print msg and repeat prompt

            print("INVALID AMOUNT... PLEASE ENTER A POSITIVE MULTIPLE OF 10. EX: $50, $110\n")
        else:
            tenCheck = True



    
    print("... checking available balance ....")
    #pause to simulate loading for fun  
    time.sleep(2)
    return wAmt



#declare variables
bal = 823.00
wAmt = 0.00
choice = True


#loop so user can withdraw more than once    
while(choice):

    #prompt user
    wAmt = checkInput()

    #if user input is greater than balance print message
    if(wAmt > bal):
        print("Sorry ! You're withdrawal amount of $"+format(wAmt, ",.2f")+" is greater than your balance of $"+format(bal, ",.2f"))


    #if user input is good, withdrawal from balance and display new balance
    elif(bal >= wAmt):
        bal -= wAmt
        print("You have withdrawn $"+format(wAmt,",.2f")+" from your account. You're balance is now $"+format(bal, ",.2f"))


    #ask user if they want to withdraw again and check if user input is "w"
    choice = bool(input("Press W to withdraw again...\n").upper() == "W") 

#display ty messsage and pause before close       
print("*** T H A N K  Y O U ***")
time.sleep(4)



