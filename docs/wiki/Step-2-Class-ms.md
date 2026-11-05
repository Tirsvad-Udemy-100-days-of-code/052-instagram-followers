[English](Step-2-Class) · [Dansk](Step-2-Class-da) · **Bahasa Malaysia**

# Langkah 2 - Kelas

Oleh sebab bot mempunyai beberapa langkah, kod disusun dalam sebuah kelas, `InstaFollower`. `__init__` mencipta pemacu Selenium. Tiga kaedah `login()`, `find_followers()` dan `follow()` dipanggil mengikut urutan itu.

![Outline of the InstaFollower class](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step2-class-outline.png)

Kelas ini ialah penyesuai Selenium dalam lapisan `infrastructure`. Satu kes guna kecil, `run_bot`, memanggil tiga kaedah melalui protokol `Follower`, jadi urutan diuji tanpa pelayar.

## Apa yang kami peroleh

- Mengumpulkan langkah yang berkongsi keadaan (pemacu) dalam satu kelas.
- Menyuntik pemacu dan fungsi tidur supaya ujian menggunakan pemacu palsu dan tidak menunggu.
- Menutup pelayar dengan context manager (`with InstaFollower() as follower:`).
