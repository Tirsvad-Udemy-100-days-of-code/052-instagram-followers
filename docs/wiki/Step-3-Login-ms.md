[English](Step-3-Login) · [Dansk](Step-3-Login-da) · **Bahasa Malaysia**

# Langkah 3 - Log masuk

`login()` membuka halaman log masuk, mengisi e-mel dan kata laluan, kemudian menekan "Log in". Dua tetingkap timbul menyusul: "Save your login info?" dan "Turn on notifications". Kedua-duanya ditutup dengan butang "Not Now".

![Share-a-Naan login page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-login-page.jpg)

![Save your login info pop-up](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-save-info-popup.jpg)

![Turn on notifications pop-up](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-notifications-popup.jpg)

Pada Instagram sebenar, XPath dan pemilih berubah pada setiap lawatan. Penyelesaiannya ialah mencari butang melalui perkataannya, contohnya `//button[contains(text(), 'Not Now')]`, dan bukan melalui nama kelas yang dijana.

## Apa yang kami peroleh

- Mencari elemen melalui teks yang kelihatan dengan `contains()` dan `text()`, yang tahan perubahan reka letak.
- Menunggu elemen dengan `WebDriverWait` dan bukan jeda tetap.
- Mengendalikan tetingkap timbul pilihan: klik jika ada dan teruskan jika tiada.
