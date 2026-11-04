## @file insta_follower.py
#  @brief Selenium bot that logs in and follows the followers of an account.
import time
from collections.abc import Callable
from types import TracebackType
from typing import Self

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from instagram_followers import constants
from instagram_followers.infrastructure.config import read_credentials


## @brief Bot that follows the followers of constants.SIMILAR_ACCOUNT.
class InstaFollower:
    ## @brief Create the bot.
    #  @param driver Optional WebDriver (injected in tests); Chrome if None.
    #  @param headless Run Chrome without a window when creating the driver.
    #  @param sleep Function used to pause; injectable so tests do not wait.
    def __init__(
        self,
        driver: WebDriver | None = None,
        headless: bool = False,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._owns_driver = driver is None
        self._driver = driver if driver is not None else self._create_driver(headless)
        self._sleep = sleep

    ## @brief Enter the context.
    #  @return This bot.
    def __enter__(self) -> Self:
        return self

    ## @brief Leave the context and close the driver if this bot created it.
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()

    ## @brief Quit the browser; an injected driver is left to its owner.
    def close(self) -> None:
        if self._owns_driver:
            self._driver.quit()

    @staticmethod
    def _create_driver(headless: bool) -> WebDriver:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        return webdriver.Chrome(options=options)

    def _click_if_present(self, xpath: str) -> bool:
        elements = self._driver.find_elements(By.XPATH, xpath)
        if not elements:
            return False
        elements[0].click()
        return True

    ## @brief Log in, dismissing the cookie warning and any pop-ups.
    #  @throws MissingCredentialsError if the credentials are not in the environment.
    def login(self) -> None:
        credentials = read_credentials()
        self._driver.get(constants.LOGIN_URL)
        self._click_if_present(constants.COOKIE_BUTTON_XPATH)
        wait = WebDriverWait(self._driver, constants.WAIT_TIMEOUT)
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, constants.USERNAME_FIELD_ID))
        )
        username_field.send_keys(credentials.username)
        self._driver.find_element(By.ID, constants.PASSWORD_FIELD_ID).send_keys(
            credentials.password
        )
        self._driver.find_element(By.XPATH, constants.SUBMIT_BUTTON_XPATH).click()
        self._sleep(constants.PAGE_SETTLE_DELAY)
        # "Save login info", then notifications: both are "Not Now" buttons.
        for _ in range(2):
            self._click_if_present(constants.NOT_NOW_BUTTON_XPATH)

    ## @brief Open the similar account and scroll its followers list.
    def find_followers(self) -> None:
        account_url = constants.ACCOUNT_URL_TEMPLATE.format(account=constants.SIMILAR_ACCOUNT)
        self._driver.get(account_url)
        self._sleep(constants.PAGE_SETTLE_DELAY)
        wait = WebDriverWait(self._driver, constants.WAIT_TIMEOUT)
        wait.until(
            EC.presence_of_element_located((By.XPATH, constants.FOLLOWERS_LINK_XPATH))
        ).click()
        wait.until(EC.presence_of_element_located((By.XPATH, constants.FOLLOWERS_MODAL_XPATH)))
        scroll_container = wait.until(
            EC.presence_of_element_located((By.XPATH, constants.FOLLOWERS_SCROLL_XPATH))
        )
        for _ in range(constants.SCROLL_COUNT):
            # The modal has overflow hidden; only the list inside it scrolls.
            self._driver.execute_script(constants.SCROLL_CONTAINER_SCRIPT, scroll_container)
            self._sleep(constants.SCROLL_DELAY)

    ## @brief Click every Follow button in the followers list.
    #  An interception means an unfollow confirmation opened (the account is
    #  already followed); its Cancel button is clicked and the loop goes on.
    def follow(self) -> None:
        container = self._driver.find_element(By.XPATH, constants.FOLLOWERS_SCROLL_XPATH)
        for button in container.find_elements(By.XPATH, constants.FOLLOW_BUTTON_XPATH):
            try:
                button.click()
            except ElementClickInterceptedException:
                self._click_if_present(constants.CANCEL_BUTTON_XPATH)
            self._sleep(constants.FOLLOW_DELAY)
