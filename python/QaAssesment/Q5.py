def five(inputnum):
    if inputnum > 0:
        return inputnum * five(inputnum - 1)
    else: 
        inputnum == 0
    return 1




enterint = int(input("Please enter your number "))
inputnum = five(enterint)
print (inputnum)
