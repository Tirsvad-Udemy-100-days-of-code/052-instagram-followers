**English** · [Dansk](Step-4-Find-Followers-da) · [Bahasa Malaysia](Step-4-Find-Followers-ms)

# Step 4 - Find the followers

`find_followers()` opens the page of the target account at `/u/<account>` and clicks the followers link. The list in the modal loads about a dozen followers at first, so we scroll to load the rest.

![Profile of the target account](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-target-profile.jpg)

![Followers modal](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-followers-modal.jpg)

The modal is not the scrolling element. The scrollable part is the inner `followers-scroll` element, so the script scrolls that element: `arguments[0].scrollTop = arguments[0].scrollHeight`.

![Followers modal scrolled to the end](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step4-followers-scrolled.jpg)

## What we gained

- Running JavaScript from Selenium with `execute_script`.
- Finding the element that really scrolls by inspecting the page, instead of scrolling the whole window.
- Pausing between scrolls so the page can load more entries.
