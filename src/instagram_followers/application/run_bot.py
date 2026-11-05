## @file run_bot.py
#  @brief Use case: log in, find the followers and follow them.
from instagram_followers.application.ports import Follower


## @brief Run the three steps of the bot in order.
#  @param follower The follower implementation to drive.
def run_bot(follower: Follower) -> None:
    follower.login()
    follower.find_followers()
    follower.follow()
