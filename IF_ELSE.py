# 📌 1. if operatori
# if — shartli operator. Ya'ni, agar berilgan shart True (rost) bo‘lsa, ichidagi kod ishlaydi.
yosh = 20

if yosh >= 18:
    print("Siz balog‘at yoshiga yetgansiz.")

# 📌 2. else operatori
# else — agar if sharti False bo‘lsa, alternativ kod bajariladi.

yosh = 16

if yosh >= 18:
    print("Siz ovoz berishingiz mumkin.")
else:
    print("Siz hali voyaga yetmagansiz.")


# 📌 3. elif (else if)
# elif — bu qo‘shimcha shartlarni tekshirish uchun ishlatiladi. Bir nechta variantlar bo‘lganda foydali.

baho = 85

if baho >= 90:
    print("A")
elif baho >= 80:
    print("B")
elif baho >= 70:
    print("C")
else:
    print("Bahoyingiz juda past.")

# 📌 if-else bilan (ternary if):

result = ["juft" if i % 2 == 0 else "toq" for i in range(5)]
print(result)  # ['juft', 'toq', 'juft', 'toq', 'juft']




