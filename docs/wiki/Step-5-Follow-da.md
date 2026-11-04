[English](Step-5-Follow) · **Dansk** · [Bahasa Malaysia](Step-5-Follow-ms)

# Trin 5 - Følg

`follow()` finder hver "Follow"-knap i følgerlisten og klikker på den med et sekunds pause mellem klikkene, så botten ligner en maskine mindre. Knapper, der allerede siger "Following", springes over.

Hvis et klik opfanges af pop-up'en "Unfollow?" (en konto, man allerede følger), rejser Selenium `ElementClickInterceptedException`. Botten klikker på "Cancel" og fortsætter med næste knap.

![Unfollow pop-up with a Cancel button](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step5-unfollow-popup.jpg)

![Followers after the follow loop](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step5-followed.jpg)

## Hvad vi lærte

- At håndtere en bestemt undtagelse med vilje: ingen bar `except`, kun det tilfælde, opgaven beskriver.
- At teste fejlstien med en falsk driver, der rejser undtagelsen.
- At vise respekt for tjenesten: et sekund mellem klik og en mock-tjeneste med en "Reset Share-a-Naan"-knap til rene genkørsler.
