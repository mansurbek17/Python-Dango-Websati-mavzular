# 🔐 JWT Authentication haqida to‘liq ma’lumot
# 1️⃣ JWT nima?
#
# JWT (JSON Web Token) — bu foydalanuvchini aniqlash (authentication) va unga ruxsat berish (authorization) uchun ishlatiladigan tokenlash usuli.
#
# JWT — oddiy string, lekin ichida foydalanuvchi haqida kodlangan ma’lumot bor.
#
# JWT 3 qismdan iborat bo‘ladi:
#
# xxxxx.yyyyy.zzzzz
#
#
# Header → Token turi va algoritm (masalan: HS256).
#
# Payload → Foydalanuvchi haqida ma’lumot (id, username, role va h.k.).
#
# Signature → Token qalbakilashtirilmaganini isbotlovchi maxfiy imzo.
#
# 2️⃣ JWT qanday ishlaydi?
#
# Foydalanuvchi login qiladi (username + password yuboradi).
#
# Server foydalanuvchini tekshiradi va unga JWT token beradi.
#
# Foydalanuvchi keyingi barcha so‘rovlarda HTTP header orqali shu tokenni yuboradi:
#
# Authorization: Bearer <token>
#
#
# Server tokenni tekshiradi:
#
# Agar token yaroqli bo‘lsa → foydalanuvchiga ruxsat beradi.
#
# Agar token noto‘g‘ri yoki muddati tugagan bo‘lsa → xatolik qaytaradi.
#
# 3️⃣ JWT afzalliklari
#
# Stateless – server foydalanuvchini sessiyada saqlamaydi, faqat tokenni tekshiradi.
#
# Tezkor – chunki token ichida ma’lumot bo‘ladi, qo‘shimcha bazaga murojaat qilish shart emas.
#
# Xavfsiz – token imzo bilan himoyalangan, uni qalbakilashtirish qiyin.
#
# Universallik – JWT ni mobil ilova, front-end (React, Vue, Angular) va boshqa xizmatlar bilan ishlatish oson.
#
# 4️⃣ Django’da JWT ishlatish
# 1. Kerakli kutubxonani o‘rnatish
# pip install djangorestframework-simplejwt
#
# 2. settings.py ga qo‘shish
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }
#
# 3. urls.py da JWT endpointlarni qo‘shish
# from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
#
# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]
#
# 4. Login qilib token olish
#
# POST /api/token/
#
# {
#   "username": "admin",
#   "password": "12345"
# }
#
#
# ✅ Javob:
#
# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
# }
#
# 5️⃣ JWT Token turlari
#
# Access Token
#
# Foydalanuvchini aniqlash uchun ishlatiladi.
#
# Amal qilish vaqti juda qisqa (odatda 5-15 daqiqa).
#
# Har bir API so‘rovida yuboriladi.
#
# Refresh Token
#
# Access token muddati tugaganda yangisini olish uchun ishlatiladi.
#
# Amal qilish muddati uzunroq (odatda 1-7 kun).
#
# Faqat /api/token/refresh/ ga yuboriladi.
#
# 👉 Shu usul xavfsizlikni oshiradi: agar access token o‘g‘irlanib qolsa, u tezda eskiradi.
#
# 6️⃣ JWT ishlash jarayoni (bosqichma-bosqich)
#
# Login: foydalanuvchi login va parol yuboradi.
#
# Token olish: server foydalanuvchiga access va refresh token beradi.
#
# So‘rov yuborish: foydalanuvchi har safar API ga access token yuboradi.
#
# Token tugasa: refresh token orqali yangi access token olinadi.
#
# Logout: refresh tokenni yo‘q qilish orqali chiqib ketiladi.
#
# 7️⃣ Hayotiy misol
#
# Siz universitet kutubxonasiga kirdingiz. Sizga kirish kartasi berishdi:
#
# Access token – bir kunga berilgan vaqtinchalik kartochka.
# 
# Refresh token – semestr davomida amal qiladigan asosiy a’zolik hujjati.
#
# Agar vaqtinchalik kartochkangiz tugasa, kutubxonachi sizning a’zolik hujjatingiz (refresh token) asosida yangisini beradi.
#
# 8️⃣ Xulosa
#
# JWT foydalanuvchini aniqlash uchun eng ko‘p ishlatiladigan tokenlash usuli.
#
# Django’da djangorestframework-simplejwt orqali ishlatiladi.
#
# Access token – qisqa muddatli, tez-tez yangilanadi.
#
# Refresh token – uzun muddatli, access tokenni yangilash uchun ishlatiladi.
#
# JWT stateless, xavfsiz va zamonaviy API lar uchun juda qulay.