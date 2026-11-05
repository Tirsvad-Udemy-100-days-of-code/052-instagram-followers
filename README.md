# 🚀 Instagram Followers

A Python Selenium bot from Day 52 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": it logs in to the Share-a-Naan mock service, opens a target account and follows each of its followers. It is for course participants who want readable, runnable code and for visitors looking for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The assignment has five steps: get credentials, create the `InstaFollower` class, log in, find the followers of the target account and follow them. The code keeps the assignment's names (`InstaFollower`, `login`, `find_followers`, `follow`).

- `src/instagram_followers/` holds the bot in clean-architecture layers (`domain`, `application`, `infrastructure`, `presentation`) and `constants.py`.
- `tests/` holds the pytest tests, which use a fake driver and need no browser or network.
- `docs/` holds the project documents and the wiki (English, Danish and Bahasa Malaysia).

The bot targets the mock service Share-a-Naan. Running bots against the real Instagram can get an account banned and is not supported.

### Lecture steps

Each step of the assignment, with what the screen looks like on the Share-a-Naan mock. Screenshots were taken on 2026-11-04.

**Step 1 - Get your credentials.** The mock's profile page lists your login (your email is the username) and the target accounts to pick `SIMILAR_ACCOUNT` from. The password is read from the environment and never stored in the repository.

![Target accounts on the Share-a-Naan profile page][img-step1]

**Step 2 - Create a class.** `InstaFollower` creates the Selenium driver in `__init__` and has the three methods `login()`, `find_followers()` and `follow()`.

![Outline of the InstaFollower class][img-step2]

**Step 3 - Log in.** The login page, then two pop-ups that are dismissed with the "Not Now" button, found by its text with `contains()`.

![Share-a-Naan login page][img-step3-login]
![Save your login info pop-up][img-step3-save]
![Turn on notifications pop-up][img-step3-notifications]

**Step 4 - Find the followers.** Open `/u/<account>`, click the followers link and scroll the list inside the modal (the `followers-scroll` element), not the page behind it.

![Profile of the target account][img-step4-profile]
![Followers modal][img-step4-modal]
![Followers modal scrolled to the end][img-step4-scrolled]

**Step 5 - Follow all the followers.** Click every "Follow" button with a 1 second pause. If a click is intercepted by the "Unfollow?" pop-up (an account that is already followed), click "Cancel" and carry on.

![Unfollow pop-up with a Cancel button][img-step5-unfollow]
![Followers after the follow loop][img-step5-followed]

## 📋 Requirements

- Python 3.13 or newer.
- Google Chrome (Selenium 4 downloads a matching driver by itself).
- A Share-a-Naan account from the mock dashboard (`https://app.100daysofpython.dev/`).

## 🛠️ Setup

Create and use a local virtual environment named `.venv`, then upgrade pip and install the project with its test tools.

```bash
python -m venv .venv
```

Activate it (Windows PowerShell: `.venv\Scripts\Activate.ps1`; Git Bash, Linux, macOS: `source .venv/bin/activate` or `source .venv/Scripts/activate`).

```bash
python -m pip install --upgrade pip
```

```bash
python -m pip install -e ".[dev]"
```

Credentials are read from environment variables, never from the code. Do not commit a `.env` file; it is ignored by git.

```bash
export INSTA_USERNAME="your_email"
export INSTA_PASSWORD="your_password"
```

## ▶️ Run

```bash
python -m instagram_followers.presentation.main
```

Run it sparingly and log out between test runs by hand. The mock has a "Reset Share-a-Naan" button on its profile page that clears your follows for a clean re-run.

## 🧪 Tests

```bash
python -m pytest
```

API documentation can be generated with `doxygen Doxyfile` (output in `docs/doxygen/`).

## 📄 License

AGPL-3.0, see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[img-step1]: ./docs/images/step1-target-accounts.jpg
[img-step2]: ./docs/images/step2-class-outline.png
[img-step3-login]: ./docs/images/step3-login-page.jpg
[img-step3-save]: ./docs/images/step3-save-info-popup.jpg
[img-step3-notifications]: ./docs/images/step3-notifications-popup.jpg
[img-step4-profile]: ./docs/images/step4-target-profile.jpg
[img-step4-modal]: ./docs/images/step4-followers-modal.jpg
[img-step4-scrolled]: ./docs/images/step4-followers-scrolled.jpg
[img-step5-unfollow]: ./docs/images/step5-unfollow-popup.jpg
[img-step5-followed]: ./docs/images/step5-followed.jpg
[license]: ./LICENSE
[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
