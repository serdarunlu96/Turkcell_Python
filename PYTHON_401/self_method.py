class VeriBilimci(): # sınıf
    calisanlar = []
    def __init__(self): # her örnek kendi içinde degisen özellikler nesneler ( ali, veli vs ) 
        self.bildigi_diller = []
        self.bolum=''
    def dil_ekle(self, yeni_dil): # ali, veli vs dil ekleme
        self.bildigi_diller.append(yeni_dil)

ali=VeriBilimci()
ali.dil_ekle("R")
print(ali.bildigi_diller)