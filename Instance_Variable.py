class Student:
    def __init__(self,name,id):    #Constructor
        self.name = name   #instance Variable
        self.id = id   #instance Variable
        #print("A student object Created")
        
    def details(self):
        print("Name: ",self.name, " ID: ",self.id) 

#========================================================

s1 = Student("Shanchita", 21)  
s2 = Student("Debadrita", 22)
s1.name = "Moumita"
s1.details()
print("--------------------")
s2.name = "Moumita"
s2.details()