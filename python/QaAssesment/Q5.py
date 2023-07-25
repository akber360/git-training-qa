def five(inputnum):
    if inputnum == 0:
        return 1
    else:
        return inputnum * five(inputnum - 1)





enterint = int(input("Please enter your number "))
inputnum = five(enterint)
print (inputnum)
