import os 
import re 

def regexSearch(regexStr,folderPath):
    """
    """
    if not os.path.isdir(folderPath):
        return "Input a directory path"
    
    userRegex = re.compile(regex)
    
    for filename in os.listdir(folderPath):
        
        if filename in os.listdir(folderPath):
            with open(filename) as file:
                
                for line in file:
                    mo = userRegex.search(line)
                    if mo:
                        print(line,end="")
                        
    if __name__== "__main__":
        regex = input("Enter regex:")
        regexSearch(regex,".")