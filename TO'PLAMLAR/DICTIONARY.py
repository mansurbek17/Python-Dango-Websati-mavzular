# 📌 Ta’rif:
# dict — bu kalit-qiymat juftliklaridan tashkil topgan ma’lumot turi.
#
# ✅ Xususiyatlari:
# Har bir element kalit (key) va qiymat (value) juftligidan iborat.
#
# Kalitlar unikal bo‘ladi, qiymatlar esa takrorlanishi mumkin.
#
# Tartibsiz (Python 3.6+ versiyalaridan boshlab tartibli saqlanadi, lekin bu kafolat emas).
#
# Kalitlar ham hashlanadigan bo‘lishi kerak (int, str, tuple, va hokazo).


student = {
    "ism": "Ali",
    "yosh": 20,
    "kurs": 2
}
print(student["ism"])  # Natija: Ali


student["universitet"] = "TATU"   # Yangi juftlik qo‘shish
student["yosh"] = 21              # Qiymatni yangilash
student.pop("kurs")              # Kalit bo‘yicha o‘chirish
student.keys()                   # Faqat kalitlar
student.values()                 # Faqat qiymatlar
student.items()                  # Kalit-qiymat juftliklari






