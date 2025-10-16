# 🟩 1. Fayllarni ochish: open()
# 📌 Sintaksis:

# open(file_name, mode)

# | Mode (rejim) | Ma’nosi                                                          |
# | ------------ | ---------------------------------------------------------------- |
# | `'r'`        | **Read** — faqat o‘qish                                          |
# | `'w'`        | **Write** — yozish (agar fayl mavjud bo‘lsa o‘chadi!)            |
# | `'a'`        | **Append** — oxiriga qo‘shib yozish                              |
# | `'x'`        | **Create** — yangi fayl yaratish, agar mavjud bo‘lsa xato beradi |
# | `'b'`        | **Binary** rejim (rasm, audio, video) uchun                      |
# | `'+'`        | O‘qish va yozish rejimi                                          |

# Tavsiya: Har doim with open(...) as f: shaklida foydalaning — bu faylni avtomatik yopadi.


# 🟦 2. Faylga yozish (write, w, a rejim)
# ✅ Misol: Faylga yozish (w)

with open("data.txt", "w") as f:
    f.write("Salom, dunyo!\n")
    f.write("Bu Python faylidir.")

# ⚠️ w rejimi faylni tozalab yozadi. Eski ma’lumotlar o‘chadi.

# ✅ Misol: Oxiriga qo‘shish (a)
with open("data.txt", "a") as f:
    f.write("\nYana bir qatordan yozildi.")
# Fayldagi mavjud matn saqlanadi, yangi matn oxiriga qo‘shiladi.

# 🟨 3. Fayldan o‘qish (read, r rejim)
# ✅ read() — butun faylni o‘qish

with open("data.txt", "r") as f:
    content = f.read()
    print(content)


# ✅ readline() — bitta qatordan o‘qish
with open("data.txt", "r") as f:
    first_line = f.readline()
    print(first_line)

# ✅ readlines() — barcha qatorlarni list ko‘rinishida o‘qish
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Salom, dunyo!\n', 'Bu Python faylidir.\n', ...]

# 🟪 4. Faylga ro‘yxat yozish / o‘qish
# ✅ List yozish:

lines = ["Ali\n", "Vali\n", "Hasan\n"]
with open("names.txt", "w") as f:
    f.writelines(lines)

# ✅ List o‘qish:

with open("names.txt", "r") as f:
    names = f.readlines()
    print(names)

# 🟥 5. Fayl mavjudligini tekshirish

import os

if os.path.exists("data.txt"):
    print("Fayl mavjud.")
else:
    print("Fayl topilmadi.")

# 🟫 6. Faylni o‘chirish

import os

os.remove("data.txt")  # Faylni o‘chiradi


# 🟧 7. Faylga string formatlash bilan yozish

name = "Ali"
age = 22

with open("student.txt", "w") as f:
    f.write(f"Ism: {name}\nYosh: {age}")


# 🟦 8. Faylni o‘qib, har bir qatorni o‘zgartirish (masalan, katta harflarga)

with open("data.txt", "r") as f:
    lines = f.readlines()

with open("data.txt", "w") as f:
    for line in lines:
        f.write(line.upper())


# 🟨 9. Binary fayllar (rasmlar, PDF, va h.k.)

with open("image.jpg", "rb") as f:
    data = f.read()

with open("copy.jpg", "wb") as f:
    f.write(data)

# ✅ Xulosa

# | Amal                         | Kod                                       |
# | ---------------------------- | ----------------------------------------- |
# | Fayl yaratish/ochish         | `open("file.txt", "w")`                   |
# | Faylga yozish                | `write()`, `writelines()`                 |
# | Fayldan o‘qish               | `read()`, `readline()`, `readlines()`     |
# | Fayl mavjudligini tekshirish | `os.path.exists()`                        |
# | Faylni o‘chirish             | `os.remove()`                             |
# | Tavsiya etilgan usul         | `with open(...) as f:` (avtomatik yopadi) |








