#
#
# 🟩 Inheritance (Meros olish) nima?
# Inheritance — bu bitta klass (sinf) boshqa bir klassdan xususiyatlar (atributlar) va metodlarni meros qilib olishi degani.
#
# ✅ Qachon kerak bo‘ladi?
# Kodni qayta ishlatish (reusability) uchun.
#
# Bir nechta sinflar o‘rtasidagi bog‘liqlikni tashkil qilish uchun.
#
# Asosiy klass (parent/superclass) dan ko‘plab maxsus klasslar (child/subclass) yaratish uchun.

# 🟨 Terminlar:

# | Inglizcha    | O‘zbekcha    | Tushuntirishi                                        |
# | ------------ | ------------ | ---------------------------------------------------- |
# | Parent class | Ota sinf     | Asosiy klass                                         |
# | Child class  | Farzand sinf | Meros oluvchi klass                                  |
# | Inheritance  | Meros olish  | Ota klassdan farzand klassga atribut/metodlar o‘tadi |

# 🟦 Python’da inheritance qanday yoziladi?
# 📌 Sintaksis:

# class Parent:
    # ota klass

# class Child(Parent):
    # parent'dan meros oladi

# 🔹 Misol 1: Oddiy meros olish

class Hayvon:
    def ovoz_chiqar(self):
        print("Hayvon ovoz chiqaryapti")

class It(Hayvon):
    def ovoz_chiqar(self):
        print("It havlayapti")

# Obyektlar
h = Hayvon()
h.ovoz_chiqar()  # Hayvon ovoz chiqaryapti

i = It()
i.ovoz_chiqar()  # It havlayapti


# 🔹 Misol 2: Parent metodidan foydalanish

class Ota:
    def salom(self):
        print("Salom, men otaman")

class Bola(Ota):
    def ozini_tanishtir(self):
        print("Men bolaman")

b = Bola()
b.salom()              # Ota klassdan meros
b.ozini_tanishtir()   # O‘ziga xos metod


# 🟧 super() funksiyasi
# ✅ super() — bu parent klassning metodlarini chaqirish uchun ishlatiladi.

class Hayvon:
    def __init__(self, ism):
        self.ism = ism

    def tanishtir(self):
        print(f"Men — hayvon: {self.ism}")

class Mushuk(Hayvon):
    def __init__(self, ism, turi):
        super().__init__(ism)  # Hayvon klassining __init__ metodini chaqiradi
        self.turi = turi

    def tanishtir(self):
        super().tanishtir()
        print(f"Men {self.turi} mushukman.")

m = Mushuk("Murka", "uy")
m.tanishtir()

# Men — hayvon: Murka
# Men uy mushukman.



# 🟥 Inheritance turlari
# 1. 🧱 Single inheritance (Oddiy)

class Ota:
    def salom(self):
        print("Salom, men Ota klassman.")

class Bola(Ota):
    def ism(self):
        print("Men Bola klassman.")

b = Bola()
b.salom()  # Ota klassdan
b.ism()    # Bola klassdan

# 2. 🏗 Multiple inheritance (Ko‘p ota)

class A:
    def f1(self):
        print("A")

class B:
    def f2(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.f1()  # A
obj.f2()  # B


# 3. 🏢 Multilevel inheritance (Bir necha bosqichli)
class A:
    def f1(self):
        print("A klass")

class B(A):
    def f2(self):
        print("B klass")

class C(B):
    def f3(self):
        print("C klass")

obj = C()
obj.f1()  # A
obj.f2()  # B
obj.f3()  # C


# 4. 🏗️ Hierarchical inheritance (Bir ota, ko‘p farzand)
class Ota:
    def umumiy(self):
        print("Ota klass")

class Bola1(Ota):
    def bola1_fun(self):
        print("Bola1 klass")

class Bola2(Ota):
    def bola2_fun(self):
        print("Bola2 klass")

b1 = Bola1()
b2 = Bola2()

b1.umumiy()  # Ota klass
b2.umumiy()  # Ota klass

# 🔹 5. Hybrid Inheritance (Gibrid meros)
# Turli inheritance turlarining kombinatsiyasi. Masalan: multiple + multilevel.

class A:
    def f1(self):
        print("A")

class B(A):
    def f2(self):
        print("B")

class C:
    def f3(self):
        print("C")

class D(B, C):  # B -> A dan meros olgan, C ham alohida
    def f4(self):
        print("D")

obj = D()
obj.f1()  # A
obj.f2()  # B
obj.f3()  # C
obj.f4()  # D


# 📌 BONUS: Amaliy misol – Transport sinflari
class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

    def info(self):
        print(f"{self.nomi} tezligi: {self.tezlik} km/h")

class Mashina(Transport):
    def __init__(self, nomi, tezlik, model):
        super().__init__(nomi, tezlik)
        self.model = model

    def info(self):
        super().info()
        print(f"Model: {self.model}")

m = Mashina("Avtomobil", 180, "Malibu")
m.info()

# Avtomobil tezligi: 180 km/h
# Model: Malibu
















































