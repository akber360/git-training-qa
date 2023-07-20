mirror = 'My Name is Jessa'
#revers = mirror.split # reverses order of list but not like [::-1] 
elps= mirror.split()
#elp.reverse()
relp = [elp[::-1] for elp in elps]
#print (relp)

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = 0
total = len(number_list)

while x < total:
    if number_list[x] >50:
        del number_list[x]
        total = total - 1
      #  print (x)
    else:
        x = x + 1
 #       print(x)

#print(number_list)

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

switchd = {value:key for key, value in ascii_dict.items()}
#print (switchd) # you made a new dict
#print(ascii_dict) # the original dict is still here un changed (dicts are immutable!)

#sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
#total = len(sample_list)#
#x = 0
#while x < total:
#    if sample_list[x]!=sample_list:
#        sample_list.pop(x)
#        total = total + 1
#else:
#    x = x + 1 
#print(sample_list) 
import collections

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

duplicates = []
for item, count in collections.Counter(sample_list).items():
    if count > 1:
        duplicates.append(item)
#print(duplicates)

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50] 
#Change the element 35 to 3500
#print (list1)
#print (list1[1:])
#print (list1[1:][2:0])
#print (list1[1][2])
#print (list1[1][2][1])
#print (list1[1][2][2])
print (list1[1][2][2:1])
print (list1[1][2][2])
print (list1[1][2][2][1])
list1[1][2][2][1] = 3500
print (list1)

