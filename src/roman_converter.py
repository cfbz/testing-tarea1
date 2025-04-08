def convert(number):
 
    result = ""

    while number >= 500:
        result += "D"
        number -= 500

    while number >= 100:
        result += "C"
        number -= 100

    while number >= 50:
        result += "L"
        number -= 50

    while number >= 10:
        result += "X"
        number -= 10

    while number == 9:
        result+= "IX"
        number -= 9

    while number >= 5:
        result += "V"
        number -= 5

    while number == 4:
        result+= "IV"
        number -= 4

    
    while number >= 1:
        result += "I"   
        number -= 1 
    return result    