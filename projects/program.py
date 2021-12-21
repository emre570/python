import tkinter as tk
import sqlite3 as sql

pencere = tk.Tk()
pencere.title("test")
pencere.geometry("600x670")

UrunDB = sql.connect("UrunDB.sqlite", timeout=3600)
crs = UrunDB.cursor()

#Tablonun olup olmadığını kontrol eder. Eğer yoksa, oluşturur.
olustur = """CREATE TABLE IF NOT EXISTS urunler (
    "id"	INTEGER NOT NULL UNIQUE,
	"ad"	TEXT NOT NULL,
	"fiyat"	NUMERIC DEFAULT 0,
	PRIMARY KEY("id")
);"""
crs.execute(olustur)
UrunDB.commit()

def EkleBtn():
    try:
        urunid = identry.get()
        urunad = adentry.get()
        urunfiyat = fiyatentry.get()
        
        ekle = """INSERT INTO urunler(id, ad, fiyat) VALUES({}, "{}", {});""".format(urunid, urunad, urunfiyat)
        crs.execute(ekle)
        UrunDB.commit()

        lblid.config(text=urunid)
        lblad.config(text=urunad)
        lblfiyat.config(text=urunfiyat)
        lbldizi.config(text="Ürün eklendi.")
            
        identry.delete(0, tk.END)
        adentry.delete(0, tk.END)
        fiyatentry.delete(0, tk.END)
    except sql.OperationalError:
        lbldizi.config(text="Lütfen girişi boş bırakmayınız!")
        
def SilBtn():
    try:
        id_sil = identry_sil.get()
        sil = """DELETE FROM urunler WHERE id = {}""".format(id_sil)
        crs.execute(sil)
        UrunDB.commit()

        lblid.config(text="-----")
        lblad.config(text="-----")
        lblfiyat.config(text="-----")
        lbldizi.config(text="Ürün silindi.")
        
        identry_sil.delete(0, tk.END)
    except sql.OperationalError:
        lbldizi.config(text="Lütfen girişi boş bırakmayınız!")
    
def BulBtn():
    try:
        id_bul = identry_bul.get()
        identry_bul.delete(0, tk.END)
        
        bul = """SELECT * FROM urunler WHERE id = {}""".format(id_bul)
        crs.execute(bul)
        UrunDB.commit()
        
        bulunan = crs.fetchone()
        lblid.config(text=bulunan[0])
        lblad.config(text=bulunan[1])
        lblfiyat.config(text=bulunan[2])
        lbldizi.config(text="Ürün bulundu.")
        
        identry_bul.delete(0, tk.END)
    except TypeError:
        lbldizi.config(text="Böyle bir ürün yok.")
    except sql.OperationalError:
        lbldizi.config(text="Lütfen girişi boş bırakmayınız!")
    
def GuncelleBtn():
    try:
        yenifiyat = fiyatentry_guncelle.get()
        urunid = identry_guncelle.get()
        
        guncelle = """UPDATE urunler SET fiyat = {} WHERE id = {}""".format(yenifiyat, urunid)
        crs.execute(guncelle)
        UrunDB.commit()

        lblid.config(text="-----")
        lblad.config(text="-----")
        lblfiyat.config(text="-----")
        lbldizi.config(text="Ürün fiyatı güncellendi.")
        
        identry_guncelle.delete(0, tk.END)
        fiyatentry_guncelle.delete(0, tk.END)
    except sql.OperationalError:
        lbldizi.config(text="Lütfen girişleri boş bırakmayınız!")


###------------------------------------ ÜRÜN EKLEME YERİ ------------------------------------###
ekleme = tk.Label(text="Ürün Ekleme", font="Arial 12 bold", justify="left")
ekleme.pack()
 
#ID için label ve giriş kutusu   
id_label = tk.Label(text="ID", justify="left")
id_label.pack()
identry = tk.Entry(width=30)
identry.pack()

#Ürün adı için label ve giriş kutusu  
ad_label = tk.Label(text="Ürün Adı", justify="left")
ad_label.pack()
adentry = tk.Entry(width=30)
adentry.pack()    

#Ürün fiyatı için label ve giriş kutusu  
fiyat_label = tk.Label(text="Fiyatı", justify="left")
fiyat_label.pack()
fiyatentry = tk.Entry(width=30)
fiyatentry.pack()

#Giriş butonu
girisEkle = tk.Button(text="Ekle", bg="#4dff9a", command=EkleBtn, font="Arial 10 bold")
girisEkle.pack()
###------------------------------------------------------------------------------------------###

###------------------------------------ ÜRÜN SİLME YERİ ------------------------------------###
silme = tk.Label(text="Ürün Silme", font="Arial 12 bold", justify="left")
silme.pack()
 
#ID için label ve giriş kutusu   
id_sil_label = tk.Label(text="ID", justify="left")
id_sil_label.pack()
identry_sil = tk.Entry(width=30)
identry_sil.pack()

#Silme butonu
silBtn = tk.Button(text="Sil", bg="#ff8533", command=SilBtn, font="Arial 10 bold")
silBtn.pack()
###------------------------------------------------------------------------------------------###

###------------------------------------ ÜRÜN FİYAT GÜNCELLEME YERİ ------------------------------------###
guncelleme = tk.Label(text="Ürün Fiyat Güncelleme", font="Arial 12 bold", justify="left")
guncelleme.pack()

id_guncel_label = tk.Label(text="ID", justify="left")
id_guncel_label.pack()
identry_guncelle = tk.Entry(width=30)
identry_guncelle.pack()

fiyat_guncel_label = tk.Label(text="Yeni Fiyat")
fiyat_guncel_label.pack()
fiyatentry_guncelle = tk.Entry(width=30)
fiyatentry_guncelle.pack()

guncelleBtn = tk.Button(text="Güncelle", bg="#ffff33", command=GuncelleBtn, font="Arial 10 bold")
guncelleBtn.pack()
###------------------------------------------------------------------------------------------###

###------------------------------------ ÜRÜN BULMA YERİ ------------------------------------###
bulma = tk.Label(text="Ürün Bulma", font="Arial 12 bold", justify="left")
bulma.pack()

id_bul_label = tk.Label(text="ID")
id_bul_label.pack()

identry_bul = tk.Entry(width=30)
identry_bul.pack()

bulBtn = tk.Button(text="Bul", bg="#4da6ff", command=BulBtn, font="Arial 10 bold")
bulBtn.pack()
###------------------------------------------------------------------------------------------###

###------------------------------------ ÜRÜN LİSTELEME YERİ ------------------------------------###
idtitle = tk.Label(text="ID")
idtitle.pack()
lblid = tk.Label(text="-----")
lblid.pack()

adtitle = tk.Label(text="İsim")
adtitle.pack()
lblad = tk.Label(text="-----")
lblad.pack()

fiyattitle = tk.Label(text="Fiyat")
fiyattitle.pack()
lblfiyat = tk.Label(text="-----")
lblfiyat.pack()

lblbaslik = tk.Label(text="Durum Bilgisi")
lblbaslik.pack()
lbldizi = tk.Label(text="-----")
lbldizi.pack()
###------------------------------------------------------------------------------------------###
pencere.mainloop()
