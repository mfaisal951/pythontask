# # Ducomentations for website is Greek for Greek 

# # ---- variable ----





# x= 5 
# y=2.5
# z="Day 1 of PCAP";  #single line string 
# bool= True
# a =None


# print(x)
# print(y)
# print(z)


# #                                       indexing 
# name ="Faisal";
# print(name[5])


# text= """ Day One of Pcap
# we learning of cone
# Python"""
# print(text)



# # s="string"
# # print(1)

# s="hello greek";
# s1="h"+s[1:]
# s2= s.replace("greeks", "greeksforGreek")
# print(s2)
# # print(len(s))


# #               -------------- python I/O


# name= input("enter the name: ")
# age=input("enter your age")
# print("faisal" + name)

# # --string formating--

# print("h1 {}".format(name))
# print("h1 {} your age is : {}" .format(name, age))
# print(f"your name is {name} your age is {age}")






# x=input("Enter a value :")
# y= input("Enter another value:")
# print(x, type(x)) # type checking
# print(x+y)

# #    type casting 


# x=int(input("Enter a value :"))
# y= int(input("Enter another value:"))
# print(x, type(x)) # type checking
# print(x+y)

#         Basic Operation (+, -, /, %, **)



# a= int(input("enter the number:"))

# b=int(input("enter the second number :"))
# print(a+b)
   




#  implicite & Explicite



# x=10;
# y=2.5;
# print(x+y)   # implicit type converstion


# ---                    Data Structure


# ----List--

# langs =['Python','C++', 'JavaScript','Java']
# print(langs, type(langs))

# langs[1]='C#'
# # Indexing 
# print(langs[1])
# print(langs[1:3])
# print(langs[1:])
# print(langs)



# list Method 

# langs.append('C++')
# print(langs)


# langs.insert(
#     'c++', 'React'
# )
# print(langs)


# langs.remove('C#')
# print(langs) 




# removed_item= langs.pop(2)
# print(removed_item)




#  Touple


# langs =('Python','C++', 'JavaScript','Java')
# print (langs, type(langs))
# print(langs[1])



# print('Java' in langs)

# del langs



#---------------------- Set


# number= {1,2,3,4,5}
# print(number, type(number))





# cars={'honda', 'suzuki', 'bmw'}
# print(cars)
# cars.add('ferory')
# print(cars)



#    Set Method

# set_1={1,3,5}
# set_2={2,4,6}
# set_3={} # this dictionary 


# union_set=set_1.union(set_2)
# print(union_set)
# 


# intersction_set=set_1.intersection(set_2)
# print(intersction_set)


# difference_set=set_1.difference(set_2)
# print(difference_set)




# -------------------------------------------------Dictionary

# student = {'name': 'faisal', 'age':23, 'marks':100}
# print(student)
# print(student['marks'])
# student['marks']= 70
# student["grade"]= 'A+'





#    Reverse list


# name= ['faisal','Ali', 'hamza' ]
# reversed_name=list(reversed(name))
# print(reversed_name)



# #                   Find common elements between two sets of integers.

# Set_a={1,2,3}
# set_b={3,6,9}
# intersection=Set_a.intersection(set_b)
# print(intersection)

# Set_x=input("enter the set :").split()
# s=set(map(int,Set_x))
# Set_y=input("enter the second set: ").split()
# S1=set(map(int,Set_y))

# print(s)
# print(S1)
# intersection_s=s.intersection(S1)
# print(intersection_s)


#                       Check if a particular key exists in a dictionary.



# Subject = {
#     'name':'math',
#     'marks':23,
#     'Grade': 'A+'
#     }

# print('Grade'in Subject.keys())




# Greek for Greeks


# x = input()
# y = input()
# print(x+5)

#         --                     --- Conditional Statements            2 days 

# x=5;
# if x>0:
#     print('value is positive ')
# elif x==0:
#     print('value is zreo')    
# else:
#     print('value is negative ')    
       
       
       
    #    Ternary if           operator
    
# print("positive" if x>0 else "negative ")      
    
    
    
    
# num= int(input("enter the number : "))

# if num>10:
#     print("number is greater than 10")
# # elif num==10:
# #     print("number is equal to tan") 
# else:
#     num<10
#     print("number is less than")
           
           
        #     --          Function
        
        
# def add():  #    defining a function
#     print(5+6)  
# print("first show")         
# add()     


# def product(x,y=0):
#     result= x * y
#     print(result)
# product(3,5)  # argument
# num=int(input("enter first"))
# num1=int(input("enter second "))

# product(num)   


#######################
# def greet(name, city):
#     print(f"hi, {name} from {city}")
# greet('Ahmad', 'Lahore')
# greet('Muneeb')    


#################3

# def student(*details):
#     print(details, type(details))
# student('Ahmad', 'Ali', 23)    


#              ---   return statement


# def student(*details):
#     return details
# print(student('Ahmad', 'Ali', 23) )


# return_val=student('muneeb', 20)
# print(return_val)


#                                       --variable --

# x='Global'  # Global varibale 
# def scope():
#     global x   # this means x is converte global varibale to local variable 
#     x='local' # local variable 
#     print(x) # calling a global var inside the function if local x does not exit
    
# scope()
# print(x)  # calling a global var outside function 




#    --      Grade calculator--


# def grade_calculate(marks):
#     if marks>=0 and marks<=100 :
#             if marks>=90 and marks<=100:
#                 return 'A+'
#             elif marks>=80 and marks<90:
#                 return 'A'
#             elif marks>=70 and marks<80:
#                 return 'B'
#             elif marks>=60 and marks<70:
#                 return 'c'
#             else:
#                 return 'f'
#     else:
#         return 'invalid value'
#         # print("enter valid value")
# marks= float(input("Enter your marks : "))
# grade = grade_calculate(marks)
# if grade=='invalid input':
#     print("Invalid value. Enter a number between 0 to 100")
# else:
#     print(f'Your garde is {grade}')










#                                 --- loop



#  -- for loop


# for i in range(5):
#     print(i)
    
    
  # -  range( Start , stop , step(incremen , decrement)) 
# for i in range(1,10,7):   # Start , stop , step 
#     print(i)
    
    
# for i in range(1,10):
#     if i%2==0:
#         print(i)


# -- Iteration over a list  ---
# list_1=['a','b','c','d']
# for i in list_1:
#     print(i)



# list_2 =[1,2,3,4]
# list_3=[]

# for i in list_2:
#     list_3.append(i**2)
# print(list_3)    


#  -------------- List comprenence ---



# a=[i for i in range(10)]
# print(a)

# create a list for loop
# a=[]
# for i in range(10):
#     a.append(i)


#  -------------

# list_1=[1,2,3,4,5]
# list_2=[val**2 for val in list_1]
# print(list_2)




#-------------- filter even number 


# list_1=[1,2,3,4,5]
# even_list=[val for val in list_1 if val%2==0]
# print(even_list)




# ------------------------while loop


# x=0
# while x<5:
#     print(x)
#     x+=1
    
    
    
#          loooop  

# user_val=int(input("enter a value : "))
# val=0
# while user_val!=0:
#     # print(user_val)
#     print(f"you entered {user_val}")
#     if user_val ==0:
#         break
   
#     val+=user_val
#     user_val= int(input("enter a value(enter 0 to exit : )"))
# print(val)


#################################################
# a=int(input("enter the value"))
# val=0
# while a!=0:
#     print("this is user value: ", a)
#     val+=a
#     a=int(input("enter a value( enter 0 to exit : )"))
# print(val)    








############################## Excercise 


# #
# 5. List Comprehension

    



#          Statement: Given a list of words i.e. words = ["hello", "world", "python"] , 
#            create a list of their lengths using list comprehension.








#       Exercise 5: Extract Vowels from String
# Statement: From a given string, extract all vowels and add those vowels into a list using list comprehension.


Vol_list ='Hello, I am learning python'
vowels='aeiouAEIOU'
vow=[word for word in Vol_list if word in vowels]
print(vow)

