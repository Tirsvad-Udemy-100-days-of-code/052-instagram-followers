from typing import Any

import pytest

from instagram_followers import constants
from instagram_followers.application.run_bot import run_bot
from instagram_followers.infrastructure.insta_follower import InstaFollower
from tests.fakes import FakeDriver, FakeElement


def test_run_bot_drives_selenium_follower_through_all_steps(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(constants.ENV_USERNAME, "someone")
    monkeypatch.setenv(constants.ENV_PASSWORD, "test-value")
    button = FakeElement()
    driver = FakeDriver(
        {
            constants.USERNAME_FIELD_ID: [FakeElement()],
            constants.PASSWORD_FIELD_ID: [FakeElement()],
            constants.SUBMIT_BUTTON_XPATH: [FakeElement()],
            constants.FOLLOWERS_LINK_XPATH: [FakeElement()],
            constants.FOLLOWERS_MODAL_XPATH: [FakeElement(children=[button])],
        }
    )
    fake: Any = driver
    run_bot(InstaFollower(driver=fake, sleep=lambda _seconds: None))
    assert driver.visited[0] == constants.LOGIN_URL
    assert button.clicks == 1
