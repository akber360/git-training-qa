#class Student:

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#John = Student("John", "21")
#Jane = Student("Jane", "22")
#print(getattr(John, "age"))

class students:
    def __init__(self,iname,iage,iyear_class="student"):
        self.name = iname
        self.age = iage
        self.year_class = iyear_class 


    def avgScore(self, a, b, c):
        return (a + b + c) / 3

s1= students("akber",20,"y12") 
s2 = students("jake",24,"y14")
s3 = students("ali",12,"y8")

avgScore = s1.avgScore(50, 25, 10)

print(s1.name,"s", "Avergae score is ",avgScore)

