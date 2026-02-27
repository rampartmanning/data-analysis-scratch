# Data Marketplaces — Bootstrap List (v2)

**Date**: 2026-02-27
**Purpose**: Platforms where a startup with no track record can sell data to build credibility, evaluated against our four selection criteria (see `data-marketplace-selection-criteria.md`).

> **v2 note**: Original list was aspirational. This version applies the four hard criteria (API-managed, generalist, traction, no fees) rigorously. Many platforms from v1 have been eliminated.

---

## Criteria Applied

Every platform must pass ALL four:

1. **API-managed** — full lifecycle automation after sign-up (no portal friction)
2. **Generalist** — multi-category, not domain-locked
3. **Traction** — real buyers, real transactions, not a ghost town
4. **No fees** — commission/revenue-share only, no subscription to participate

---

## Results Summary

After deep research into API capabilities, provider onboarding, and market traction for every candidate:

| Platform | API | Generalist | Traction | No Fees | Verdict |
|----------|-----|------------|----------|---------|---------|
| **Azure Marketplace** | Yes | Yes | Massive | Yes (3%) | **PASS** |
| **Databricks Marketplace** | Yes | Yes | Strong | Yes (0%) | **PASS** (was "investigate", now confirmed) |
| **RapidAPI** | Yes | Yes | Very strong | Yes (20–25%) | **PASS** (API delivery model) |
| **APILayer** | Yes | Yes | Moderate | Yes (15%) | **PASS** (API delivery model) |
| **Dewey Data** | No API | Yes | Yes | Yes | **CONDITIONAL** (they absorb friction) |
| Datarade | No API | Yes | Yes | Portal-only or via Monda ($6K+/yr) | **FAIL** |
| Nomad Data | No API | Yes | Thin | Yes | **FAIL** |
| Opendatabay | No API | Yes | None | Yes | **FAIL** |
| Data & Sons | Unverified | Yes | Unverified | Yes | **FAIL** (traction unverifiable) |
| Monda | Pro tier only | Yes | N/A (tool) | No ($6K+/yr subscription) | **FAIL** |
| Nasdaq Data Link | Yes | No | Yes | Yes | **FAIL** (finance-only) |
| Eagle Alpha | No API | Partial | Yes | Yes | **FAIL** |
| Neudata | No API | Partial | Yes | Yes | **FAIL** |
| Defined.ai | Unverified | Partial | Growing | Yes | **FAIL** (not generalist) |

**Only 5 platforms pass or conditionally pass.** The landscape is thin.

---

## Platforms That Pass

### 1. Azure Marketplace

| Field | Detail |
|-------|--------|
| **URL** | https://azure.microsoft.com/en-us/partners/marketplace |
| **API** | Yes — Partner Center APIs + SaaS Fulfillment APIs v2. Programmatic offer creation, listing management, billing. |
| **Generalist** | Yes — 58,000+ products across all categories. Data products sold as SaaS offers or via Azure Data Share. |
| **Traction** | Massive — enterprise buyers across every sector. Integrated with Azure consumption commitments (MACC drawdown). |
| **Fees** | 3% flat store service fee on transactions. No upfront listing fees. |
| **Approval** | Must join Microsoft Partner Network (free tier available). Standard review process. |
| **Data delivery** | SaaS with API delivery, or Azure Data Share for dataset access. |
| **Why bootstrap** | Same approval rigour as AWS/Snowflake, but the Microsoft Partner Network free tier and SaaS model may be more accessible for a startup packaging data as an API product. |

**Note**: Azure was excluded from our original primary list because it was judged "fragmented, smaller data catalog" compared to AWS/Snowflake. But it passes all four criteria and has massive buyer reach. It belongs in our distribution strategy — whether as primary or bootstrap depends on our Azure infrastructure investment.

---

### 2. Databricks Marketplace (UPGRADED from "investigate")

| Field | Detail |
|-------|--------|
| **URL** | https://www.databricks.com/product/marketplace |
| **API** | **Yes — full programmatic API confirmed.** REST API (`/api/2.0/marketplace-provider/listings` — create, get, list, update, delete), Python SDK (`databricks-sdk` — `w.provider_listings`, `w.provider_files`, `w.provider_exchanges`), CLI (`databricks provider-listings create`). Full CRUD for listings, files, exchanges, provider profiles, analytics dashboards. Delta Sharing shares also fully API-managed via Unity Catalog API. |
| **Generalist** | Yes — all industries. |
| **Traction** | Strong — 2,200+ listings, 230+ providers, growing ~40-50 new providers/quarter. |
| **Fees** | 0% — no commission, no listing fee, no transaction fee. |
| **What changed** | Previously scored "INVESTIGATE" on API. Research confirmed full provider API across REST, SDK, and CLI. Every step after initial partner approval is automatable. |

**Databricks should be promoted from "investigate" to "confirmed pass" on the primary marketplace list.** The full automation story is:
```
Terraform → create Unity Catalog + schemas + tables
Pipeline  → ETL populates tables
SDK       → CREATE SHARE + ADD TABLE
SDK       → provider_files.create() (icon, notebooks)
SDK       → provider_listings.create() (listing referencing share)
Monitor   → system.marketplace.listing_funnel_events
Update    → provider_listings.update()
```

---

### 3. RapidAPI (API delivery model)

| Field | Detail |
|-------|--------|
| **URL** | https://rapidapi.com |
| **API** | Yes — full provider tooling: documentation generation, tiered pricing plans, billing automation, key management, analytics dashboard. |
| **Generalist** | Yes — 35,000+ APIs across 30+ categories. |
| **Traction** | Very strong — largest API marketplace globally. 4M+ developers, 175 countries. Billions of API calls/month. Acquired by Nokia (Nov 2024). |
| **Fees** | 20–25% marketplace fee on transactions. No upfront costs. |
| **Payout** | PayPal only. |
| **Fit** | Best for data products delivered as REST APIs (e.g., a geocoding API, an economic indicators API) rather than static file downloads. The 20–25% commission is steep but acceptable for the reach. |
| **Caveat** | Nokia acquisition could change terms. Commission is high. PayPal-only payouts add friction. |

**Strategic angle**: If we build data products with API access (which aligns with our "agent-ready distribution" thesis), RapidAPI gives us access to 4M+ developers with zero upfront cost. We'd need to build an API layer, but we're likely building that anyway.

---

### 4. APILayer (API delivery model)

| Field | Detail |
|-------|--------|
| **URL** | https://apilayer.com |
| **API** | Yes — providers host their own APIs; APILayer handles key management, payment collection, customer acquisition. |
| **Generalist** | Yes — 75+ curated APIs across AI/ML, finance, geolocation, and more. |
| **Traction** | Moderate — curated marketplace (quality over quantity). Active developer community. Established since 2022. |
| **Fees** | 15% marketplace fee. No upfront costs. Monthly payouts. |
| **Hosting requirement** | Providers must host on approved cloud platforms (AWS, GCP, Azure, DigitalOcean, Scaleway, Hetzner). |
| **Fit** | Same as RapidAPI but lower commission (15% vs 20–25%) and smaller audience. Curated means they may reject low-quality submissions — which could work in our favour once listed. |

---

### 5. Dewey Data (CONDITIONAL pass)

| Field | Detail |
|-------|--------|
| **URL** | https://www.deweydata.io |
| **API** | **No provider API.** All APIs (Python, R, CLI) are consumer-facing only. No listing management, no data upload, no metadata updates via API. |
| **Why conditional** | Dewey operates a white-glove managed service. Provider sets up one data feed (S3/Snowflake/SFTP, ~30 min), and Dewey handles everything else: listing creation, metadata, sales, delivery, contracts, support, compliance. The "no friction" goal is met through a different mechanism — they absorb the friction entirely. |
| **Generalist** | Yes — real estate, mobility, labor, consumer, corporate, government, financial, weather, technology. |
| **Traction** | Yes — ~30 providers, named academic buyers (MIT, Stanford, NYU, Berkeley). Small but real. |
| **Fees** | Revenue share only (% undisclosed). |
| **Small provider evidence** | LobbyingData.com (single founder), NatureQuant, Capology. |
| **Limitation** | Schema changes or major revisions require manual coordination with Dewey's team. No self-service control over your listing. Buyer audience is academic (lower revenue per sale). |

**Verdict**: Does not meet the letter of criterion 1 (no API), but meets the spirit (zero ongoing friction). Include with a documented exception.

---

## Platforms That Fail (with evidence)

### Datarade — FAIL (no API, fee via Monda)

- **What we found**: Datarade has no public provider API. The only way to manage listings programmatically is through Monda (their sister company spun off in 2024), which requires a paid subscription (~$6K+/year minimum) plus 20–30% commission on Datarade sales. Monda's API is only available on the Professional tier, and has no public documentation.
- **Fails**: Criterion 1 (no API without Monda), Criterion 4 (Monda subscription = participation fee).

### Nomad Data — FAIL (no API, thin traction)

- **What we found**: No API whatsoever. Provider interaction is email-based: buyer submits request → Nomad matches → provider gets email → negotiates offline. No listing management, no dashboard, no programmatic control. $4.8M total funding over 5+ years, ~7 employees, no Series A. No independent reviews on G2/Capterra. "4,900 providers" is inflated — free sign-up with minimal engagement required.
- **Fails**: Criterion 1 (email-only, no API), Criterion 3 (traction is thin/unverifiable).

### Opendatabay — FAIL (no API, no traction)

- **What we found**: No provider API. Upload features are still "being developed" (per their own docs). Founded May 2024, 1 FTE + 13 volunteers, no disclosed funding. 46 providers, 327 datasets. "30,000+ professionals" claim is unverifiable and likely inflated. First company accounts overdue at UK Companies House. 17 total GitHub stars. No independent reviews anywhere.
- **Fails**: Criterion 1 (no API, uploads still in development), Criterion 3 (garage-band scale — exactly what we said to avoid).

### Data & Sons — FAIL (traction unverifiable)

- **What we found**: No independent reviews, no verifiable buyer activity metrics, no press coverage beyond their own marketing. Cannot confirm real transactions happening.
- **Fails**: Criterion 3 (unverifiable traction).

### Monda — FAIL (subscription fee)

- **What we found**: Subscription starts at ~$6K+/year (Standard tier). Annual commitment. API access only on Professional tier (higher price, undocumented). On top of subscription, takes 20–30% commission on Datarade sales. Does not integrate with AWS Data Exchange.
- **Fails**: Criterion 4 ($6K+/year subscription is a participation fee).

### Nasdaq Data Link — FAIL (not generalist)

- Finance/investment only. Buyers are hedge funds and quant researchers. Data must have investment relevance.
- **Fails**: Criterion 2 (not generalist).

### Eagle Alpha / Neudata — FAIL (no API)

- Lead-gen/introduction models. Human-mediated connections, not programmable. No listing management API.
- **Fails**: Criterion 1 (no API — fundamentally incompatible with automated operations).

### Defined.ai — FAIL (not generalist)

- AI training data only (speech, text, image, video). Not general-purpose across business data categories.
- **Fails**: Criterion 2 (not generalist).

---

## Updated Full Marketplace Strategy

Combining the primary list (from `marketplace-provider-terms.md`) with confirmed bootstrap platforms:

### Pass All 4 Criteria — Dataset Marketplaces

| # | Platform | Fee | API | Buyer Reach | Status |
|---|----------|-----|-----|-------------|--------|
| 1 | AWS Data Exchange | 3% | Full (Catalog API, CLI) | AWS customers (millions) | Primary |
| 2 | Snowflake Marketplace | 0% | Full (SQL API) | Snowflake customers (~10K+) | Primary |
| 3 | Databricks Marketplace | 0% | Full (REST, SDK, CLI) | Databricks + Delta Sharing | **Primary (confirmed)** |
| 4 | Google Analytics Hub | 2–3% | Full (REST, Terraform) | BigQuery customers | Primary (weak traction) |
| 5 | Narrative.io | 0% from seller | Full (platform APIs) | Cross-platform | Primary |
| 6 | Azure Marketplace | 3% | Full (Partner Center API) | Azure customers (massive) | **New addition** |

### Pass All 4 Criteria — API Marketplaces

| # | Platform | Fee | Buyer Reach | Fit |
|---|----------|-----|-------------|-----|
| 7 | RapidAPI | 20–25% | 4M+ developers, 175 countries | Data-as-API products |
| 8 | APILayer | 15% | Curated developer community | Data-as-API products |

### Conditional Pass

| # | Platform | Fee | Exception |
|---|----------|-----|-----------|
| 9 | Dewey Data | Revenue share | No API, but they manage everything — zero provider friction |

---

## Revised Recommended Sequence

```
IMMEDIATE (zero cost)
├── Narrative.io      → Self-service, no approval gate, API-managed
└── Dewey Data        → Submit partnership form (they do all the work)

MONTH 1-2 (cloud marketplaces — apply in parallel)
├── AWS Data Exchange → Submit qualification request
├── Snowflake         → Create provider profile, begin paid listing vetting
├── Databricks        → Apply to Data Partner Program
├── Google Analytics Hub → Enable API, create exchange (free listings first)
└── Azure Marketplace → Join Microsoft Partner Network, submit listing

MONTH 2-3 (API marketplaces — if building API delivery layer)
├── RapidAPI          → List data APIs (20-25% commission but 4M+ devs)
└── APILayer          → List data APIs (15% commission, curated)

ONGOING
├── Re-evaluate Datarade if they launch a free provider API
├── Monitor Monda pricing for a free/commission-only tier
└── Watch for new marketplaces meeting all 4 criteria
```

---

## Key Insight: The Bootstrap Gap

The honest finding is that **there is no rich ecosystem of small, easy-entry, API-managed data marketplaces**. The landscape is sharply bifurcated:

1. **Big cloud marketplaces** — API-managed, high traction, but require approval/vetting
2. **Small platforms** — low barrier, but portal-based, low traction, or both

The bootstrap strategy therefore shifts from "build credibility on small platforms first" to:

- **Apply to the big platforms simultaneously** — the approval timelines are undefined, so start early
- **Use Narrative.io as the easiest on-ramp** — self-service, API-managed, no approval gate
- **Use Dewey Data for academic credibility** — they do all the work, precedent of small providers
- **Build API delivery for RapidAPI/APILayer** — different channel, different buyers, zero approval friction
- **Don't wait for bootstrap credibility** — just apply to everything in parallel and see who approves first
