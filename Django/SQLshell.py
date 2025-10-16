# SQL Shell (psql) nima?
#
# SQL Shell (psql) — bu PostgreSQL ma’lumotlar bazasi boshqaruv tizimida ishlatiladigan buyruqlar qatori interfeysi (CLI).
#
# U orqali foydalanuvchi PostgreSQL serveriga ulanib, SQL buyruqlarini bajarishi, ma’lumotlar bazasini boshqarishi, jadvallar yaratishi, o‘chirish va tahrirlash kabi amallarni bajarishi mumkin.
#
# SQL Shell odatda PostgreSQL o‘rnatilganda avtomatik tarzda o‘rnatiladi.
#
# SQL Shell’ning asosiy imkoniyatlari
#
# Serverga ulanish
#
# PostgreSQL o‘rnatilgandan keyin SQL Shell ochilganda, sizdan quyidagi ma’lumotlarni so‘raydi:
#
# Server: odatda localhost yoki server IP manzili.
#
# Database: ulanish kerak bo‘lgan ma’lumotlar bazasi nomi.
#
# Port: standart port 5432.
#
# Username: PostgreSQL foydalanuvchi nomi (odatda postgres).
#
# Password: foydalanuvchi paroli.
#
# SQL buyruqlarini bajarish
#
# Masalan:
#
# CREATE DATABASE testdb;
# \c testdb
# CREATE TABLE student (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50),
#     age INT
# );
# INSERT INTO student (name, age) VALUES ('Ali', 20);
# SELECT * FROM student;
#
#
# PostgreSQL’ning maxsus buyruqlari (faqat psqlda ishlaydi):
#
# \l — mavjud bazalarni ko‘rish
#
# \c dbname — bazaga ulanish
#
# \dt — jadvallar ro‘yxatini ko‘rish
#
# \d tablename — jadval strukturasi haqida ma’lumot olish
#
# \du — foydalanuvchilarni ko‘rish
#
# \q — SQL Shell’dan chiqish
#
# Interaktiv imkoniyatlar
#
# Buyruqlarni yozishda avto-to‘ldirish (Tab tugmasi bilan).
#
# SQL natijalarini formatlab ko‘rsatish.
#
# Buyruqlar tarixini saqlash va qayta chaqirish.
#
# SQL Shell (psql)ning afzalliklari
#
# Yengil va tezkor — grafik interfeys talab qilmaydi.
#
# Keng imkoniyatli — faqat SQL buyruqlari emas, balki PostgreSQL’ga xos buyruqlarni ham bajaradi.
#
# Masofaviy boshqaruv — boshqa serverdagi PostgreSQL’ga ulanib ishlash mumkin.
#
# Ma’lumotlarni boshqarish — foydalanuvchilar, rollar, ruxsatlar, tranzaksiyalarni boshqarish mumkin.
#
# SQL Shell va boshqa vositalar farqi
#
# SQL Shell (psql) — bu CLI vosita.
#
# pgAdmin — PostgreSQL uchun grafik interfeys (GUI).
#
# Ikkalasi ham bir xil ishlaydi, lekin biri buyruq qatori asosida, ikkinchisi esa grafik interfeys orqali.
#
# ✅ Xulosa: SQL Shell (psql) – PostgreSQL foydalanuvchilari uchun eng muhim vosita bo‘lib, u orqali bazaga ulanib, SQL va maxsus buyruqlar yordamida to‘liq boshqaruv amalga oshiriladi.