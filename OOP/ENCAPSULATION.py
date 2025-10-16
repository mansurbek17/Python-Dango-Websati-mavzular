# 1. Encapsulation nima?
# Encapsulation — bu ma’lumotlarni (data) va ularga ishlov beruvchi funksiyalarni
#
# (methods) bir joyga to‘plash va tashqi muhitdan himoya qilish jarayonidir.
#
# OOP-da bu quyidagilarni anglatadi:
#
# Klass ichidagi atributlar (variables) va methodlar birga bo‘ladi.
#
# Klass tashqarisidagi kod ushbu atributlarga bevosita kira olmaydi, faqat maxsus methodlar orqali kira oladi.
#
# Shu bilan ma’lumotlar himoyalangan bo‘ladi va katastrofik xatolardan saqlanadi.
#
# 2. Encapsulationning asosiy maqsadlari
# Ma’lumotlarni himoya qilish – atributlarga bevosita kirish cheklanishi mumkin.
#
# Data integrity – atributlar faqat ruxsat etilgan qiymatlarni oladi.
#
# Interface yaratish – tashqi kod klass bilan ishlash uchun faqat ruxsat etilgan methodlardan foydalanadi.
#
# Modularity – kodni boshqarish osonlashadi, classning ichki tuzilishi tashqariga ta’sir qilmaydi.

# 3. Python-da encapsulation
# Python-da encapsulation 3 darajada bo‘ladi:
#
# Daraja	Belgilanishi	Tavsif
# Public	var yoki method	Tashqaridan erkin foydalanish mumkin.
# Protected	_var yoki _method	Faqat subclass yoki klass ichida ishlatish tavsiya etiladi (konvensiya, majburiy emas).
# Private	__var yoki __method	Klass tashqarisidan kira olmaysiz (name mangling orqali himoyalangan).

# 3.1 Public misol

class Car:
    def __init__(self, brand):
        self.brand = brand  # public attribute

my_car = Car("Toyota")
print(my_car.brand)  # ishlaydi

# 3.2 Protected misol

class Car:
    def __init__(self, brand):
        self._brand = brand  # protected attribute

my_car = Car("Honda")
print(my_car._brand)  # ishlaydi, lekin "protected" deb hisoblanadi
# Eslatma: Python-da protected faqat konvensiya, ruxsatni cheklamaydi.

# 3.3 Private misol

class Car:
    def __init__(self, brand):
        self.__brand = brand  # private attribute

    def get_brand(self):
        return self.__brand  # public method orqali olish mumkin

    def set_brand(self, new_brand):
        self.__brand = new_brand  # public method orqali o‘zgartirish mumkin

my_car = Car("BMW")
# print(my_car.__brand)  # xato beradi
print(my_car.get_brand())  # BMW
my_car.set_brand("Audi")
print(my_car.get_brand())  # Audi
# __brand ni tashqaridan chaqirish mumkin emas. Faqat getter va setter orqali ishlash mumkin.
#
# 4. Getter va Setter
# Getter va Setter — encapsulationni amalga oshirishda ishlatiladigan methodlar:
#
# Getter – atribut qiymatini olish.
#
# Setter – atribut qiymatini o‘zgartirish, shart va tekshiruv bilan.


class Student:
    def __init__(self, name):
        self.__name = name  # private

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if len(new_name) > 0:
            self.__name = new_name
        else:
            print("Ism bo‘sh bo‘lishi mumkin emas.")

s = Student("Ali")
print(s.get_name())  # Ali
s.set_name("Vali")
print(s.get_name())  # Vali

# 5. Python-da property dekoratori
# Python-da getter va setter ni yanada osonroq qilish uchun @property va @<var>.setter ishlatiladi:


class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self.__name = new_name
        else:
            print("Ism bo‘sh bo‘lishi mumkin emas.")

s = Student("Ali")
print(s.name)  # Ali
s.name = "Vali"
print(s.name)  # Vali
# Shu bilan kod toza va Pythonic bo‘ladi.

# 6. Xulosa
# Encapsulation — ma’lumotlarni himoya qilish va methodlar bilan ishlashni birlashtirish.
#
# U data integrity va modularity ni ta’minlaydi.
#
# Python-da 3 tur mavjud: public, protected, private.
#
# Getter/setter yoki property orqali atributlar ustidan nazorat o‘rnatiladi.
#
# Agar xohlasang, men siz uchun Encapsulation diagrammasi va
#
# real hayot misoli bilan tushuntirib beradigan vizual tasvir ham tayyorlab bera olaman,
#
# shunda yanada oson eslab qolasan.












