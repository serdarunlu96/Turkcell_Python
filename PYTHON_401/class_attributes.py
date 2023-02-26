# class VeriBilimci(): #sınıf tanımlama
#     print("Bu bir sınıftır.")

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

print(VeriBilimci.sql) # class attributes access

VeriBilimci.sql="Hayır" # class attributes change
print(VeriBilimci.sql)

ali=VeriBilimci() # instantiation - sınıf örnkelendirmesi
print(ali.sql)
ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)
veli = VeriBilimci()
print(veli.sql)
print(veli.bildigi_diller)