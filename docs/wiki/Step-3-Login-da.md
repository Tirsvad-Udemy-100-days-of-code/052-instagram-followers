[English](Step-3-Login) · **Dansk** · [Bahasa Malaysia](Step-3-Login-ms)

# Trin 3 - Login

`login()` åbner loginsiden, udfylder e-mail og adgangskode og trykker på "Log in". Så følger to pop-ups: "Save your login info?" og "Turn on notifications". Begge lukkes med knappen "Not Now".

![Share-a-Naan login page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-login-page.jpg)

![Save your login info pop-up](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-save-info-popup.jpg)

![Turn on notifications pop-up](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-notifications-popup.jpg)

På den rigtige Instagram ændrer XPaths og selektorer sig ved hvert besøg. Løsningen er at finde en knap på dens tekst, for eksempel `//button[contains(text(), 'Not Now')]`, og ikke på et genereret klassenavn.

## Hvad vi lærte

- At finde elementer på synlig tekst med `contains()` og `text()`, som overlever ændringer i layoutet.
- At vente på et element med `WebDriverWait` i stedet for en fast pause.
- At håndtere valgfrie pop-ups: klik på dem, hvis de findes, og fortsæt, hvis de ikke gør.
