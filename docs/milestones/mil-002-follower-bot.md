# MIL-002 Follower bot

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted on RC-006 (Go)<br>Mode: autonomous, not independent | pending |

---

## Purpose

Decide whether the InstaFollower bot is implemented, tested and reviewed against the Python checklist.

## Deliverable

A `src/` package with `constants.py` and `InstaFollower` (`login`, `find_followers`, `follow`) and an entry point, pytest tests using a fake driver, and Doxygen comments; reviewed against `QC-PY-001`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes with no browser and no network | Exit code 0 | Any failing test |
| 2 | Constants (URLs, locators, delays) live only in `constants.py` | No literals elsewhere | Locator or URL literal in the class |
| 3 | Credentials come from environment variables, not from code | No secret in source | Hard-coded credential |
| 4 | The Python code review record is `Go` | RC verdict is Go | Verdict is No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Tooling and configuration must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1, 2, 3, 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-05 — within the one-week plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create constants module | Add `constants.py` with `SIMILAR_ACCOUNT`, `BASE_URL`, `LOGIN_URL`, locator XPaths using `contains()` and `text()`, delays and scroll settings. Credentials are read from the environment variables `INSTA_USERNAME` and `INSTA_PASSWORD`. | No | |
| 2 | Implement InstaFollower login | Create the class with a Selenium driver in `__init__` and a `login()` that dismisses the cookie banner, fills the Share-a-Naan form and dismisses follow-up pop-ups. | No | |
| 3 | Implement find_followers and follow | `find_followers()` opens the target account and scrolls the followers modal; `follow()` clicks each Follow button with a 1 second delay and handles `ElementClickInterceptedException` by clicking Cancel. | No | |
| 4 | Add entry point and pytest tests | Add `main.py` that runs the three methods in order, and unit tests with a fake driver for login, scrolling, follow and the intercepted-click path. | No | |
| 5 | Add Doxygen comments and review code | Document the public API with Doxygen comments, review against `QC-PY-001` and record the `RC-*`. | No | |

---

[BC-001]: ../business-case.md
