#Packing in python
# Abstraction in OOP
# Sqlite with python










   # ----------------------        Abstraction ---------
# decorated method is used for inhance the msg of user 

# Abstract class 
from abc import ABC, abstractmethod
import sqlite3
# import requests 
# from bs4 import BeautifulSoup
# class vehicale(ABC):
#     @abstractmethod
#     def engine_start():
#         pass
    
# class car(vehicale):
#     def engine_start():
#         print("car engine starts")    

# class bike(vehicale):
#     def engine_start():
#         print("A bike engine is start")
        
# new_vehicle=vehicale()
# new_vehicle.engine_start()
                

#######################   -------- sqlite -------

conn= sqlite3.connect('students.db')   # connect the database 
cursor = conn.cursor()


cursor.execute("""
               CREATE TABLE IF NOT EXISTs student(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   MARKS INTEGER,
                   grade TEXT
               )
               
               """)

conn.commit()


###########  INSERTING DATA 


cursor.execute("INSERT INTO student (name, marks, grade) VALUES ('Ahmad', 90, 'A')")
conn.commit()

                               #fetching data 
cursor.execute("SELECT *FROM student")
rows=cursor.fetchall()
for row in rows:
    print(row)  

# cursor.execute("INSERT INTO student (name, marks,grade) VALUES (?,?,?), ('Abdullah', 56,'C')")
# cursor.execute("SELECT *FROM student")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)     
############### UPDATE 

cursor.execute("UPDATE student SET marks = 30 WHERE name ='Ahmad'")    

# cursor.execute("SELECT *FROM student")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)    


cursor.execute("DELETE FROM student WHERE name = 'Ahmad'")
    
cursor.execute("SELECT *FROM student")
   
 
 
 
 ## scraping
 
 
 
 URL ="https://www.geeksforgeeks.org/python-programming-language-tutorial/"
 r=requests.get(URL)
 # print(r.content)
 soup= BeautifulSoup(r.text, 'html5lip')
 headings= soup.find_all('h2')
 for heading in headings:
     print(heading.text.strip())