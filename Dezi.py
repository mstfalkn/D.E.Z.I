#Bu Uygulama Mustafa ALKAN Tarafından Yazılmıştır.


import random
import time
import datetime
import webbrowser
import requests
import json
import feedparser




print("-----------------------------")
print("           MERHABA           ")
print("Ben kişisel asistanın D.E.Z.İ")
print("-----------------------------")
time.sleep(1)
durum=input("Bugün Nasılsın ?")
print("-----------------------------")
print("Seni görmek beni mutlu etti ")
time.sleep(1)



while True :

    durum2=random.randint(1,12)
    tarihVeSaat=datetime.datetime.now()
    yıl=tarihVeSaat.year
    ay=tarihVeSaat.month
    gün=tarihVeSaat.day
    saat=tarihVeSaat.hour
    dakika=tarihVeSaat.minute
        
    print("-----{}/{}/{}-----{}.{}-----".format(gün,ay,yıl,saat,dakika))
    istek=input("Nasıl yardımcı Olabilirim ? ")
    print("----------------------------")
        


    if istek=="oturumu kapat" or istek=="OTURUMU KAPAT":
        print("Oturumunuz Kapatılıyor")
        time.sleep(5)
        break

    elif istek=="?" :
        print("Bu uygulama Mustafa ALKAN Tarafından\n18/09/2020 Tarihinde demo olarak Yazılmıştır\nHala Geliştirme Sürecindedir.")
        print("----------------------------")
        time.sleep(6)

    elif istek=="günün sözü" or istek=="GÜNÜN SÖZÜ" :
        if durum2==1:
            print("Başarı bir yolculuktur, bir varış noktası değil. Ben Sweetland")
            time.sleep(3)
        elif durum2==2:
            print("Yapabildiğimiz her şeyi yapsaydık, buna kendimiz bile şaşardık. Thomas Edison")
            time.sleep(3)
        elif durum2==3:
            print("Bütün büyük işler, küçük başlangıçlarla olur. Cicero")
            time.sleep(3)
        elif durum2==4:
            print("Deneyim: En acımasız öğretmen odur. Fakat en iyi öğretmen de odur. C.S. Lewis")
            time.sleep(3)
        elif durum2==5:
            print("Başarıya ulaşıp sıçrama yapan bireyler, aynı zamanda değişimin ustaları olacaklardır. Kanter")
            time.sleep(3)
        elif durum2==6:
            print("Dünyada bir çok kabiliyetli kişiler, küçük bir cesaret sahibi olmadıkları için kaybolurlar. Sydney Smith")
            time.sleep(3)
        elif durum2==7:
            print("Ne kadar bilirsen bil, söylediklerin karşındakilerin anlayabileceği kadardır. Mevlana")
            time.sleep(3)
        elif durum2==8:
            print("Güçlükler başarının değerini artıran süslerdir. Moliere")
            time.sleep(3)
        elif durum2==9:
            print("Ders alınmış başarısızlık başarı demektir.")
            time.sleep(3)
        elif durum2==10:
            print("Herşeyi denerim; ama yapabildiklerimi yaparım. Herman Melville")
            time.sleep(3)
        elif durum2==11:
            print("Derdi dünya olanın, dünya kadar derdi olur. Yunus Emre")
            time.sleep(3)
        else :
            print("Başarı insana belki çok şey öğretmez, fakat başarısızlık çok şey öğretir. çin atasözü")
            time.sleep(3)
    
    elif istek=="whatsapp aç" or istek=="WHATSAPP AÇ" or istek=="whatsapp web" or istek=="WHATSAPP WEB" :
        print("Whatsapp açılıyor.")
        webbrowser.open_new_tab("https://web.whatsapp.com/")
        time.sleep(3)

    elif istek=="instagram aç" or istek=="İNSTAGRAM AÇ" :
        print("İnstagram açılıyor.")
        webbrowser.open_new_tab("https://www.instagram.com/")
        time.sleep(3)
        
    elif istek=="youtube aç" or istek=="YOUTUBE AÇ":
        print("YouTube açılıyor.")
        webbrowser.open_new_tab("https://www.youtube.com/")
        time.sleep(3)

    elif istek=="hava durumu aç" or istek=="HAVA DURUMU AÇ":
        def hava():
            parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|35890|IZMIR|")
            parse = parse["entries"][0]["summary"]
            parse = parse.split()
            print ("İzmir Kiraz:", parse[4], parse[5])
            return (hava)
        hava()
        time.sleep(3)
        
    elif istek=="mail aç" or istek=="MAİL AÇ":
        print("Outlook açılıyor.")
        webbrowser.open_new_tab("https://outlook.live.com/mail/0/inbox")
        time.sleep(3) 

    elif istek=="borsa aç" or istek=="BORSA AÇ":
        adres="https://finans.truncgil.com/today.json"
        durum=requests.get(adres)
        veriler=durum.json()
        güncellemeTarihi=veriler["Güncelleme Tarihi"]
        
        gramAltın=veriler["Gram Altın"]
        gramAltınAlış=gramAltın["Alış"]
        gramAltınSatış=gramAltın["Satış"]
        gramAltınyazı=("{} tarihinde \nGram Altın Alışı: {}.\nGram Altın Satışı: {}".format(güncellemeTarihi,gramAltınAlış,gramAltınSatış))

        abdDoları=veriler["ABD DOLARI"]
        abdDolarıAlış=abdDoları["Alış"]
        abdDolarıSatış=abdDoları["Satış"]
        abdDolarıYazı=("{} tarihinde \nUSD Alışı: {}.\nUSD Satışı: {}".format(güncellemeTarihi,abdDolarıAlış,abdDolarıSatış))

        euro=veriler["EURO"]
        euroalış=euro["Alış"]
        eurosatış=euro["Satış"]
        euroyazı=("{} tarihinde \nEURO Alışı: {}.\nEURO Satışı: {}".format(güncellemeTarihi,euroalış,eurosatış))

        
        soru=input("Hangi Borsa Değerini Merak Ediyorsun ?") 
        if soru=="USD" or soru=="usd":
            print(abdDolarıYazı)
            time.sleep(3)
        elif soru=="EURO" or soru=="euro" :
            print(euroyazı)
            time.sleep(3)
        elif soru=="ALTIN" or soru=="altın":
            print(gramAltınyazı)
            time.sleep(3)
        else:
            print("Henüz Bunu Desteklemiyorum.")
            print("Bu Komutu eklemesi için Yönteiciye Başvurun")
            time.sleep(3)

    elif istek=="oyun aç" or istek=="OYUN AÇ":
        bilgisayarınSeçtiğiSayı=random.randint(1,100) 
        print("-----Sayı Tahmin Oyunu------")

        benimTahminEtiğimSayı=int(input("Tuttuğum sayıyı tahmin et: ")) 
        print("----------------------------")
        while True:
            if bilgisayarınSeçtiğiSayı==benimTahminEtiğimSayı:   
                print("Doğru Bildin. Tebrikler") 
                time.sleep(5) 
                break
            elif benimTahminEtiğimSayı>bilgisayarınSeçtiğiSayı:  
                benimTahminEtiğimSayı=int(input("Daha küçük bir sayı dene: ")) 
                print("----------------------------")
            else: 
                benimTahminEtiğimSayı=int(input("Daha büyük bir sayı dene: "))
                print("---------------------------")

    elif istek=="E-DEVLET AÇ" or istek=="e-devlet aç" or istek=="e devlet aç" or istek=="E DEVLET AÇ":
        webbrowser.open_new_tab("https://www.turkiye.gov.tr")
        print("E-devlet Açılıyor")
        time.sleep(3)

    elif istek=="linkedin aç" or istek=="LİNKEDIN AÇ" or istek=="LINKEDIN AÇ":
        webbrowser.open_new_tab("https://www.linkedin.com/")
        print("LinkedIn açılıyor")
        time.sleep(3)

    elif istek=="discord aç" or istek=="DISCORD AÇ" or istek=="diskort aç" :
        webbrowser.open_new_tab("https://discord.com/app")
        print("Discord açılıyor")
        time.sleep(3)

    elif istek=="microsoft teams aç" or istek=="microsoft teams" or istek=="MICROSOFT TEAMS AÇ" :
        webbrowser.open_new_tab("https://teams.microsoft.com/")
        print("Microsoft Teams açılıyor")
        time.sleep(3)

    elif istek=="uzaktan eğitim aç" or istek=="UZAKTAN EĞİTİM AÇ" or istek=="uzaktan eğitim":
        webbrowser.open_new_tab("http://ue.bakircay.edu.tr/")
        print("Bakırçay Üniversitesi Uzaktan Eğitim\nProgramı açılıyor.")
        time.sleep(3)

    elif istek=="spotify aç" or istek=="SPOTIFY AÇ":
        webbrowser.open_new_tab("https://open.spotify.com")
        print("Spotify Açılıyor.")

    elif istek=="github aç" or istek=="GITHUB AÇ":
        webbrowser.open_new_tab("https://github.com")
        print("GitHub açılıyor.")

    elif istek=="araştırma yap" or istek=="ARAŞTIRMA YAP":
        ara=input("Araştırma Yapmak İstediğiniz konuyu giriniz: ")
        plartform=input("Hangi Plartform Üzerinden Araştırma Yapmak istersiniz ? (wikipadia, google) ")
        if plartform=="wikipadia" or plartform=="WİKİPADİA":
            print("Wikipadia da ilgili araştırma yapılıyor")
            time.sleep(1)
            webbrowser.open_new_tab("https://tr.wikipedia.org/wiki/{}".format(ara))
        elif plartform=="google" or plartform=="GOOGLE":
            print("Google de ilgili araştırma yapılıyor")
            time.sleep(1)
            webbrowser.open_new_tab("https://www.google.com/search?q={}".format(ara))
    
    else :
        print("Henüz Bunu Desteklemiyorum.")
        print("Geri Bildirim için: m.alkan35@hotmail.com")
        time.sleep(4)
        break
