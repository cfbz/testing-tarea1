def convert(number):
    if number == 4:
        return "IV"
    
    result = ""
    
    if number >= 5:
        result += "V"
        number -= 5


    
    while number >= 1:
        result += "I"   
        number -= 1 
    return result    