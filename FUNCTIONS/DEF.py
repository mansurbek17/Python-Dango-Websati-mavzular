# 🟦 1. Funksiya nima?
# Funksiya — bu ma’lum bir vazifani bajaradigan kodlar to‘plami.
#
# Ular yordamida kodni modullashtirish, qayta ishlatish va soddalashtirish mumkin.
#
# 🔸 Nega funksiyadan foydalanamiz?
# ✅ Kodni takrorlamaslik uchun
# ✅ Katta dasturlarni sodda bloklarga bo‘lish uchun
# ✅ Kodni o‘qish osonroq bo‘ladi
# ✅ Xatoliklarni topish va test qilish oson bo‘ladi


# 🟦 2. Funksiya qanday yaratiladi?
def salom_ber():
    print("Assalomu alaykum!")

salom_ber()  # Funksiyani chaqiramiz


# 🟦 3. Argumentli funksiya
def salom_ber(ism):
    print(f"Salom, {ism}!")

salom_ber("Ali")
salom_ber("Laylo")

# 🟦 4. Bir nechta argument

def hisobla(a, b):
    print("Yig'indisi:", a + b)

hisobla(5, 3)

# 🟦 5. return operatori
# Funksiya natijani qaytarishi kerak bo‘lsa — return ishlatiladi.

def kvadrat(son):
    return son ** 2

x = kvadrat(4)
print(x)  # 16

# 🟦 6. Default argument (standart qiymat)
def salom_ber(ism="Mehmon"):
    print(f"Salom, {ism}!")

salom_ber("Olim")   # Salom, Olim!
salom_ber()         # Salom, Mehmon!

# 🟦 7. *args va **kwargs
# *args — Cheksiz sonli argumentlar (ro‘yxat sifatida)
def yigindi(*sonlar):
    return sum(sonlar)

print(yigindi(1, 2, 3))         # 6
print(yigindi(4, 5, 6, 7, 8))   # 30

# **kwargs — Kalit=qiymat ko‘rinishidagi argumentlar (dict sifatida)
def print_info(**malumot):
    for kalit, qiymat in malumot.items():
        print(f"{kalit}: {qiymat}")

print_info(ism="Ali", yosh=22)

# 🟦 8. Funksiya ichida funksiya (Nested Function)
def tashqi():
    def ichki():
        print("Ichki funksiya")
    ichki()

tashqi()

# 🟦 10. Rekursiv funksiya (o‘zini o‘zi chaqiradi)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# Ehtiyot bo‘lish kerak: base case (if n == 1) bo‘lmasa, cheksiz chaqiruv yuz beradi.

# 🟦 11. Docstring (funksiya haqida izoh)
def salom_ber(ism):
    """
    Bu funksiya ism argumenti qabul qiladi
    va salom beradi.
    """
    print(f"Salom, {ism}")

help(salom_ber)




        
