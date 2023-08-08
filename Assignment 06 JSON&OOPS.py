# ASSIGNMNENT NO. 06]

# Assignment 1
# 1. Create a JSON file (employee.json) containing employee information of minimum 
#    5 employees. Each employee information consists of Name, DOB, Height, City, State. 
#    a python program that reads this information from the JSON file and saves the 
#    information into a list of objects of Employee class. Finally print the list of the 
#    Employee objects.
    
import json

employee = {"1":{
        "Name":"Rohit",
        "DOB":"07/12/1996",
        "Height":"5.9feet",
        "City":"Jagdalpur",
        "State":"Chhatisgarh",
        },
     "2":{
         "Name":"Sanchi",
         "DOB":"19/01/1990",
         "Height":"5feet",
         "City":"Hyderabad",
         "State":"Telangana"
     },
     "3":{
         "Name":"Poorvi",
         "DOB":"11/04/1989",
         "Height":"5feet",
         "City":"Bhuvneshwar",
         "State":"Odissa"
     },
     "4":{
         "Name":"Lata",
         "DOB":"29/11/1995",
         "Height":"5.3feet",
         "City":"vishakapatnam",
         "State":"Andra Pradesh"
     },
     "5":{
         "Name":"Preeti",
         "DOB":"16/05/1993",
         "Height":"5.1feet",
         "City":"Banglore",
         "State":"Karnataka"
     }
        }


with open("employee.json","w") as f:
    json.dump(employee,f,indent=1)

employee_list=[]

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
        employee_list.append({"Name":self.name,"DOB":self.dob,"Height":self.height,"City":self.city,"State":self.state})

class add_json(Employee):
    def __init__(self, jsonfile):
        self.jsonfile = jsonfile
        with open(jsonfile,"r") as f:
            x = json.load(f)
            employee_list.append(x)


z = Employee("Yash","18/9/1997", 5.9,"jdp","cg" )
y = add_json("employee.json")
print(employee_list)





#  02] Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

dict = {"chattisgarh":"Raipur","Madhya Pradesh":"Bhopal","Bihar":"Patna","Gujrat":"Gandhinagar","Assam":"Dispur","Arunachal Pradesh":"Itanagar","Goa":"Panaji"}
with open("capital.json","w") as f:
    x = json.dump(dict,f,indent=4)
    print(dict)


# Assignment 02
# 01] 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
#        You must perform the following operations:

#        a. It should have a function ‘description()’ which prints the name and age of the dog.
#        b. It should have a function ‘get_info()’ which prints the coat color of the dog.
#        c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. 
#           It should have at least two methods of its own.
#        d. Create objects and implement the above functionalities.



class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def discription(self):
        print(self.name)
        print(self.age)

    def get_info(self):
        print(self.coat_color)

class JackRussellTerrier(Dog):
    def __init__(self, coat_color, age):
        self.coat_color = coat_color
        self.age = age

    def color(self):
        print(self.coat_color)

    def get_age(self):
        print(self.age)

class Bulldog(Dog):
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def get_weight(self):
        print(self.weight)
    
    def get_age(self):
        print(self.age)

x = Dog("Labra", 4, "White")
x.get_info()
y = JackRussellTerrier("Brown", 5)
y.get_age()
z = Bulldog("4kg", 8)
z.get_weight()
z.get_age()