# MIL-003 README and screenshots

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted on RC-007 (Go)<br>Mode: autonomous, not independent | pending |

---

## Purpose

Decide whether the README lets a reader install, run and test the project and see each lecture step.

## Deliverable

A completed `README.md` with run and test instructions and one screenshot per lecture step (1 to 5) stored under `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README follows the framework template and passes `check-readme.sh` | Script exits 0 | Script fails |
| 2 | One screenshot per lecture step 1 to 5 is referenced | 5 images exist | A step lacks an image |
| 3 | Instructions work from a fresh clone | Commands in README succeed | A command fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The bot must exist to be described |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-06 — within the one-week plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots per lecture step | Capture one screenshot per assignment step (credentials, class, login, followers modal, follow) from the Share-a-Naan mock using the built-in browser or a headless driver, never the desktop of the user. If the mock needs the owner login, stop and report. | No | |
| 2 | Complete README with steps and screenshots | Finish the README with install, run and test instructions and embed the screenshots with a short explanation per step. | No | |
| 3 | Validate README against framework check | Run `framework/scripts/check-readme.sh` and fix its findings. | No | |

---

[BC-001]: ../business-case.md
