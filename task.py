                                #   Conditional Statements
 
#         Exercise 1: Positive, Negative or Zero
# Statement: Write a program that takes an integer as input and prints whether it is positive, negative, or zero.
try:
    num= int(input("enter the number"))
    if num>0:
        print("postive number", num)
    elif num==0:
        print("number is zero ", num)
    else:
        print("number is negative")
    
except ValueError:
    print("invalid number enter")


#                        Exercise 2: Find the Largest Number
# Statement: Write a program that takes three numbers and prints the largest one.

a=10
b=3
c=20
if a>b and a>c:
    print("the of a is greater than all number ", a)
elif b>a and b>c:
    print("B is greater number than other ",b)
elif c>a and c>b:
    print("c is greater than other", c)
else:
    print("invalid number not any number is greater ")

#                            ----- Get user value

try:
    a=int(input('enter the first number: '))
    b=int(input('enter the second number: '))
    c=int(input('enter the third number: '))
    if a>b and a>c:
        print("the of a is greater than all number ", a)
    elif b>a and b>c:
        print("B is greater number than other ",b)
    elif c>a and c>b:
        print("c is greater than other", c)
    else:
        print("invalid number not any number is greater ")
except ValueError:
    print("enter the invalid number ")





#                                  2. Functions with Parameters and Arguments

#              Exercise 1: Greet User
# Statement: Define a function that takes a name as a parameter and prints a greeting.



#### simple######

def add(name):
    print("A greeting ")
add('faisal')

##################### other simple

def greet(name):
    print(f"h1 my name is {name}")
greet('faisal')    


######## next #####


def add(name):
    x=input("enter the name: " )
    print("this is greety")
add('x')    


# ################################### condition with function
def add(name):
    
    if get=='faisal':
        print("this not greety ", name)
    else:
        print("this is grerty", name)
get=input("enter the required data : ")        
add(get)            
    
    ################### other conditionls used infunction 
    
def greet(name):
    if name.isnumeric():
        print("you enter the numeric data and this is not allowed",name)
    elif name=='faisal':
        print("this is not a greety",name) 
    else:
        print("this greety")           
user=input("enter the required data : ")
greet(user)        
    
    
    # Exercise 2: Check Even Number
# Statement: Write a function that accepts a number and prints if it is even or odd.

# num=int(input("enter the number : "))
def check(val):
    if num % 2!=0:
        print("number is odd :", num)
    else:
        print("number is even : ", num)
try:
    num = int(input("Enter the number: "))
    check(num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")        
    



#                                      Exercise 3: Vowel Checker
# Statement: Write a function that checks whether a character is a vowel. Return True or False.

def vowel_check(char):
    vowel=['a','e','i','o','u']
    
    return char.lower() in vowel

char=input('Enter the character')
if len(char)==1 and char.isalpha():
    
    result=vowel_check(char)
    print("Is vowels", result)
else:
    print("Invalid value")   


#                                                      3. Variable Scope
#             Exercise 1: Local vs Global Scope
# Statement: Demonstrate the difference between a local and global variable using a print statement inside and outside a function.

x=5   #  Global variables
def func():
    y=7 # this is local variable 
    
    print("this is global variables", x)
    print('this is loacl variable', y)
func()
print("out side function ")
print('global variable : ',x)



#                                 Exercise 2: Using Global Keyword
# Statement: Create a function that modifies a global variable using the global keyword.

var=2;
def Modify():
    global var
    
    var+=1
print("before modificatin", var)

Modify()
print("after modifications", var)
    

#                                         4. Loops with Loop Control Statements

#                      Exercise 1: Break Statement
# Statement: Write a loop that stops when it reaches number 4 using break.

for i in range(1, 10):
    if i == 4:
        print("Reached 4, stopping the loop.")
        break
    print("Number:", i)


#                                Exercise 2: Break in While Loop
#         Statement: Use a while loop to print numbers from 1 to 5 and stop when number 3 is reached.

a=1;
while a<=5:
    print(a)
    if a==3:
        break
        
    a=a+1
    
    
    
    
    
    
    
    #                             Exercise 3: Print Even Numbers
#                    Statement: Use a for loop to print only even numbers from 1 to 9.

for i in range(1,9):
    if i % 2==0:
        print(i)
     

    
    
#                                  5. List Comprehension
#                 Exercise 1: Squares of Numbers
# Statement: Use list comprehension to create a list of squares of numbers from 1 to 5.


squares = [x**2 for x in range(1, 6)]
print("Squares from 1 to 5:", squares)

#                     Exercise 2: Even Numbers List
# Statement: Create a list of even numbers from 0 to 9 using list comprehension.

even=[x for x in range(0, 9) if x%2==0]
print(even)
    
#         Exercise 3: Word Lengths
# Statement: Given a list of words i.e. words = ["hello", "world", "python"] , create a list of their lengths using list comprehension.



Words=['Zeeshan', 'Ali Haider','Lahore']
print(Words)
length=[len(word) for word in Words]
print(length)



# Exercise 4: Filter Positive Numbers
# Statement: Use list comprehension to filter out positive numbers from a list

#   ################# simple 
list= [12,24,8,-8,-2,6]
positive=sorted([word for word in list if word>0])
print(positive)

###                 get from user 

list_1=input("enter the list num :" )
list_user=list_1.split()

list_user= [int(num) for num in list_user]
print(list_user)
positive_1=sorted([num for num in list_user if num>0])
print(f"I filter the positve {positive_1}")





#                 valid number 



list_1=input("enter the list num :" )
list_user=list_1.split()
valid_num=[]
for num in list_user:
    try:
        valid_num.append(int (num))
    except ValueError:
        print(f"Skipping invalid {num}")    
print(valid_num)
positive_1=sorted([num for num in valid_num if num>0])
print(f"I filter the positve {positive_1}")



    
#                     Exercise 5: Extract Vowels from String
# Statement: From a given string, extract all vowels and add those vowels into a list using list comprehension.


Vol_list ='Hello, I am learning python'
vowels='aeiouAEIOU'
vow=[word for word in Vol_list if word in vowels]
print(vow)
    