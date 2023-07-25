def three(string_low):
    string_low = string_low.lower()
    #return string_low
    vowels = "aeiou"
    vowel_count = 0

    for char in string_low:
        if char in vowels:
            vowel_count = vowel_count + 1
    return vowel_count

#vowel_count = 0
#vowels = "aeiou"
stringss = input("enter text ")
answer = three(stringss)
#print (answer)
#print (string_low)
answer = three(stringss)
print (answer)
#print (answer)