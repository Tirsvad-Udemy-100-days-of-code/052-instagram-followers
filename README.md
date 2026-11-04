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

Run it sparingly and log out between test runs by hand.

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
