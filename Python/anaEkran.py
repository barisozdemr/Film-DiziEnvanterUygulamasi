import customtkinter as ctk
from tkinter import messagebox
import json
from PIL import Image

from typing import Dict, List

# Tema ayarları
ctk.set_appearance_mode("System")  # "Light", "Dark" veya "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

icon_path = "../Images/movieIcon.png"  # Simgenizin dosya yolu
icon_image = ctk.CTkImage(Image.open(icon_path), size=(25, 25))

app_icon_path = "../Images/app_icon.ico"  # program logosu dosya yolu

girisYapanKullaniciAdi = ""

# Verilerin tutulacağı liste
kullaniciVerileri: Dict[str, List[Dict]] = {}

secili_oge = None

onceki_frame = None

current_sort = "Eklenme Sırası"


def anaEkran_calistir():

    # Dosya işlemleri
    def dosya_kaydet():
        try:
            with open("../Data/kullaniciVerileri.json", "w", encoding="utf-8") as dosya:
                json.dump(kullaniciVerileri, dosya, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilirken hata oluştu: {e}")

    def dosya_yukle():
        global kullaniciVerileri
        try:
            with open("../Data/kullaniciVerileri.json", "r", encoding="utf-8") as dosya:
                kullaniciVerileri = json.load(dosya)
                listeyi_guncelle()
        except FileNotFoundError:
            kullaniciVerileri = {}
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya yüklenirken hata oluştu: {e}")

    # Listeyi güncelle =================================================================================================
    def listeyi_guncelle():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
            inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

            text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
            label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525", font=ctk.CTkFont(size=14))
            label.bind("<Button-1>", lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri, par_frame))
            label.pack(pady=2, padx=(10, 2), anchor="w")

            inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "Eklenme Sırası"

    # Listeyi güncelle (Film)
    def listeyi_guncelle_film():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
            if veri['Tür'] == "Film":
                inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

                text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
                label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525",
                                     font=ctk.CTkFont(size=14))
                label.bind("<Button-1>",
                           lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri,
                                                                                                  par_frame))
                label.pack(pady=2, padx=(10, 2), anchor="w")

                inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "Film"

    # Listeyi güncelle (Dizi)
    def listeyi_guncelle_dizi():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
            if veri['Tür'] == "Dizi":
                inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

                text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
                label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525",
                                     font=ctk.CTkFont(size=14))
                label.bind("<Button-1>",
                           lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri,
                                                                                                  par_frame))
                label.pack(pady=2, padx=(10, 2), anchor="w")

                inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "Dizi"

    # Listeyi güncelle (İzlendi)
    def listeyi_guncelle_izlendi():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
            if veri['Durum'] == "İzlendi":
                inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

                text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
                label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525",
                                     font=ctk.CTkFont(size=14))
                label.bind("<Button-1>",
                           lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri,
                                                                                                  par_frame))
                label.pack(pady=2, padx=(10, 2), anchor="w")

                inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "İzlendi"

    # Listeyi güncelle (İzlenecek)
    def listeyi_guncelle_izlenecek():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
            if veri['Durum'] == "İzlenecek":
                inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

                text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
                label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525",
                                     font=ctk.CTkFont(size=14))
                label.bind("<Button-1>",
                           lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri,
                                                                                                  par_frame))
                label.pack(pady=2, padx=(10, 2), anchor="w")

                inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "İzlenecek"

    # Listeyi güncelle (Bekleniyor)
    def listeyi_guncelle_bekleniyor():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
            if veri['Durum'] == "Bekleniyor":
                inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

                text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
                label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525",
                                     font=ctk.CTkFont(size=14))
                label.bind("<Button-1>",
                           lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri,
                                                                                                  par_frame))
                label.pack(pady=2, padx=(10, 2), anchor="w")

                inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "Bekleniyor"

    # Listeyi güncelle (Puan önce en yüksek)
    def listeyi_guncelle_puan_yuksek():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for i in range(5,0,-1):
            for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
                if veri['Puan'] == i:
                    inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

                    text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
                    label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525",
                                         font=ctk.CTkFont(size=14))
                    label.bind("<Button-1>",
                               lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri,
                                                                                                      par_frame))
                    label.pack(pady=2, padx=(10, 2), anchor="w")

                    inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "Puan Yüksek"

    # Listeyi güncelle (Puan önce en düşük)
    def listeyi_guncelle_puan_dusuk():
        global current_sort
        global secili_oge
        secili_oge = None  # Seçili öğeyi sıfırlama

        # Listeyi temizle
        for widget in frame_liste.winfo_children():
            widget.destroy()

        # Listeyi bastır
        for i in range(1, 6):
            for veri in kullaniciVerileri.get(girisYapanKullaniciAdi, []):
                if veri['Puan'] == i:
                    inner_frame2 = ctk.CTkFrame(frame_liste, border_width=2, border_color="#505050", fg_color="#252525")

                    text = f"     Ad: {veri['Ad']}    |    Tür: {veri['Tür']}    |    Durum: {veri['Durum']}    |    Puan: {veri['Puan']}    |    Not: {veri['Not']}      "
                    label = ctk.CTkLabel(inner_frame2, image=icon_image, compound="left", text=text, bg_color="#252525",
                                         font=ctk.CTkFont(size=14))
                    label.bind("<Button-1>",
                               lambda event, par_veri=veri, par_frame=inner_frame2: secileni_degistir(event, par_veri,
                                                                                                      par_frame))
                    label.pack(pady=2, padx=(10, 2), anchor="w")

                    inner_frame2.pack(pady=5, padx=10, anchor="w")

        current_sort = "Puan Düşük"

    def tekrar_sirala():
        if current_sort == "Eklenme Sırası":
            listeyi_guncelle()
        elif current_sort == "Film":
            listeyi_guncelle_film()
        elif current_sort == "Dizi":
            listeyi_guncelle_dizi()
        elif current_sort == "İzlendi":
            listeyi_guncelle_izlendi()
        elif current_sort == "İzlenecek":
            listeyi_guncelle_izlenecek()
        elif current_sort == "Bekleniyor":
            listeyi_guncelle_bekleniyor()
        elif current_sort == "Puan Yüksek":
            listeyi_guncelle_puan_yuksek()
        elif current_sort == "Puan Düşük":
            listeyi_guncelle_puan_dusuk()

    # ==================================================================================================================

    # Yeni kayıt ekle
    def ekle():
        ad = entry_ad.get().strip()
        tur = combo_tur.get()
        durum = combo_durum.get()
        puan = int(slide_puan.get())
        not_ = entry_not.get().strip()

        if not ad or not tur or not durum:
            messagebox.showwarning("Uyarı", "Tüm alanları doldurmalısınız!")
            return

        yeni_veri = {"Ad": ad, "Tür": tur, "Durum": durum, "Puan": puan, "Not": not_}

        if girisYapanKullaniciAdi not in kullaniciVerileri:
            kullaniciVerileri[girisYapanKullaniciAdi] = []

        kullaniciVerileri.get(girisYapanKullaniciAdi).append(yeni_veri)
        tekrar_sirala()
        dosya_kaydet()
        temizle()

    # Kayıt sil
    def sil():
        global onceki_frame
        global secili_oge
        if secili_oge is None:
            messagebox.showwarning("Uyarı", "Lütfen önce bir film/dizi seçin!")
            return
        else:
            # Seçilen öğeyi sil
            kullaniciVerileri[girisYapanKullaniciAdi].remove(secili_oge)
            tekrar_sirala()
            dosya_kaydet()
            secili_oge = None
            onceki_frame = None

    # İzlendi işaretle
    def izlendi_isaretle():
        global onceki_frame
        global secili_oge
        if secili_oge is None:
            messagebox.showwarning("Uyarı", "Lütfen önce bir film/dizi seçin!")
            return
        else:
            # Seçilen öğeyi izlendi işaretle
            if secili_oge['Durum'] == "İzlenecek" or secili_oge['Durum'] == "Bekleniyor":
                secili_oge['Durum'] = "İzlendi"
                tekrar_sirala()
                dosya_kaydet()
            else:
                messagebox.showwarning("Uyarı", "Seçilen film/dizi zaten izlenmiş!")
                tekrar_sirala()
            secili_oge = None
            onceki_frame = None

    # Seçilen öğenin arka plan rengini değiştir
    def secileni_degistir(event, veri, frame):
        global secili_oge
        global onceki_frame
        if onceki_frame and onceki_frame.winfo_exists():
            onceki_frame.configure(fg_color="#252525")

        secili_oge = veri
        onceki_frame = frame
        frame.configure(fg_color="#606060")

    def puan_guncelle(value):
        puan.configure(text=str(int(value)))

    # Formu temizle
    def temizle():
        entry_ad.delete(0, ctk.END)
        combo_tur.set("")
        combo_durum.set("")
        slide_puan.set(1)
        puan.configure(text="1")
        entry_not.delete(0, ctk.END)

    def mouse_hover(event, frame):
        frame.configure(fg_color="#494949")

    def mouse_leave(event, frame):
        frame.configure(fg_color="#2b2b2b")

    def ekleme_sirasi_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle()

    def film_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle_film()

    def dizi_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle_dizi()

    def izlendi_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle_izlendi()

    def izlenecek_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle_izlenecek()

    def bekleniyor_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle_bekleniyor()

    def puan_yuksek_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle_puan_yuksek()

    def puan_dusuk_pressed(event, frame):
        frame.configure(fg_color="#090909")
        listeyi_guncelle_puan_dusuk()

    def mouse_release(event, frame):
        frame.configure(fg_color="#494949")

    # Ana pencere
    anaPencere = ctk.CTk()
    anaPencere.title("Film/Dizi Takip Uygulaması")
    anaPencere.geometry("1300x750")
    anaPencere.resizable(False, False)
    anaPencere.iconbitmap(app_icon_path)

    # Başlık
    frame_baslik = ctk.CTkFrame(anaPencere, border_width=1, border_color="#909090", width=1240, height=60)

    baslik = ctk.CTkLabel(frame_baslik, text="Film/Dizi Takip Uygulaması", font=ctk.CTkFont(size=24, weight="bold"))
    baslik.pack(side="left", padx=110, pady=10)
    kullanici_adi = ctk.CTkLabel(frame_baslik, text="Hoşgeldiniz! "+girisYapanKullaniciAdi, font=ctk.CTkFont(size=15, weight="bold"))
    kullanici_adi.pack(side="right", padx=(470, 150), pady=10)

    frame_baslik.place(x=20, y=10)

    # Filtreleme
    frame_filtreleme = ctk.CTkFrame(anaPencere, width=1260, height=56, fg_color="#242424")

    ctk.CTkLabel(frame_filtreleme, text="Filtrele:", font=ctk.CTkFont(size=14)).place(x=20, y=10)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=95, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: ekleme_sirasi_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="Eklenme Sırası", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: ekleme_sirasi_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=15, y=1)

    inner_frame.place(x=80, y=9)  # ---------------------------------------------------------inner frame (Ekleme Sırası)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=50, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: film_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="Film", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: film_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=15, y=1)

    inner_frame.place(x=215, y=9)  # -----------------------------------------------------------inner frame (Film)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=50, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: dizi_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="Dizi", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: dizi_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=15, y=1)

    inner_frame.place(x=275, y=9)  # -----------------------------------------------------------inner frame (Dizi)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=75, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: izlendi_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="İzlendi", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: izlendi_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=23, y=1)

    inner_frame.place(x=365, y=9)  # -----------------------------------------------------------inner frame (İzlendi)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=75, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: izlenecek_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="İzlenecek", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: izlenecek_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=17, y=1)

    inner_frame.place(x=450, y=9)  # -----------------------------------------------------------inner frame (İzlenecek)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=75, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: bekleniyor_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="Bekleniyor", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: bekleniyor_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=15, y=1)

    inner_frame.place(x=535, y=9)  # -----------------------------------------------------------inner frame (Bekleniyor)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=122, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: puan_yuksek_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="Puan önce en yüksek", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: puan_yuksek_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=15, y=1)

    inner_frame.place(x=650, y=9)  # ------------------------------------------------inner frame (Puan önce en yüksek)

    inner_frame = ctk.CTkFrame(frame_filtreleme, width=122, height=31, border_width=1, border_color="#909090",
                               corner_radius=15)
    inner_frame.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    inner_frame.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    inner_frame.bind("<ButtonPress>", lambda event, frame=inner_frame: puan_dusuk_pressed(event, frame))
    inner_frame.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))

    film_label = ctk.CTkLabel(inner_frame, text="Puan önce en düşük", font=ctk.CTkFont(size=10))
    film_label.bind("<Enter>", lambda event, frame=inner_frame: mouse_hover(event, frame))
    film_label.bind("<Leave>", lambda event, frame=inner_frame: mouse_leave(event, frame))
    film_label.bind("<ButtonPress>", lambda event, frame=inner_frame: puan_dusuk_pressed(event, frame))
    film_label.bind("<ButtonRelease>", lambda event, frame=inner_frame: mouse_release(event, frame))
    film_label.place(x=17, y=1)

    inner_frame.place(x=782, y=9)  # -------------------------------------------------inner frame (Puan önce en düşük)

    frame_filtreleme.place(x=20, y=60)

    # Liste alanı
    frame_liste = ctk.CTkScrollableFrame(anaPencere, width=1240, height=405)
    frame_liste.place(x=20, y=108)

    # Form alanı
    frame_form = ctk.CTkFrame(anaPencere)
    frame_form.place(x=20, y=545)

    ctk.CTkLabel(frame_form, text="Ad:").grid(row=0, column=0, padx=30, pady=5)
    entry_ad = ctk.CTkEntry(frame_form, width=250)
    entry_ad.grid(row=0, column=1, padx=(5, 30), pady=5, sticky="e")

    ctk.CTkLabel(frame_form, text="Tür:").grid(row=1, column=0, padx=30, pady=5)
    combo_tur = ctk.CTkComboBox(frame_form, values=["Film", "Dizi"], state="readonly", width=250)
    combo_tur.grid(row=1, column=1, padx=(5, 30), pady=5, sticky="e")

    ctk.CTkLabel(frame_form, text="Durum:").grid(row=2, column=0, padx=30, pady=5)
    combo_durum = ctk.CTkComboBox(frame_form, values=["İzlendi", "İzlenecek", "Bekleniyor"], state="readonly", width=250)
    combo_durum.grid(row=2, column=1, padx=(5, 30), pady=5, sticky="e")

    ctk.CTkLabel(frame_form, text="Puan:").grid(row=3, column=0, padx=30, pady=5)
    inner_frame = ctk.CTkFrame(frame_form, width=250, height=28)  # --------------------------inner frame

    slide_puan = ctk.CTkSlider(inner_frame, from_=1, to=5, number_of_steps=4, width=200, command=puan_guncelle)
    slide_puan.place(x=10, y=5)
    puan = ctk.CTkLabel(inner_frame, text="3")
    puan.place(x=225, y=0)

    inner_frame.grid(row=3, column=1, padx=30, pady=5)  # ------------------------------------inner frame

    ctk.CTkLabel(frame_form, text="Not:").grid(row=4, column=0, padx=30, pady=5)
    entry_not = ctk.CTkEntry(frame_form, width=250)
    entry_not.grid(row=4, column=1, padx=(5, 30), pady=5, sticky="e")

    # Butonlar
    frame_butonlar = ctk.CTkFrame(anaPencere, width=1250, height=50)
    frame_butonlar.place(x=470, y=685)

    ctk.CTkButton(frame_butonlar, text="Ekle", command=ekle).grid(row=0, column=0, padx=10, pady=10)
    ctk.CTkButton(frame_butonlar, text="Seçileni Sil", command=sil).grid(row=0, column=1, padx=10, pady=10)
    ctk.CTkButton(frame_butonlar, text="Seçileni İzlendi Olarak İşaretle", command=izlendi_isaretle).grid(row=0, column=2, padx=10, pady=10)

    dosya_yukle()  # Uygulama açılırken veriyi yükle

    temizle()

    listeyi_guncelle()

    anaPencere.mainloop()
