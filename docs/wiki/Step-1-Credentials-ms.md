[English](Step-1-Credentials) · [Dansk](Step-1-Credentials-da) · **Bahasa Malaysia**

# Langkah 1 - Maklumat log masuk

Tugasan bermula dengan sebuah akaun. Kami menggunakan perkhidmatan tiruan Share-a-Naan dan bukannya Instagram sebenar, supaya halaman yang berubah atau sekatan tidak menjejaskan sesiapa. Halaman profil perkhidmatan tiruan itu menunjukkan log masuk (e-mel ialah nama pengguna) dan akaun sasaran untuk memilih `SIMILAR_ACCOUNT`.

![Target accounts on the profile page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step1-target-accounts.jpg)

## Apa yang kami peroleh

- Tempat selamat untuk berlatih: perkhidmatan tiruan membolehkan kami membetulkan logik sebelum akaun sebenar berisiko.
- Rahsia dijauhkan daripada kod: kata laluan dibaca daripada pemboleh ubah persekitaran `INSTA_USERNAME` dan `INSTA_PASSWORD`, dan `.env` ada dalam `.gitignore`.
- Pemalar disimpan dalam satu fail, `constants.py`: `SIMILAR_ACCOUNT`, `BASE_URL` dan `LOGIN_URL`.
