# Django Classlar haqida to‘liq tushuncha
#
# Django’da class tushunchasi markaziy o‘rin tutadi. Chunki Django obyektga yo‘naltirilgan dasturlash (OOP) asosida ishlaydi.
#
# Django loyihasida ishlatiladigan asosiy classlar quyidagilar:
#
# Model classlar – ma’lumotlar bazasi jadvallari uchun.
#
# View classlar (CBV – Class-Based Views) – sahifalarni boshqarish uchun.
#
# Form classlar – foydalanuvchi ma’lumotlarini olish va tekshirish uchun.
#
# Admin classlar – admin panelni sozlash uchun.
#
# Meta va boshqa ichki classlar – qo‘shimcha konfiguratsiyalar uchun.
#
# Endi bularni batafsil ko‘rib chiqamiz.
#
# 1️⃣ Model Classlar
#
# Django’da ma’lumotlar bazasi jadvallari models.py faylida class sifatida yoziladi.
#
# from django.db import models
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     phone = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# 🔎 Bu yerda:
#
# Student → jadval nomi.
#
# name, age, phone → ustunlar.
#
# Har bir obyekt → jadval qatori.
#
# 👉 Django ORM shu class orqali SQL yaratadi:
#
# CREATE TABLE student (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER,
#     phone VARCHAR(20)
# );
#
# 2️⃣ View Classlar (CBV – Class Based Views)
#
# Django’da ikki xil view mavjud:
#
# FBV (Function-Based Views) → oddiy def bilan yoziladi.
#
# CBV (Class-Based Views) → class yordamida yoziladi.
#
# Misol: FBV
# from django.http import HttpResponse
#
# def hello(request):
#     return HttpResponse("Salom Django!")
#
# Misol: CBV
# from django.http import HttpResponse
# from django.views import View
#
# class HelloView(View):
#     def get(self, request):
#         return HttpResponse("Salom Django Class!")
#
#
# 🔎 CBV afzalligi:
#
# Kod modulli va tartibli bo‘ladi.
#
# GET, POST, PUT, DELETE metodlarini alohida yozish mumkin.
#
# Mixins va Generic Views yordamida kodni qisqartirish mumkin.
#
# 3️⃣ Form Classlar
#
# Django’da foydalanuvchidan ma’lumot olish uchun forms.py da class yoziladi.
#
# from django import forms
#
# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     age = forms.IntegerField()
#     phone = forms.CharField(max_length=20)
#
#
# 🔎 Bu class:
#
# Foydalanuvchidan input olishni osonlashtiradi.
#
# Validatsiya (to‘g‘ri kiritilganini tekshirish) ni avtomatik bajaradi.
#
# Agar ModelForm ishlatsak, model bilan to‘g‘ridan-to‘g‘ri bog‘lash mumkin:
#
# from django.forms import ModelForm
# from .models import Student
#
# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'age', 'phone']
#
# 4️⃣ Admin Classlar
#
# Django admin panelini sozlash uchun classlar yoziladi.
#
# from django.contrib import admin
# from .models import Student
#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'age', 'phone')
#     search_fields = ('name',)
#     list_filter = ('age',)
#
# admin.site.register(Student, StudentAdmin)
#
#
# 🔎 Bu yerda:
#
# list_display → admin panelda ko‘rinadigan ustunlar.
#
# search_fields → qidirish uchun maydonlar.
#
# list_filter → filter menyusi.
#
# 5️⃣ Meta Class
#
# Model ichida ishlatiladigan ichki class bo‘lib, jadval nomi, tartiblash, huquqlar va boshqa konfiguratsiyalarni belgilaydi.
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#     class Meta:
#         db_table = "talabalar"
#         ordering = ['-age']
#         verbose_name = "Talaba"
#         verbose_name_plural = "Talabalar"
#
#
# 🔎 Bu yerda:
#
# db_table → bazadagi jadval nomi.
#
# ordering → natijalarni avtomatik tartiblash.
#
# verbose_name → admin panelda chiroyli nom.
#
# ✅ Xulosa
#
# Django’da classlar quyidagi vazifalarni bajaradi:
#
# Model classlar – bazani yaratadi va ORM bilan ishlaydi.
#
# View classlar – sahifa logikasini boshqaradi.
#
# Form classlar – foydalanuvchi ma’lumotini boshqaradi.
#
# Admin classlar – admin panelni sozlaydi.
#
# Meta class – modelning maxsus parametrlarini belgilaydi.