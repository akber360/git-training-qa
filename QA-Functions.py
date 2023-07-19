
def workout(username,homework,assesment,exam):  
    return username,"your homework score is ", homework/25,"your assesment score is ", assesment/50,"your exam score is ", exam/100
    #homework = (homework/25)
    return homework/50
    #assesment = (assesment/50)
    return assesment/100
    #exam = (exam/100)
    return exam/100
   

#grade = input("do you want to work out your grade? y/n ")


username = input("Please enter user name ")
homework = int(input("Please enter your homework score "))
assesment = int(input("Please enter your assesment score "))
exam = int(input("Please enter your final exam score "))
workout(username,homework,assesment,exam)

print (workout(username, homework,assesment,exam))


