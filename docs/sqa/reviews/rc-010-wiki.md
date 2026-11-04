# Review of MIL-004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-04 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [0e12087] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-WIKI-001]
- Scope: full review of docs/wiki on branch mil-004-wiki
- Language and domain: n/a
- Language reviewer: none (the stand-in for S01 reads English and the IT domain)
- Mode: autonomous, not independent (reviewer is AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass |  exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, one English page list, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All six English pages are listed; a script checked that no link in the wiki points to a missing page. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so no Related section exists, as the criterion requires. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last, one line per language in that language. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not by a generator. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Malaysia, as the Product Owner asked (the PO language is English). |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 6 pages in each of en, da and ms (18 pages). |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the line, the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Suffixes -da and -ms, English has none. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code, commands, file names and IDs are English in all languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The wiki is published only after the pull request merges into main, so it cannot be checked on the host yet. The images also resolve only after the merge. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No change to layout rules. |

## Overall Verdict

Go-with-conditions — All checkable Mandatory criteria pass. Criterion 14 is Pending until the wiki is published, so Go-with-conditions is the highest verdict.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge, open the published wiki and check the sidebar, every page, every link and every image on the host | S01 | 2026-11-04 |

---

[MIL-004]: ../../milestones/mil-004-wiki.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[0e12087]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/052-instagram-followers/commit/0e1208726f3ae1b083b198598311137e2fc99f58
