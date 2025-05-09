import constant as const
import math
from math import sqrt
import random
from functools import reduce
# 1 Modules
# Lambda function with highr order function

#   ---------------- Modules 

# python ma ksis b kism ka constant ka conscept nahi hota 



# print(const.NAME)
# print(const.CITY)
# print(math.sqrt(10))
# print(math.pi)

# print(random.random())
# print(random.randint(1,10))










#                                    Lamda function



# num =lambda x:x**2
# print(num(5))
##################
# num1=lambda x,y:x*y
# print(num1(4,5))

##########################

# even_num= lambda x: "Even" if x%2==0 else "Odd"
# print(even_num(6))
# print(even_num(7))



#Lamba with higher order function (map, Reduced,folter) 
# # map
# list_1=[1,2,3,5,4]
# list_2=list(map(lambda x:x**2, list_1))
# print(list_2)    


#filter

# even_list=list(filter(lambda x: x%2==0,list_2))
# print(even_list)



# reduce 

# sum= reduce(lambda x,y:x+y, list_1)
# print(sum)


# cars=['honda', 'bmw','toyota','mercedes']
# # cars=['abc','cde','bmw','faw']

# longest_word=reduce(lambda x,y:x if len(x)>len(y) else y, cars)
# print(longest_word)




# l1=[1,2,3,4]
# l2=[2,4,5,6]
# add=list(map(lambda x ,y: x+y, l1 , l2))
# print(add)



# name=['Faisal', 'ali', 'ahmad']
# f1=list(filter(lambda x:x.startswith('a'),name ))
# print(f1)

# (lambda x,y: print(f'{x}*{y}={x*y}'))(5,10)








#                 -------------------        OOP --------------







class Student:  # difining a class 
    school='Corvit' #classvariable
    def __init__(self,name,age,marks,grade): # constructor function
        self.name=name # self.name is used a instance variable 
        self.age=age  # age is used a instance variable 
        self.marks=marks # marks is used a instance  variable 
        self.grade=grade 
    def student_info(self):
        print(f"Student name : {self.name}, Student age : {self.age}, Student mark: {self.marks} ")    
    def passed(self):
        return self.grade !='F'     
student_1 =Student('Ahmad',20,90,'A+')   
student_2 =Student('Abdullah',23,90,'F')   
        
# print(student_1.age)
# student_2.student_info()        
for student in [student_1,student_2]:
    student.student_info()
    if student.passed():
        print("Student is pass")
    else:
        print("Student is fail")


##################################

class car:
    def __init__(self, name, color, model,showroom):
        self.n=name
        self.c=color
        self.m=model
        self.s=showroom
    def car_info(self):
        print(f"car name : {self.n}, car color : {self.c}")    
        
car1=car('honda','white',2013, 'faisal trader')        
car1.car_info()



##############################




class Student:  # difining a class 
    school='Corvit' #classvariable
    def __init__(self,name,age,marks,grade): # constructor function
        self.name=name # self.name is used a instance variable 
        self.age=age  # age is used a instance variable 
        self.marks=marks # marks is used a instance  variable 
        self.grade=grade 
    def student_info(self):
        print(f"Student name : {self.name}, Student age : {self.age}, Student mark: {self.marks} ")    
    def passed(self):
        return self.grade !='F'  
    
std_name=input("enter the name: ")
std_age=int(input("enter the age: "))
std_mark=int(input("enter the marks: "))
std_grade=input("enter the name: ")
       
student_1 =Student('Ahmad',20,90,'A+')   
student_2 =Student('Abdullah',23,90,'F') 
student_3=Student(std_name,std_age,std_mark, std_grade)  
        
# print(student_1.age)
# student_2.student_info()        
for student in [student_1,student_2]:
    student.student_info()
    if student.passed():
        print("Student is pass")
    else:
        print("Student is fail")
        
        
 ###################### Inheritance ############
 
 
 
class car:
    def __init__(self, brand, model, color):
         self.b=brand
         self.m=model
         self.c=color
    def start(self):
        print("a car start")
class electic_car(car):        
    def __init__(self, brand, model, color, battery):
        super().__init__(brand, model, color)
        self.be=battery
    def car_info(self):
        print(f"Car Brand: {self.b}")
        print(f"Car model: {self.m}")
        print(f"Car color: {self.c}")
        print(f"Car Battery: {self.be}")
tesla=electic_car('tesla', 'Model s', 'blue', 100)
tesla.car_info()        
            
                
        
            
             
               
