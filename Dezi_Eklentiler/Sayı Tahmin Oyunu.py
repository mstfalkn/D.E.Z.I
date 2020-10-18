#Bu oyun Mustafa ALKAN Tarafından Yazılmıştır.
soru="evet"
while soru=="evet" or soru=="EVET" or soru=="Evet":
    import random 
    import time  
    bilgisayarınSeçtiğiSayı=random.randint(1,100) 
    print("------------Sayı Tahmin Oyunu------------")

    benimTahminEtiğimSayı=int(input("Tuttuğum sayıyı tahmin et: ")) 
    print("-----------------------------------------")
    while True:
        if bilgisayarınSeçtiğiSayı==benimTahminEtiğimSayı:   
            print("Doğru Bildin. Tebrikler")
            soru=input("Tekrar Oynamak İster misin ? ") 
            time.sleep(5) 
            break
        elif benimTahminEtiğimSayı>bilgisayarınSeçtiğiSayı:  
            benimTahminEtiğimSayı=int(input("Daha küçük bir sayı dene: ")) 
            print("-----------------------------------------")
        else: 
            benimTahminEtiğimSayı=int(input("Daha büyük bir sayı dene: "))
            print("-----------------------------------------")
