# import time
from turtledemo.penrose import start


# Decorator — bu Python’da bir funksiyani oladigan va uni kengaytiradigan (o‘rab oladigan)
#
# funksiya yoki sinfdir.
#
# U asl funksiyaning kodini o‘zgartirmasdan, unga qo‘shimcha imkoniyatlar qo‘shish uchun ishlatiladi.


# Qanday ishlaydi?
#
# Decorator asl funksiyani qabul qiladi, unga o‘zgartirish kiritadigan
#
# yangi funksiya qaytaradi va asl funksiyani shu yangi funksiya bilan almashtiradi.

def decorator(func):
    def wrapper():
        print("Funksiya bajarilishidan oldin")
        func
        print("Funksiya bajarilishidan keyin")
    return wrapper

@decorator
def salom_ber():
    print("Salom!")

salom_ber()
# def decorator(func):
#     def wrapper():
#         print("Funksiya bajarilishidan oldin")
#         func()
#         print("Funksiya bajarilishidan keyin")
#     return wrapper
#
# @decorator
# def salom_ber():
#     print("Salom!")
#
# salom_ber()


# def decarator(func):
#     def wrapper():
#         start = time.time()
#         print("nice")
#         func()
#         end = time.time()
#         print(f"Masala {end-start} sekunda bajarildi")
#     return wrapper
#
# @decarator
# def sanab_ber():
#     c = 0
#     for i in range(100000):
#         c+=i
#
#     print(c)
#
# sanab_ber()





def deca(func):
    def salom():
        print("Salom1")
        func()
        print("Salom1")

    return salom

@deca
def salom_ber():
    print("ASSSALOM ALEYKUM")

salom_ber()
  