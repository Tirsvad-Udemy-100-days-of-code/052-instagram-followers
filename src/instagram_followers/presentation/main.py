## @file main.py
#  @brief Composition root: wires and runs the follower bot.
from instagram_followers.application.run_bot import run_bot
from instagram_followers.infrastructure.insta_follower import InstaFollower


## @brief Build the Selenium follower and run the bot.
def main() -> None:
    with InstaFollower() as follower:
        run_bot(follower)


if __name__ == "__main__":
    main()
