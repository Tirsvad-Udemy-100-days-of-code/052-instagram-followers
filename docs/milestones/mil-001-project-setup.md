# MIL-001 Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted on RC-005 (Go)<br>Mode: autonomous, not independent | pending |

---

## Purpose

Decide whether the repository foundation is ready for code: configuration, tooling, documentation skeleton and git host metadata.

## Deliverable

Repository with `pyproject.toml` (Python 3.13 or newer, selenium runtime dependency, pytest dev extra), a Python `.gitignore` that excludes `.env` and `.venv`, a `Doxyfile`, a README skeleton from the framework template with `.venv` instructions, the baseline documents, and the repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python >=3.13` and only `selenium` as runtime dependency | `pip install -e .[dev]` succeeds | Missing or extra runtime dependency |
| 2 | `.gitignore` excludes `.env`, `.venv` and caches | `git check-ignore .env` prints the path | `.env` is trackable |
| 3 | Baseline documents are `Accepted` with `Go` reviews | RC records exist | Any baseline row is `Proposed` |
| 4 | Repository description and topics are set on the git host | API read-back shows both | Description or topics missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First phase |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3, 5, 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-04 — within the one-week plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject, gitignore and Doxyfile | Create `pyproject.toml` (Python 3.13 or newer, `selenium` runtime, `pytest` dev extra, `src` layout), a Python `.gitignore` that ignores `.env` and `.venv`, and a `Doxyfile` for `src/`. These satisfy the project constraints without touching `src/` or `tests/`. | No | |
| 2 | Write README skeleton with venv instructions | Fill the framework README template with the project purpose and how to create and use `.venv`, run `python -m pip install --upgrade pip`, install, run and test. Screenshots are added in MIL-003. | No | |
| 3 | Set repository description and topics | Set a description and topics (python, selenium, udemy, 100-days-of-code, instagram-bot, share-a-naan) on the Gitea repository through the API, using the token from `.env`. The token is read from the environment only and never written to the repository. | No | |
| 4 | Review baseline documents | Review Business Case, Stakeholder Analysis, Project Plan and milestones against their QC checklists and record the `RC-*` records. | No | |

---

[BC-001]: ../business-case.md
