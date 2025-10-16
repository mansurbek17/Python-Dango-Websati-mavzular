# Serializers haqida to‘liq tushuncha
# 1️⃣ Serializer nima?
#
# Serializer — bu Django REST Framework’da Python obyektlari (masalan, Django modeli obyektlari) ni JSON, XML yoki boshqa formatlarga o‘tkazuvchi vosita.
#
# Shuningdek, serializer JSON’dan qaytib Python obyektiga (ya’ni modelga) ma’lumotni o‘tkazib beradi.
#
# 👉 Qisqasi: Serializer – bu Django modeli bilan API o‘rtasida “ko‘prik” vazifasini bajaradi.
#
# 2️⃣ Serializer’ning asosiy vazifalari
#
# Serialization – Python obyektlarini (Model obyektlari) JSON yoki boshqa formatga aylantirish.
#
# Deserialization – JSON ma’lumotni qabul qilib, Python obyektiga o‘tkazish.
#
# Validation – kelgan ma’lumotlarni tekshirish (masalan, ism bo‘sh bo‘lmasligi, yosh manfiy bo‘lmasligi).
#
# 3️⃣ Serializers turlari
# 🔹 1. Oddiy Serializer (qo‘lda maydonlar yoziladi)
# from rest_framework import serializers
#
# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     phone = serializers.CharField(max_length=20)
#
#
# 👉 Bu yerda har bir maydon qo‘lda aniqlanadi. Validatsiyani ham o‘zingiz yozishingiz kerak bo‘ladi.
#
# 🔹 2. ModelSerializer (eng ko‘p ishlatiladi)
# from rest_framework import serializers
# from .models import Student
#
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
#
#
# 👉 Bu usulda:
#
# Modeldagi barcha ustunlar avtomatik olinadi.
#
# Qisqa va aniq yoziladi.
#
# Validatsiya va boshqa qo‘shimcha metodlarni qo‘shish mumkin.
#
# 🔹 3. Nested Serializers (ichma-ich serializer)
#
# Agar model boshqa modelga ForeignKey bilan bog‘langan bo‘lsa, ichki serializer yozish kerak.
#
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['id', 'title']
#
# class StudentSerializer(serializers.ModelSerializer):
#     course = CourseSerializer()  # Nested serializer
#
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'age', 'course']
#
#
# 👉 Bu usul orqali bog‘langan ma’lumotlar ham JSON ichida qaytariladi.
#
# 🔹 4. Serializer Methods (SerializerMethodField)
#
# Agar ma’lumotni qo‘shimcha hisoblash yoki o‘zgartirish kerak bo‘lsa:
#
# class StudentSerializer(serializers.ModelSerializer):
#     full_info = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'age', 'full_info']
#
#     def get_full_info(self, obj):
#         return f"{obj.name} ({obj.age} yosh)"
#
#
# 👉 Endi JSON’da full_info degan yangi maydon chiqadi.
#
# 4️⃣ Validatsiya (Validation) Serializers’da
#
# Serializer foydalanuvchi yuborgan ma’lumotni avtomatik tekshiradi.
#
# Oddiy validatsiya
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
#
#     def validate_age(self, value):
#         if value < 0:
#             raise serializers.ValidationError("Yosh manfiy bo‘lishi mumkin emas!")
#         return value
#
#
# 👉 Endi foydalanuvchi age = -5 yuborsa, xatolik qaytadi.
#
# Umumiy validatsiya
#     def validate(self, data):
#         if data['age'] < 18 and "student" not in data['name'].lower():
#             raise serializers.ValidationError("18 yoshdan kichiklar ismida 'student' bo‘lishi shart")
#         return data
#
# 5️⃣ Serializer bilan View ishlash jarayoni
# views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
#
# class StudentListView(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# 👉 Bu view’da:
#
# GET → bazadagi barcha studentlar JSON’da chiqadi.
#
# POST → JSON yuborsangiz, yangi student yaratiladi.
#
# 6️⃣ Serializer afzalliklari
#
# Django modelini JSON formatiga oson o‘tkazadi.
#
# Validatsiya avtomatik amalga oshadi.
#
# Qisqa kod (ModelSerializer yordamida).
#
# API va ma’lumotlar bazasi orasida “ko‘prik” bo‘lib xizmat qiladi.
#
# Ichki bog‘lanishlarni (ForeignKey, ManyToMany) ham JSON’da ko‘rsatib beradi.
#
# ✅ Xulosa
#
# Serializer — DRF’ning asosiy komponenti bo‘lib, Model ↔ JSON o‘rtasida ma’lumot almashinuvini boshqaradi.
#
# Serializer uchta ishni bajaradi: Serialization, Deserialization, Validation.
#
# Serializer, ModelSerializer, Nested Serializer, SerializerMethodField kabi turlari bor.
#
# API’da foydalanuvchi yuborgan ma’lumotni tekshirishda ham juda katta rol o‘ynaydi.