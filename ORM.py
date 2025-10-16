# ORM (Object Relational Mapping) haqida to‘liq tushuncha
# 1️⃣ ORM nima?
#
# ORM — bu Object-Relational Mapping degan atama bo‘lib, u obyektga yo‘naltirilgan dasturlash tillari (Python, Java, C#) va relatsion ma’lumotlar bazalari (PostgreSQL, MySQL, SQLite) o‘rtasidagi ko‘prik hisoblanadi.
#
# Oddiy qilib aytganda:
#
# SQL yozish o‘rniga biz klasslar va obyektlar orqali bazani boshqaramiz.
#
# Ma’lumotlar bazasidagi jadval → class, ustun → atribut, qator → obyekt ga mos keladi.
#
# 👉 Bu degani, siz bazaga SQL yozib murojaat qilmasdan, oddiy Python kodida class va obyektlar bilan ishlaysiz.
#
# 2️⃣ ORMning asosiy maqsadi
#
# Kod va SQLni ajratish – SQL yozmasdan Python kodida ishlash.
#
# Xavfsizlik – SQL injection kabi hujumlardan himoya.
#
# Portativlik – agar bazani SQLite’dan PostgreSQL’ga o‘tkazsangiz, ko‘p kodni o‘zgartirmaysiz.
#
# OOP bilan integratsiya – hamma narsa obyektlar sifatida ko‘riladi.
#
# 3️⃣ Oddiy SQL va ORM farqi
# 📝 SQL bilan yozsak:
# -- Talabalar jadvalidan barcha yozuvlarni olish
# SELECT * FROM student WHERE age > 18;
#
# 📝 ORM (Django misolida) bilan yozsak:
# Student.objects.filter(age__gt=18)
#
#
# 👉 Ko‘rdingizmi, hech qanday SQL yo‘q. Barchasi Python obyektlari orqali.
#
# 4️⃣ ORM qanday ishlaydi?
#
# Model yaratamiz (class sifatida).
#
# Har bir class → jadvalga mos keladi.
#
# Har bir atribut → ustunga mos keladi.
#
# Har bir obyekt → jadval qatoriga mos keladi.
#
# from django.db import models
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     phone = models.CharField(max_length=20)
#
#
# Bu kod orqali student jadvali yaratiladi.
#
# name → VARCHAR(100)
#
# age → INTEGER
#
# phone → VARCHAR(20)
#
# 5️⃣ ORM orqali asosiy CRUD amallari
# 🔹 C → Create (yangi yozuv qo‘shish)
# student = Student(name="Ali", age=20, phone="998901234567")
# student.save()
#
#
# 👉 Bazaga yangi qator qo‘shiladi. SQL’da INSERT ga teng.
#
# 🔹 R → Read (o‘qish, select qilish)
# # Hammasini olish
# students = Student.objects.all()
#
# # Bitta talabani olish
# student = Student.objects.get(id=1)
#
# # Shart bilan filterlash
# students = Student.objects.filter(age__gt=18)
#
#
# 👉 SQL’da SELECT * FROM ... amallariga mos keladi.
#
# 🔹 U → Update (yangilash)
# student = Student.objects.get(id=1)
# student.age = 25
# student.save()
#
#
# 👉 SQL’da UPDATE student SET age=25 WHERE id=1 ga teng.
#
# 🔹 D → Delete (o‘chirish)
# student = Student.objects.get(id=1)
# student.delete()
#
#
# 👉 SQL’da DELETE FROM student WHERE id=1 ga teng.
#
# 6️⃣ ORM afzalliklari
#
# ✅ SQL yozishga hojat yo‘q.
# ✅ Turli bazalar bilan ishlash oson.
# ✅ Xavfsizlik yuqori (SQL injection’dan himoya).
# ✅ Kod OOP tamoyillariga asoslangan.
#
# 7️⃣ ORM kamchiliklari
#
# ❌ Juda katta loyihalarda murakkab SQL so‘rovlarini ORM’da yozish qiyin bo‘lishi mumkin.
# ❌ ORM biroz sekinroq ishlashi mumkin, chunki u oraliq qatlam.
# ❌ Har doim ham optimallashtirilgan SQL chiqarmaydi.
#
# 8️⃣ Xulosa
#
# ORM — bu ma’lumotlar bazasi bilan ishlashni yengillashtiradigan vosita.
#
# Django’da models.py orqali jadval yaratasiz va obyektlar bilan ishlagandek bazani boshqarasiz.
#
# CRUD amallari Python kodida yoziladi, SQL o‘zi avtomatik generatsiya qilinadi.