# MIL-004 Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [4cd695e] |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted on RC-008 (Go)<br>Mode: autonomous, not independent | [4cd695e] |

---

## Purpose

Decide whether the wiki is complete in English, Danish and Bahasa Malaysia and says what each lecture step teaches.

## Deliverable

`docs/wiki/` with Home, one page per lecture step and `_Sidebar.md`, in English (no suffix), Danish (`-da`) and Bahasa Malaysia (`-ms`), with the screenshots, reviewed against `QC-WIKI-001`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Same page set in en, da and ms | File listing matches | A page is missing in a language |
| 2 | Every step page has a screenshot and a "what we gained" section | Present on each page | Missing section |
| 3 | Sidebar follows the framework shape | `QC-WIKI-001` item passes | Sidebar defect |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Screenshots and README text are reused |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-07 — within the one-week plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write English wiki pages | Write Home and one page per lecture step 1 to 5 with the screenshot and a section on what was gained (Selenium locators, waits, scrolling a modal, exception handling), plus `_Sidebar.md`. | No | |
| 2 | Translate wiki to Danish | Create the same page set with the `-da` suffix; code, commands and file names stay in English. | No | |
| 3 | Translate wiki to Bahasa Malaysia | Create the same page set with the `-ms` suffix; code, commands and file names stay in English. | No | |
| 4 | Review wiki against QC-WIKI-001 | Check page sets, language lines, sidebar and links and record the `RC-*`. | No | |

---

[BC-001]: ../business-case.md
[4cd695e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/commit/4cd695e8db91dd3f01f69e097cdf02098de2c144
