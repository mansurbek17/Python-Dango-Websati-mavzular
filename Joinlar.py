# 📘 SQL JOIN — Jadval va ma’lumotlarni bog‘lash
# 1. JOIN nima?
#
# JOIN — SQL’da ikki yoki undan ko‘p jadvallarni umumiy ustun (key) orqali bog‘lab, yagona natija chiqarish uchun ishlatiladi.
#
# 👉 Masalan, sizda:
#
# students jadvali (talabalar haqida)
#
# groups jadvali (guruhlar haqida)
#
# Agar talabalar qaysi guruhda o‘qishini ko‘rmoqchi bo‘lsangiz, ikkala jadvalni JOIN qilishingiz kerak.
#
# 2. JOIN turlari
#
# SQL’da asosan 5 xil JOIN bor:
#
# INNER JOIN
#
# LEFT JOIN (LEFT OUTER JOIN)
#
# RIGHT JOIN (RIGHT OUTER JOIN)
#
# FULL JOIN (FULL OUTER JOIN)
#
# CROSS JOIN
#
# 🔹 1) INNER JOIN
#
# Faqat mos keladigan yozuvlarni chiqaradi.
#
# Ikkala jadvalda ham mos keluvchi qiymat bo‘lsa, natijaga kiradi.
#
# Sintaksis:
#
# SELECT s.name, g.group_name
# FROM students s
# INNER JOIN groups g
# ON s.group_id = g.id;
#
#
# 👉 Natija: faqat guruhga biriktirilgan talabalar chiqadi. Guruhsiz talabalar chiqmaydi.
#
# 🔹 2) LEFT JOIN
#
# Chap jadvaldagi hamma yozuvlar chiqadi.
#
# Agar o‘ng jadvalda mos yozuv bo‘lmasa → NULL bo‘ladi.
#
# Sintaksis:
#
# SELECT s.name, g.group_name
# FROM students s
# LEFT JOIN groups g
# ON s.group_id = g.id;
#
#
# 👉 Natija: hamma talabalar chiqadi. Guruhsiz talabalar uchun group_name = NULL bo‘ladi.
#
# 🔹 3) RIGHT JOIN
#
# O‘ng jadvaldagi hamma yozuvlar chiqadi.
#
# Chap jadvalda mos yozuv bo‘lmasa → NULL bo‘ladi.
#
# Sintaksis:
#
# SELECT s.name, g.group_name
# FROM students s
# RIGHT JOIN groups g
# ON s.group_id = g.id;
#
#
# 👉 Natija: hamma guruhlar chiqadi. Agar guruhda talaba bo‘lmasa → student.name = NULL.
#
# 🔹 4) FULL JOIN
#
# Har ikkala jadvaldagi barcha yozuvlar chiqadi.
#
# Mos kelmasa → NULL bo‘ladi.
#
# Sintaksis:
#
# SELECT s.name, g.group_name
# FROM students s
# FULL JOIN groups g
# ON s.group_id = g.id;
#
#
# 👉 Natija: hamma talabalar + hamma guruhlar chiqadi. Guruhsiz talaba va talabasisiz guruh ham chiqadi.
#
# 🔹 5) CROSS JOIN
#
# Ikkala jadvaldagi hamma yozuvlarni kombinatsiya qiladi.
#
# Matematikada “Dekart ko‘paytma” deyiladi.
#
# Sintaksis:
#
# SELECT s.name, g.group_name
# FROM students s
# CROSS JOIN groups g;
#
#
# 👉 Natija: Har bir talaba har bir guruh bilan bog‘lanadi (agar 10 ta talaba va 5 ta guruh bo‘lsa → 50 ta kombinatsiya chiqadi).
#
# 3. JOIN’larni taqqoslash jadvali
# JOIN turi	Natija
# INNER JOIN	Faqat mos keladigan yozuvlar
# LEFT JOIN	Chap jadvaldagi hamma yozuvlar + mos kelganlari
# RIGHT JOIN	O‘ng jadvaldagi hamma yozuvlar + mos kelganlari
# FULL JOIN	Har ikkala jadvaldagi hamma yozuvlar (mos kelmaganlar ham)
# CROSS JOIN	Har bir yozuvni ikkinchisining hamma yozuvi bilan kombinatsiya qiladi
# 4. Hayotiy misol
#
# 📌 Tasavvur qiling, sizda:
#
# Talabalar jadvali (students):
#
# id	name	group_id
# 1	Ali	1
# 2	Vali	2
# 3	Gani	NULL
#
# Guruhlar jadvali (groups):
#
# id	group_name
# 1	101-A
# 2	102-B
# 3	103-C
#
# INNER JOIN → faqat Ali (101-A) va Vali (102-B) chiqadi.
# LEFT JOIN → Ali, Vali va Gani chiqadi (Gani uchun NULL).
# RIGHT JOIN → Ali, Vali va 103-C chiqadi (NULL bilan).
# FULL JOIN → Ali, Vali, Gani va 103-C chiqadi.
# CROSS JOIN → 3 ta student × 3 ta group = 9 ta natija chiqadi.
#
# 📌 Xulosa
#
# JOIN → jadvallarni umumiy ustun orqali bog‘lash uchun ishlatiladi.
#
# INNER JOIN → faqat mos yozuvlar.
#
# LEFT JOIN → chap jadval to‘liq chiqadi.
#
# RIGHT JOIN → o‘ng jadval to‘liq chiqadi.
#
# FULL JOIN → har ikkisi chiqadi.
#
# CROSS JOIN → barcha kombinatsiyalarni chiqaradi.