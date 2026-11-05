## @file credentials.py
#  @brief Login credentials value object.
from dataclasses import dataclass, field


## @brief Username and password used to log in; the password is hidden from repr.
@dataclass(frozen=True, slots=True)
class Credentials:
    username: str
    password: str = field(repr=False)
