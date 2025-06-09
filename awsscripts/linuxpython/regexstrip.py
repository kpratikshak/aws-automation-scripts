import re 

def strip(text):
    """
    """
    stripStartRegex = re.compile(r"(^\s*))
    stripEndRegex = re.compile(r"(\s*$)")
    
    stripStartRegex = re.compile(r"(^\s*)")   
    stripEndRegex = re.compile(r"(\s*$)")   
    
    textStartStripped = stripStartRegex.sub("",text)                       
    textStartStripped = stripEndRegex.sub("",textStartStripped)
    
    return textStartStripped
    
    if __name__ =="__main__":
        text = "test ffs"
        print(strip(text))