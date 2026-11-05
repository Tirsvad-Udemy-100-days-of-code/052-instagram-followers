import pytest

from instagram_followers import constants
from instagram_followers.domain.errors import MissingCredentialsError
from instagram_followers.infrastructure.config import read_credentials


def test_read_credentials_returns_values_from_mapping() -> None:
    environ = {constants.ENV_USERNAME: "u", constants.ENV_PASSWORD: "test-value"}
    credentials = read_credentials(environ)
    assert (credentials.username, credentials.password) == ("u", "test-value")


def test_read_credentials_rejects_empty_value() -> None:
    with pytest.raises(MissingCredentialsError, match="INSTA_PASSWORD"):
        read_credentials({constants.ENV_USERNAME: "u", constants.ENV_PASSWORD: ""})


def test_read_credentials_names_every_missing_variable() -> None:
    with pytest.raises(MissingCredentialsError, match="INSTA_USERNAME, INSTA_PASSWORD"):
        read_credentials({})
