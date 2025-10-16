# lambda funksiyasi — bu Python’da anonim (nom berilmagan) funksiya bo‘lib,

# odatda bitta qatorda yoziladi.

# U tez, qisqa, va oddiy funksiyalarni yaratish uchun ishlatiladi.

# lambda argumentlar: ifoda
#
# lambda — bu nom berilmagan (anonim) funksiya bo‘lib,
#
# odatda bir qatorlik va tez-tez foydalaniladigan hisob-kitoblar uchun ishlatiladi.

#lambda argumentlar: ifoda

# Oddiy funksiya

def kvadrat(x):
    return x * x

# Lambda bilan
kvadrt = lambda x: x * x

print(kvadrt(5))  # Natija: 25


# 💡 Qachon ishlatiladi?
#
# map(), filter(), sorted() kabi funksiyalar ichida
#
# Funksiya yaratib, darhol ishlatmoqchi bo‘lsang
#
# Kodni qisqartirish va soddalashtirish uchun

sonlar = [1, 2, 3, 4, 5]

natija = map(lambda x: x * x, sonlar)

print(list(natija))  # [1, 4, 9, 16, 25]
