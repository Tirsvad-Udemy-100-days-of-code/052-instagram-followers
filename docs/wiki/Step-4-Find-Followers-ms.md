[English](Step-4-Find-Followers) · [Dansk](Step-4-Find-Followers-da) · **Bahasa Malaysia**

# Langkah 4 - Cari pengikut

`find_followers()` membuka halaman akaun sasaran di `/u/<akaun>` dan mengklik pautan pengikut. Senarai dalam modal pada mulanya memuatkan kira-kira sedozen pengikut, maka kami menatal untuk memuatkan selebihnya.

![Profile of the target account](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-target-profile.jpg)

![Followers modal](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-followers-modal.jpg)

Modal bukan elemen yang menatal. Bahagian yang boleh ditatal ialah elemen dalaman `followers-scroll`, jadi skrip menatal elemen itu: `arguments[0].scrollTop = arguments[0].scrollHeight`.

![Followers modal scrolled to the end](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-followers-scrolled.jpg)

## Apa yang kami peroleh

- Menjalankan JavaScript daripada Selenium dengan `execute_script`.
- Mencari elemen yang benar-benar menatal dengan memeriksa halaman, bukan menatal seluruh tetingkap.
- Berhenti seketika antara tatalan supaya halaman sempat memuatkan lebih banyak entri.
