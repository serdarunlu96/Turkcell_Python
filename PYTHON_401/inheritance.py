class Employees():
    def __init__(self):
        self.FirstName=""
        self.LastName=''
        self.Adress=""

class DataScience(Employees): # inheritance miras Employees class sınıfı ve attributes degiskenleri
    def __init__(self):
        self.Programming=""
       
veribilimci1 = DataScience()
# print(veribilimci1.FirstName)

class Marketing():
    def __init__(self):
        self.StoryTelling=""

class Employee_new():
    def __init__(self,FirstName,LastName,Adress):
        self.FirstName=FirstName
        self.LastName=LastName
        self.Adress=Adress

ali=Employee_new("ali","candan","istanbul")
print(ali.FirstName,ali.LastName,ali.Adress)
