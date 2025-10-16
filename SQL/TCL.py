# 📘 TCL (Transaction Control Language) — Tranzaksiyalarni boshqarish tili
# 1. TCL nima?
#
# TCL — bu SQL’ning bir bo‘lagi bo‘lib, tranzaksiyalarni (transaction) boshqarish uchun ishlatiladi.
# Tranzaksiya — bu ma’lumotlar bazasida bajariladigan amallar ketma-ketligi, ya’ni bir butun operatsiya sifatida ko‘riladi.
#
# 👉 Masalan: bankdagi pul o‘tkazmasi:
#
# Bir hisobdan pul yechiladi
#
# Ikkinchi hisobga qo‘shiladi
#
# Agar bu jarayonning bir qismi bajarilib, ikkinchisi bajarilmasa — ma’lumotlar noto‘g‘ri bo‘lib qoladi. Shu uchun tranzaksiya ishlatiladi.
#
# 2. Tranzaksiyaning asosiy xususiyatlari (ACID printsipi)
#
# TCL ishlaganda tranzaksiyalar quyidagi xususiyatlarga ega bo‘ladi:
#
# Atomicity (Atomarlik) → tranzaksiya to‘liq bajariladi yoki umuman bajarilmaydi.
#
# Consistency (Izchillik) → tranzaksiya bazani izchil holatda qoldiradi.
#
# Isolation (Izolyatsiya) → bir vaqtning o‘zida bir nechta tranzaksiya bajarilsa ham, ular bir-biriga xalaqit bermaydi.
#
# Durability (Mustahkamlik) → tranzaksiya tasdiqlangach (COMMIT), ma’lumotlar doimiy saqlanadi, hatto tizim o‘chib qolsa ham.
#
# 3. TCL’dagi asosiy komandalar
# 🔹 1) COMMIT
#
# Tranzaksiyani yakunlaydi va barcha o‘zgarishlarni saqlab qo‘yadi.
#
# Bu komandadan keyin qaytarib bo‘lmaydi.
#
# Misol:
#
# UPDATE accounts
# SET balance = balance - 1000
# WHERE id = 1;
#
# UPDATE accounts
# SET balance = balance + 1000
# WHERE id = 2;
#
# COMMIT;
#
#
# 👉 Bu yerda birinchi hisobdan 1000 yechib, ikkinchi hisobga qo‘shdik. COMMIT qilgandan keyin bu o‘zgarishlar saqlanib qoladi.
#
# 🔹 2) ROLLBACK
#
# Agar tranzaksiya davomida xatolik chiqsa, avvalgi holatga qaytaradi.
#
# Faqat COMMIT qilinmagan o‘zgarishlarni bekor qiladi.
#
# Misol:
#
# UPDATE accounts
# SET balance = balance - 1000
# WHERE id = 1;
#
# -- Xatolik chiqdi, ikkinchisiga yozilmadi
#
# ROLLBACK;
#
#
# 👉 Bu kod bajarilgach, 1-hisobdan yechilgan pul qaytadi, chunki tranzaksiya bekor qilindi.
#
# 🔹 3) SAVEPOINT
#
# Tranzaksiya ichida oraliq nuqta (checkpoint) qo‘yadi.
#
# Keyinchalik ROLLBACK qilganda, butun tranzaksiyani emas, balki shu nuqtadan keyingi qismini bekor qiladi.
#
# Misol:
#
# BEGIN TRANSACTION;
#
# UPDATE accounts SET balance = balance - 500 WHERE id = 1;
# SAVEPOINT sp1;
#
# UPDATE accounts SET balance = balance + 500 WHERE id = 2;
# SAVEPOINT sp2;
#
# ROLLBACK TO sp1;
#
# COMMIT;
#
#
# 👉 Bu yerda sp1 nuqtasiga qaytganimizda, 1-hisobdan 500 pul kamayganicha qoladi, lekin ikkinchisiga qo‘shilmagan bo‘ladi.
#
# 🔹 4) SET TRANSACTION
#
# Tranzaksiyaning xususiyatlarini belgilash uchun ishlatiladi (masalan, izolatsiya darajasi).
#
# Misol:
#
# SET TRANSACTION READ WRITE;
#
#
# 👉 Bu yerda tranzaksiya o‘qish va yozishga ruxsat beradi.
#
# 4. TCL jarayonining bosqichlari
#
# Tranzaksiya boshlanadi → (BEGIN TRANSACTION yoki avtomatik).
#
# Amallar bajariladi → (INSERT, UPDATE, DELETE).
#
# Agar hammasi to‘g‘ri bo‘lsa → COMMIT.
#
# Agar xatolik bo‘lsa → ROLLBACK.
#
# 5. Real hayotiy misol
#
# 📌 Bank misoli:
#
# O‘tkazma paytida bir hisobdan pul yechiladi (UPDATE)
#
# Ikkinchi hisobga qo‘shiladi (UPDATE)
#
# Hammasi muvaffaqiyatli bo‘lsa → COMMIT
#
# Xatolik chiqsa (masalan, ikkinchi hisob topilmadi) → ROLLBACK
#
# 6. TCL’ning afzalliklari
#
# ✅ Ma’lumotlarning yaxlitligini saqlaydi
# ✅ Xatoliklarda bazani buzilishdan himoya qiladi
# ✅ Bir nechta amalni yagona “paket” sifatida bajaradi
# ✅ Ma’lumotlar ishonchliligini oshiradi
#
# 📌 Xulosa
#
# TCL → tranzaksiyalarni boshqaradi.
#
# Asosiy komandalar: COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION.
#
# Tranzaksiya bir butun amal sifatida ishlaydi: to‘liq bajariladi yoki bekor qilinadi.
#
# Hayotiy qo‘llanish: bank operatsiyalari, buyurtma tizimlari, moliyaviy hisob-kitoblar.