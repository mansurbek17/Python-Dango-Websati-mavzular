# 🟩 Polimorfizm (Polymorphism) nima?
# Polimorfizm — bu so‘z grek tilidan olingan bo‘lib, "ko‘p shakllilik" degan ma’noni anglatadi.
#
# Oddiy qilib aytganda: bir xil nomdagi metod yoki funksiya turli klasslar tomonidan har xil ishlashi mumkin.
#
# 🔑 Asosiy g‘oya:
# Bir xil metod nomi, ammo har xil klasslarda turlicha ishlaydi.

# 🟦 Polimorfizm OOP'da nimaga kerak?
# ✅ Katta dasturlarda kodni soddalashtirish
# ✅ Bir xil interfeys orqali turli klasslar bilan ishlash
# ✅ Kengaytiriladigan va oson boshqariladigan kod yozish

# 🔹 2 asosiy ko‘rinishi bor:

# | Turi                                                             | Ta’rifi                                                                            |
# | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
# | 1️⃣ Method overriding                                            | Farzand klass ota klass metodini **qayta yozadi**                                  |
# | 2️⃣ Method overloading (Python’da to‘liq qo‘llab-quvvatlanmaydi) | **Bir nechta argumentli** bir xil metod — Python’da bu funksiyalar orqali qilinadi |

# 🔶 1. Polimorfizm orqali turli klasslarda bir xil metod

class Mushuk:
    def ovoz(self):
        print("Miyov")

class It:
    def ovoz(self):
        print("Vov")

# Funksiya har qanday hayvonga ishlaydi
def ovoz_chiqar(hayvon):
    hayvon.ovoz()

# Obyektlar
m = Mushuk()
i = It()

ovoz_chiqar(m)  # Miyov
ovoz_chiqar(i)  # Vov

# ovoz_chiqar() funksiyasi bir xil bo‘lsa-da, turli obyektlar har xil natija beradi. Bu — polimorfizm.


# 🔶 2. Method overriding (Qayta yozish)


class Hayvon:
    def harakat(self):
        print("Harakatlanmoqda")

class Quyon(Hayvon):
    def harakat(self):
        print("Sakrayapti")

class Qush(Hayvon):
    def harakat(self):
        print("Uchayapti")

obj1 = Quyon()
obj2 = Qush()

obj1.harakat()  # Sakrayapti
obj2.harakat()  # Uchayapti


# Bu yerda harakat() metodi ota klassda bor, lekin har bir farzand uni o‘zicha yozgan.


# 🔶 3. Polimorfizm va for orqali ishlash

class A:
    def yoz(self):
        print("Bu A klass")

class B:
    def yoz(self):
        print("Bu B klass")

class C:
    def yoz(self):
        print("Bu C klass")

for obj in (A(), B(), C()):
    obj.yoz()

# Har xil klasslar bir xil metodga ega bo‘lsa, ularni bir joyda ishlatish mumkin — bu ham polimorfizm

# 🔶 4. isinstance() bilan polimorfizmni tekshirish

class Avtomobil:
    def yur(self):
        print("Mashina yurmoqda")

class Avtobus:
    def yur(self):
        print("Avtobus yurmoqda")

def test(obj):
    if isinstance(obj, (Avtomobil, Avtobus)):
        obj.yur()

test(Avtomobil())  # Mashina yurmoqda
test(Avtobus())    # Avtobus yurmoqda



# 🔴 Python-da Method Overloading haqida (cheklangan)
# Pythonda method overloading (ya’ni: bitta nomda bir nechta metod, turli argumentlar bilan)
# ruxsat etilmagan, lekin uni *args, **kwargs orqali amalga oshirish mumkin:)

class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.add(1, 2, 3, 4))  # 10



# 📘 Xulosa

# | Tushuncha          | Ma’nosi                                         | Misol                  |
# | ------------------ | ----------------------------------------------- | ---------------------- |
# | Polimorfizm        | Bir xil nom, turli natija                       | `obj.method()`         |
# | Method overriding  | Ota klass metodini farzand klassda qayta yozish | `def harakat(self):`   |
# | Method overloading | Turli argumentlar bilan metodlar                | `def add(self, *args)` |
# | `super()`          | Ota klassga murojaat qilish                     | `super().metod()`      |




















































































