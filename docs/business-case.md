# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [4cd695e] |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted on RC-001 (Go)<br>Mode: autonomous, not independent | [4cd695e] |

---

## Executive Summary

Day 52 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" asks the course participant to build an Instagram follower bot with Selenium. The bot logs in, opens a target account, scrolls its followers list and follows each follower. This project delivers that assignment as a readable, runnable, tested Python repository against the Share-a-Naan mock service, with a README and a three-language wiki (English, Danish, Bahasa Malaysia) that explain what each lecture step teaches.

## Methodological and Standards Foundation

The project follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`: artifacts are reviewed against their QC checklists, and quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Code is structured by Clean Architecture and reviewed against `QC-PY-001` (Python).

## Problem Statement

- The assignment is described only as lecture prose; there is no tested, documented reference solution to compare against.
- Following accounts by hand does not scale, and automating it against the real Instagram risks an account ban and breaks when XPaths change.
- Course solutions shared online often lack tests, setup instructions and an explanation of what was learned.

## Business Opportunity

A small, well-documented repository helps the participant prove the skill, helps other course participants compare solutions, and gives GitHub visitors an example of a Selenium bot that is testable and safe to run against a mock service.

## Objectives

1. Deliver the `InstaFollower` class with `login()`, `find_followers()` and `follow()` as the assignment names them.
2. Run safely against the Share-a-Naan mock; the real Instagram is out of the default path.
3. Keep all constants in `constants.py` and all secrets out of the repository.
4. Test the logic with pytest without a live browser or network.
5. Document run and test instructions, including a local `.venv`, in the README.
6. Publish a wiki in English, Danish and Bahasa Malaysia, with a screenshot per lecture step and a note on what each step teaches.
7. Set a repository description and topics on the git host.

## Scope

### In Scope

- Python 3.13 or newer, `venv`, `pyproject.toml`, Python `.gitignore`.
- Selenium bot for the Share-a-Naan mock (login, cookie/pop-up dismissal, follower modal scroll, follow with ElementClickIntercepted handling).
- pytest unit tests with a fake driver; Doxygen comments and a `Doxyfile`.
- README from the framework template; wiki in `en`, `da`, `ms`; screenshots per lecture step.
- Git host metadata (description, topics) and one pull request per milestone.

### Out of Scope

- Running the bot against the real Instagram, or any evasion of bot detection.
- Committing, printing or testing the contents of `.env` (tokens are for the maintainer's own use).
- Packaging for PyPI; any runtime dependency other than Selenium.

## Expected Benefits

### Tangible Benefits

- A runnable solution with passing tests and documented set-up.
- A wiki in three languages with one screenshot per lecture step.

### Intangible Benefits

- Practice with Selenium, XPath, exceptions and a class-based design.
- A reusable pattern for later bootcamp days.

## Strategic Alignment

The repository belongs to the Tirsvad-Udemy-100-days-of-code collection and shows consistent use of the SQA and QC framework on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Unit tests pass | 100 % of tests green | `pytest` exit code 0 |
| 2 | Wiki completeness | 3 languages with the same page set | file listing in `docs/wiki/` |
| 3 | Lecture-step screenshots | one per step 1 to 5 in README and wiki | image files referenced |
| 4 | Secrets in repository | 0 | scan for token values |
| 5 | Runtime dependencies | only `selenium` | `pyproject.toml` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Share-a-Naan page layout differs from the lecture | Locators fail | Keep locators in `constants.py`; use `contains()` and `text()` |
| Login to the mock needs credentials the AI does not have | Screenshots cannot be captured | Credentials come from environment variables; capture screenshots of the public pages and mark what needs the owner's login |
| Token leaks into history | Security incident | `.env` in `.gitignore`; never read into code; stop on any exposure |
| GUI test takes the host desktop | Disturbs the user | Run the browser headless or in a container, as `gui-testing.md` says |

## Assumptions

- The Product Owner (S01) is also developer and reviewer, and reaches the other stakeholders.
- The git host accepts the token in `.env` for the repository and its wiki.
- Python 3.13 or newer is installed locally.

## Constraints

- Python 3.13 or newer; `venv`; `pytest`; constants in `constants.py`; `pyproject.toml`.
- Layout `src/`, `tests/`, `docs/`.
- Product Owner language English, domain IT.
- One branch and pull request per milestone.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| Qualitative: a few hours of the participant's time and AI assistance; no licence cost. | Qualitative: a documented, tested learning artifact that other participants and visitors can reuse. |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the product, builds it and reviews it |
| S02 | Wants readable, runnable code and run instructions |
| S03 | Wants a clear description, topics and README, with no runtime dependencies |

## Recommendation

Proceed — the scope is small, the risk is contained by the mock service, and the deliverable is verifiable.

---

[SA-001]: ./stakeholder-analysis.md
[4cd695e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/commit/4cd695e8db91dd3f01f69e097cdf02098de2c144
