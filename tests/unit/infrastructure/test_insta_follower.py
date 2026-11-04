from pathlib import Path
from typing import Any

import pytest

from instagram_followers import constants
from instagram_followers.domain.errors import MissingCredentialsError
from instagram_followers.infrastructure.insta_follower import InstaFollower
from tests.fakes import FakeDriver, FakeElement


def make_bot(driver: FakeDriver, sleeps: list[float]) -> InstaFollower:
    fake: Any = driver
    return InstaFollower(driver=fake, sleep=sleeps.append)


@pytest.fixture
def credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(constants.ENV_USERNAME, "someone")
    monkeypatch.setenv(constants.ENV_PASSWORD, "test-value")


def login_form() -> dict[str, list[FakeElement]]:
    return {
        constants.USERNAME_FIELD_ID: [FakeElement()],
        constants.PASSWORD_FIELD_ID: [FakeElement()],
        constants.SUBMIT_BUTTON_XPATH: [FakeElement()],
    }


def test_login_fills_form_and_submits_without_popups(credentials: None) -> None:
    form = login_form()
    driver = FakeDriver(form)
    make_bot(driver, []).login()
    assert driver.visited == [constants.LOGIN_URL]
    assert form[constants.USERNAME_FIELD_ID][0].typed == ["someone"]
    assert form[constants.PASSWORD_FIELD_ID][0].typed == ["test-value"]
    assert form[constants.SUBMIT_BUTTON_XPATH][0].clicks == 1


def test_login_dismisses_popups_when_present(credentials: None) -> None:
    cookie, not_now = FakeElement(), FakeElement()
    form = login_form()
    form[constants.COOKIE_BUTTON_XPATH] = [cookie]
    form[constants.NOT_NOW_BUTTON_XPATH] = [not_now]
    make_bot(FakeDriver(form), []).login()
    assert cookie.clicks == 1
    assert not_now.clicks == 2


def test_login_raises_when_credentials_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(constants.ENV_USERNAME, raising=False)
    monkeypatch.delenv(constants.ENV_PASSWORD, raising=False)
    with pytest.raises(MissingCredentialsError, match="INSTA_USERNAME"):
        make_bot(FakeDriver({}), []).login()


def test_find_followers_scrolls_the_scroll_container_n_times() -> None:
    modal, scroll_container, link = FakeElement(), FakeElement(), FakeElement()
    driver = FakeDriver(
        {
            constants.FOLLOWERS_LINK_XPATH: [link],
            constants.FOLLOWERS_MODAL_XPATH: [modal],
            constants.FOLLOWERS_SCROLL_XPATH: [scroll_container],
        }
    )
    make_bot(driver, []).find_followers()
    expected_url = constants.ACCOUNT_URL_TEMPLATE.format(account=constants.SIMILAR_ACCOUNT)
    assert driver.visited == [expected_url]
    assert link.clicks == 1
    assert (
        driver.scripts
        == [(constants.SCROLL_CONTAINER_SCRIPT, scroll_container)] * constants.SCROLL_COUNT
    )
    assert all(target is not modal for _, target in driver.scripts)


def test_follow_clicks_every_button_with_one_second_delay() -> None:
    buttons = [FakeElement(), FakeElement(), FakeElement()]
    driver = FakeDriver({constants.FOLLOWERS_SCROLL_XPATH: [FakeElement(children=buttons)]})
    sleeps: list[float] = []
    make_bot(driver, sleeps).follow()
    assert [b.clicks for b in buttons] == [1, 1, 1]
    assert sleeps == [1, 1, 1]


def test_follow_cancels_popup_and_continues_when_click_intercepted() -> None:
    cancel = FakeElement()
    buttons = [FakeElement(), FakeElement(intercepted=True), FakeElement()]
    driver = FakeDriver(
        {
            constants.FOLLOWERS_SCROLL_XPATH: [FakeElement(children=buttons)],
            constants.CANCEL_BUTTON_XPATH: [cancel],
        }
    )
    make_bot(driver, []).follow()
    assert cancel.clicks == 1
    assert buttons[2].clicks == 1


def test_constants_hold_no_credential_value() -> None:
    source = Path(constants.__file__).read_text(encoding="utf-8")
    assert not hasattr(constants, "PASSWORD")
    assert not hasattr(constants, "USERNAME")
    assert "PASSWORD =" not in source.replace("ENV_PASSWORD =", "")


def test_context_exit_quits_driver_created_by_the_bot(monkeypatch: pytest.MonkeyPatch) -> None:
    driver = FakeDriver({})
    fake: Any = driver
    monkeypatch.setattr(InstaFollower, "_create_driver", staticmethod(lambda headless: fake))
    with InstaFollower(sleep=lambda _seconds: None) as bot:
        assert isinstance(bot, InstaFollower)
    assert driver.quit_calls == 1


def test_context_exit_leaves_injected_driver_open() -> None:
    driver = FakeDriver({})
    with make_bot(driver, []):
        pass
    assert driver.quit_calls == 0


def test_context_exit_quits_owned_driver_when_body_raises(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    driver = FakeDriver({})
    fake: Any = driver
    monkeypatch.setattr(InstaFollower, "_create_driver", staticmethod(lambda headless: fake))
    with pytest.raises(RuntimeError), InstaFollower():
        raise RuntimeError("boom")
    assert driver.quit_calls == 1


def test_follow_never_clicks_the_profile_follow_button() -> None:
    profile_button, row_button = FakeElement(), FakeElement()
    driver = FakeDriver(
        {
            "//profile-follow-button": [profile_button],
            constants.FOLLOWERS_SCROLL_XPATH: [FakeElement(children=[row_button])],
        }
    )
    make_bot(driver, []).follow()
    assert profile_button.clicks == 0
    assert row_button.clicks == 1


def test_follow_button_locator_is_relative_and_matches_exact_follow_text() -> None:
    assert constants.FOLLOW_BUTTON_XPATH.startswith(".//")
    assert "normalize-space(text())='Follow'" in constants.FOLLOW_BUTTON_XPATH
