# 🟢 Django CRUD (Create, Read, Update, Delete)
# 1. CRUD nima?
#
# CRUD – bu ma’lumotlar bazasi bilan ishlashda eng muhim 4 ta asosiy amal:
#
# C – Create → Yangi yozuv (record) qo‘shish
#
# R – Read → Ma’lumotlarni olish (ko‘rish)
#
# U – Update → Mavjud ma’lumotlarni yangilash
#
# D – Delete → Ma’lumotlarni o‘chirish
#
# 👉 Django’da CRUD amallari ORM (Object Relational Mapping) orqali bajariladi. Bu esa SQL yozmasdan, faqat Python kodida ishlash imkonini beradi.
#
# 2. CRUD jarayonini amalga oshirish bosqichlari
#
# Django’da CRUD ni tushuntirish uchun oddiy Student modeli ustida ishlaymiz.
#
# 2.1. Model yaratish (Jadval)
# # models.py
# from django.db import models
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# 📌 Bu kod SQL’da quyidagi jadvalni hosil qiladi:
#
# CREATE TABLE student (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER,
#     email VARCHAR(254) UNIQUE
# );
#
# 3. CRUD amallari
# 🔹 3.1. CREATE (Yangi yozuv qo‘shish)
#
# Django ORM orqali yangi obyekt qo‘shishning 2 usuli bor:
#
# 1️⃣ .create() metodi bilan:
#
# Student.objects.create(name="Ali", age=20, email="ali@gmail.com")
#
#
# 2️⃣ Obyektni yaratib, .save() bilan saqlash:
#
# student = Student(name="Vali", age=22, email="vali@gmail.com")
# student.save()
#
#
# 👉 SQL’dagi ekvivalenti:
#
# INSERT INTO student (name, age, email) VALUES ('Ali', 20, 'ali@gmail.com');
#
# 🔹 3.2. READ (Ma’lumotlarni olish)
#
# 1️⃣ Hamma yozuvlarni olish:
#
# students = Student.objects.all()
#
#
# SQL:
#
# SELECT * FROM student;
#
#
# 2️⃣ Filtrlash:
#
# Student.objects.filter(age__gte=18)   # yoshi 18 dan katta
#
#
# SQL:
#
# SELECT * FROM student WHERE age >= 18;
#
#
# 3️⃣ Bitta yozuvni olish:
#
# student = Student.objects.get(id=1)
#
#
# SQL:
#
# SELECT * FROM student WHERE id=1;
#
# 🔹 3.3. UPDATE (Ma’lumotlarni yangilash)
# student = Student.objects.get(id=1)
# student.age = 25
# student.save()
#
#
# SQL’da bu shunday bo‘ladi:
#
# UPDATE student SET age=25 WHERE id=1;
#
# 🔹 3.4. DELETE (Ma’lumotlarni o‘chirish)
# student = Student.objects.get(id=1)
# student.delete()
#
#
# SQL’dagi ekvivalenti:
#
# DELETE FROM student WHERE id=1;
#
# 4. CRUD ni View va Template orqali ishlatish
#
# Django’da CRUD faqat ORM orqali emas, balki View + Template bilan ham bajariladi.
#
# 4.1. Create View
# # views.py
# from django.shortcuts import render, redirect
# from .models import Student
#
# def add_student(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         age = request.POST['age']
#         email = request.POST['email']
#         Student.objects.create(name=name, age=age, email=email)
#         return redirect('student_list')
#     return render(request, 'add_student.html')
#
# 4.2. Read View
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'student_list.html', {'students': students})
#
# 4.3. Update View
# def update_student(request, id):
#     student = Student.objects.get(id=id)
#     if request.method == "POST":
#         student.name = request.POST['name']
#         student.age = request.POST['age']
#         student.email = request.POST['email']
#         student.save()
#         return redirect('student_list')
#     return render(request, 'update_student.html', {'student': student})
#
# 4.4. Delete View
# def delete_student(request, id):
#     student = Student.objects.get(id=id)
#     student.delete()
#     return redirect('student_list')
#
# 5. CRUD ning afzalliklari Django’da
#
# ✅ SQL yozishga hojat yo‘q
# ✅ Xavfsizlik yuqori (SQL Injectiondan himoya)
# ✅ Kod tushunarli va ixcham
# ✅ Bitta kod MySQL, PostgreSQL, SQLite’da ham ishlaydi
#
# ✅ Xulosa
#
# Django CRUD — bu ma’lumotlar bazasi bilan ishlashning asosiy tamoyili.
# 
# Create – .create() yoki .save()
#
# Read – .all(), .get(), .filter()
#
# Update – .save()
#
# Delete – .delete()
#
# CRUD jarayonlari ORM, Views, Templates orqali amalga oshiriladi