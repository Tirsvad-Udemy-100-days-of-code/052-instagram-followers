**English** · [Dansk](Step-2-Class-da) · [Bahasa Malaysia](Step-2-Class-ms)

# Step 2 - Class

Because the bot has several steps, the code is organised in a class, `InstaFollower`. `__init__` creates the Selenium driver. The three methods `login()`, `find_followers()` and `follow()` are called in that order.

![Outline of the InstaFollower class](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/raw/branch/main/docs/images/step2-class-outline.png)

The class is the Selenium adapter in the `infrastructure` layer. A small use case, `run_bot`, calls the three methods through a `Follower` protocol, so the order is tested without a browser.

## What we gained

- Grouping steps that share state (the driver) in a class.
- Injecting the driver and the sleep function, so tests use a fake driver and never wait.
- Closing the browser with a context manager (`with InstaFollower() as follower:`).
