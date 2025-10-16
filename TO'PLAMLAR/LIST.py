# List – Python’da tartiblangan (ordered) va o‘zgartiriladigan (mutable) elementlar to‘plami.
#
# Ichida har xil turdagi (int, str, list va hokazo) elementlar bo‘lishi mumkin.
#
# Elementlar indeks orqali chaqiriladi (list[0], list[1]).
#
# O‘zgartirish, qo‘shish (append), o‘chirish (remove) mumkin.



my_list = [1, 2, 3]
my_list[0] = 100  # O‘zgartirish mumkin

# | Metod          | Tushuntirish                                             | Misol                        |
# | -------------- | -------------------------------------------------------- | ---------------------------- |
# | `append()`     | Oxiriga element qo‘shadi                                 | `my_list.append(6)`          |
# | `insert(i, x)` | i-pozitsiyaga x-ni qo‘yadi                               | `my_list.insert(1, "salom")` |
# | `extend()`     | Boshqa ro‘yxatni qo‘shadi                                | `my_list.extend([7, 8])`     |
# | `remove(x)`    | x qiymatni o‘chiradi                                     | `my_list.remove(3)`          |
# | `pop(i)`       | i-pozitsiyadagi elementni o‘chiradi (yo‘q bo‘lsa oxirgi) | `my_list.pop(2)`             |
# | `index(x)`     | x qiymatining indeksini qaytaradi                        | `my_list.index(5)`           |
# | `count(x)`     | x qiymat necha marta uchrashganini hisoblaydi            | `my_list.count(3)`           |
# | `sort()`       | Ro‘yxatni tartiblaydi (o‘sish tartibida)                 | `my_list.sort()`             |
# | `reverse()`    | Teskari tartiblaydi                                      | `my_list.reverse()`          |
# | `clear()`      | Ro‘yxatni bo‘sh qiladi                                   | `my_list.clear()`            |
# | `copy()`       | Ro‘yxatning nusxasini yaratadi                           | `new_list = my_list.copy()`  |

my_list = [3, 1, 4, 1, 5]

my_list.append(9)         # [3, 1, 4, 1, 5, 9]
my_list.remove(1)         # [3, 4, 1, 5, 9]  (birinchi 1 o‘chadi)
my_list.insert(2, 10)     # [3, 4, 10, 1, 5, 9]
my_list.sort()            # [1, 3, 4, 5, 9, 10]
my_list.reverse()         # [10, 9, 5, 4, 3, 1]
print(my_list.count(3))   # 1
print(my_list.index(9))   # 1


nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))
print(unique)  # Masalan: [1, 2, 3]

