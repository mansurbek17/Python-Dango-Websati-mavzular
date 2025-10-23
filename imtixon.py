# #1-misol
# #Map va filterni ishlatish misollar bilan tushuntirib bering 
# # map har bir elementni ozgartiradi

# b= [2,4,5,6]

# a = list(map(lambda x: x**2, b))
# print(a)  #[4, 16, 25, 36]

# # filter shartga mos kelgan elementlarni tanlaydi

# a= [1,2,3,4,5,6]

# def juft(x):
#     return x%2==0

# b = list(filter(juft, a))
# print(b) #[2, 4, 6]

# #2-misol
# #list competations ni tushuntirib bering
# #list competations har bir elementni ozgartiradi

# a = [1,2,3]
# c = [x**2 for x in a]
# print(c) #[1, 4, 9]

# #3-misol 
# #Acces mode filelar va encapshulation tushuntiring

# Acsess mode filelar u encapsulation dagi private protect public


# #4-misol 
# #abbstaction ni tushuntiring  abstrack method nima 
# #faqat kerakli funksionallikni korsatib , Kerakli tafsilotlarni yashirish
# #Pythonda abc (abstrac Base Class  ) yordamida qilinadi 
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
    

# Circle = Circle(5)
# print(Circle.area()) #78.5


# #5-misol
# #Sqlda order by ni tushuntirib  bering
# #order by malumotlarni malum ustun boyicha saraylaydi
# #order byda asc va desc bor 
# #asc bu  o'sish tartibi
# #desc bu  kamayish tartibi
# #limit  cheklash
# import sqlite3

# # SELECT * FROM students
# # ORDER BY age ASC
# # LIMIT 1;


# #6-misol 
# #DDL va DML   
# # Sturukturani yaratish va ozgartirish 
# #DDL Data Definition Language
# #CREATE TABLE
# #DROP TABLE
# #ALTER TABLE
# #TRUNCATE TABLE

# #DML Data Manipulation Language
# #INSERT
# #UPDATE
# #DELETE

# #7-misol
# #forin key 
# #Foreign Key (tashqi kalit) — bu bitta jadvaldagi ustunni (yoki ustunlar to‘plamini) boshqa 
# #jadvaldagi Primary Key (asosiy kalit) bilan bog‘lash uchun ishlatiladigan kalitdir.

# from django.db import models

# class Group(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Student(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

    
# #8-misol
# #GROUP BY — bu SQL operatori bo‘lib, bir xil qiymatga ega bo‘lgan qatorlarni guruhlash uchun ishlatiladi.
# # U ko‘pincha SUM(), COUNT(), AVG(), MAX(), MIN() kabi agregat funksiyalar bilan birga ishlatiladi.
# # SELECT group_name, COUNT(*) AS student_count
# # FROM students
# # GROUP BY group_name;

# #9-misol
# #having  va where ni farqini tushuntirib bering 
# #where guruhlashdan oldin 
# #heving guruhlashdan keyin ishlatiladi 

# # SELECT → WHERE → GROUP BY → HAVING → ORDER BY

# #10-misol

# # inner join va natural joinni  , joinlar misolida tushuntirib bering 
# #inner join  ikkala jadvalga mos keladiganlarni (ya’ni ikkisida ham mavjud) yozuvlarni chiqaradi.
# # SELECT s.student_name, g.group_name
# # FROM students s
# # INNER JOIN groups g
# # ON s.group_id = g.group_id;
# #natural join ikkala jadvalda bir xil nomli ustunlarni avtomatik topadi
# # SELECT student_name, group_name
# # FROM students
# # NATURAL JOIN groups;


# # 11-misol
# #decarotorlar 
# # bu pythonda 1 fynksiyani oladigan va uni kengaytiradigan (orab oladigan )
# # funksiya yoki sinfdir
# def decorator(func):
#     def wrapper():
#         print("mansurbek")
#         func()
#         print("sobirov")
#     return wrapper

# @decorator
# def salom():
#     print("salom")

# salom()
# #12-misol
# #Theread 
# #  Thread (Ip) nima?
# #  Thread — bu bitta dastur ichida bir nechta mustaqil bajariladigan kod oqimi.
# #  Ular bir xil xotirada ishlaydi, shuning uchun o‘zaro oson ma'lumot almasha oladi

# #13 - misol
# # Iterators Iterable  va Generatorlarni tushuntirib bering
# # iterator takrorlanuvchi obyekt masalan (tuple , list , string va hokoza)
# # iterable takrorlanmas obyekt masalan (dict, set)  #  xatolik qaytati (stop interotion)
# # Generator – iterator qaytaruvchi funksiyaga bo‘lib, 
# # iterator yaratishning oson yo‘li hisoblanadi.
# # yield bu funksiya ichida ishlatiladi
# def my_generator():
#     for i in range(10):
#         yield i 
        
# #14 -misol
# #sinxron Dastur bir vaqtda  faqat bitta ish bajaradi. Navbatdagi kutadi.
# #asinxron Dastur bir nechta ishni bir vaqtda bajaradi.


 

# import asyncio
# import time

# async def a():
#     print("a ishga tushdi")
#     await asyncio.sleep(2)
#     print("a tugadi")

# async def b():
#     print("b ishga tushdi")
#     await asyncio.sleep(3)
#     print("b tugadi")

# async def c():
#     await asyncio.gather(a(), b())

# asyncio.run(c())]


def deca(func):
    def salom():
        print("Salom1")
        func()
        print("Salom1")

    return salom

def salom_ber():
    print("ASSSALOM ALEYKUM")