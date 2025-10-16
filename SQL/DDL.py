# DDL – bu Data Definition Language. U ma’lumotlar bazasi tuzilmasi bilan ishlaydi.
# # Masalan, yangi jadval yaratish (CREATE), ustun qo‘shish
# # yoki o‘chirish (ALTER), a o‘chirish (DROP), jadvalni tozalash (TRUNCATE)
# # kabi amallarni bajaradi. Bu buyruqlar ma’lumot bilan emas, balki strukturasi bilan ishlaydi.”
#
#===============================================================================
# 📘 DDL — Data Definition Language
# 🔹 DDL nima?
#===============================================================================
# DDL – bu SQL buyruqlari to‘plami bo‘lib, ular ma’lumotlar bazasi obyektlarini 
# yaratish, o‘zgartirish va o‘chirish uchun ishlatiladi.
# Obyektlarga quyidagilar kiradi:
# ==============================================================================
# 👉 Ya’ni DDL tuzilma (strukturani) boshqaradi, ma’lumotni emas.
# ==============================================================================
# 🔑 DDL komandalar ro‘yxati
#===============================================================================
# 1️⃣ CREATE
# 📌 Misol: Yangi jadval yaratish:
#==================================================================
# CREATE TABLE Students (
#     id INT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INT,
#     email VARCHAR(100) UNIQUE
# );
# ==================================================================
# Izoh:
# PRIMARY KEY → har bir yozuv uchun yagona identifikator.
# NOT NULL → qiymat bo‘lishi shart.
# UNIQUE → qiymat takrorlanmasligi kerak.
#=================================================================
# 2️⃣ ALTER
# Mavjud obyekt tuzilishini o‘zgartiradi.
# 📌 Misollar:
# Ustun qo‘shish:
# ALTER TABLE Students ADD address VARCHAR(150);
# Ustun turini o‘zgartirish:
# ALTER TABLE Students ALTER COLUMN age TYPE SMALLINT;
# Ustunni o‘chirish:
# ALTER TABLE Students DROP COLUMN email;
# ================================================================
# 3️⃣ DROP
# Obyektni butunlay o‘chiradi (jadval, baza, view).
# 📌 Misollar:
# Jadvalni o‘chirish:
# DROP TABLE Students;
# Bazani o‘chirish:
# DROP DATABASE UniversityDB;
# ⚠️ Eslatma: DROP buyruqni ishlatsangiz, ichidagi barcha ma’lumot 
# ham butunlay o‘chadi va qaytarib bo‘lmaydi.
#=================================================================
# 4️⃣ TRUNCATE
# Jadval ichidagi hamma yozuvlarni tozalaydi, lekin jadval tuzilmasi 
# o‘zgarmaydi.
# 📌 Misol:
# TRUNCATE TABLE Students;
# Izoh:
# DELETE bilan farqi → DELETE shart (WHERE) bilan ishlaydi, TRUNCATE esa 
# hammasini birdaniga o‘chiradi.
# TRUNCATE tezroq ishlaydi, lekin tranzaksiya bo‘lmasa, qaytarib bo‘lmaydi.
#===================================================================
# 5️⃣ RENAME (ba’zi DBMSlarda mavjud)
#
# Jadval yoki ustun nomini o‘zgartirish.
#
# 📌 Misol (Oracle/PostgreSQL):
#
# ALTER TABLE Students RENAME TO Pupils;
#====================================================================
# 6️⃣ COMMENT (qo‘llab-quvvatlasa)
#
# Jadval yoki ustunga izoh qo‘shadi.
#
# 📌 Misol (PostgreSQL):
#
# COMMENT ON COLUMN Students.age IS 'Talabaning yoshi';
#
# ⚖️ DDL va DML farqi
# 	DDL	DML
# Vazifasi	Tuzilmani boshqarish (jadval yaratish, o‘zgartirish)	
# Ma’lumotlarni boshqarish (qo‘shish, o‘chirish, yangilash) Komandalar	
# CREATE, ALTER, DROP, TRUNCATE, RENAME	INSERT, UPDATE, DELETE
# Rollback	Odatda rollback qilib bo‘lmaydi	Rollback qilish mumkin
# 📝 Xulosa
# DDL – bu ma’lumotlar bazasi strukturasi bilan ishlaydigan buyruqlar.
# Asosiy komandalar: CREATE, ALTER, DROP, TRUNCATE, RENAME, COMMENT.
# DDL orqali siz jadval yaratishingiz, ustun qo‘shishingiz, jadvalni 
# o‘chirishingiz yoki tozalashingiz mumkin.
#
# Bu buyruqlar odatda tranzaksiyasiz ishlaydi va bajarilgandan keyin qaytarib bo‘lmaydi.
