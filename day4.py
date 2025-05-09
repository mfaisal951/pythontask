# 
import csv
# 
# 
# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.__marks=marks  # Private attribute
    
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         if marks>=0 and marks <=100:
#             self.__marks=marks
#         else:
#             print("enetr the validvalue ")            
        
#     def student_info(self):
#         print(f"Student name : {self.name}, Student Marks : {self.__marks}") 
        
        
# s1=Student('Ahmed', 100)
# s1.set_marks(95)
# s1.student_info()
# print(s1.get_marks())
# s2=s1.set_marks(85)
# print(s2)           



#################                 Polymorphism 



# class  Car:
#     def __init__(self, brand , model):
#         self.b=brand
#         self.m=model
        
#     def car_engine(self):
#         print("car is start")
# class Electric_car(Car):
#     def car_engine(self):
#         print("An electic car is atart")
# car1=Electric_car("tesla", "Model s")                    
# car2=Car('brand', 'Civic')
# car1.car_engine() 
# car2.car_engine()       
        
        ################
        
        
# class  Car:
#     def __init__(self, brand , model):
#         self.b=brand
#         self.m=model
#     @staticmethod   # decorated 
#     def car_engine():
#         print("car is start")
# class Electric_car(Car):
#     @staticmethod
#     def car_engine():
#         print("An electic car is atart")
# car1=Electric_car("tesla", "Model s")                    
# car2=Car('brand', 'Civic')
# car1.car_engine() 
# car2.car_engine() 










####################------------ file handling ----------

# with open("python.txt", 'a') as file:
#     file.write(" some content written text ")


# with open("python.txt", "r") as file:
#     content = file.read()
#     print(content)
    
    
    
    
    
    
    
    
    
    #   Csv file 
    
    
# with open('student_data.csv','w' , newline="") as file:
#     file_write= csv.writer(file)
#     file_write.writerow(['name', 'Age', 'Marks'])
#     file_write.writerow(['ahmad', 20,90])
# with open('student_data.csv', 'r') as file:
#     file_read=csv.reader(file)
#     for  row in file_read:
#         print(row)       
    
    
    
# ---------------------------- Exception Handling ---------------------


# user_input = int(input("enter the number"))    
# print(user_input/0)
####################################


# try: 
#     user_input = int(input("enter the number"))    
#     user_input1 = int(input("enter the number"))    
#     user_input2 = int(input("enter the number"))    
#     print(user_input/user_input1)
# except ZeroDivisionError:
#     print("you cannot diivde a number with zero")
    
    
#########################################33    
# with open('student.txt', 'r') as file:                # error dee raha 
#     content= file.read()
#     print(content)
    
    
    
# try:
#     with open('student.txt', 'w')as file:
#         file.write('the write the data ')
        
# except:
#     print(' file handler  create the ')          


# --------------------------------------------------------



# try:
#     num_1=float(input("enter the first number: "))
#     num_2=float(input("enter the second number: "))
#     oper=input("enter the operator +, -,*,/")
#     operation={
#         '+':num_1+num_2,
#         '-':num_1-num_2,
#         '*':num_1*num_2,
#         '/':num_1/num_2,
        
#     }
#     if oper not in operation:
#         raise KeyError("Key not found ")   # keyError : key not found
#     print(f"Result: {operation[oper]}")
# except ZeroDivisionError:
#     print("Division by zero is not allowed ")     
# except ValueError:
#     print('Invalid value ')
# except KeyError as ke:
#     print(f'Error {ke}' +ke)     
    
    
    
    
    
    
    
    
    
    
    







# ---------------- OOP WITH  FILE HANDLING -------------------------

class Student:
    def __init__(self, name, age, marks ):
        self.name=name
        self.age=age
        self.marks=marks
        
    def student_info(self):
        print(f"student name : {self.name}, Student age : {self.age } student marks {self.marks}")    

def read_student_data(filename):
    students=[]
    with open (filename, 'r') as file:
        for row in file:
            line=row.strip().split(',')
            if len(line)==3:
                name=line[0]
                age= int(line[1])
                marks=int(line[2])
                student=Student(name,age,marks)
                students.append(student)
    return students

student_list=read_student_data('student_data.csv')
for std in student_list:
    std.student_info()            

             