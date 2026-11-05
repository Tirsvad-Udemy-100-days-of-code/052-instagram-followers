## @file constants.py
#  @brief All constants of the follower bot. No credential value is held here.

## Account whose followers are followed.
SIMILAR_ACCOUNT = "chefsteps"

## Root of the Share-a-Naan mock service.
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
## Login page.
LOGIN_URL = f"{BASE_URL}/login"
## Account page template; fill with the account name.
ACCOUNT_URL_TEMPLATE = f"{BASE_URL}/u/{{account}}"

## Environment variables the credentials are read from at runtime.
ENV_USERNAME = "INSTA_USERNAME"
ENV_PASSWORD = "INSTA_PASSWORD"

## Locators below were verified against the live mock on 2026-11-04.
USERNAME_FIELD_ID = "username"
PASSWORD_FIELD_ID = "password"
SUBMIT_BUTTON_XPATH = "//button[@type='submit']"
## Both post-login pop-ups ("Save your login info?", notifications) use this button.
NOT_NOW_BUTTON_XPATH = "//button[contains(@class, 'naan-popup-dismiss')]"
FOLLOWERS_LINK_XPATH = "//a[contains(@class, 'naan-followers-link')]"
## The followers modal; the hidden naan-post-modal dialog does not match.
FOLLOWERS_MODAL_XPATH = "//div[@role='dialog' and contains(@class, 'naan-modal')]"
## The scrollable list inside the modal (the modal itself has overflow hidden).
FOLLOWERS_SCROLL_XPATH = "//div[contains(@class, 'followers-scroll')]"
## Relative to the scroll container, so the profile header Follow button never matches.
FOLLOW_BUTTON_XPATH = (
    ".//button[contains(@class, 'naan-follow-btn') and normalize-space(text())='Follow']"
)
CANCEL_BUTTON_XPATH = "//button[contains(@class, 'naan-unfollow-cancel')]"

## UNVERIFIED: no cookie banner was seen on the live mock; the dismissal is optional.
COOKIE_BUTTON_XPATH = (
    "//button[contains(text(), 'Accept') or contains(text(), 'Allow') "
    "or contains(text(), 'Agree') or contains(text(), 'OK')]"
)

## Timing, in seconds.
FOLLOW_DELAY = 1
SCROLL_DELAY = 1
PAGE_SETTLE_DELAY = 2
WAIT_TIMEOUT = 10

## Number of times the followers list is scrolled to load more entries.
SCROLL_COUNT = 5
## Script that scrolls the element passed as arguments[0] to its bottom.
SCROLL_CONTAINER_SCRIPT = "arguments[0].scrollTop = arguments[0].scrollHeight"
