# Django REST Framework (DRF) haqida to‘liq tushuncha
# 1️⃣ DRF nima?
#
# DRF – bu Django REST Framework qisqartmasi.
#
# U Django asosida RESTful API yaratishga mo‘ljallangan kuchli kutubxona.
#
# Oddiy Django’da API yozish qiyin, DRF esa bu jarayonni osonlashtiradi va ko‘plab qulayliklar beradi.
#
# 👉 Qisqasi: DRF – bu Django’da backend API yozishni tezlashtiradigan framework.
#
# 2️⃣ DRF asosiy vazifalari
#
# REST API yaratish
#
# JSON formatida ma’lumot yuborish va qabul qilish.
#
# Mobil ilovalar, frontend (React, Vue, Angular) bilan ishlash.
#
# Serializer’lar
#
# Modeldagi obyektlarni Python → JSON va JSON → Python ko‘rinishiga o‘tkazadi.
#
# Viewlar (APIView, GenericView, ViewSet)
#
# API yozishning turli darajadagi qulay usullari.
#
# Authentication & Permission
#
# Token, JWT, Session authentication orqali foydalanuvchini tekshirish.
#
# Kimga ruxsat beriladi, kimga taqiqlanadi – boshqarish.
#
# Browsable API
#
# DRF API’ni brauzerda chiroyli ko‘rinishda ishlatish imkoniyatini beradi (test qilish oson).
#
# 3️⃣ DRF ishlash prinsipi (asosiy oqim)
# (a) Model yaratish
# # models.py
# from django.db import models
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
# (b) Serializer yozish
# # serializers.py
# from rest_framework import serializers
# from .models import Student
#
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
#
#
# 👉 Bu serializer Student modelini JSON formatga o‘tkazadi.
#
# (c) View yozish
# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
#
# class StudentListView(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#
# 👉 Bu view GET so‘roviga barcha talabalarni JSON ko‘rinishida qaytaradi.
#
# (d) URL sozlash
# # urls.py
# from django.urls import path
# from .views import StudentListView
#
# urlpatterns = [
#     path('students/', StudentListView.as_view(), name='student-list'),
# ]
#
#
# 👉 Endi http://127.0.0.1:8000/students/ ga kirilsa, JSON qaytadi.
#
# 4️⃣ DRF’da ishlatiladigan asosiy komponentlar
# 1. Serializer’lar
#
# Model ma’lumotlarini JSON ga aylantiradi.
#
# Validatsiya qiladi (to‘g‘ri kiritilganini tekshiradi).
#
# 2. APIView
#
# REST API yozish uchun class-based view.
#
# get(), post(), put(), delete() metodlari yoziladi.
#
# 3. Generic Views va Mixins
#
# API yozishni tezlashtiradi.
#
# Masalan: ListCreateAPIView, RetrieveUpdateDestroyAPIView.
#
# from rest_framework.generics import ListCreateAPIView
# from .models import Student
# from .serializers import StudentSerializer
#
# class StudentListCreateView(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# 👉 Bu class GET (list) va POST (create) metodlarini avtomatik ishlatadi.
#
# 4. ViewSets va Routers
#
# CRUD amallarni bir joyda yozib beradi.
#
# URL’larni ham avtomatik generatsiya qiladi.
#
# from rest_framework.viewsets import ModelViewSet
#
# class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# urls.py da:
#
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet
#
# router = DefaultRouter()
# router.register('students', StudentViewSet)
#
# urlpatterns = router.urls
#
#
# 👉 Endi /students/ orqali CRUD amallar tayyor bo‘ladi.
#
# 5️⃣ DRF’da Authentication & Permissions
#
# Authentication → foydalanuvchini aniqlash.
#
# BasicAuth, TokenAuth, JWTAuth, SessionAuth.
#
# Permissions → kimga ruxsat, kimga yo‘qligini belgilash.
#
# IsAuthenticated, IsAdminUser, AllowAny, custom permissions.
#
# from rest_framework.permissions import IsAuthenticated
#
# class StudentListView(APIView):
#     permission_classes = [IsAuthenticated]
#
#
# 👉 Foydalanuvchi login qilmagan bo‘lsa, API ishlamaydi.
#
# 6️⃣ DRF afzalliklari
#
# Django bilan integratsiyasi juda kuchli.
#
# Kod yozish tezlashadi (ViewSets, Serializers, Routers).
#
# Browsable API → frontend yozmasdan ham API’ni test qilish mumkin.
# 
# Security (token, JWT, permissionlar).
#
# Har qanday frontend yoki mobil ilova bilan ishlaydi.
#
# ✅ Xulosa
#
# DRF – Django’da RESTful API yaratish uchun kuchli framework.
#
# Asosiy komponentlari: Serializer, View, Generic, ViewSet, Router, Permission, Authentication.
#
# JSON bilan ishlaydi, frontend va mobil ilovalar bilan integratsiyani osonlashtiradi.
#
# Oddiy Django’dan farqi – DRF API’ni maxsus vositalar bilan osonroq va tezroq yaratib beradi.