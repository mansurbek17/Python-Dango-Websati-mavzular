# 🔹 Abstraction (Abstraksiya) nima?
#
# 👉 Abstraksiya dasturlashdagi obyektga yo‘naltirilgan dasturlash (OOP) prinsiplardan biridir.
# Uning maqsadi — keraksiz tafsilotlarni yashirish, faqatgina foydalanuvchiga kerak bo‘lgan funksiyalarni ko‘rsatishdir.
#
# Ya’ni:
#
# Biz ichki mexanizmlarni yashiramiz, faqat tashqi interfeys orqali ishlaymiz.
#
# Foydalanuvchi obyekt bilan ishlayotganda faqat kerakli metodlarni ko‘radi, lekin ichkarida qanday ishlashini bilishi shart emas.
#
# 🔹 Kundalik hayotdan misol
#
# Mashina: Siz mashinani haydashda gaz, tormoz va ruldan foydalanasiz.
# Ammo dvigatel ichida qanday portlashlar bo‘lyapti, yoqilg‘i qanday yonmoqda, piston qanday harakatlanmoqda — buni bilishingiz shart emas.
# 👉 Bu abstraksiya.
#
# Bank kartasi: Siz kartani terminalga qo‘yasiz va pul yechasiz.
# Ichkarida qanday shifrlash algoritmlari ishlayotgani siz uchun muhim emas.
# 👉 Bu ham abstraksiya.
#
# 🔹 Dasturlashdagi abstraksiya
#
# Python’da abstraksiya asosan Abstract Class (abstrakt klass) va Abstract Method (abstrakt metod) orqali amalga oshiriladi.
#
# Buning uchun abc (Abstract Base Class) moduli ishlatiladi.
#
# 🔹 Abstraksiya qanday ishlaydi?
#
# Abstrakt klass — bu to‘liq ishlamaydigan klass.
# Undan bevosita obyekt yaratilmaydi.
#
# Abstrakt metod — bu faqat e’lon qilingan, lekin tanasi (body) yozilmagan metod.
# Uni meros olgan klass albatta o‘zida implementatsiya qilishi kerak.
#
# 🔹 Python misoli
# from abc import ABC, abstractmethod
#
# # Abstrakt klass
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# # Meros oluvchi klass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
#
# # Meros oluvchi boshqa klass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# # Foydalanish
# circle = Circle(5)
# print("Doira yuzi:", circle.area())
# print("Doira perimetri:", circle.perimeter())
#
# rectangle = Rectangle(4, 6)
# print("To‘rtburchak yuzi:", rectangle.area())
# print("To‘rtburchak perimetri:", rectangle.perimeter())
#
# ✅ Natija:
# Doira yuzi: 78.5
# Doira perimetri: 31.400000000000002
# To‘rtburchak yuzi: 24
# To‘rtburchak perimetri: 20
#
#
# 👉 Bu yerda Shape abstrakt klassi faqat interfeys rolini bajaradi. U obyekt yaratmaydi.
# 👉 Lekin Circle va Rectangle klasslari uni meros qilib, metodlarni o‘zicha yozib chiqadi.
#
# 🔹 Abstraksiyaning afzalliklari
#
# Kod modularligi – murakkab kodni soddalashtiradi.
#
# O‘qilishi oson – foydalanuvchi faqat kerakli metodlarni ko‘radi.
#
# Kodni kengaytirish oson – yangi klass qo‘shish mumkin.
#
# Xavfsizlik – keraksiz yoki ichki tafsilotlar yashiriladi.
#
# 🔹 Abstraksiya vs Inkapsulyatsiya
#
# Ko‘pincha chalkash tushunchalar:
#
# 	Abstraksiya	Inkapsulyatsiya
# Maqsadi	Keraksiz tafsilotni yashirish	Ma’lumotni tashqi ta’sirdan himoya qilish
# Qanday ishlaydi	Abstract class, interface orqali	Private/protected attributlar orqali
# Foydalanuvchi uchun	Faqat kerakli metodlar ko‘rinadi	Faqat ruxsat etilgan joydan foydalaniladi
# 🔹 Django va Abstraksiya
#
# Django’da ham abstraksiya ishlatiladi:
#
# Model klassi abstrakt bo‘lishi mumkin (abstract = True).
#
# Bu umumiy fieldlarni meros qilib olishga yordam beradi.
#
# from django.db import models
#
# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True  # bu klassdan to‘g‘ridan-to‘g‘ri jadval yaratilmaydi
#
# class Product(BaseModel):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#
#
# 👉 Bu yerda BaseModel abstrakt klass. Uni jadval sifatida DB’da ko‘rmaymiz, lekin created_at va updated_at har bir Productda avtomatik ishlaydi.
#
# 🔹 Xulosa
#
# Abstraksiya — bu OOP’ning asosiy prinsipi.
#
# U keraksiz detallarni yashiradi, foydalanuvchiga faqat kerakli narsani ko‘rsatadi.
#
# Python’da abc moduli orqali abstrakt klasslar yoziladi.
#
# Django’da abstract = True orqali model abstraksiyasi qilinadi.
#
# Afzalliklari: xavfsizlik, kod soddaligi, kengaytirilish imkoniyati.