#  “DML – bu Data Manipulation Language. U jadval ichidagi ma’lumotlarni qo‘shish (INSERT),
# # o‘zgartirish (UPDATE), o‘chirish (DELETE) va kerak bo‘lsa birlashtirish (MERGE) uchun ishlatiladi.
# # DML tranzaksiyaga kiradi, ya’ni COMMIT va ROLLBACK orqali boshqariladi.”
#============================================
# 📘 DML — Data Manipulation Language
# 🔹 DML nima?
# DML – bu SQL buyruqlari guruhi bo‘lib, ular jadval ichidagi ma’lumotlar bilan ishlash uchun qo‘llaniladi.
# 👉 Ya’ni DDL struktura (jadval, ustunlar) bilan ishlasa, DML ichidagi ma’lumotlarni qo‘shadi, yangilaydi, o‘chiradi.
#
# DML orqali CRUD amallari bajariladi:
#
# C (Create) → INSERT
#
# R (Read) → SELECT (ko‘pincha DQLga kiradi, lekin ba’zi manbalarda DML tarkibida qaraladi)
#
# U (Update) → UPDATE
#
# D (Delete) → DELETE
#=======================================================
# 🔑 DML komandalar ro‘yxati
# 1️⃣ INSERT – Yangi ma’lumot qo‘shish
#
# 👉 Jadvalga yangi yozuv kiritadi.
#
# 📌 Misollar:
#
# Bitta yozuv qo‘shish:
#
# INSERT INTO Students (id, name, age)
# VALUES (1, 'Ali', 20);
#
#
# Barcha ustunlarga qiymat qo‘shish (ustunlarni ko‘rsatmasdan):
#
# INSERT INTO Students
# VALUES (2, 'Hasan', 22);
#
#
# Bir nechta yozuvni birdaniga qo‘shish:
#
# INSERT INTO Students (id, name, age) VALUES
# (3, 'Dilnoza', 19),
# (4, 'Otabek', 23);
#=================================================
# 2️⃣ UPDATE – Ma’lumotni yangilash
#
# 👉 Mavjud yozuvni o‘zgartirish uchun ishlatiladi.
#
# 📌 Misollar:
#
# Bitta ustunni yangilash:
#
# UPDATE Students
# SET age = 21
# WHERE id = 1;
#
#
# Bir nechta ustunni yangilash:
#
# UPDATE Students
# SET name = 'Hasanboy', age = 23
# WHERE id = 2;
#
#
# ⚠️ Eslatma: WHERE qo‘ymasangiz, hamma yozuv yangilanadi!
#
# UPDATE Students SET age = 25;  -- Barcha studentlar yoshi 25 bo‘lib ketadi
#========================================================
# 3️⃣ DELETE – Ma’lumotni o‘chirish
#
# 👉 Jadvaldan yozuvlarni o‘chiradi.
#
# 📌 Misollar:
#
# Bitta yozuvni o‘chirish:
#
# DELETE FROM Students
# WHERE id = 3;
#
#
# Shart bo‘yicha yozuvlarni o‘chirish:
#
# DELETE FROM Students
# WHERE age < 20;
#
#
# Barcha yozuvlarni o‘chirish (jadval strukturasi qoladi):
#
# DELETE FROM Students;
#
#
# ⚠️ Eslatma: DELETE va TRUNCATE farqli.
#
# DELETE → yozuvlarni shart bilan yoki shartsiz o‘chiradi, tranzaksiya qo‘llab-quvvatlaydi (ROLLBACK mumkin).
#
# TRUNCATE (DDL) → hamma yozuvni birdan o‘chiradi, ROLLBACK qila olmaymiz.
#=================================================================================
# 4️⃣ MERGE – Ma’lumotlarni birlashtirish (Upsert)
#
# 👉 INSERT va UPDATE kombinatsiyasi.
#
# Agar yozuv mavjud bo‘lsa → yangilanadi.
#
# Agar mavjud bo‘lmasa → qo‘shiladi.
#
# 📌 Misol (Oracle / SQL Server):
#
# MERGE INTO Students AS target
# USING NewStudents AS source
# ON target.id = source.id
# WHEN MATCHED THEN
#     UPDATE SET target.age = source.age
# WHEN NOT MATCHED THEN
#     INSERT (id, name, age)
#     VALUES (source.id, source.name, source.age);
#
# ⚖️ DML xususiyatlari
#
# Jadvaldagi ma’lumotlar bilan ishlaydi, strukturaga tegmaydi.
#
# Tranzaksiyaga kiradi → COMMIT yoki ROLLBACK qilish mumkin.
#
# WHERE sharti bilan ehtiyot bo‘lish kerak, aks holda barcha yozuvlar o‘zgarishi mumkin.
#
# 📊 DML buyruqlari taqqoslash
# Buyruq	Vazifasi	Misol
# INSERT	Yangi yozuv qo‘shish	INSERT INTO Students VALUES (1, 'Ali', 20);
# UPDATE	Mavjud yozuvni yangilash	UPDATE Students SET age = 21 WHERE id = 1;
# DELETE	Yozuvni o‘chirish	DELETE FROM Students WHERE id = 1;
# MERGE	Yozuvni qo‘shish yoki yangilash	MERGE INTO ...
# 📝 Xulosa
#
# DML (Data Manipulation Language) – bu SQL komandalar guruhi bo‘lib, jadval ichidagi ma’lumotlarni boshqaradi.
#
# Asosiy komandalar: INSERT, UPDATE, DELETE, MERGE.
#
# Tranzaksiyaga kiradi → ROLLBACK va COMMIT ishlatish mumkin.
#
# Ehtiyot bo‘lish kerak: WHERE sharti qo‘yilmasa, barcha yozuvlar o‘zgarib ketadi.
#
#
#