# 📘 SQL’da ALL va ANY operatorlari
# 1. ALL operatori
#
# Ma’nosi: Shart ichki so‘rovdan chiqqan barcha qiymatlarga nisbatan tekshiriladi.
# Ya’ni, ALL → hamma qiymatlarga mos bo‘lsa shart bajariladi.
#
# Sintaksis:
# operator ALL (subquery)
#
# Misollar:
#
# 1️⃣ Eng katta maoshni topish:
#
# SELECT *
# FROM employees
# WHERE salary >= ALL (SELECT salary FROM employees);
#
#
# 👉 Bu so‘rov faqat eng katta maosh oladigan xodimni qaytaradi.
# Chunki uning maoshi barcha maoshlardan katta yoki teng.
#
# 2️⃣ Maoshi barcha 5000 dan katta bo‘lgan xodimlar:
#
# SELECT *
# FROM employees
# WHERE salary > ALL (SELECT salary FROM employees WHERE salary < 5000);
#
# 2. ANY (yoki SOME) operatori
#
# Ma’nosi: Shart ichki so‘rovdan chiqqan qiymatlardan kamida bittasiga nisbatan tekshiriladi.
# Ya’ni, ANY → hech bo‘lmasa bitta qiymatga mos bo‘lsa shart bajariladi.
#
# Sintaksis:
# operator ANY (subquery)
#
# Misollar:
#
# 1️⃣ Maoshi boshqa xodimlardan birortasidan ko‘proq bo‘lgan xodimlar:
#
# SELECT *
# FROM employees
# WHERE salary > ANY (SELECT salary FROM employees WHERE department_id = 10);
#
#
# 👉 Bu so‘rov department_id = 10 bo‘lgan bo‘limdagi kamida bitta odamdan ko‘proq maosh oladigan xodimlarni chiqaradi.
#
# 2️⃣ Eng kichik maoshni topish:
#
# SELECT *
# FROM employees
# WHERE salary <= ANY (SELECT salary FROM employees);
#
#
# 👉 Bu so‘rov eng kichik maoshni topadi, chunki u boshqa kamida bitta maoshdan kichik yoki teng bo‘ladi.
#
# 3. ALL va ANY farqi
# Operator	Ma’nosi	Shart bajarilishi
# ALL	Barcha qiymatlar bilan taqqoslanadi	Shart faqat hamma qiymatga mos bo‘lsa bajariladi
# ANY	Istalgan (hech bo‘lmasa bitta) qiymat bilan taqqoslanadi	Shart kamida bitta qiymatga mos bo‘lsa bajariladi
# 4. Hayotiy analogiya
#
# ALL → “Hamma imtihondan o‘tganmi?” ✅ → Ha bo‘lsa, keyingi bosqichga o‘tasiz.
#
# ANY → “Kamida bitta imtihondan o‘tganmi?” ✅ → Ha bo‘lsa, imkoniyat bor.
#
# 📌 Xulosa
#
# ALL → shart barcha qiymatlarga mos bo‘lishi kerak.
#
# ANY → shart kamida bitta qiymatga mos bo‘lsa yetarli.
#
# Har ikkisi odatda subquery bilan birga ishlatiladi (=, >, <, <> bilan).