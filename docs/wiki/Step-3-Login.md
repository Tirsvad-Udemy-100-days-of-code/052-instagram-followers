**English** · [Dansk](Step-3-Login-da) · [Bahasa Malaysia](Step-3-Login-ms)

# Step 3 - Login

`login()` opens the login page, fills in the email and password and presses "Log in". Two pop-ups follow: "Save your login info?" and "Turn on notifications". Both are closed with the "Not Now" button.

![Share-a-Naan login page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-login-page.jpg)

![Save your login info pop-up](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-save-info-popup.jpg)

![Turn on notifications pop-up](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step3-notifications-popup.jpg)

On the real Instagram the XPaths and selectors change on every visit. The fix is to find a button by its words, for example `//button[contains(text(), 'Not Now')]`, and not by a generated class name.

## What we gained

- Locating elements by visible text with `contains()` and `text()`, which survives layout changes.
- Waiting for an element with `WebDriverWait` instead of a fixed pause.
- Handling optional pop-ups: click them if present and carry on if not.
