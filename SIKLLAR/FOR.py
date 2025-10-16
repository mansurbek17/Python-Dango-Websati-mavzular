# for sikli — bu ketma-ket elementlar ustida aylanish (iteratsiya) qilish uchun ishlatiladi.
#
# Asosan iterable (list, tuple, string, range va boshqalar) ustida ishlaydi.
#
# Qo‘shimcha:
#
# for sikli har bir elementni ketma-ket oladi va sikl ichidagi kodni bajaradi.
#
# Agar iterable bo‘sh bo‘lsa, sikl ichidagi kod bajarilmaydi.

mevalar = ['olma', 'anor', 'banan']

for meva in mevalar:
    print(meva)


# 3. break operatori
# break — sikl (for yoki while) ichida ishlatiladi va siklni darhol to‘xtatadi,
# ya’ni sikldan chiqib ketadi.

for i in range(10):
    if i == 5:
        break
    print(i)


# 4. continue operatori
# continue — sikl ichida ishlatiladi va joriy iteratsiyani to‘xtatib,
# siklning keyingi iteratsiyasiga o‘tadi.

for i in range(5):
    if i == 3:
        continue
    print(i)
