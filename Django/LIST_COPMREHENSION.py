# List comprehension — bu Python’da yangi ro‘yxat (list) yaratish uchun qisqa va samarali sintaksis bo‘lib,
#
# odatda bir qatorda ifodalanadi.
#
# U for siklini va shartlarni (filter) bitta ifoda ichida jamlaydi,
#
# shuning uchun kod o‘qilishi oson va ko‘proq ixcham bo‘ladi.

# map(funksiya, iterable)


# natija = [x * x for x in range(5)]
# print(natija)  # [0, 1, 4, 9, 16]

# even = [x for x in range(10) if x % 2 == 0]
# print(even)  # [0, 2, 4, 6, 8]

# labels = ["juft" if x % 2 == 0 else "toq" for x in range(5)]
# print(labels)  # ['juft', 'toq', 'juft', 'toq', 'juft']

# my_list = [1, 2, 3, 4]
# double = list(map(lambda x: x * 2, my_list))
# print(double)  # [2, 4, 6, 8]


# names = ["ali", "vali", "hasan"]
# result = list(map(str.upper, names))
# print(result)  # ['ALI', 'VALI', 'HASAN']

# 🟪 4. filter() funksiyasi

# nums = [1, 2, 3, 4, 5]
# result = list(filter(lambda x: x % 2 == 0, nums))
# print(result)  # [2, 4]

# words = ["salom", "hi", "assalomu alaykum", "yo"]
# result = list(filter(lambda x: len(x) > 3, words))
# print(result)  # ['salom', 'assalomu alaykum']

# 🟥 5. reduce() funksiyasi
# reduce() — bu elementlarni ketma-ket birlashtirib bitta yakuniy qiymat hosil qiladi.
#
# Masalan, yig‘indisini yoki ko‘paytmasini hisoblash.
#
# ⚠️ reduce() funksiyasi functools modulidan import qilinadi:


# from functools import reduce

# nums = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, nums)
# print(result)  # 10



# nums = [1, 2, 3, 4]
# result = reduce(lambda x, y: x * y, nums)
# print(result)  # 24


# | Nomi                 | Maqsadi                           | Funksiya turi           | Natija turi     |
# | -------------------- | --------------------------------- | ----------------------- | --------------- |
# | `list comprehension` | Tez list qurish                   | ifoda                   | List            |
# | `lambda`             | Qisqa funksiya                    | funksiya (bir qatorlik) | Funksiya        |
# | `map()`              | Har bir elementga amal            | funksional              | Iterator (list) |
# | `filter()`           | Shartga mos elementlarni ajratish | funksional              | Iterator (list) |
# | `reduce()`           | Barchani bir qiymatga tushirish   | funksional              | Bitta qiymat    |


# ✅ XULOSA
# 🔹 lambda — kichik, qisqa funktsiyalar uchun.
#
# 🔹 map() — elementlarni o‘zgartirish.
#
# 🔹 filter() — elementlarni saralash.
#
# 🔹 reduce() — yig‘ish yoki jamlash.
#
# 🔹 list comprehension — tez va tushunarli ro‘yxat yasash.




