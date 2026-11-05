[English](Step-2-Class) · **Dansk** · [Bahasa Malaysia](Step-2-Class-ms)

# Trin 2 - Klasse

Fordi botten har flere trin, er koden organiseret i en klasse, `InstaFollower`. `__init__` opretter Selenium-driveren. De tre metoder `login()`, `find_followers()` og `follow()` kaldes i den rækkefølge.

![Outline of the InstaFollower class](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step2-class-outline.png)

Klassen er Selenium-adapteren i laget `infrastructure`. Et lille use case, `run_bot`, kalder de tre metoder gennem en `Follower`-protokol, så rækkefølgen testes uden en browser.

## Hvad vi lærte

- At samle trin, der deler tilstand (driveren), i en klasse.
- At injicere driveren og sleep-funktionen, så tests bruger en falsk driver og aldrig venter.
- At lukke browseren med en context manager (`with InstaFollower() as follower:`).
