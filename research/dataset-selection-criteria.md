# Dataset Selection Criteria

**Purpose**: Define what makes a dataset a good candidate for this project — a data product we can build, maintain, and sell on commercial marketplaces.

---

## The Three Requirements

A candidate dataset must pass all three tests. Failing any one disqualifies it.

### 1. Recreatable From Public Internet Sources

**The question**: Can we build this dataset ourselves, from scratch, using data that is currently available on the public internet and will continue to be available?

**Passes**:
- Data originates from a government agency, international body, or public institution that publishes ongoing feeds (APIs, bulk downloads, open data portals)
- Data can be assembled by scraping structured public web pages (e.g. product listings, public records, event results)
- Data comes from public APIs with documented, stable endpoints (e.g. YouTube Data API, World Bank API, NOAA weather, BTS flight data)
- The underlying source refreshes on a known cadence (daily, monthly, annually) — we can automate collection
- Multiple independent sources exist for the same domain, allowing us to build a richer composite than any single source

**Fails**:
- A company published internal/proprietary data as a one-time public release (e.g. anonymized customer records, internal transaction logs, clinical trial data from a specific study)
- The data was collected via a now-defunct API, a time-limited research grant, or a platform that has since restricted access
- The dataset requires hardware, sensors, or physical-world collection we can't replicate (e.g. medical imaging from a hospital, IoT sensor deployments, lab experiments)
- The original source is paywalled, requires institutional credentials, or has terms that prohibit redistribution
- The data is synthetic or generated — we'd just be replicating someone's simulation parameters

**Why this matters**: We are not repackaging Kaggle datasets. We are using Kaggle as a demand signal, then building our own version from the same (or better) public sources. If we can't independently recreate and refresh the data, we don't have a product — we have a one-time copy.

---

### 2. Strong Demand Signal on Kaggle

**The question**: Is there clear evidence that people want this data — enough to justify building and maintaining a product around it?

**Signals we look for** (rough thresholds, not rigid cutoffs):

| Signal | Strong | Moderate | Weak |
|---|---|---|---|
| **Votes** | >1,000 | 400–1,000 | <400 |
| **Downloads** | >100k | 40k–100k | <40k |
| **Views** | >500k | 200k–500k | <200k |
| **Multiple similar datasets** | 3+ datasets on same topic all popular | 1-2 | Only one, niche |
| **Staleness** | Years out of date, still getting downloads | Somewhat stale | Freshly maintained |

**Why staleness is a positive signal**: A dataset that is 5+ years out of date but still accumulates downloads proves durable demand. People want this data badly enough to use a stale version. That's our gap to fill — a maintained, current version has clear value.

**Why multiple similar datasets matter**: If Kaggle has several popular datasets on the same topic (e.g. 3+ stock market datasets, multiple air quality datasets), that confirms the demand is for the *domain*, not just one particular file. Multiple versions also suggest no single version satisfies users — there's room for a definitive product.

**What to watch out for**:
- Inflated numbers from competition/course requirements (some datasets are popular only because a Kaggle competition or university course pointed students there — check if demand is organic)
- One-time topical spikes (COVID datasets surged in 2020 — is there ongoing demand?)
- ML toy/benchmark datasets (Iris, Titanic, MNIST) — popular for learning, but no commercial buyer would pay for them

---

### 3. Commercially Favorable Licensing Signal

**The question**: Does the Kaggle dataset's license suggest that the underlying data is freely available for commercial use?

**Why this matters as a *signal***: We are not redistributing the Kaggle dataset itself. But the license the uploader chose tells us something important about the nature of the underlying data:

| Kaggle License | What it signals | Our action |
|---|---|---|
| **CC0 (Public Domain)** | Uploader believes the data is freely available with no restrictions. Likely sourced from government, public APIs, or openly published sources. | Strong signal. Verify the original source independently. |
| **CC-BY** | Source is open but expects attribution. Often academic or institutional data. | Good signal. Attribution is easy to comply with. |
| **DbCL / ODbL** | Database-specific open license. Common for curated public data compilations. | Good signal. Review share-alike requirements. |
| **World Bank / Gov Open License** | Institutional open data with clear commercial-use terms. | Strong signal. Go directly to the institution's API. |
| **CC-BY-NC (Non-Commercial)** | Uploader restricts commercial use. But the *underlying public data* may still be freely available — the NC restriction may only apply to their specific compilation. | Demand signal is valid. Do NOT use their dataset. Go to the original public source and build our own. |
| **CC-BY-NC-SA** | Same as NC, plus share-alike. | Same approach — use as demand signal only. |
| **Unknown / Other / Copyright** | Unclear provenance. May be proprietary data published without clear rights. | Caution. Investigate before investing effort. |

**The key distinction**: We care about the license of the *underlying source data*, not the Kaggle upload. A CC0 Kaggle license is a strong positive signal that the raw data is public and unencumbered. An NC license doesn't disqualify the *topic* — it just means we must source independently.

**Verification step**: Before building a pipeline for any candidate, independently confirm:
1. The original data source exists and is accessible
2. The source's own license/terms permit commercial redistribution
3. The source provides an API or bulk download suitable for automation

---

## Applying the Three Criteria Together

A candidate must satisfy all three simultaneously:

```
Recreatable?  ──── Can we build it from live public sources?
     │
     ▼
Demand?       ──── Do Kaggle numbers prove people want this?
     │
     ▼
License?      ──── Does the licensing landscape allow commercial use?
     │
     ▼
CANDIDATE     ──── Proceed to enrichment planning
```

### Strong Candidate Example

**US Stock Market Data** (Kaggle: `borismarjanovic/price-volume-data-for-all-us-stocks-etfs`)

| Criterion | Assessment |
|---|---|
| Recreatable? | Yes — Yahoo Finance, SEC EDGAR, and other public sources provide daily OHLCV for all US stocks. APIs exist. Data refreshes daily. |
| Demand? | 4,608 votes, 141k downloads, 1.2M views. 8+ years stale and still downloaded constantly. Multiple similar datasets (S&P 500, NYSE) confirm domain demand. |
| License? | CC0 on Kaggle. Stock price data is factual/public — no copyright on facts. Original sources (exchanges) publish with public access. |
| **Verdict** | Strong candidate. All three criteria clearly met. |

### Disqualified Example

**Credit Card Fraud Detection** (Kaggle: `mlg-ulb/creditcardfraud`)

| Criterion | Assessment |
|---|---|
| Recreatable? | **No** — This is anonymized PCA-transformed transaction data from a European bank's internal records. We cannot access this bank's transaction stream. No public source exists for real credit card transactions. |
| Demand? | 12,936 votes, 1.1M downloads — among the most popular on all of Kaggle. |
| License? | DbCL — technically permissive. |
| **Verdict** | Disqualified. Fails criterion #1 despite massive demand. This is a one-time proprietary data release we cannot recreate. |

### Borderline Example

**FitBit Fitness Tracker Data** (Kaggle: `arashnic/fitbit`)

| Criterion | Assessment |
|---|---|
| Recreatable? | **Borderline** — This is survey-collected data from 30 FitBit users via Amazon Mechanical Turk. We could run a similar survey, but it requires recruiting participants and collecting personal health data. No public API provides this at scale. Not truly "data on the internet." |
| Demand? | 2,620 votes, 194k downloads. Strong demand signal for wearable/health data. |
| License? | CC0. |
| **Verdict** | Borderline. The *demand signal* is valid (people want wearable health data), but recreating this specific product requires human subject recruitment, not internet data collection. Better approach: look for public health datasets from government sources (CDC, WHO) that satisfy criterion #1. |

---

## Quick Disqualification Checklist

Before deep evaluation, check for these immediate disqualifiers:

- [ ] **One-time proprietary dump?** Company published internal data once → can't recreate → skip
- [ ] **Requires physical collection?** Medical imaging, sensor data, lab results → can't recreate from internet → skip
- [ ] **Synthetic/generated data?** Someone ran a simulation → no unique value in recreating → skip
- [ ] **Platform-specific export?** Data from a platform that has since restricted API access (e.g. old Twitter/X datasets) → can't recreate → skip
- [ ] **Kaggle competition artifact?** Dataset exists solely as a competition target with no real-world application → skip
- [ ] **ML toy/benchmark?** Iris, Titanic, MNIST, etc. → no commercial buyer → skip
- [ ] **NC license with no independent source?** If NC-licensed AND we can't find the underlying public source → skip

---

## Summary

We are looking for datasets that sit at the intersection of three things:

1. **Buildable** — Live public data sources we can automate pipelines against
2. **Wanted** — Proven demand from Kaggle's popularity metrics
3. **Legal** — Licensing landscape that permits commercial data products

Kaggle is our **demand signal source**, not our **data source**. We use it to discover what people want, then we build our own superior version from the original public data.
