sinir=50000
magaza_adi=input("Magaza adi nedir?: ")
gelir=int(input("Gelirinizi giriniz: "))
if gelir > sinir:
    print("Tebrikler: " + magaza_adi + " 5promosyon kazandınız.")
elif gelir < sinir:
    print("Uyarı, dusuk gelir: " + str(gelir))
else:
    print("Takibe devam.")