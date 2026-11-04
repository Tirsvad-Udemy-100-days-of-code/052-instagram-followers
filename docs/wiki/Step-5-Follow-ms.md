[English](Step-5-Follow) · [Dansk](Step-5-Follow-da) · **Bahasa Malaysia**

# Langkah 5 - Ikut

`follow()` mencari setiap butang "Follow" dalam senarai pengikut dan mengkliknya dengan jeda satu saat antara klik, supaya bot kurang kelihatan seperti mesin. Butang yang sudah menyatakan "Following" dilangkau.

Jika klik dipintas oleh tetingkap timbul "Unfollow?" (akaun yang sudah diikuti), Selenium menimbulkan `ElementClickInterceptedException`. Bot mengklik "Cancel" dan meneruskan dengan butang seterusnya.

![Unfollow pop-up with a Cancel button](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step5-unfollow-popup.jpg)

![Followers after the follow loop](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step5-followed.jpg)

## Apa yang kami peroleh

- Mengendalikan pengecualian tertentu dengan sengaja: tiada `except` kosong, hanya kes yang diterangkan dalam tugasan.
- Menguji laluan ralat itu dengan pemacu palsu yang menimbulkan pengecualian.
- Menghormati perkhidmatan: satu saat antara klik, dan perkhidmatan tiruan dengan butang "Reset Share-a-Naan" untuk larian semula yang bersih.
