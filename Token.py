# 🔑 Token haqida to‘liq ma’lumot (Django REST Framework misolida)
# 1️⃣ Token nima?
#
# Token – bu maxfiy raqamli kalit (string), foydalanuvchini aniqlash (authentication) va unga ruxsat berish (authorization) uchun ishlatiladi.
#
# Token foydalanuvchi tizimga kirgandan so‘ng unga biriktiriladi va keyingi barcha so‘rovlarda parol o‘rniga ishlatiladi.
#
# Ya’ni foydalanuvchi login va parolni faqat bir marta yuboradi, keyingi safarlarda Token orqali tizim tanib oladi.
#
# 2️⃣ Nima uchun Token kerak?
#
# HTTP protokoli stateless – ya’ni server har bir so‘rovni alohida ko‘radi, foydalanuvchini “eslab qolmaydi”.
#
# Shu sababli foydalanuvchini aniqlash uchun Token ishlatiladi.
#
# Token yordamida:
#
# Parolni har safar yuborish shart bo‘lmaydi.
#
# API xavfsiz bo‘ladi.
#
# Mobil ilovalar yoki front-end (React, Vue, Angular) bilan bog‘lash osonlashadi.
#
# 3️⃣ Django REST Framework’da Token ishlash jarayoni
#
# Foydalanuvchi login qiladi (username + password yuboradi).
#
# Server token yaratadi va uni foydalanuvchiga qaytaradi.
#
# Keyingi barcha API so‘rovlarda foydalanuvchi Authorization header orqali token yuboradi:
#
# Authorization: Token 2f1a53c1abf6a9d2e...
#
#
# Server shu tokenni tekshiradi va foydalanuvchini tanib oladi.
#
# 4️⃣ Token Authentication ishlatish (Django DRF misolida)
# 1. rest_framework.authtoken qo‘shish
#
# settings.py ichiga yozamiz:
#
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'rest_framework.authtoken',
# ]
#
# 2. Migratsiya qilish
# python manage.py migrate
#
# 3. Har bir foydalanuvchi uchun token yaratish
# python manage.py drf_create_token <username>
#
#
# Yoki avtomatik tarzda foydalanuvchi yaratilganda token ham yaratilishi mumkin.
#
# 4. views.py da login endpoint yaratish
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
#
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         return Response({"error": "Noto‘g‘ri login yoki parol"}, status=400)
#
# 5. Token bilan so‘rov yuborish (Postman yoki cURL orqali)
# curl -H "Authorization: Token 2f1a53c1abf6a9d2e..." http://127.0.0.1:8000/api/products/
#
# 5️⃣ Token turlari
#
# Simple Token – oddiy bir marta yaratiladigan token (rest_framework.authtoken).
#
# JWT (JSON Web Token) – eng ko‘p ishlatiladi. 3 qismdan iborat:
#
# Header (algoritm va token turi)
#
# Payload (foydalanuvchi ma’lumotlari)
#
# Signature (xavfsizlik imzosi)
# JWT foydalanuvchini tezkor va xavfsiz tanib olish uchun ishlatiladi.
#
# OAuth2 Tokens – katta tizimlarda (Google, Facebook login) ishlatiladi.
#
# 6️⃣ Hayotiy misol (tushunarli qilib)
#
# Siz supermarket saytida login qildingiz.
#
# Sizga a’zo kartochka berishadi (bu – Token).
#
# Endi siz har safar sotib olishda ismingizni aytib o‘tirmaysiz, shunchaki kartochkani ko‘rsatasiz – tizim sizni tanib oladi.
#
# Xuddi shunday, foydalanuvchi API da tokenni yuboradi va server uni tanib oladi.
#
# 7️⃣ Xulosa
#
# Token – foydalanuvchini aniqlash uchun maxfiy kalit.
#
# Django REST Framework’da TokenAuthentication yoki JWT Authentication ishlatiladi.
#
# Token xavfsizlikni oshiradi va API lar bilan ishlashni osonlashtiradi.