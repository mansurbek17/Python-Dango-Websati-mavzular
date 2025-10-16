# 🔐 Django REST Framework (DRF) – Permissions (Ruxsatlar)
# 1️⃣ Permission nima?
#
# Permission (ruxsat) — bu foydalanuvchining ma’lum bir amalni bajarishga haqqi bormi-yo‘qmiligini tekshiruvchi mexanizm.
#
# Authentication (kimligini aniqlash) → foydalanuvchini aniqlaydi.
#
# Permission → aniqlangan foydalanuvchi qila oladimi yoki yo‘qmi degan savolga javob beradi.
#
# 👉 Oddiy qilib aytganda:
#
# Authentication – “Bu kim?”
#
# Permission – “Bu foydalanuvchi bunga haqlimi?”
#
# 2️⃣ Permissions nima uchun kerak?
#
# Xavfsizlikni ta’minlash uchun.
#
# Har kim ham API orqali CRUD (Create, Read, Update, Delete) amallarini bajarib yubormasligi uchun.
#
# Masalan:
#
# Faqat admin foydalanuvchi ma’lumotni o‘chira oladi.
#
# Odatta foydalanuvchi faqat o‘z postlarini tahrirlay oladi.
#
# Login qilmagan odam API ma’lumotlarini ko‘ra olmaydi.
#
# 3️⃣ DRF’da mavjud asosiy Permissions
#
# DRF bizga bir nechta tayyor ruxsatlarni beradi:
#
# AllowAny
#
# Barcha foydalanuvchilarga ruxsat beradi (hatto login qilmaganlarga ham).
#
# from rest_framework.permissions import AllowAny
#
# class MyView(APIView):
#     permission_classes = [AllowAny]
#
#
# IsAuthenticated
#
# Faqat login qilgan foydalanuvchilar uchun ruxsat beradi.
#
# from rest_framework.permissions import IsAuthenticated
#
# class MyView(APIView):
#     permission_classes = [IsAuthenticated]
#
#
# IsAdminUser
#
# Faqat is_staff=True bo‘lgan admin foydalanuvchilarga ruxsat beradi.
#
# from rest_framework.permissions import IsAdminUser
#
# class MyView(APIView):
#     permission_classes = [IsAdminUser]
#
#
# IsAuthenticatedOrReadOnly
#
# Login qilmaganlar faqat GET (ko‘rish) amallarini bajarishi mumkin.
#
# Login qilganlar esa POST, PUT, DELETE ham qila oladi.
#
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
#
# class MyView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
# 4️⃣ Global (umumiy) permission sozlash
#
# Barcha viewlarda umumiy permission ishlatish uchun settings.py da yoziladi:
#
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }
#
#
# 👉 Bu holda barcha API faqat login qilingan foydalanuvchilar uchun ochiq bo‘ladi.
#
# 5️⃣ Custom (o‘zingiz yozadigan) Permissions
#
# Ko‘pincha tayyor ruxsatlar yetarli bo‘lmaydi. Masalan:
#
# Har bir foydalanuvchi faqat o‘z postini o‘zgartira olishi kerak.
#
# Yoki foydalanuvchi faqat o‘z buyurtmalarini ko‘rishi kerak.
#
# Bunday vaziyatlarda biz custom permission yozamiz.
#
# Misol: Faqat post egasi tahrirlashga haqli
# from rest_framework import permissions
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Har kim ko‘rishi mumkin (GET, HEAD, OPTIONS)
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Faqat egasi o‘zgartira oladi
#         return obj.owner == request.user
#
#
# View’da ishlatish:
#
# from rest_framework.views import APIView
#
# class PostDetailView(APIView):
#     permission_classes = [IsOwnerOrReadOnly]
#
# 6️⃣ Object-level permissions va View-level permissions
#
# View-level permission – butun API uchun ruxsat (masalan, faqat adminlar kiradi).
#
# Object-level permission – ma’lum obyekt uchun ruxsat (masalan, faqat post egasi o‘zgartiradi).
#
# 7️⃣ Hayotiy misol
#
# Tasavvur qiling, sizning supermarket API mavjud:
#
# Admin → mahsulot qo‘shishi, narxni o‘zgartirishi mumkin.
#
# Oddiy foydalanuvchi → faqat mahsulotlarni ko‘rishi va xarid qilishi mumkin.
#
# Login qilmagan odam → API ga kira olmaydi.
#
# Bu holatda quyidagilar ishlatiladi:
#
# Admin uchun → IsAdminUser
#
# Oddiy foydalanuvchi uchun → IsAuthenticatedOrReadOnly
#
# Har bir foydalanuvchi faqat o‘z buyurtmalarini ko‘rishi uchun → Custom Permission (IsOwnerOrReadOnly)
#
# 8️⃣ Xulosa
#
# Permissions – foydalanuvchining amal bajarish huquqini belgilaydi.
#
# DRF’da mavjud asosiy ruxsatlar: AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly.
#
# Global va local (view ichida) sozlash mumkin.
#
# Custom permission yozib, loyihaga moslab ishlatish mumkin.
#
# Permissions xavfsizlikni ta’minlaydi va API’ni foydalanuvchi darajalariga qarab boshqaradi.