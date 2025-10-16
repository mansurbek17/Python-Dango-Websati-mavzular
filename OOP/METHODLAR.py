# 🟦 3. __init__() metodi (konstruktor)
# __init__() bu konstruktor metod bo‘lib, obyekt yaratilganda avtomatik chaqiriladi.

class Person:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

# Obyekt
shaxs = Person("Ali", 22)

print(shaxs.ism)   # Ali
print(shaxs.yosh)  # 22

# self — bu obyektning o‘zi. Har bir metodda birinchi parametr sifatida yoziladi (lekin chaqirilganda ko‘rsatilmaydi).

# 🟥 4. Method (usul) nima?
# method — bu class ichida e’lon qilingan funksiya bo‘lib, obyektlar bilan ishlaydi.

class Person:
    def __init__(self, ism):
        self.ism = ism

    def salom_ber(self):
        print(f"Salom, mening ismim {self.ism}")

p1 = Person("Ali")
p1.salom_ber()  # Salom, mening ismim Ali


# 🟪 5. Class atributlari vs obyekt atributlari

# | Turi                        | Qayerda e’lon qilinadi                 | Kimga tegishli           |
# | --------------------------- | -------------------------------------- | ------------------------ |
# | Class attribute             | Class ichida, lekin `def` tashqarisida | Hamma obyektlarga umumiy |
# | Instance (obyekt) attribute | `__init__` ichida `self.` bilan        | Faqat o‘sha obyektga xos |

class Student:
    universitet = "TATU"  # class atribut

    def __init__(self, ism):
        self.ism = ism  # obyekt atribut

s1 = Student("Ali")
s2 = Student("Vali")

print(s1.universitet)  # TATU
print(s2.ism)          # Vali


# 🟨 6. self so‘zi haqida
# self — bu obyektning o‘zini anglatadi. Har bir metodda birinchi argument sifatida yoziladi.

class Dog:
    def __init__(self, name):
        self.name = name  # self.name — bu obyektga xos

    def bark(self):
        print(f"{self.name} havlayapti!")

dog = Dog("Sharik")
dog.bark()  # Sharik havlayapti!


# 🟧 7. Class ichida boshqa metodlar

# | Metod turi    | Ta'rifi                                           | Qanday yoziladi                    |
# | ------------- | ------------------------------------------------- | ---------------------------------- |
# | Obyekt metodi | Oddiy metod (`self`)                              | `def metod(self):`                 |
# | Class metodi  | Butun klassga tegishli (`@classmethod`)           | `@classmethod` + `def metod(cls):` |
# | Static metod  | Ne klassga, ne obyektga bog‘liq (`@staticmethod`) | `@staticmethod` + `def metod():`   |


class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def obyek_soni(cls):
        print(f"Obyektlar soni: {cls.count}")

obj1 = MyClass()
obj2 = MyClass()

MyClass.obyek_soni()  # Obyektlar soni: 2


# 🔹 Static method misol:

class Math:
    @staticmethod
    def kvadrat(x):
        return x * x

print(Math.kvadrat(5))  # 25


# 🔁 8. Mavjud metodlar (magic methods)

# Python’da __init__(), __str__(), __len__() kabi "dunder" metodlar mavjud.
#
# Misol: __str__()

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Kitob: {self.title}"

b = Book("Python 101")
print(b)  # Kitob: Python 101

# | Narsa            | Ta’rifi                                      |
# | ---------------- | -------------------------------------------- |
# | `class`          | Obyektlar uchun shablon                      |
# | `__init__()`     | Konstruktor, obyekt yaratilganda chaqiriladi |
# | `self`           | Obyektning o‘zi                              |
# | Method           | Class ichidagi funksiya                      |
# | Class attribute  | Hamma obyektlarga umumiy xossa               |
# | Object attribute | Faqat 1 obyektga xos xossa                   |
# | `@classmethod`   | Klassga oid metod                            |
# | `@staticmethod`  | Klassdan mustaqil metod                      |



























