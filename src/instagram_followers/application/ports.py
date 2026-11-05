## @file ports.py
#  @brief Ports the use cases need from the outside.
from typing import Protocol


## @brief Something that can log in and follow the followers of an account.
class Follower(Protocol):
    ## @brief Log in to the service.
    def login(self) -> None: ...

    ## @brief Open the list of followers to follow.
    def find_followers(self) -> None: ...

    ## @brief Follow everyone in the opened list.
    def follow(self) -> None: ...
