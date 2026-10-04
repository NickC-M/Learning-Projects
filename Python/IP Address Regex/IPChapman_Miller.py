#nicholas chapman-miller
#IP address regex program

import re
import pyperclip
import time
import sys


print("-------------------------------------")
print("\tWelcome to IP Finder")
print("-------------------------------------")

print("Scanning the text in your clipboard.....\n")
#pause so cmd isn't spammed with ip listed
time.sleep(3)

#take in text that is copied to clipboard
text = pyperclip.paste()

#use regex to put matching text in list
result = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", text)

#exit if result empty aka no ips found
if(len(result) < 1):
    print("NO IP ADDRESSES FOUND SRY :( ")
    time.sleep(2)
    sys.exit()



print("\tIP ADDRESSES FOUND")
print("------------------------------------")

cnt = 1

print("#   ||\t IP")
print("------------------------------------")
#for loop through the list to print each IP neatly
for ip in result:
    #fix misaligned ||
    if(cnt > 9):
        print(format(cnt)+": ||  "+ip)
    else:
        print(format(cnt)+":  ||  "+ip)

    cnt = cnt + 1

print("------------------------------------")
#use length of result var to count how many ips were found
print("Total IP Addresses found: "+format(len(result)))
print("------------------------------------")
print("\n\n T H A N K  Y O U ! ! !")

