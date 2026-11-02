from pathlib import Path
import shutil
import os
import time

#nicholas chapman-miller

#program to organize directory into these categories:

#Folder	   || File Extensions
#----------||----------------------
#Images	   || .jpg .jpeg .png .gif
#Documents || .pdf .txt .docx
#Music     || .mp3 .wav
#Videos    || .mp4 .mov
#Other     || everything else

#####################################


#function for picking folder to organize
def getDownloadsFolders():

    path = Path.home() / "Downloads"

    #filter for subdirectories aka folders 
    folders = [f for f in path.iterdir() if f.is_dir()]

    #sort most recent first
    folders.sort(key = os.path.getmtime, reverse = True )

    folderList = list(folders)

    #return top 10 in list
    return folderList[:10]



#function to get folder path from the users choice
def getFolderPath(userChoice, downloadsFolders):
    
    index = int(userChoice) -1

    if 0 <= index < len(downloadsFolders):
        return downloadsFolders[index].absolute()
    return None


#function to get category based on file format
def getFileCategory(file):
    
    extension = file.suffix.lower()

    for category, extensions in fileCategories.items():

        if extension in extensions:
            return category
    
    return "Other"


#function to organize folder with file extension based categories
def organizeFolder(folderPath):

    #create folders for all categories
    for category in fileCategories:

        categoryPath = folderPath / category

        categoryPath.mkdir(exist_ok = True)

    #loop through selected directory
    for file in folderPath.iterdir():
        
        #skip folders
        if file.is_dir():
            continue

        #get category
        category = getFileCategory(file)

        
        newPath = folderPath / category / file.name

        #put file into folder matching the category
        shutil.move(str(file), str(newPath))

        #show user the change
        print(f"Moved {file.name} -> {category}")




#dictionary for file formats/categories
fileCategories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents" : [".pdf", ".txt", ".docx"],
    "Music" : [".mp3", ".wav"],
    "Videos" : [".mp4", ".mov"],
    "Other" : []
    }




mainUserC = "y"
while(mainUserC.lower() == "y"):

    downloadsFolders = getDownloadsFolders()

    print("\n\n\n*********************************")
    print("*   Welcome to Folder Sorter\t*")
    print("*********************************\n")



    print("Most Recent Folders In Downloads : ")

    #folders list / menu
    cnt = 0
    for folder in downloadsFolders:
        cnt = cnt + 1
        print(f"{cnt}. {folder.name}")
    print("*********************************\n")
    userFolderC = input("What folder do you want to organize? (1-10) : ")

    folderPath = getFolderPath(userFolderC, downloadsFolders)


    if folderPath is not None:

        print(f"\nOrganizing: {folderPath.name}\n")

        time.sleep(2.5)

        organizeFolder(folderPath)

        print("\nFolder organization complete !!!")
    else:
        print("Invalid folder selection. 1 - 10 only")

    #prompt user to repeat or end
    mainUserC = input("Would you like to organize another folder? (y / n)\n\n")

print("! ! ! T H A N K  Y O U ! ! !")