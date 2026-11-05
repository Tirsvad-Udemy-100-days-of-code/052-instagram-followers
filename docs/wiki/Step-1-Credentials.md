**English** · [Dansk](Step-1-Credentials-da) · [Bahasa Malaysia](Step-1-Credentials-ms)

# Step 1 - Credentials

The assignment starts with an account. We use the Share-a-Naan mock instead of the real Instagram, so a changed page or a ban cannot hurt. The profile page of the mock shows the login (the email is the username) and the target accounts to choose `SIMILAR_ACCOUNT` from.

![Target accounts on the profile page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step1-target-accounts.jpg)

## What we gained

- A safe place to practise: a mock service lets us get the logic right before any real account is at risk.
- Secrets stay out of the code: the password is read from the environment variables `INSTA_USERNAME` and `INSTA_PASSWORD`, and `.env` is in `.gitignore`.
- Constants live in one file, `constants.py`: `SIMILAR_ACCOUNT`, `BASE_URL` and `LOGIN_URL`.
