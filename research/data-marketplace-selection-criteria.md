# Data Marketplace Selection Criteria

**Date**: 2026-02-27
**Purpose**: Define what makes a data marketplace worth joining — both for the bootstrap phase (building credibility) and long-term scaled distribution.

> **Context**: We are a startup with no track record. We want to be on many marketplaces simultaneously (none require exclusivity). Every marketplace we join must meet ALL four criteria below. No exceptions.

---

## The Four Requirements

A marketplace must pass all four tests. Failing any one disqualifies it.

### 1. Full API-Driven Dataset Management

**The question**: After initial sign-up, can we create, update, and manage all our listings entirely through APIs — with zero manual portal interaction?

**Passes**:
- Platform provides a documented REST/GraphQL API (or CLI/SDK) for creating listings, uploading data, updating metadata, publishing revisions, and managing pricing
- We can automate the full lifecycle: create dataset → push new revision → update description → adjust pricing → monitor usage — all from our pipelines
- Bulk operations are supported (we will have 10–20+ datasets, potentially many more)
- API has reasonable rate limits and supports our update cadences (daily/weekly/monthly depending on dataset)

**Fails**:
- Listing creation or updates require clicking through a web portal
- Data uploads must be done manually (drag-and-drop, file picker)
- Metadata changes (description, pricing, tags) can only be made through a GUI
- Any recurring step in the publishing workflow requires human interaction beyond the initial account setup
- "API available" but only for read/query — not for publishing or management

**Why this matters**: We are building an automated factory. Every manual step is a scaling bottleneck and an operational cost we refuse to carry. If a marketplace forces us into a portal for routine operations, the maintenance burden will compound across 10–20+ datasets and kill us. One-time sign-up friction is acceptable. Ongoing friction is not.

---

### 2. Generalist Coverage

**The question**: Can we list datasets across multiple unrelated categories without restriction?

**Passes**:
- Platform supports listings across many industries/domains (financial, geospatial, environmental, economic, demographic, etc.)
- No requirement that all our listings be in a single category
- Category taxonomy is broad enough to accommodate whatever we build
- Platform's buyer base spans multiple use cases (analytics, ML, research, business intelligence)

**Fails**:
- Platform restricts to a single domain (e.g. "financial data only", "healthcare only", "advertising/identity only")
- Platform technically allows multiple categories but buyer base is monolithic (e.g. only hedge funds browse it)
- Platform requires data to be linkable to people/devices/identities (e.g. AdTech marketplaces)
- Our data would be a poor fit for the platform's core audience across most categories

**Why this matters**: We don't yet know which datasets will have legs. We need marketplaces where we can cast a wide net — listing an economic indicators dataset next to a geospatial dataset next to a sports dataset. Joining a niche marketplace locks us into one bet. We want optionality.

---

### 3. Demonstrated Market Traction

**The question**: Does this marketplace have real buyers making real purchases, or is it a ghost town?

**Passes**:
- Published or verifiable metrics on provider count, listing count, buyer activity, or transaction volume
- Named enterprise customers or institutional buyers using the platform
- Active provider community with visible evidence of small/new providers succeeding
- Platform has been operating for 2+ years with evidence of growth (not stagnation)
- Independent reviews, press coverage, or community discussion confirming real usage

**Fails**:
- No verifiable metrics on buyer activity — just marketing claims
- Platform launched recently with no evidence of completed transactions
- Only a handful of providers listed, or provider count is inflated (registered but not active)
- No independent mentions — only the platform's own marketing materials reference it
- Buyer base is theoretical ("enterprise buyers will come once we have more data")

**Why this matters**: A marketplace with no buyers is just a website. We need platforms where someone is actually paying for data today, even if the scale is modest. We'll accept small if it's real. We won't accept big promises with no evidence.

**Acceptable traction signals by tier**:
- **Large-scale**: Thousands of providers, named enterprise buyers, public revenue/growth numbers (e.g. AWS Data Exchange, Snowflake Marketplace)
- **Mid-scale**: Hundreds of providers or thousands of listed products, verifiable buyer community, documented transactions (e.g. Datarade with 2,600+ providers)
- **Small-scale**: Tens of providers, but named customers and evidence of real sales — especially if the platform handles sales for you (e.g. Dewey Data with ~30 providers but MIT/Stanford as documented buyers)
- **Unacceptable**: No buyer evidence, only provider sign-ups, or platform is in "beta" with a waitlist

---

### 4. No Fees to Participate

**The question**: Can we list and sell data without paying upfront fees, subscription costs, or platform access charges?

**Passes**:
- Free to create an account and list data products
- Platform monetizes through commission/revenue-share only — they earn when we earn
- Transaction-based fees are acceptable (e.g. 3% of sales, payment processing fees)
- Standard cloud infrastructure costs are acceptable (e.g. S3 storage for our own data, compute for our own queries)
- One-time setup costs that are part of normal infrastructure (e.g. setting up a Snowflake account we'd use anyway) are acceptable

**Fails**:
- Monthly/annual subscription fee to maintain a provider account or listing
- Per-listing fees (pay to list each dataset)
- Platform access fees separate from transaction revenue
- Required paid partnership or membership program to list (e.g. paid-tier partner programs)
- "Freemium" where free tier is too limited to be useful (e.g. can only list 1 dataset, must upgrade to list more)

**Why this matters**: As a startup, every dollar spent on marketplace fees is a dollar not spent on building datasets. We want to be on as many marketplaces as possible — if 5 platforms each charge $500/month, that's $30K/year before we've sold a single record. Revenue-share models align incentives: the platform invests in helping us sell because they only earn when we do. Fixed fees are a tax on being present, regardless of results.

**Nuance — cloud platform costs**: We will need AWS, Snowflake, and/or Databricks accounts to operate our data pipelines regardless of marketplace participation. The cost of these accounts is infrastructure, not marketplace participation fees. If a marketplace is embedded in a cloud platform we already use (e.g. AWS Data Exchange within our existing AWS account), the incremental cost to list is effectively zero. But if a marketplace requires us to adopt a new paid platform solely to list data (e.g. requiring a Databricks Premium workspace we wouldn't otherwise need), that is a de facto participation fee.

---

## Applying the Four Criteria Together

A marketplace must satisfy all four simultaneously:

```
API-Managed?   ──── Can we automate everything after sign-up?
     │
     ▼
Generalist?    ──── Can we list across many categories?
     │
     ▼
Traction?      ──── Are real buyers actually purchasing data here?
     │
     ▼
No Fees?       ──── Can we list without paying to participate?
     │
     ▼
APPROVED       ──── Add to our distribution list
```

---

## Assessment of Known Marketplaces

### Primary Marketplaces (Large-Scale Growth)

| Platform | API-Managed | Generalist | Traction | No Fees | Verdict |
|----------|-------------|------------|----------|---------|---------|
| AWS Data Exchange | Yes — Catalog API, Data Exchange API, CLI | Yes | Yes — 3,500+ products, 300+ providers | Yes — 3% commission only | **Pass** |
| Snowflake Marketplace | Yes — SQL API (`CREATE LISTING`) | Yes | Yes — 2,700+ listings, 670+ providers | Yes — 0% commission | **Pass** |
| Databricks Marketplace | Partial — Provider Console, but no public listing API documented | Yes | Yes — 2,200+ listings, 230+ providers | Yes — 0% fee | **Investigate API** |
| Google Analytics Hub | Yes — REST API, gcloud CLI, Terraform | Yes | Moderate — "underrated", lower adoption | Yes — 2–3% commission | **Pass (weak traction)** |
| Narrative.io | Yes — platform APIs for data ingestion and product management | Yes | Moderate — buyer base skews AdTech | Yes — 0% from seller | **Pass** |

### Bootstrap Marketplaces

| Platform | API-Managed | Generalist | Traction | No Fees | Verdict |
|----------|-------------|------------|----------|---------|---------|
| Dewey Data | No — Dewey manages listings for you (no self-service API) | Yes | Yes — ~30 providers, named academic buyers | Yes — revenue share only | **Conditional pass** — no API but they do the work for you |
| Datarade | Investigate — listing management may be portal-only | Yes (500+ categories) | Yes — 2,600+ providers, 120K monthly visitors | Yes — commission on deals only | **Investigate API** |
| Nomad Data | Investigate | Yes | Yes — 2,500+ sources | Yes — zero fees | **Investigate API** |
| Opendatabay | Investigate — appears portal-based | Yes | Unverified — newer platform | Yes — 5–30% commission | **Investigate traction + API** |
| Nasdaq Data Link | Yes — well-documented API (Quandl heritage) | No — finance-focused | Yes — ~950K users, ~250 premium datasets | Yes — revenue share | **Fail (not generalist)** |
| Eagle Alpha | No — lead-gen model, introductions are manual | Partial — alt data broadly | Yes — 2,500+ products | Yes — zero fees | **Fail (no API management)** |
| Neudata | No — scouting/introduction model | Partial — alt + traditional data | Yes — 2,000 vendors, 1,000+ buyers | Yes — zero fees | **Fail (no API management)** |
| Data & Sons | Investigate | Yes | Unverified — limited traction evidence | Yes | **Investigate traction** |
| Defined.ai | Investigate | Partial — AI training data | Yes — growing fast (1,200% marketplace expansion 2025) | Yes — revenue share | **Investigate API + generalist fit** |

### Key Observations

- The **primary cloud marketplaces** (AWS, Snowflake, Google) all pass on API management — this is expected, they're built for enterprise automation.
- **Databricks** needs investigation on whether listing management can be fully API-driven or requires the Provider Console GUI.
- The **bootstrap marketplaces** mostly fail or need investigation on the API criterion — smaller platforms tend to have portal-based workflows.
- **Dewey Data** is an interesting exception: it fails the API test technically, but because Dewey manages everything for you, there's no manual work on our side. The "no friction" goal is met through a different mechanism (they absorb the friction).
- The **lead-gen platforms** (Eagle Alpha, Neudata) inherently fail API management because their model is human introductions, not automated listing management. They're still worth using for zero-cost lead generation, but they don't qualify as "marketplaces" under these criteria.

---

## Practical Application

When evaluating a new marketplace, score it against the four criteria:

| Score | Meaning |
|-------|---------|
| **Pass** | Clearly meets the criterion |
| **Conditional** | Meets the spirit but not the letter (e.g. Dewey does it for you instead of API) |
| **Investigate** | Information not available — need to test or contact the platform |
| **Fail** | Does not meet the criterion |

**Decision rules**:
- 4x Pass → **Join immediately**
- 3x Pass + 1x Conditional → **Join with documented exception**
- Any "Investigate" → **Research before committing time**
- Any "Fail" → **Do not join** (unless the fail is on generalist coverage and the platform serves a category we're specifically targeting)
