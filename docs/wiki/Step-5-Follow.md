**English** · [Dansk](Step-5-Follow-da) · [Bahasa Malaysia](Step-5-Follow-ms)

# Step 5 - Follow

`follow()` finds every "Follow" button in the followers list and clicks it with a one second pause between clicks, so the bot looks less like a machine. Buttons that already say "Following" are skipped.

If a click is intercepted by the "Unfollow?" pop-up (an account that is already followed), Selenium raises `ElementClickInterceptedException`. The bot clicks "Cancel" and carries on with the next button.

![Unfollow pop-up with a Cancel button](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step5-unfollow-popup.jpg)

![Followers after the follow loop](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step5-followed.jpg)

## What we gained

- Handling a specific exception on purpose: no bare `except`, and only the case the assignment describes.
- Testing that error path with a fake driver that raises the exception.
- Respecting the service: one second between clicks, and a mock service with a "Reset Share-a-Naan" button for clean re-runs.
