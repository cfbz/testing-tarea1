def convert(number):
    if number == 4:
        return "IV"
    
    result = ""

    if number >= 10:
        result += "X"
        number -= 10

    if number == 9:
        result+= "IX"
        number -= 9

    if number >= 5:
        result += "V"
        number -= 5


    
    while number >= 1:
        result += "I"   
        number -= 1 
    return result    