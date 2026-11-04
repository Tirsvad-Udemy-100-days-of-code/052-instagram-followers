# Review of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [2a2838f] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review of `src/` and `tests/` at the head of branch mil-002-follower-bot (code review of the milestone deliverable)
- Language and domain: n/a
- Language reviewer: none (the stand-in for S01 reads English and the IT domain)
- Mode: autonomous, not independent (reviewer is AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Meets the criterion; see src/instagram_followers. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Meets the criterion; see src/instagram_followers. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` leaves files unchanged and `ruff check` reports no finding; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict src tests` reports no issue in 26 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; the only caught exception, `ElementClickInterceptedException`, is handled on purpose by clicking Cancel, as the assignment says. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Meets the criterion; see src/instagram_followers. |
| 7 | Files, locks and connections are managed with context managers | Pass | `InstaFollower` is a context manager and quits the driver it created; tests cover this. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions carry Doxygen-style `##` comments (the Doxyfile reads them), as the Product Owner required. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print or logging; credentials are hidden from repr and never logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No design class diagram exists: [PP-001] models no use cases. The structure (Follower port, InstaFollower adapter, run_bot use case) is recorded here as the deviation. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 16 tests in tests/unit and tests/integration use a fake driver, no network, injected sleep. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` clean; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dependencies are declared and pinned in pyproject.toml (selenium, pytest, ruff, mypy). Fixed after the first draft of this review. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Meets the criterion; see src/instagram_followers. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` and `application` import no selenium (grep empty); no import cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Meets the criterion; see src/instagram_followers. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers domain, application, infrastructure, presentation in snake_case; tests/unit, tests/integration, tests/e2e (e2e needs a container browser and is not yet written). |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Meets the criterion; see src/instagram_followers. |

## Overall Verdict

Go — Every Mandatory criterion passes. Optional criterion 13 was fixed (pinned versions).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None; criterion 13 was fixed before this record was finalised. | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-follower-bot.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[2a2838f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/commit/2a2838fba36dd4d83c3bb1a4a12fc2d143c7d211
