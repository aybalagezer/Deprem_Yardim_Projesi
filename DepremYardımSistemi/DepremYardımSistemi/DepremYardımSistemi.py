#5 ÜYELİ SİSTEM#
giris_bildiri="SİSTEMİMİZE HOŞGELDİNİZ\n"
karakter_hesap=len(giris_bildiri)
ortala_hesap=(116-karakter_hesap)//2
print(" "*ortala_hesap+giris_bildiri+" "*ortala_hesap)
print("****** SEÇENEKLER *******\n")
print("1-Sisteme Üye Ol")
print("2-Sisteme Giriş Yap")
print("3-Şifremi Unuttum")
print("4-Admin Girişi\n")
secim=int(input("Seçiminizi Giriniz:"))
kullanici_liste=["ali","veli","ahmet","ayşe","fatma"]
sifre_liste=[123,456,789,915,825]
print("\n")

if(secim==1):
    print("****** YENİ ÜYELİK ******\n")
    ad_soyad=input("Ad Soyad:")
    telefon=int(input("Telefon Numaranızı Ekleyiniz:"))
    sirket_adi=input("Tır Şirketinizin Adı/Bireysel İse Plaka Giriniz:")
    kullanici_adi=input("Kullanıcı Adını Bellirleyiniz:")
    sifre=int(input("Şifrenizi Belirleyiniz:"))
    print("****** ÜYELİĞİNİZ KABUL EDİLMİŞTİR ******\n\n")
    kullanici_liste.append(kullanici_adi)
    sifre_liste.append(sifre)
    print("GİRİŞ")
    yeni_kullanici=input("Kullanıcı Adınız:")
    yeni_sifre=int(input("Şifreniz:"))
    if(yeni_kullanici==kullanici_liste[0],kullanici_liste[1],kullanici_liste[2],kullanici_liste[3],kullanici_liste[4],kullanici_liste[5] and yeni_sifre==sifre_liste[0],sifre_liste[1],sifre_liste[2],sifre_liste[3],sifre_liste[4],sifre_liste[5]):
        print("Giriş Başarıyla Yapılmıştır")
    else:
        print("Kullanıcı Adı veya Şifre Hatalıdır Lütfen Tekrar Deneyiniz")
elif(secim==2):
    print("****** Üye GİRİŞİ ******\n")
    kullanici_adi=input("Kullanıcı Adınız:")
    sifre=int(input("Şifreniz:"))
    if(kullanici_adi==kullanici_liste[0],kullanici_liste[1],kullanici_liste[2],kullanici_liste[3],kullanici_liste[4] and sifre==sifre_liste[0],sifre_liste[1],sifre_liste[2],sifre_liste[3],sifre_liste[4]):
        print("Giriş Başarıyla Yapılmıştır")
    else:
        print("Kullanıcı Adı veya Şifre Hatalıdır Lütfen Tekrar Deneyiniz")
elif(secim==3):
    print("****** ŞİFRE YENİLEME ******\n")
    telefon=int(input("Telefon Numaranızı Giriniz:"))
    gönderilen_kod=104
    print("Telefonunuza Kod Gönderilmiştir.")
    kod=int(input("Gelen Kodu Giriniz:"))
    if(kod==gönderilen_kod):
        yenisifre=int(input("Yeni Şifre Belirleyiniz:"))
        print("Şifreniz Yenilenmiştir")
    else:
        print("Kod Yanlıştır Yeniden Deneyiniz")
else:
    print("****** ADMİN GİRİŞİ ******\n")
    admin_kullanici=input("Kullanıcı Adınız:")
    admin_sifre=int(input("Şifreniz:"))
    print("\n")
    adminsifre=105
    if(admin_sifre==adminsifre):
        print("****** YAPILACAK İŞLEMLER ******\n")
        print("1-Yola Çıkan Yeni Yardım Tırı Ekleme")
        print("2-Yeni Tırdaki Ürün Sayısını Ekle")
        print("3-Ulaşan Tırları Listele\n")
        secim_admin=int(input("Seçiminizi Giriniz:"))
        print("\n")
        if(secim_admin==1):
            tır_plaka=input("Tırın Plakasını Giriniz:")
            tır_sahibi=input("Tır Bir Şirkete Bağlı İse Şirket İsmi/Bireysel İse Kişi Adı:")
            tır_söför_adsoyad=input("Tırı Alana Ulaştıracak Şöför Ad Soyad:")
            tır_söför_telefon=int(input("Şöför'ün Telefon Numarası:"))
            yol_süresi=int(input("İstanbul'a Gidiş Süresi:"))
            print("{} Plakalı Tır İstanbula'a {} saat sonra ulaşacaktır.".format(tır_plaka, yol_süresi))
        elif(secim_admin==2):
            makarnasayisi=int(input("Makarna Sayısı:"))
            corbasayisi=int(input("Çorba Sayısı:"))
            susayisi=int(input("Su Sayısı:"))
            battaniyesayisi=int(input("Battaniye Sayısı:"))
            ekmeksayisi=int(input("Ekmek Sayısı:"))
            print("\n")
            print("ÜRÜNLER")
            print("Makarna:{}".format(makarnasayisi))
            print("Çorba:{}".format(corbasayisi))
            print("Su:{}".format(susayisi))
            print("Battaniye:{}".format(battaniyesayisi))
            print("Ekmek:{}".format(ekmeksayisi))
        elif(secim_admin==3):
            tır_plaka=input("Ulaşan Tırın Plakasını Giriniz:")
            print("{} Plakalı Tır İstanbula'a ulaşmıştır.".format(tır_plaka))
        else:
            print("Yanlış Seçim Girdiniz")
           





