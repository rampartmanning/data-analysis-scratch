# Data Marketplace Provider Terms — Research Report

**Date**: 2026-02-27
**Scope**: General-purpose, paid-data marketplaces from our focus list
**Purpose**: Understand payment terms, approval process, and ease of publishing for data providers

---

## Selection Criteria

From the 10-platform focus list (`research/data-marketplaces-selected.md`), filtered for:
- **(a) General-purpose** — not niche to one domain
- **(b) Paid-for data** — marketplace supports commercial data transactions

| Platform | General? | Paid Data? | Included? | Reason if Excluded |
|----------|----------|------------|-----------|-------------------|
| AWS Data Exchange | Yes | Yes | **Yes** | — |
| Snowflake Marketplace | Yes | Yes | **Yes** | — |
| Databricks Marketplace | Yes | Yes | **Yes** | — |
| Google Cloud Analytics Hub | Yes | Yes | **Yes** | — |
| Narrative.io | Yes | Yes | **Yes** | — |
| Datarade | — | — | No | Aggregator/directory, not a transactional marketplace |
| Kaggle | Yes | No | No | Community/free datasets only |
| Hugging Face | Yes | No | No | Community/free datasets only |
| Nasdaq Data Link | No | Yes | No | Finance-heavy, not general-purpose |
| Google Dataset Search | — | — | No | Meta-search engine, not a marketplace |

---

## Comparative Summary

| Dimension | AWS Data Exchange | Snowflake Marketplace | Databricks Marketplace | Google Analytics Hub | Narrative.io |
|---|---|---|---|---|---|
| **Platform fee** | 3% (public); 1.5–3% (private, tiered) | 0% (currently) | 0% | 2–3% (tiered) | 0% from seller (25% charged to buyer) |
| **Payment mechanism** | AWS disburses monthly | Stripe (or Snowflake for MCD) | None — offline billing | Google pays ~21st monthly | Narrative billing system |
| **Pricing models** | Subscription (1–36 mo), private offers | Usage, subscription, installment | Offline negotiation | Free, paid subscription, trial | CPM, direct deals |
| **Approval timeline** | Undefined (manual review) | ~1 day profile; paid = vetting call | Manual partner review (days–weeks) | 2–4 weeks for commercial | Self-service, no gate |
| **Publishing effort** | Low–moderate (AWS-native) | Low–medium | Low if on Databricks; moderate otherwise | Low (free); high (commercial) | Moderate (S3 + schema setup) |
| **Exclusivity** | None | None | None | None | None |
| **Buyer lock-in** | Must be AWS customer | Must be Snowflake customer | Databricks or Delta Sharing | Must be BigQuery customer | Platform-agnostic |

---

## 1. AWS Data Exchange

### Payment Terms

- **Platform fee**: 3% on public offers. Private offers tiered: <$1M = 3%, $1–10M = 2%, >$10M = 1.5%. Renewals = 1.5%. BYOS offers = 0%.
- **Disbursement**: Monthly rolling basis, only after AWS collects from subscriber. Net of fees.
- **Currency**: USD only.
- **Pricing models**: Subscription-based (1–36 month durations, up to 5 price/duration combos per offer). Private offers with custom terms. No metered or one-time purchase model.
- **Refunds**: Provider-controlled. Provider must approve all refund requests.
- **Infrastructure costs borne by provider**: Data grant fees ($0.04/grant/hour), S3 storage ($0.023/GB/month), API Gateway fees for API products.

### Approval Process

1. Must be AWS customer in good standing in an eligible jurisdiction (~16 countries: US, EU, UK, AU, JP, IN, etc.).
2. Register on AWS Marketplace Management Portal. Complete tax (W-9/W-8) and banking info.
3. Submit qualification request via AWS Support case.
4. AWS Data Exchange team conducts detailed review — **timeline not published**.
5. Once qualified, can list products.

**Key constraint**: The AWS account used to register is permanently locked to the provider identity.

### Ease of Publishing

- **Formats**: Any file format (Parquet recommended). Also supports REST APIs (API Gateway), Redshift datashares, S3 direct access, Lake Formation (preview).
- **Tooling**: Console GUI, Marketplace Catalog API, Data Exchange API, CLI — all support automation.
- **Workflow**: Create dataset → create revision → import assets → finalize → create product → publish. AWS says "can be done in minutes."
- **Updates**: New revisions auto-publish to subscribers after finalization.
- **Subscription verification**: Optional (required for PII products). Providers can review/approve subscribers. 45-day auto-expiry on pending requests.

### Other Notable Terms

- **No exclusivity** — multi-platform distribution allowed.
- **PII restrictions**: No PII by default. Extended Provider Program (additional review) required for sensitive personal data.
- **Prohibited**: Sensitive location data linking individuals to healthcare facilities, places of worship, correctional facilities, etc.
- **Export control**: Cannot distribute bulk US personal data to "Countries of Concern" (EO 14117).
- **API support SLA**: Must respond to subscriber questions within 1 business day.
- **No cross-promotion**: Cannot promote products outside AWS Marketplace.
- **All datasets in a product must be same AWS Region** (but catalog is global).
- **Provider feedback**: Limited organic traffic, limited seller analytics, some UX complaints. Integration with AWS infra praised.

---

## 2. Snowflake Marketplace

### Payment Terms

- **Platform fee: 0% currently.** Snowflake does not charge any commission or listing fee. They monetize indirectly through compute consumption by consumers. Legal terms reserve the right to introduce fees in the future.
- **Payment mechanism**: Stripe Express (new account required — can't reuse existing). Stripe pays providers directly after collecting from consumers.
- **MCD program**: Consumers can use existing Snowflake capacity commitments to pay for marketplace listings. In this case, Snowflake pays providers directly. Currently US-to-US only.
- **Pricing models**:
  - **Usage-based**: Per-query, monthly base fee, or billable events (with mandatory monthly cost cap).
  - **Subscription**: 1–36 months, recurring or non-recurring.
  - **Installment**: Periodic payments with optional skip periods.
  - Free, limited trial, and paid tiers all supported.
- **Refunds**: All product costs are non-cancelable and non-refundable.

### Approval Process

1. Full Snowflake account required (no trial accounts). ACCOUNTADMIN role needed.
2. Accept Provider and Consumer Terms.
3. Create provider profile in Provider Studio. **Profile review: ~1 business day.**
4. For **free listings**: Create listing, submit for review. **Listing review: ~1 business day.**
5. For **paid listings**: Must demonstrate "go-to-market readiness." Partners with a Snowflake Partner Manager must engage them first. Others submit a case and may undergo a **vetting call**. Approval at Snowflake's discretion.
6. Stripe Express account setup required.
7. Billing address must be in one of **19 approved countries**.

**Max 100 listings per provider.**

### Ease of Publishing

- **Product types**: Secure Share (simplest — share tables/views), Native App (packaged app), Connected App (external app).
- **Tooling**: Snowsight/Provider Studio GUI, SQL API (`CREATE LISTING`), notebook attachments.
- **Required metadata**: Title, subtitle, description, legal terms, data dictionary (mandatory), SQL examples, categories, contact info (business domain email), logo.
- **Effort**: Free listing = low-medium. Paid listing = medium-high (Stripe setup, monetization approval, go-to-market vetting).

### Other Notable Terms

- **No exclusivity** — multi-platform distribution fully supported.
- **Content quality**: Must accurately describe update frequency, scope, completeness. Cannot remove core fields or reduce frequency post-listing.
- **Response SLA**: 3 business days for consumer inquiries.
- **No sensitive personal data** in public listings.
- **AI products**: Must disclose LLM model/version, logic, safety guardrails, example prompts.
- **Usage data confidentiality**: Consumer usage data is confidential, limited to internal business purposes.
- **One provider profile per legal entity.**

---

## 3. Databricks Marketplace

### Payment Terms

- **Platform fee: 0%.** Databricks takes no revenue share, listing fee, or transaction fee. This is because the marketplace has **no built-in payment processing**.
- **Payment mechanism**: None. All commercial transactions happen offline between provider and consumer. Provider negotiates, invoices, and collects independently. After payment, provider clicks "Fulfill" to provision access.
- **Implication**: Great for margins, but requires your own billing/sales infrastructure.
- **Pricing models**: Whatever you negotiate offline. No structured pricing framework within the platform.

### Approval Process

- **Public Marketplace**: Apply through the [Databricks Data Partner Program](https://www.databricks.com/partners/data-partner-program). Manual review — no published SLA (expect days to weeks). Requires Databricks Premium workspace with Unity Catalog enabled.
- **Private Exchange**: Self-service, no external approval needed. Listings visible only to invited members.

### Ease of Publishing

- **Formats**: Delta Lake tables, views, volumes (non-tabular files), AI/ML models, notebooks, Git repos, apps, MCP servers. Tables are the only type accessible to non-Databricks consumers via open Delta Sharing protocol.
- **Tooling**: Provider Console GUI for creating shares and listings.
- **Effort if already on Databricks**: Low — minutes to hours from existing Unity Catalog tables.
- **Effort if NOT on Databricks**: Moderate-high — must provision Premium workspace, set up Unity Catalog, load data into Delta Lake.

### Other Notable Terms

- **No exclusivity** — multi-platform distribution allowed.
- **No sensitive personal data** allowed, ever. Regular personal data requires legal authorization.
- **30-day minimum notice** before discontinuing a product.
- **Response SLAs**: 3 business days for access requests, 5 business days for other inquiries.
- **Dataset freshness**: Must update at "the most frequent logical refresh rate."
- **One provider profile per organization** (unless exception granted).
- **No geographic restrictions** on listing or consuming.
- **Scale**: ~230+ providers, ~2,200+ listings as of mid-2024.

---

## 4. Google Cloud Analytics Hub (BigQuery Sharing)

### Payment Terms

- **Platform fee**: 2–3% (via Google Cloud Marketplace integration). Variable revenue share (April 2025):
  - Standard/small offers: 3%
  - New deals: 2%
  - $1–10M TCV: 2%
  - Native renewals: 1.5%
  - >$10M TCV: 1.5%
- **Disbursement**: ~21st of each month, aggregated across all customers for the period.
- **Currency**: Prices set in USD. Customers pay in 30+ currencies across 65 countries.
- **Pricing models**: Free (subscriber pays own BigQuery compute only), paid subscription (flat fee + cloud resource charges, monthly auto-renew), trial (time-limited free), custom private offers.

### Approval Process

**Free/private listings** (non-commercial):
- Google Cloud project with BigQuery enabled. Enable Analytics Hub API. Grant yourself Publisher role. No formal approval.

**Commercial Marketplace listings**:
1. Join Google's **Partner Advantage** program.
2. Must be incorporated in an eligible jurisdiction (65+ countries).
3. Product must be production-ready and enterprise-ready (professional web presence, support, security).
4. Onboarding through Partner Hub with documentation submission.
5. Complete Cloud Marketplace Project Info Form for Producer Portal access.
6. Create BigQuery Sharing listing, link to Marketplace product, submit for review.
7. **Review: 2–5 business days**, up to 2 weeks. Up to 2 additional days for public visibility.
8. **Total timeline: plan 2–4 weeks.**

### Ease of Publishing

- **Supported types**: BigQuery datasets (tables, views, materialized views, external tables), ML models, routines (UDFs, stored procedures), Pub/Sub topics (streaming data).
- **Tooling**: Cloud Console GUI, REST API, gcloud CLI, Terraform/Pulumi, Python SDK, Producer Portal.
- **Free listing effort**: Under an hour. Create exchange, create listing, configure metadata, publish.
- **Commercial listing effort**: Significantly more — Partner Advantage onboarding, payment profile, tax docs, Producer Portal setup, pricing config, review cycle.

### Other Notable Terms

- **No exclusivity** — but feature-parity required (Marketplace listing cannot be stripped-down vs. other channels).
- **Data egress controls**: Can restrict copying, exporting, cloning of shared data.
- **Subscriber monitoring**: Can log subscriber identities running queries on shared data.
- **Max 1,000 subscribers per listing** (could constrain scale).
- **Region-locked exchanges** (same region as dataset; cross-region in preview).
- **No PII** per Protecting Americans' Data from Foreign Adversaries Act of 2024.
- **Maturity concern**: Described as "underrated" with lower discoverability than Snowflake/AWS. Smaller commercial ecosystem.

---

## 5. Narrative.io

### Payment Terms

- **Platform fee: 0% from seller.** The ~25% transaction fee is charged to the **buyer** on top of the seller's price. Example: seller lists at $80, buyer pays $100 (= $80 + 25% platform fee).
- **Seller receives 100% of their stated CPM price.**
- **Platform usage fees (separate)**: Storage (TB-hours/month), processing (bytes processed/month), and transaction services (% of licensed data fees). **Rates not publicly disclosed** — must contact sales.
- **Pricing models**: CPM (cost per thousand records, primary model), direct deals (custom offline terms), zero-cost data streams (free samples).
- **Payout timing**: Not publicly documented. Revenue appears in monthly usage reports.

### Approval Process

- **Self-service, no formal approval gate.** Sign up, ingest data, create products, start selling.
- No documented minimum data volume or revenue thresholds.
- Sellers are responsible for their own regulatory compliance.
- Platform provides column-level PII protection and compliance questionnaire tools.

### Ease of Publishing

- **Formats**: Parquet (recommended), JSON Lines, CSV. Uploaded to managed S3 bucket.
- **Tooling (no-code)**:
  - **Dataset Manager**: Upload, auto-validate, schema inference, field configuration.
  - **Seller Studio**: Package data into buyable products, set CPM, configure access rules.
  - **Shop Builder**: Custom-branded storefront with own domain, colors, SEO, Google Analytics.
- **Time to market**: Narrative claims "fully-realized data business in a few hours" and a Data Shop "up and running in an hour or less."
- **Dual listing**: Products appear on both central Data Streams Marketplace and seller's branded Data Shop.

### Other Notable Terms

- **No exclusivity** — non-exclusive license, multi-platform distribution allowed.
- **Data ownership**: "Narrative neither buys nor sells data." Pure software platform. Sellers retain full ownership.
- **Default license**: 30-day omni-use license for buyers. Custom terms via Direct Deals.
- **No geographic restrictions** found.
- **Data-type agnostic**: Agricultural, financial, healthcare, industrial, geolocation, demographic, etc.
- **Buyer lock-in**: Low — Narrative is platform-agnostic. Connectors to The Trade Desk, Snowflake, etc.
- **Maturity note**: Platform originated in adtech/identity data. Broader data types now supported but existing ecosystem skews toward audience/identity data.
- **Key unknowns**: Exact storage/processing rates, payout schedule, whether buyer transaction fee is negotiable.

---

## Analysis & Recommendations

### Revenue to Provider (Best → Worst)

| Rank | Platform | Effective Provider Revenue | Notes |
|------|----------|---------------------------|-------|
| 1 | Snowflake | **100%** | 0% fee (for now). Best margins but may change. |
| 2 | Databricks | **100%** | 0% fee, but you handle your own billing. |
| 3 | Narrative.io | **100% of listed price** | Buyer pays the 25% on top. But opaque platform usage fees. |
| 4 | Google Analytics Hub | **97–98.5%** | 2–3% fee, tiered by deal size. |
| 5 | AWS Data Exchange | **97–98.5%** | 3% public, tiered for private. Plus infra costs. |

### Ease of Entry (Easiest → Hardest)

| Rank | Platform | Barrier | Notes |
|------|----------|---------|-------|
| 1 | Narrative.io | Self-service | No approval gate. But need to set up S3 + schemas. |
| 2 | AWS Data Exchange | Moderate | Registration + undefined qualification review. |
| 3 | Snowflake | Moderate | Fast for free listings. Paid requires go-to-market vetting. |
| 4 | Databricks | Moderate | Partner program review (days–weeks). |
| 5 | Google Analytics Hub | High (commercial) | Partner Advantage + 2–4 week review. Low for free. |

### Buyer Reach (Largest → Smallest)

| Rank | Platform | Buyer Pool | Notes |
|------|----------|-----------|-------|
| 1 | AWS Data Exchange | AWS customers (millions) | Largest cloud customer base. But "limited organic traffic" reported. |
| 2 | Snowflake | Snowflake customers (~10K+) | Strong enterprise presence. MCD reduces buyer friction. |
| 3 | Databricks | Databricks customers + Delta Sharing | Open protocol expands reach beyond Databricks users. |
| 4 | Google Analytics Hub | BigQuery/GCP customers | "Underrated" — lower adoption for data commerce. |
| 5 | Narrative.io | Platform users (niche) | Smaller, skews adtech. But platform-agnostic distribution. |

### Key Takeaway

**None of the 5 marketplaces require exclusivity.** A multi-marketplace strategy is fully viable — the same dataset can be listed on all five simultaneously. The three cloud marketplaces (AWS, Snowflake, Databricks) are the most strategically important for reaching enterprise buyers, with Snowflake currently offering the best provider economics (0% fee + MCD program). Narrative.io is worth considering as a supplementary channel for its self-service model and branded storefront capability, especially if expanding beyond cloud-native buyers.
