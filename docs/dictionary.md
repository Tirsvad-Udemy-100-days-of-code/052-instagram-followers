# Domain Dictionary (PO and IT terms)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |
| 2026-11-04 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Accepted on RC-004 (Go)<br>Mode: autonomous, not independent | pending |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language: English (`en`), domain `it`. It covers the words of the Day 52 assignment and the IT terms used in code.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| follow | en | Follow action | Click the Follow button of an account so that it is followed. | BC, PP, MIL | PY |
| follower | en | Follower | An account that follows the target account. | BC, PP, MIL | PY |
| log in | en | Authenticate | Sign in to the service with a username and a password. | BC, PP, MIL | PY |
| mock service | en | Test double service | A practice copy of the real service that behaves like it but cannot harm a real account. | BC, PP, MIL | PY |
| pop-up | en | Modal dialog | A window that opens over the page and asks for an answer. | BC, PP, MIL | PY |
| target account | en | Source account | The account whose followers the bot goes through. | BC, PP, MIL | PY |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation
  Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- Rows are in ascending order of the PO term (case-insensitive, by the
  alphabet of the PO language), so a term is found without searching.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
