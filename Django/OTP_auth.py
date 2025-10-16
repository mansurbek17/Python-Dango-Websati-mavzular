# 🔑 OTP Authentication haqida to‘liq ma’lumot
# 1️⃣ OTP nima?
#
# OTP (One-Time Password) — bu bir martalik parol, foydalanuvchini aniqlash va tizimga xavfsiz kiritish uchun ishlatiladi.
#
# Har safar foydalanuvchi login qilmoqchi bo‘lganda, unga sms, email, yoki authenticator ilova orqali yuboriladi.
#
# OTP odatda 6 ta raqam bo‘ladi va ma’lum vaqt (30-60 soniya) amal qiladi.
#
# 👉 Oddiy qilib aytganda: OTP — “faqat bir marta ishlatiladigan parol”.
#
# 2️⃣ OTP nima uchun kerak?
#
# Oddiy login (username + password) xavfsizlik uchun yetarli emas. Chunki parol o‘g‘irlanishi mumkin.
#
# OTP esa foydalanuvchiga qo‘shimcha xavfsizlik qatlami beradi.
#
# OTP ishlatiladigan joylar:
#
# Bank tizimlari (to‘lov tasdiqlash).
#
# Mobil ilovalar (Telegram, Gmail kirishda).
#
# Ikki faktorli autentifikatsiya (2FA).
#
# 3️⃣ OTP Authentication qanday ishlaydi?
#
# Foydalanuvchi login qilishni boshlaydi.
#
# Server foydalanuvchining telefon raqami yoki emailiga OTP kod yuboradi.
#
# Foydalanuvchi shu kodni kiritadi.
#
# Server tekshiradi:
#
# Agar kod to‘g‘ri va muddati tugamagan bo‘lsa → foydalanuvchi tizimga kiradi.
#
# Agar noto‘g‘ri yoki muddati tugagan bo‘lsa → rad etiladi.
#
# 4️⃣ OTP turlari
#
# SMS OTP → eng ko‘p ishlatiladi. Kod SMS orqali yuboriladi.
#
# Email OTP → email orqali yuboriladi.
#
# TOTP (Time-based OTP) → vaqtga asoslangan (Google Authenticator, Authy).
#
# Masalan: har 30 soniyada yangi kod generatsiya qilinadi.
#
# HOTP (HMAC-based OTP) → har bir login urinishida yangi kod generatsiya qilinadi.
#
# 5️⃣ Django’da OTP Authentication ishlatish
# 1. Kutubxonani o‘rnatish
#
# Eng mashhur kutubxona – django-otp.
#
# pip install django-otp qrcode
#
# 2. settings.py da sozlash
# INSTALLED_APPS = [
#     ...
#     'django_otp',
#     'django_otp.plugins.otp_email',   # Email OTP
#     'django_otp.plugins.otp_totp',    # Time-based OTP
# ]
#
# 3. OTP generatsiya qilish (TOTP misolida)
# import pyotp
#
# # 32 belgili secret key yaratamiz
# totp = pyotp.TOTP(pyotp.random_base32())
#
# # Kod generatsiya qilish
# print(totp.now())   # Masalan: 482931
#
# 4. Kodni tekshirish
# if totp.verify("482931"):
#     print("✅ To‘g‘ri OTP")
# else:
#     print("❌ Noto‘g‘ri OTP")
#
# 5. SMS yoki Email orqali yuborish
#
# Django’da django.core.mail.send_mail() orqali email OTP yuborish mumkin.
#
# SMS uchun esa twilio, uzsms, kannel kabi servislar ishlatiladi.
#
# 6️⃣ OTP va 2FA (Two-Factor Authentication)
#
# OTP ko‘pincha ikki faktorli autentifikatsiya (2FA) sifatida ishlatiladi.
#
# Birinchi faktor: foydalanuvchi paroli.
#
# Ikkinchi faktor: OTP (telefon yoki email orqali).
#
# Shu orqali xavfsizlik sezilarli darajada oshadi.
#
# 7️⃣ Hayotiy misol
#
# Tasavvur qiling, siz bank ilovasiga kirmoqchisiz:
#
# Siz login qilasiz (username + password).
#
# Bank sizning telefoningizga 6 xonali OTP yuboradi.
#
# Siz shu kodni kiritasiz.
#
# Kod faqat 1 daqiqa amal qiladi.
#
# Shu orqali parolingiz o‘g‘irlangan bo‘lsa ham, begona odam OTP bo‘lmasa tizimga kira olmaydi.
#
# 8️⃣ Xulosa
#
# OTP — bu foydalanuvchi uchun bir martalik, vaqtga bog‘liq kod.
#
# Xavfsizlikni oshiradi, ayniqsa moliyaviy va muhim tizimlarda ishlatiladi.
#
# Django’da django-otp, pyotp, twilio kabi kutubxonalar yordamida joriy etiladi.
#
# OTP ko‘pincha 2FA bilan birga ishlatiladi.