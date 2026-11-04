from instagram_followers.application.run_bot import run_bot


class FakeFollower:
    def __init__(self) -> None:
        self.calls: list[str] = []

    def login(self) -> None:
        self.calls.append("login")

    def find_followers(self) -> None:
        self.calls.append("find_followers")

    def follow(self) -> None:
        self.calls.append("follow")


def test_run_bot_calls_steps_in_order() -> None:
    follower = FakeFollower()
    run_bot(follower)
    assert follower.calls == ["login", "find_followers", "follow"]
