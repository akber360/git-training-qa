mirror = 'My Name is Jessa'
#revers = mirror.split # reverses order of list but not like [::-1] 
elps= mirror.split()
#elp.reverse()
relp = [elp[::-1] for elp in elps]
print (relp)
