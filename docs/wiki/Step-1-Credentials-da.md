[English](Step-1-Credentials) · **Dansk** · [Bahasa Malaysia](Step-1-Credentials-ms)

# Trin 1 - Loginoplysninger

Opgaven starter med en konto. Vi bruger mock-tjenesten Share-a-Naan i stedet for den rigtige Instagram, så en ændret side eller en udelukkelse ikke kan gøre skade. Mock-tjenestens profilside viser login (e-mailen er brugernavnet) og de målkonti, man kan vælge `SIMILAR_ACCOUNT` blandt.

![Target accounts on the profile page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step1-target-accounts.jpg)

## Hvad vi lærte

- Et sikkert sted at øve: en mock-tjeneste lader os få logikken rigtig, før en rigtig konto er i fare.
- Hemmeligheder holdes ude af koden: adgangskoden læses fra miljøvariablerne `INSTA_USERNAME` og `INSTA_PASSWORD`, og `.env` står i `.gitignore`.
- Konstanter ligger i én fil, `constants.py`: `SIMILAR_ACCOUNT`, `BASE_URL` og `LOGIN_URL`.
