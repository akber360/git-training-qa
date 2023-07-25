def four(input_str):
    for i in range(len(input_str) - 1):
        if input_str[i:i + 2] == "ei":
            if i == 0 or (i > 0 and input_str[i - 1] != "c"):
                return False
        elif input_str[i:i + 2] == "ie":
            if i == 0 or (i > 0 and input_str[i - 1] == "c"):
                return False

    return True

enterword = input("enter word ")
word = four(enterword)
print (word)