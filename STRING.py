# String (str) — bu matn bo‘lib, u ikki yoki qo‘sh tirnoq ichida yoziladi.
#
# Misollar:
#
s1 = "Salom"
s2 = 'Dunyo'
s3 = "Men 'Python' o‘rganayapman"
s4 = 'Bugun "juma" kuni'
#
# Python'da string — o‘zgarmas (immutable). Ya’ni, stringdagi harflarni to‘g‘ridan-to‘g‘ri o‘zgartirib bo‘lmaydi,
#
# yangi string yaratish kerak bo‘ladi.

a = "Salom"
b = "Dunyo"
print(a + " " + b)  # Salom Dunyo

print("Ha" * 3)  # HaHaHa

s = "Python"
print(s[0])     # P
print(s[-1])    # n
print(s[0:3])   # Pyt
print(s[::2])   # Pto

# 🔤 Katta-kichik harflar:

# | Metod           | Tavsif                            | Misol                                     |
# | --------------- | --------------------------------- | ----------------------------------------- |
# | .lower()`      | Hammasini kichik harfga o‘tkazadi | `'Salom'.lower()` → `'salom'`             |
# | .upper()`      | Hammasini katta harfga o‘tkazadi  | `'Salom'.upper()` → `'SALOM'`             |
# | .capitalize()` | Faqat 1-harf katta                | `'salom'.capitalize()` → `'Salom'`        |
# | .title()`      | Har bir so‘z bosh harfi katta     | `'salom dunyo'.title()` → `'Salom Dunyo'` |
# | .swapcase()`   | Katta → kichik, kichik → katta    | `'Salom'.swapcase()` → `'sALOM'`          |

# 🔍 Qidirish va tekshirish:

# | Metod              | Tavsif                                                      | Misol                               |
# | ------------------ | ----------------------------------------------------------- | ----------------------------------- |
# | .find(sub)`       | Substring qayerda boshlanganini qaytaradi, yo‘q bo‘lsa `-1` | `'python'.find('th')` → `2`         |
# | .index(sub)`      | find() ga o‘xshaydi, ammo topilmasa xatolik                | `'python'.index('th')`              |
# | .startswith(sub)` | Belgilangan so‘z bilan boshlanadimi                         | `'hello'.startswith('he')` → `True` |
# | .endswith(sub)`   | Belgilangan so‘z bilan tugaydimi                            | `'hello'.endswith('lo')` → `True`   |
# | .count(sub)`      | Substring nechta marta bor                                  | `'banana'.count('a')` → `3`         |

# 🧹 Bo‘sh joylar va tozalash:

# | Metod       | Tavsif                                           | Misol                           |
# | ----------- | ------------------------------------------------ | ------------------------------- |
# | .strip()`  | Boshi va oxiridagi bo‘sh joylarni olib tashlaydi | `' hello '.strip()` → `'hello'` |
# | .lstrip()` | Faqat chap tomondan olib tashlaydi               | `'  test'.lstrip()` → `'test'`  |
# | .rstrip()` | Faqat o‘ng tomondan olib tashlaydi               | `'test  '.rstrip()` → `'test'`  |

# 🧩 Bo‘lish va qo‘shish:
# | Metod         | Tavsif                                                      | Misol                                            |
# | ------------- | ----------------------------------------------------------- | ------------------------------------------------ |
# | .split(sep)` | Belgilangan ajratgich bo‘yicha bo‘ladi (default: bo‘sh joy) | `'a,b,c'.split(',')` → `['a', 'b', 'c']`         |
# | .join(list)` | Listdagi elementlarni birlashtiradi                         | `' '.join(['Salom', 'dunyo'])` → `'Salom dunyo'` |

# 🔧 O‘zgartirish:
# | Metod                | Tavsif                         | Misol                                       |
# | -------------------- | ------------------------------ | ------------------------------------------- |
# | .replace(old, new)` | `old` ni `new` ga almashtiradi | `'python'.replace('py', 'ja')` → `'jathon'` |
