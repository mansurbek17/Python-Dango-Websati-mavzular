# Class — bu shablon yoki andoz (template), ya’ni obyektlar yaratish uchun model.
#
# Unda atributlar (xususiyatlar) va metodlar (funksiyalar) bo‘ladi.
#
# Object — bu class asosida yaratilgan haqiqiy nusxa (instance).
#
# Har bir object classdagi xususiyat va metodlarga ega bo‘ladi.

class Avtomobil:
    def __init__(self, model, yil):
        self.model = model
        self.yil = yil

    def info(self):
        print(f"Model: {self.model}, Yil: {self.yil}")

# Object yaratish
mashina = Avtomobil("Toyota", 2020)

mashina.info()  # Model: Toyota, Yil: 2020


# Izoh:
#
# Avtomobil — class.
#
# mashina — Avtomobil classining obyekti.
#
# Class — andoza, object — undan yaratilgan narsa.