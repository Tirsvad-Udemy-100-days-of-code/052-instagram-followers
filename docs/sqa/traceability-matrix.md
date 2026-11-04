# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [DICT-001], [RC-001], [RC-002], [RC-003], [RC-004], [RC-005], [RC-006], [RC-007], [RC-008] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [4cd695e] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-003] |
| [DICT-001] | DICT | en | it | [BC-001] | - | [RC-004] |
| [MIL-001] | MIL | en | it | [PP-001] | - | [RC-005] |
| [MIL-002] | MIL | en | it | [PP-001], [MIL-001] | - | [RC-006] |
| [MIL-003] | MIL | en | it | [PP-001], [MIL-002] | - | [RC-007] |
| [MIL-004] | MIL | en | it | [PP-001], [MIL-003] | - | [RC-008] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] | - | - | Gap |
| CN-002 | [MIL-001], [MIL-002] | - | - | Gap |
| CN-003 | [MIL-002] | - | - | Gap |
| CN-004 | [MIL-001], [MIL-003] | - | - | Gap |
| CN-005 | [MIL-001] | - | - | Gap |
| CN-006 | [MIL-001] | - | - | Gap |
| CN-007 | [MIL-002] | - | - | Gap |
| CN-008 | [MIL-004] | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |

## Coverage Notes

No design views (use case, domain model, design class diagram) exist: the project models none, as [PP-001] states. A concern is `Gap` until the milestone that answers it is done. `-` in Upstream means foundational, in Downstream that nothing is built on it yet, and in Last Reviewed that no review record exists yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[DICT-001]: ../dictionary.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-follower-bot.md
[MIL-003]: ../milestones/mil-003-readme-and-screenshots.md
[MIL-004]: ../milestones/mil-004-wiki.md
[RC-001]: ./reviews/rc-001-bc.md
[RC-002]: ./reviews/rc-002-sa.md
[RC-003]: ./reviews/rc-003-pp.md
[RC-004]: ./reviews/rc-004-dict.md
[RC-005]: ./reviews/rc-005-mil-001.md
[RC-006]: ./reviews/rc-006-mil-002.md
[RC-007]: ./reviews/rc-007-mil-003.md
[RC-008]: ./reviews/rc-008-mil-004.md
[4cd695e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/commit/4cd695e8db91dd3f01f69e097cdf02098de2c144
