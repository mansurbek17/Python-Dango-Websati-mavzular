
# Python'dagi context manager – bu resurslarni boshqarish uchun ishlatiladigan
# mexanizm bo‘lib, kod bloklarida ochilgan resurslarni (masalan, fayl, soket yoki
# ma'lumotlar bazasi ulanishi) avtomatik ravishda yopishni ta'minlaydi. Bu orqali
# dasturda xatolik yoki istisno sodir bo‘lganda ham resurslar to‘g‘ri
# boshqariladi va chiqib ketiladi.

# with open('file.txt', 'r') as f:
#     content = f.read()

# Bu yerda fayl avtomatik ravishda yopiladi.

# O‘zingizning context manager’ni yaratish
# Context manager’ni ikkita usul bilan yozish mumkin:

# 1. __enter__ va __exit__ metodlaridan foydalanish
# __enter__ va __exit__ metodlari bilan maxsus sinf yaratib,
# context manager hosil qilish mumkun

# class MyContextManager:
#     def __enter__(self):
#         print("Context ichiga kirdik")
#         return self  # Agar biror qiymat kerak bo'lsa, uni qaytarish mumkin

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Contextdan chiqayapmiz")
#         if exc_type:
#             print(f"Xatolik: {exc_value}")
#         return True  # Agar xatoni bostirishni istasak, 'True' qaytaramiz

# with MyContextManager() as cm:
#     print("Context manager ishlamoqda")
#     # raise ValueError("Xato yuz berdi!")  # Xatolikni sinab ko'rish uchun

# 2. contextlib moduli yordamida
# contextlib modulidagi @contextmanager dekoratori context manager yozishni osonlashtiradi.

# from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("Context ichiga kirdik")
#     try:
#         yield  # Bu yerda asosiy kod bajariladi
#     finally:
#         print("Contextdan chiqyapmiz")

# 2. contextlib moduli yordamida
# contextlib modulidagi @contextmanager dekoratori context manager yozishni osonlashtiradi.

# from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("Context ichiga kirdik")
#     try:
#         yield  # Bu yerda asosiy kod bajariladi
#     finally:
#         print("Contextdan chiqayapmiz")

# with my_context():
#     print("Context manager ishlamoqda")


# from contextlib import contextmanager

# @contextmanager
# def file_manager(file_name, mode):
#     f = None
#     try:
#         if "." not in file_name:
#             raise NameError
#         print(f"Fayl '{file_name}' ochilyapti...")
#         f = open(file_name, mode)  # Faylni ochish
#         yield f  # Fayl obyekti qaytariladi
#     finally:
#         if f:
#             print(f"Fayl '{file_name}' yopilyapti...")
#             f.close()  # Faylni yopish

# with file_manager('Polimorfizm.py', 'r') as file:
#     f = file.write("jdfndjgnfdlskgjnsdfkjklj")
#     print(f)

# with file_manager('example.txt', 'r') as file:
#     content = file.read()
#     print("Fayl mazmuni:")
#     print(content)
