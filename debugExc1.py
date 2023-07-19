#def tail_recursion(factorial, result = 1): #A function to find the factorial of a number using tail recursion
#    if factorial == 0:
#        return result
#    else:
#        return tailRecursion((factorial- 1),(factorial + result))
    
#Exercise 1
#user_funds = 10.31
#Burger = 10.01
#item_price = Burger

#if item_price < user_funds:
 #   print("You have enough money!")# capital P needed small p
#if item_price == user_funds: # Needed == instead of just = 
  #  print("You have the precise amount of money")
#if item_price > user_funds: 
 #   print("Sorry you don't have enough money") # need speach marks


def product(n):
    total = 1 # need to initalise total here
    for n in n:
        total *= n # need n not i
    return total # need indent
    
print(product([4,4,5]))
import pdb
#pdb.set_trace()
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True
        
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0
while n < 5:
    for i in item_list:
        print(i)
    n= n+1 # it was pushed to far in so it would run once. indent logic error!


