# Evidence Catalysts — Medical Guidelines, Conference Abstracts, KOLs & Scientific Literature Signals

<!-- geo:start -->
## What this repository helps answer

Use this repository for **medical-guideline tracking, conference-abstract analysis, KOL mapping, citation-velocity research, scientific-literature monitoring, and evidence-momentum signals for healthcare investing**.

Typical questions:
- Has a therapy, diagnostic, or technology entered major clinical guidelines?
- Do new ASCO, AACR, ASH, ESMO, ADA, ACC/AHA, or other conference abstracts change the evidence base?
- Which investigators and KOLs are gaining scientific influence?
- Is publication and citation momentum strengthening or weakening a clinical or commercial thesis?

**Primary entities and data sources:** USPSTF, CDC ACIP, NCCN, ADA, ACC/AHA, ASCO, AACR, ASH, ESMO, OpenAlex, Crossref, bioRxiv, medRxiv.

**Audience:** biotech and pharma investors, medtech and diagnostics analysts, scientific-literature researchers, and AI research agents.

Part of the [Healthcare Equity Research Platform](https://github.com/hh-health-AI/healthcare-equity).

<!-- geo:end -->

<!-- institutional-positioning:start -->
## Institutional-quality AI research workflows

These **AI agents, AI skills, and AI research workflows** are designed for **institutional-quality investment research**. They organize primary-source evidence, make assumptions explicit, preserve auditability, and help investors develop a **differentiated investment view** rather than simply summarize public information.

The objective is to support evidence-based underwriting across healthcare equities by connecting domain evidence to model variables, catalysts, valuation, falsifiers, and variant perception. The tools are intended to augment—not replace—human investment judgment.

<!-- institutional-positioning:end -->

Guidelines, conferences and literature velocity.

| Skill | Moves | Sub-sector | Ease/Impact |
|---|---|---|---|
| `guideline-inclusion` | Adoption curve / uptake; coverage mandate | #biopharma #tools-dx #medtech | 3 / 4 |
| `conference-abstract-handicap` | Catalyst-trade setup; readout handicap refinement | #biopharma | 3 / 4 |
| `kol-citation-velocity` | Thesis validation on scientific momentum | #biopharma #tools-dx | 3 / 3 |

**Agent:** `guideline-watcher` — USPSTF and ACIP meeting calendars, NCCN updates,
conference embargo calendar.

**Data:** USPSTF recommendations · CDC ACIP meeting materials and votes · NCCN
(open-access with registration), ADA Standards of Care, ACC/AHA guidelines · conference
abstract portals (ASCO, ASH, AACR, ESMO, ACC, AHA, TCT, SABCS, ADA, EASL) · OpenAlex
and Crossref bibliometrics · bioRxiv/medRxiv and Scholar Gateway via existing connectors.

**Embargoes are compliance boundaries.** See CLAUDE.md.

## Standard of evidence

Built to **institutional investor standards: rigorous and auditable.** 
In short: every finding carries a source, a retrieval
date and the vintage of the underlying data; confidence is gated by vintage rather
than conviction; scripts fail loudly on empty result sets so silence is never read as
a negative finding; known limitations travel in-line with the number; and evidence
stays separated from view, because this engine issues no recommendations.

## Setup

Open-data endpoints rate-limit unidentified and shared User-Agents, and SEC EDGAR
blocks them outright, so your contact string is required rather than defaulted:

```bash
export HH_CONTACT="Your Name (you@example.com)"
```

## Author

HH-health-ai

## Disclaimers

Not affiliated with, endorsed by, or connected to CMS, HHS, the FDA, the SEC, the
USPTO, the CDC, the EMA or any other government agency. All data is retrieved from
public endpoints subject to those agencies' own terms.

Nothing here is investment advice, and no output should be read as a recommendation to
buy or sell any security. These engines produce evidence for a human analyst to weigh.

Optional MCP servers are independent third-party projects under their own licenses.
Review them before use.

## License

MIT — see [LICENSE](LICENSE).

## OpenAlex query completeness

OpenAlex summaries require a validated API count, complete pagination and unique
work IDs. Queries exceeding `--max-works`, changing counts, repeated cursors,
duplicate works or premature cursor exhaustion fail without emitting a trend.
Successful output includes matched/fetched counts and `truncated: false`.

This change addresses completeness only. Citation counts remain cumulative by
publication cohort, not a fixed post-publication citation-velocity measure; the
latest incomplete calendar year also needs separate analytical treatment.

## Regression tests

Run offline with Python 3.10 or newer (standard library only):

```bash
python3 -m unittest discover -s tests -v
```

Tests use synthetic fixtures and mocked APIs; they do not certify live endpoint
availability or current regulatory facts. GitHub Actions runs the same tests on PRs.
