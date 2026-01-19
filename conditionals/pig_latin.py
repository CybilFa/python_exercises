# translate from english to pig-latin
def translate(text):
    vowels = "aeiou"
    if text[0] in vowels or text.startswith("xr") or text.startswith("yt"):
        return text + "ay"
    
    # RULE 2 if starts with consonansts 1 or more move them to end and add ay
    
    
print(translate("apple"))  
print(translate("xray"))    
print(translate("yttria"))

    