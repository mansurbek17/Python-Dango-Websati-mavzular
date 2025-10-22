# Generator — bu Python’da iteratsiya qilinadigan obyekt bo‘lib,
#
# bitta qiymatni ketma-ket yaratib beradi,
#
# lekin barcha qiymatlarni bir vaqtning o‘zida xotirada saqlamaydi.
#
# Bu katta ma’lumotlarni samarali ishlash imkonini beradi.
#
# yield kalit so‘zi:
#
# yield — bu funksiyada ishlatiladi va funksiyani generatorga aylantiradi.
#
# yield qiymatni qaytaradi, lekin funksiya bajarilishi to‘xtamaydi,
#
# keyingi chaqirilganda oldingi holatdan davom etadi.
#
# return esa funksiyani to‘liq tugatadi va qiymatni bir marotaba qaytaradi.


# def my_generator():
#     yield 1
#     yield 2
#     yield 3
 
# gen = my_generator()

# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3



# 1.Iterator va generator

# Python'da iterator va generator ma'lumotlarni ketma-ket olish uchun mo'ljallangan
# mexanizmlar bo'lib, ular katta hajmdagi ma'lumotlarni
# samarali ishlatishga yordam beradi. Quyida ularning ta'rifi va
# ishlatilish maqsadi haqida tushuncha beriladi:

# python da Sequence va Iterable ning farqi:
# s = {4,1,6}
# Iterable: Elementlar ketma-ket olinadigan har qanday obyekt
# (masalan, set, dict, yoki generator).
# Sequence: Tartiblangan va indeks orqali murojaat qilinadigan
# iterable (masalan, list, tuple, yoki str).
# print(s) # -> {1,4,6}

## Iterator nima?

# **Iteratorlar** - iterable ustidagi iteratsiyani boshqaradigan obyektlar.
# Iterator iterabledagi joriy elementni va keyingi elementni doim bilib turadi.

# Iterable dan iterator yaratish uchun uni iter() funksiyasiga solamiz:
# 1-misollar

# a = [1, 2, 4]
# a_iter = iter(a)

# print(a_iter)            # Iterator obyektini chop etadi
# print(next(a_iter))      # 1-element: 1
# print(next(a_iter))      # 2-element: 2
# print(next(a_iter))      # 3-element: 4
# print(next(a_iter))      # 4-element yo‘q -> StopIteration xatosi

# Exception bilan ishlash:
# a = [1, 2, 4]
# a_iter = iter(a)

# while True:
#     try:
#         print(next(a_iter))
#     except StopIteration:
#         break

# a = [1, 2, 4]
# for item in a:
#     print(item)

# 2. Fayl obyekti iteratormi?
# f = open('test2.py')
# print(next(f))
# print(next(f))

# Iteratorni OOP da qurish:
# class Counter:
#     def __init__(self, low, high):
#         self.current = low - 1
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#         if self.current < self.high:
#             return self.current
#         raise StopIteration


# class Counter:
#     def __init__(self, start, stop):
#         self.start = start + 1
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.start -= 1
#         if self.start > self.stop:
#             return self.start
#         raise StopIteration

# for elem in Counter(10,-10):
#     print(elem)
# print(type(Counter(1,10)))


# Generator – iterator qaytaruvchi funksiyaga bo‘lib, iterator yaratishning oson yo‘li hisoblanadi.
# 1-m

# def try_generator(y):
#     n = y
#     n += 1
#     print("bajarildi")
#     yield n

#     n *= 2
#     print("bajarildi 2")
#     yield n

#     n += 10
#     print("bajarildi 3")
#     yield n

# result = try_generator(3)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(result)

# for item in result:
#     print(item)


# for i in range(1, n+1):
#     yield i*i

# for i in generator_manager(10):
#     print(i)

# generator va for sikli:
# def for_gen(start, stop):
#     for i in range(start, stop):
#         yield i

# result = for_gen(1, 5)
# print(result)

# for item in result:
#     print(item)


# Anonim generator yaratish
# my_list_com = [num for num in range(1000)]
# print(my_list_com)

# my_generator = (num for num in range(10))
# print(my_generator)

# for i in my_generator:
#     print(i)

# class Counter:
#     def __init__(self, start, stop):
#         self.start = start - 1
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start < self.stop:
#             return self.start
#         raise StopIteration
#
# a = Counter(1, 10)
# for item in a:
#     print(item)