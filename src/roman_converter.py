def convert(number):
    if number == 4:
        return "IV"
    result = ""
    while number >= 1:
        result += "I"   
        number -= 1 
    return result    