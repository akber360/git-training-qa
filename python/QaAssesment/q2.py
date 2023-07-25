def two(numb):

     if numb % 3 !=0 and numb % 5 !=0:
        return "null"
     if numb % 3 ==0 and numb % 5 ==0:
        return "fizzbuzz"
     if numb % 3 ==0 and numb % 5 !=0:
            return "fizz"
     if numb % 5 ==0 and numb % 3 !=0:
        return "buzz"
#    if numb % 3 ==0 and numb % 7 ==0:
#        return "fizzbuzz"
#    if numb % 3 !=0 and numb % 7 !=0:
#        return "null"
number = int(input("Enter your number "))
answer = two(number)
print (answer)