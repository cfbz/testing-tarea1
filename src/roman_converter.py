def convert(number):
 
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

    if number == 4:
        result+= "IV"
        number -= 4

    
    while number >= 1:
        result += "I"   
        number -= 1 
    return result    