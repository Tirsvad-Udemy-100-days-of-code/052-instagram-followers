[English](Step-4-Find-Followers) · **Dansk** · [Bahasa Malaysia](Step-4-Find-Followers-ms)

# Trin 4 - Find følgerne

`find_followers()` åbner målkontoens side på `/u/<konto>` og klikker på linket til følgerne. Listen i modalen indlæser først omkring et dusin følgere, så vi ruller for at indlæse resten.

![Profile of the target account](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-target-profile.jpg)

![Followers modal](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-followers-modal.jpg)

Modalen er ikke det element, der ruller. Den rullende del er det indre `followers-scroll`-element, så scriptet ruller det element: `arguments[0].scrollTop = arguments[0].scrollHeight`.

![Followers modal scrolled to the end](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-followers-scrolled.jpg)

## Hvad vi lærte

- At køre JavaScript fra Selenium med `execute_script`.
- At finde det element, der virkelig ruller, ved at undersøge siden i stedet for at rulle hele vinduet.
- At holde pause mellem rulninger, så siden kan indlæse flere poster.
