class VeriBilimci():
    bildigi_diller = ["R","Python"]
    bolum = ''
    sql = ''
    deneyim_yili=0
    def __init__(self): # her örnek kendi içinde degisen özellikler ( ali, veli vs ) 
        self.bildigi_diller = []
        self.bolum=''

ali= VeriBilimci()
ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)
ali.bolum="istatistik"
print(ali.bolum)

veli= VeriBilimci()
veli.bildigi_diller.append("R")
print(veli.bildigi_diller)
veli.bolum="end_muh"
print(veli.bolum)

print(VeriBilimci.bildigi_diller)