#nicholas chapman-miller

import requests
from bs4 import BeautifulSoup
import re


scSite = "https://scvotes.gov/elections-statistics/voter-participation/"
baseSite  = "https://www.shiftline.us/reg-stats/"

#dictionary of states that shiftline has states for
supportedStates = [
    "alaska", "arizona", "california", "colorado", "connecticut", "delaware", "district-of-columbia", "florida", "idaho", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "nebraska", "nevada", "new-hampshire","new-jersey", "new-mexico", "new-york", "north-carolina", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-dakota", "utah", "west-virginia", "wyoming"
]

mainUserC = "y"
while(mainUserC.lower() == "y"):

    print("\n\n\n*************************************************")
    print("*   Welcome to Voter Registration Lookup\t*")
    print("*************************************************\n")
    #get state from user
    state = input("Enter a state: ").strip().lower()

    #convert spaces to hyphens for url
    stateURL = state.replace(" ", "-")

    #check if state is supported
    if stateURL not in supportedStates:
        print("This state is not supported by Shiftline.")
    else:
        try:
            scResponse = requests.get(scSite)
            stateSite = baseSite + stateURL
            stateResponse = requests.get(stateSite)

            #check for failed http request
            scResponse.raise_for_status()
            stateResponse.raise_for_status()


            #use beautifulsoup to parse website html
            scSoup = BeautifulSoup(scResponse.text, "html.parser")
            stateSoup = BeautifulSoup(stateResponse.text, "html.parser")

            scTxt = " ".join(scSoup.get_text().split())
            flTxt = " ".join(stateSoup.get_text().split())

            #regex to find total
            scMatch = re.search(
                r"([\d,]+)\s+Current number of registered voters in South Carolina", scTxt
                )


            stateVoters = None

            #find voter reg total in html table
            for row in stateSoup.find_all("tr"):
                cells = row.find_all(["td", "th"])
                rowData = [cell.get_text(strip=True) for cell in cells]

                #2026 row
                if rowData and rowData[0] == "2026":
                    #total is the 10th column
                    stateVoters = rowData[9]
                    break


            #check if sc regex and shiftline state table search worked
            if scMatch and stateVoters is not None:

                scVoters = scMatch.group(1)

                print("*************************************************\n")

                print("The current number of registered voters in South Carolina is "+scVoters+".")
                print("The current number of registered voters in "
                    + state.title() + " is " + stateVoters + ".")


            else:
                print("Could not find voter registration data.")

            print("\n*************************************************\n")
            #prompt user to repeat or end
            mainUserC = input("Would you like to look up another state? (y / n)\n\n")
        #if shiftline or scvotes site doesn't work
        except requests.exceptions.RequestException as error:

            print("There was an error accessing the website:", error)

print("! ! ! T H A N K  Y O U ! ! !")