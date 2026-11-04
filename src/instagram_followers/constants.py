## @file constants.py
#  @brief All constants of the follower bot. No credential value is held here.

## Account whose followers are followed.
SIMILAR_ACCOUNT = "chefsteps"

## Root of the Share-a-Naan mock service.
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
## Login page.
LOGIN_URL = f"{BASE_URL}/login"
## Account page template; fill with the account name.
ACCOUNT_URL_TEMPLATE = f"{BASE_URL}/{{account}}"

## Environment variables the credentials are read from at runtime.
ENV_USERNAME = "INSTA_USERNAME"
ENV_PASSWORD = "INSTA_PASSWORD"

## Login form locators (verified against the live mock).
USERNAME_FIELD_ID = "username"
PASSWORD_FIELD_ID = "password"
SUBMIT_BUTTON_XPATH = "//button[@type='submit']"

## Locators below are UNVERIFIED against the live mock: they use broad
#  contains(text(), ...) matches so they survive small DOM differences.
COOKIE_BUTTON_XPATH = (
    "//button[contains(text(), 'Accept') or contains(text(), 'Allow') "
    "or contains(text(), 'Agree') or contains(text(), 'OK')]"
)
NOT_NOW_BUTTON_XPATH = "//button[contains(text(), 'Not now') or contains(text(), 'Not Now')]"
FOLLOWERS_LINK_XPATH = "//a[contains(@href, 'followers') or contains(text(), 'followers')]"
FOLLOWERS_MODAL_XPATH = "//div[@role='dialog' or contains(@class, 'modal')]"
FOLLOW_BUTTON_XPATH = ".//button[contains(text(), 'Follow') and not(contains(text(), 'Following'))]"
CANCEL_BUTTON_XPATH = "//button[contains(text(), 'Cancel')]"

## Timing, in seconds.
FOLLOW_DELAY = 1
SCROLL_DELAY = 1
PAGE_SETTLE_DELAY = 2
WAIT_TIMEOUT = 10

## Number of times the followers modal is scrolled to load more entries.
SCROLL_COUNT = 5
## Script that scrolls the element passed as arguments[0] to its bottom.
SCROLL_MODAL_SCRIPT = "arguments[0].scrollTop = arguments[0].scrollHeight"
