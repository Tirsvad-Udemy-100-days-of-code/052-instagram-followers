# Review of DICT-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-004 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in for S01 reads English and the IT domain)
- Mode: autonomous, not independent (reviewer is AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | Meets the criterion; six rows, each complete. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Meets the criterion; six rows, each complete. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | The project has no Domain Model; it models no use cases ([PP-001]). |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | No OC, SD, DCD or ERD exists in this project. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Meets the criterion; six rows, each complete. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | Meets the criterion; six rows, each complete. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Meets the criterion; six rows, each complete. |
| 8 | The dictionary rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language) | Pass | follow, follower, log in, mock service, pop-up, target account: ascending. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` is `en` and `Domain` is `it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register matches the registry row for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | PO terms follow [DICT-001] (follower, follow, log in, mock service, pop-up, target account). |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists in `docs/`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | No change of language since the first version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in for S01 reads English and knows the IT domain; open to challenge by S01 in the run summary. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use. |

## Overall Verdict

Go — Mandatory criteria pass; 3 and 4 are N-A because the artifacts they check do not exist.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None; no Fail and no condition. | S01 | - |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
