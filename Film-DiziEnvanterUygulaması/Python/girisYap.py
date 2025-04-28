import customtkinter as ctk
from tkinter import messagebox
import json

import anaEkran
import kaydol

# Tema ayarları
ctk.set_appearance_mode("System")  # "Light", "Dark" veya "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app_icon_path = "../Images/app_icon.ico"  # program logosu dosya yolu

girisVerileri = {}


def girisYap_calistir():

    def dosya_yukle():
        global girisVerileri
        try:
            with open("../Data/girisVerileri.json", "r", encoding="utf-8") as dosya:
                girisVerileri = json.load(dosya)
        except FileNotFoundError:
            girisVerileri = {}
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya yüklenirken hata oluştu: {e}")

    def giris():
        if kullaniciAdi.get() in girisVerileri and girisVerileri.get(kullaniciAdi.get()) == sifre.get():
            anaEkran.girisYapanKullaniciAdi = kullaniciAdi.get()
            girisPencere.destroy()
            anaEkran.anaEkran_calistir()
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya parolanız yanlış!")

    def kaydolma_ekrani():
        girisPencere.destroy()
        kaydol.kaydol_calistir()

    def toggle_password():
        # Eğer şifre gizliyse, şifreyi göster
        if sifre.cget('show') == '*':
            sifre.configure(show='')  # 'configure' kullanılmalı
            password_icon.configure(text="🔒")  # Şifreyi göster ikonunu değiştir
        else:
            sifre.configure(show='*')  # Şifreyi gizle
            password_icon.configure(text="👁")  # Şifreyi gizle ikonunu değiştir

    girisPencere = ctk.CTk()
    girisPencere.title("Film/Dizi Takip Uygulaması - Giriş Yap!")
    girisPencere.geometry("700x500")
    girisPencere.resizable(False, False)
    girisPencere.iconbitmap(app_icon_path)

    ctk.CTkLabel(girisPencere, text="Giriş Yapın", font=ctk.CTkFont(size=50)).place(x=235, y=80)

    ctk.CTkLabel(girisPencere, text="Kullanıcı adı:", font=ctk.CTkFont(size=15)).place(x=152, y=210)
    kullaniciAdi = ctk.CTkEntry(girisPencere, width=250)
    kullaniciAdi.place(x=250, y=210)

    ctk.CTkLabel(girisPencere, text="Şifre:", font=ctk.CTkFont(size=15)).place(x=203, y=250)
    sifre = ctk.CTkEntry(girisPencere, width=250, show="*")
    sifre.place(x=250, y=250)

    # Şifreyi göster/gizle butonu
    password_icon = ctk.CTkButton(girisPencere, text="👁", command=toggle_password, width=32, height=28)
    password_icon.place(x=510, y=250)

    ctk.CTkButton(girisPencere, text="Giriş", command=giris, height=37, width=120, font=ctk.CTkFont(size=17)).place(x=290, y=320)

    ctk.CTkLabel(girisPencere, text="Hesabınız yok mu?").place(x=250, y=400)
    ctk.CTkButton(girisPencere, text="Kaydolun", command=kaydolma_ekrani, width=80).place(x=370, y=400)

    girisPencere.bind("<Return>", lambda event: giris())

    dosya_yukle()

    girisPencere.mainloop()
