from instagram_followers.domain.credentials import Credentials


def test_credentials_repr_hides_password() -> None:
    assert "test-value" not in repr(Credentials("u", "test-value"))
