# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [4cd695e] |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted on RC-002 (Go)<br>Mode: autonomous, not independent | [4cd695e] |

---

## Purpose

Identify who is affected by the Instagram follower bot repository and what each needs, so the plan, the README and the wiki serve them. The method is a power/interest grid; each concern is mapped to a FURPS+ attribute.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A working, tested solution to the Day 52 assignment that proves the skill |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository browsers looking for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies beyond need |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, builds and reviews everything.
- **Keep Informed (S02):** cannot change the project but depends on its readability and run instructions.
- **Monitor (S03):** browse occasionally; their needs are met by a good README, description and topics.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The bot follows the followers of a target account on the mock service | Functionality |
| CN-002 | S01 | Tokens and credentials never enter the repository | Functionality (security) |
| CN-003 | S02 | Code is readable and uses the assignment's names `InstaFollower`, `login`, `find_followers`, `follow` | Usability |
| CN-004 | S02 | Run and test instructions work from a fresh clone | Usability |
| CN-005 | S03 | Repository has a description, topics and a README | Usability |
| CN-006 | S03 | No runtime dependencies beyond Selenium | Supportability |
| CN-007 | S01 | Tests run without a browser or network | Reliability |
| CN-008 | S02 | The wiki explains what each lecture step teaches, in English, Danish and Bahasa Malaysia | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat summary | Per run | Merged pull requests, review verdicts, stand-in decisions | All milestones |
| CM-002 | README | Per release | Run and test instructions | MIL-003 |
| CM-003 | Wiki (en, da, ms) | Per release | Lecture steps and learning notes | MIL-004 |
| CM-004 | Repository page | Once | Description and topics | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the code to run against Instagram; the safe path is the mock | S01, S02 | Default to the Share-a-Naan mock; document that the real site risks a ban and is not supported |
| S03 wants no dependencies; Selenium is required | S03, S01 | Selenium is the only runtime dependency; dev tools are optional extras |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objective 1, 2 ([BC-001]) |
| S01 | CN-002 | Objective 3 ([BC-001]) |
| S01 | CN-007 | Objective 4 ([BC-001]) |
| S02 | CN-003, CN-004 | Objective 1, 5 ([BC-001]) |
| S02 | CN-008 | Objective 6 ([BC-001]) |
| S03 | CN-005, CN-006 | Objective 7 ([BC-001]) |

## Sign-Off

Pending review by S01 (AI as stand-in in autonomous mode).

---

[BC-001]: ./business-case.md
[4cd695e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/commit/4cd695e8db91dd3f01f69e097cdf02098de2c144
