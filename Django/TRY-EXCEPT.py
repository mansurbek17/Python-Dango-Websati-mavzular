# try-except — bu xatoliklar (exceptions) yuzaga kelganda, dasturni to‘xtatmasdan,
#
# xatoni ushlash va unga javob berish uchun ishlatiladi.
#
# try bloki ichida xatolik yuzaga kelishi mumkin bo‘lgan kod yoziladi.
#
# except bloki esa xatolik yuzaga kelganda nima qilish kerakligini belgilaydi.
#
# else bloki — agar try ichidagi kodda xatolik bo‘lmasa, else bloki bajariladi.
#
# finally bloki esa har doim, xatolik bo‘lsin yoki bo‘lmasin, bajariladi.
#
# Odatda resurslarni tozalash uchun ishlatiladi (masalan, faylni yopish).


try:
    x = int(input("Son kiriting: "))
    natija = 10 / x
except ZeroDivisionError:
    print("Nolga bo‘lish mumkin emas!")
except ValueError:
    print("Iltimos, butun son kiriting!")
else:
    print("Natija:", natija)
finally:
    print("Dastur tugadi.")
