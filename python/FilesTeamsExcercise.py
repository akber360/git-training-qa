file = open("team1.txt", "w") # creates file called teams1 "w" only mode
team1 = "Man City"+ "\n"
file.write(team1)
team2 = "Man United"+ "\n"
file.write(team2)
team3 = "Liverpool"+ "\n"
file.write(team3)
team4 = "Real Madrid"+ "\n"
file.write(team4)
team5 = "Chelsea"+ "\n"
file.write(team5)
file.close()

file = open("team1.txt", "r")
variable = file.read()
file.close()

print (variable)
#print(file.readline())
#file.readline()
#file.readline()
#print(file.readline())
#file.close()



