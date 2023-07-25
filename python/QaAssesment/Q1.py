def one (input1, input2):
    if len(input1)>len(input2):
         return input1 
    if len(input2)>len(input1):
        return input2
    if len(input1)==len(input2):
        return input1 + " " + input2
    
input1 = input("please type your first word ")
input2 = input("Please type your second word ")    
result = one(input1, input2)
print (result)