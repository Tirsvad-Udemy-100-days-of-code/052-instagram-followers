## @file config.py
#  @brief Reads configuration (credentials) from the environment.
import os
from collections.abc import Mapping

from instagram_followers import constants
from instagram_followers.domain.credentials import Credentials
from instagram_followers.domain.errors import MissingCredentialsError


## @brief Read the login credentials from the environment.
#  @param environ Mapping to read from; defaults to os.environ.
#  @return The credentials.
#  @throws MissingCredentialsError if either variable is missing or empty.
def read_credentials(environ: Mapping[str, str] | None = None) -> Credentials:
    source = os.environ if environ is None else environ
    missing = [
        name for name in (constants.ENV_USERNAME, constants.ENV_PASSWORD) if not source.get(name)
    ]
    if missing:
        raise MissingCredentialsError(f"Missing environment variable(s): {', '.join(missing)}")
    return Credentials(
        username=source[constants.ENV_USERNAME], password=source[constants.ENV_PASSWORD]
    )
