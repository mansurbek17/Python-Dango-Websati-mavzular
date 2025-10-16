# 📘 DCL (Data Control Language) — Ma’lumotlarga kirish huquqini boshqarish tili
# 1. DCL nima?
#
# DCL — bu SQL’ning bir qismi bo‘lib, foydalanuvchilarning ma’lumotlar bazasiga bo‘lgan huquqlarini boshqarish uchun ishlatiladi.
# Ya’ni, DCL yordamida biz kimga qanday ruxsat beramiz, kimni huquqini olib tashlaymiz yoki kimga cheklov qo‘yamiz — shularni nazorat qilamiz.

# Xavfsizlikni ta’minlash — faqat kerakli odamlar kerakli ma’lumotni ko‘ra oladi.
#
# Maxfiylikni boshqarish — masalan, ishchilarning maoshini faqat HR ko‘ra oladi, boshqa odamlar ko‘ra olmaydi.
#
# Huquqlarni taqsimlash — kimdir ma’lumot qo‘shishi mumkin, kimdir faqat o‘qiydi, kimdir esa o‘chirishi mumkin.
#
# Administratorlik nazorati — superadmin barcha huquqlarni boshqaradi.
#
# 3. DCL’dagi asosiy komandalar
# 🔹 1) GRANT
#
# Foydalanuvchiga yangi huquqlar berish uchun ishlatiladi.
#
# Masalan, biror kishiga faqat o‘qish huquqi yoki yozish huquqini berishimiz mumkin.
#
# Sintaksis:
#
# GRANT huquqlar
# ON obyekt
# TO foydalanuvchi;
#
#
# Misol:
#
# GRANT SELECT, INSERT
# ON employees
# TO student1;
#
#
# 👉 Bu kod student1 foydalanuvchisiga employees jadvalidan o‘qish (SELECT) va qo‘shish (INSERT) huquqini beradi.
#
# 🔹 2) REVOKE
#
# Avval berilgan huquqlarni bekor qilish uchun ishlatiladi.
#
# Sintaksis:
#
# REVOKE huquqlar
# ON obyekt
# FROM foydalanuvchi;
#
#
# Misol:
#
# REVOKE INSERT
# ON employees
# FROM student1;
#
#
# 👉 Bu kod student1 foydalanuvchisidan employees jadvaliga yozish (INSERT) huquqini olib tashlaydi.
#
# 🔹 3) DENY (faqat ayrim DBMSlarda, masalan MS SQL Server)
#
# Aniq taqiqlash uchun ishlatiladi.
#
# Farqi shundaki:
#
# GRANT → huquq beradi
#
# REVOKE → huquqni olib tashlaydi
#
# DENY → ochiqchasiga huquqni taqiqlaydi
#
# Misol:
#
# DENY DELETE
# ON employees
# TO student1;
#
#
# 👉 Bu kod student1 foydalanuvchisiga hech qachon employees jadvalidan o‘chirish (DELETE) qilishga ruxsat bermaydi.
#
# 4. DCL’da huquq turlari
#
# DCL orqali quyidagi huquqlarni berish mumkin:
#
# SELECT → jadvaldan o‘qish huquqi
#
# INSERT → jadvalga ma’lumot qo‘shish huquqi
#
# UPDATE → jadvalni yangilash huquqi
#
# DELETE → jadvaldan ma’lumot o‘chirish huquqi
#
# ALL PRIVILEGES → barcha huquqlarni berish
#
# EXECUTE → saqlangan protsedura va funksiyalarni bajarish huquqi
#
# 5. Real hayotiy misol
#
# Tasavvur qiling, sizda universitet bazasi bor:
#
# student jadvali → talabalar haqida
#
# teacher jadvali → o‘qituvchilar haqida
#
# 👨‍🏫 O‘qituvchi → faqat student jadvalidan ma’lumot ko‘ra oladi.
# 👨‍🎓 Talaba → hech narsa o‘zgartira olmaydi, faqat o‘z ma’lumotini ko‘rishi mumkin.
# 👨‍💻 Admin → barcha huquqlarga ega.
#
# Misol kodlar:
#
# -- O‘qituvchiga SELECT beramiz
# GRANT SELECT ON student TO teacher;
#
# -- Talabaga faqat SELECT huquqi
# GRANT SELECT ON student TO student1;
#
# -- Talabaga yangilash huquqini taqiqlaymiz
# DENY UPDATE ON student TO student1;
#
# -- Admin uchun barcha huquqlar
# GRANT ALL PRIVILEGES ON student TO admin;
#
# 6. DCL’ning afzalliklari
#
# ✅ Ma’lumot xavfsizligini ta’minlaydi
# ✅ Kim nima qilishi mumkinligini aniq belgilab beradi
# ✅ Ma’lumotlar ustida nazoratni markazlashtiradi
# ✅ Maxfiylik va xavfsizlik siyosatini amalga oshiradi
#
# 📌 Xulosa
#
# DCL → huquqlarni boshqarish tili.
#
# Asosiy komandalar: GRANT, REVOKE, DENY.
#
# Vazifasi: foydalanuvchilarga ruxsat berish, ruxsatni bekor qilish, yoki taqiqlash.
#
# Hayotiy qo‘llanishi: foydalanuvchilarni turli rollarga bo‘lib, ma’lumotlarni himoya qilish.