import customtkinter as ctk
from tkinter import messagebox
import json

from typing import Dict

import anaEkran
import girisYap

# Tema ayarları
ctk.set_appearance_mode("System")  # "Light", "Dark" veya "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app_icon_path = "../Images/app_icon.ico"  # program logosu dosya yolu

girisVerileri: Dict[str, str] = {}


def kaydol_calistir():

    def dosya_yukle():
        global girisVerileri
        try:
            with open("../Data/girisVerileri.json", "r", encoding="utf-8") as dosya:
                girisVerileri = json.load(dosya)
        except FileNotFoundError:
            girisVerileri = {}
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya yüklenirken hata oluştu: {e}")
            return False
        return True

    def dosya_kaydet(yeni_kullaniciAdi, yeni_sifre):
        girisVerileri.update({yeni_kullaniciAdi: yeni_sifre})

        try:
            with open("../Data/girisVerileri.json", "w", encoding="utf-8") as dosya:
                json.dump(girisVerileri, dosya, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilirken hata oluştu: {e}")

        messagebox.showinfo("Bilgi", "Başarıyla yeni bir kullanıcı oluşturdunuz!")

        girisYapma_ekrani()

    def kaydol():
        alfabe="abcçdefgğhıijklmnoöpqrsştuüvwxyz"
        rakamlar="0123456789"
        ozel_karakterler=".,+-*/-_!?^%&="

        if not kullaniciAdi.get() or not sifre.get() or not sifre_tekrar.get():
            messagebox.showerror("Hata", "Boş alan bırakamazsınız!")
            return

        if len(kullaniciAdi.get()) < 5:
            messagebox.showerror("Hata", "Kullanıcı adınız 5 karakterden kısa olamaz!")
            return

        for i in kullaniciAdi.get():
            if i not in alfabe and i not in rakamlar:
                messagebox.showerror("Hata", "Kullanıcı adınız sadece harf ve rakam içerebilir!")
                return

        if len(sifre.get()) < 8:
            messagebox.showerror("Hata", "Şifreniz 8 karakterden kısa olamaz")
            return

        for i in sifre.get():
            if i not in alfabe and i not in rakamlar and i not in ozel_karakterler:
                messagebox.showerror("Hata", "Şifrenizde tanınamayan karakterler var!")
                return

        if sifre.get() != sifre_tekrar.get():
            messagebox.showerror("Hata", "Şifreler eşleşmiyor!")
            return

        if not dosya_yukle():
            return

        if kullaniciAdi.get() in girisVerileri:
            messagebox.showerror("Hata", "Bu kullanıcı adı zaten kullanılmakta!")
            return

        dosya_kaydet(kullaniciAdi.get(), sifre.get())

    def girisYapma_ekrani():
        kaydolPencere.destroy()
        girisYap.girisYap_calistir()

    def toggle_password():
        # Eğer şifre gizliyse, her iki kutuyu da göster
        if sifre.cget('show') == '*':
            sifre.configure(show='')  # 'configure' kullanılmalı
            sifre_tekrar.configure(show='')  # Şifre tekrarını da aç
            password_icon.configure(text="🔒")  # Şifreyi göster ikonunu değiştir
        else:
            sifre.configure(show='*')  # Şifreyi gizle
            sifre_tekrar.configure(show='*')  # Şifre tekrarını da gizle
            password_icon.configure(text="👁")  # Şifreyi gizle ikonunu değiştir

    kaydolPencere = ctk.CTk()
    kaydolPencere.title("Film/Dizi Takip Uygulaması - Kaydol!")
    kaydolPencere.geometry("700x500")
    kaydolPencere.resizable(False, False)
    kaydolPencere.iconbitmap(app_icon_path)

    ctk.CTkLabel(kaydolPencere, text="Hesap Oluşturun", font=ctk.CTkFont(size=50)).place(x=180, y=80)

    ctk.CTkLabel(kaydolPencere, text="Kullanıcı adı:", font=ctk.CTkFont(size=15)).place(x=152, y=210)
    kullaniciAdi = ctk.CTkEntry(kaydolPencere, width=250)
    kullaniciAdi.place(x=250, y=210)

    ctk.CTkLabel(kaydolPencere, text="Şifre:", font=ctk.CTkFont(size=15)).place(x=203, y=250)
    sifre = ctk.CTkEntry(kaydolPencere, width=250, show="*")
    sifre.place(x=250, y=250)

    # Şifreyi göster/gizle butonu
    password_icon = ctk.CTkButton(kaydolPencere, text="👁", command=toggle_password, width=32, height=28)
    password_icon.place(x=510, y=250)

    ctk.CTkLabel(kaydolPencere, text="Şifre tekrar:", font=ctk.CTkFont(size=15)).place(x=161, y=290)
    sifre_tekrar = ctk.CTkEntry(kaydolPencere, width=250, show="*")
    sifre_tekrar.place(x=250, y=290)

    ctk.CTkButton(kaydolPencere, text="Kaydol", command=kaydol, height=37, width=120, font=ctk.CTkFont(size=17)).place(x=290, y=340)

    ctk.CTkLabel(kaydolPencere, text="Zaten hesabınız var mı?").place(x=230, y=420)
    ctk.CTkButton(kaydolPencere, text="Giriş Yapın", command=girisYapma_ekrani, width=85).place(x=377, y=420)

    kaydolPencere.mainloop()
