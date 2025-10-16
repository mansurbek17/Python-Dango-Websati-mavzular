# 📌 Ta’rif:
# set — bu elementlar to‘plami bo‘lib, takrorlanuvchi elementlarga ruxsat bermaydi.
#
# Ya’ni, har bir element yagona (unikal) bo‘ladi.
#
# ✅ Xususiyatlari:
#
# Elementlar tartibsiz bo‘ladi (ya’ni indeks yo‘q).
#
# Har bir element faqat bir marta saqlanadi.
#
# Modifikatsiya qilinadi (ya’ni, o‘zgartiriladi).
#
# Ichidagi elementlar hashlanadigan bo‘lishi kerak (ya’ni o‘zgarmas: int, float, str, tuple, va hokazo).


my_set = {1, 2, 3, 4, 4, 2}
print(my_set)  # Natija: {1, 2, 3, 4}



my_set.add(5)        # Element qo‘shish
my_set.remove(3)     # Element o‘chirish
my_set.discard(10)   # Xatolik bermasdan o‘chirish
my_set.clear()     # Bo‘shatish

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Birlashtirish: {1, 2, 3, 4, 5}
print(a & b)   # Kesishma: {3}
print(a - b)   # Farq: {1, 2}

