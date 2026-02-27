# Databricks Marketplace — Provider / Seller Terms

**Researched**: 2026-02-27
**Sources**: Databricks official docs, blog posts, Bobsled guide, Microsoft Learn (Azure Databricks docs)

---

## 1. Payment Terms to Data Provider

### Revenue Split: Databricks Takes 0%

**Databricks does not take a cut of provider revenue.** This is the single most important commercial fact: all commercial transactions happen directly between the provider and the consumer, outside of the Databricks platform. There is no listing fee, no transaction fee, and no revenue share.

- **No built-in payment processing**: As of the latest documentation (2025-2026), Databricks Marketplace does not process payments. The platform facilitates discovery and data delivery only. All financial transactions use the provider's own communications and payment platforms.
- **No listing fees**: Providers pay nothing to Databricks for the privilege of listing products on the Marketplace.
- **Provider-managed billing**: Providers negotiate pricing, contracts, and payment terms directly with each consumer. Databricks explicitly states that "data product sales are often highly customizable and shouldn't be forced into a standardized out-of-the-box pricing model."

### How Providers Get Paid

1. Consumer discovers the listing on Databricks Marketplace
2. Consumer clicks "Request access" on a paid/approval-required listing
3. Provider receives the request in their Provider Console
4. Provider and consumer negotiate terms offline (email, provider's sales process, etc.)
5. Once commercial transaction is complete, provider marks the request as "Fulfilled" in the console
6. Databricks provisions the data access via Delta Sharing

This means: **providers must have their own billing infrastructure** (or use a third-party billing service). Databricks is a lead-generation and delivery channel, not a transactional marketplace.

### Pricing Models Available

Listings support two access models that map to pricing:

| Access Model | Pricing | How It Works |
|---|---|---|
| **Instant Access** | Free / sample data | Consumer gets immediate access upon accepting ToS. No provider approval needed. Must include a Delta Share in the listing. |
| **Request Access** | Paid / commercial | Consumer requests access; provider reviews, negotiates terms offline, then fulfills. No share required upfront. |

There are no built-in subscription tiers, usage-based pricing, or per-seat licensing models within the platform itself. All of that is handled in the provider's own commercial agreements.

### Implication for Our Business

This is attractive from a margin perspective (0% marketplace take rate) but means we must build and manage our own billing/subscription infrastructure. Unlike AWS Data Exchange (which handles payments and takes 20-30%), Databricks is purely a distribution and delivery mechanism.

---

## 2. Approval Process to Become a Provider

### Two Pathways

#### Path A: Public Marketplace Provider (Full Listing Capability)
1. Go to the [Databricks Data Partner Program](https://www.databricks.com/partners/data-partner-program) page
2. Click "Apply Now" then "Apply here as a new provider"
3. Enter email address and fill out the application form, selecting "Databricks Data Provider"
4. The Databricks Partner team reviews the application and reaches out to complete onboarding
5. Upon approval, the **Provider Console** becomes available in Unity Catalog-enabled workspaces

**Requirements:**
- Databricks account on **Premium plan or above**
- Workspace enabled for **Unity Catalog**
- Agreement to Marketplace provider policies
- Provider profile: name, logo, description, website, business email, support contact, terms of service link, privacy policy link

**Timeline:** Not publicly disclosed. The documentation says "the Databricks Partner team will reach out to you to complete the application process." Anecdotally, this appears to be a manual review process. No SLA is published. Expect **days to weeks** depending on Databricks partner team capacity. Organizations already in the Databricks Partner Program should contact partnerops@databricks.com for faster processing.

#### Path B: Private Exchange Only (Self-Service)
- Available without going through the full Data Partner Program
- As a Databricks account admin, go to Marketplace > Provider Console > "Get started as a provider"
- Agree to Private Exchange provider terms and complete setup directly in-product
- **No external approval needed** — self-service onboarding
- Listings are only visible to invited exchange members (not the public marketplace)

### Provider Profile Requirements

Once approved, providers must create a profile including:
- Organization name ("use a name that consumers will recognize")
- Logo
- Organizational description
- Website URL
- Business email and support contact
- Links to terms of service and privacy policy

### Required Role
The **Marketplace admin** role is required to:
- Access the Provider Console
- Create and manage provider profiles
- Build and update listings
- Manage consumer requests

---

## 3. Ease of Publishing

### Supported Product Types

| Product Type | Description | Consumer Requirements |
|---|---|---|
| **Tables/Views** | Tabular data via Unity Catalog | Any consumer (including non-Databricks via Delta Sharing) |
| **Volumes** | Non-tabular data (files, images, etc.) | Unity Catalog-enabled workspace required |
| **AI/ML Models** | Pre-trained models (MLflow format) | Unity Catalog-enabled workspace required |
| **Notebooks** | Databricks notebooks (up to 10 per listing) | Unity Catalog-enabled workspace required |
| **Git Repositories** | Solution Accelerators as clonable repos | Unity Catalog-enabled workspace required |
| **Databricks Apps** | Runnable applications | Unity Catalog-enabled workspace required |
| **MCP Servers** | AI agent tool servers (public preview) | Unity Catalog-enabled workspace required |

**Key distinction**: Only tables/views can be consumed by non-Databricks users via Delta Sharing. All other asset types require the consumer to have a Databricks workspace.

### Supported Data Formats

- **Delta Lake** (native)
- **Apache Iceberg** (first-class support added in 2025 via Delta Sharing)
- Non-tabular data via Volumes (any file format)
- Delta Sharing supports the Apache Iceberg REST Catalog API, enabling recipients on Snowflake, Trino, Flink, and Spark to access shared data

### Technical Steps to Publish a Listing

1. **Set up Delta Sharing** on your Unity Catalog metastore (account admin enables "Allow Delta Sharing with parties outside your organization")
2. **Create a Share** — a Unity Catalog object containing a collection of tables, views, volumes, and/or AI models
3. **Create a Listing** in the Provider Console with:
   - Product name and description (Markdown supported)
   - Up to 5 categories
   - Optional attributes: geographic coverage, update frequency, data source, dataset size
   - For instant-access listings: attach the Delta Share
   - For approval-required listings: no share needed upfront (attached at fulfillment)
4. **Publish** — listing goes live immediately upon publication

### Effort Assessment

**Low-to-moderate** effort if you are already a Databricks customer:
- If data is already in Unity Catalog Delta tables, creating a share and listing is straightforward (minutes to hours)
- The Provider Console provides a GUI for listing management
- Markdown descriptions, category tagging, and sample notebooks enhance discoverability

**Moderate-to-high** effort if you are NOT a Databricks customer:
- Must provision and maintain a Databricks Premium workspace ($$$)
- Must set up Unity Catalog and Delta Sharing infrastructure
- Must load/maintain data in Delta Lake format
- The Bobsled guide notes: "infrastructure complexity for non-Databricks users" and "security configuration responsibility falls on providers"

### Listing Management

- Provider Analytics Dashboard tracks views, requests, installs, and conversion metrics
- System tables available for detailed analytics on consumer activity (public preview)
- Consumer requests are managed through the Provider Console (mark as pending, fulfill, or deny)
- Listings can be updated in real-time after publication

---

## 4. Other Notable Terms

### Provider Policies (Key Obligations)

- **One profile per provider** unless written approval from Databricks
- **Response SLAs**: 3 business days for access requests from prospective consumers; 5 business days for all other inquiries
- **Deliver as advertised**: Products must match their listing descriptions exactly
- **Notify on changes**: Must notify consumers of listing changes that affect them
- **Dataset freshness**: Must update at "the most frequent logical refresh rate"

### Content Restrictions

- **No Sensitive Personal Data**: "A Product must never include Sensitive Personal Data"
- **Personal Data requires authorization**: Must have legal authorization to share any personal data
- **Anonymized data must stay anonymous**: Even when combined with other datasets
- **No illegal, threatening, or offensive content**
- **No IP infringement**: Must own or have authorization for all content and trademarks
- **Notebooks must work**: Accompanying notebooks must function for all consumers and produce advertised results

### Exclusivity

- **No exclusivity requirement**: Databricks does NOT require exclusive listings. Providers are free to list the same data on other marketplaces (AWS Data Exchange, Snowflake Marketplace, etc.)
- **No non-compete**: There is no restriction on listing competing products or working with competing platforms

### Delisting and Discontinuation

- Providers may **delist at any time** (stops new consumer discovery)
- **Product discontinuation requires 30-day minimum notice** (or the provider's stated notice period, whichever is longer)
- Current consumers retain access through their current term after discontinuation

### Anti-Manipulation

- "Manipulation of your position in the Marketplace is expressly forbidden"
- Cannot impersonate or misrepresent affiliations
- Can only promote the listed product(s) within a listing

### Usage Data and Confidentiality

- Usage data shared by Databricks to providers is **confidential** and **internal-use only**
- Cannot be used for benchmarking
- Consumer personal data may only be used for marketing/selling products per the provider agreement and privacy policy

### Geographic Restrictions

- **No geographic restrictions on listings themselves**: Providers can set geographic coverage attributes on listings (metadata/filtering)
- Databricks operates across AWS, Azure, and Google Cloud in Americas, Europe, Asia, and India geos
- Marketplace appears to be available in all Databricks regions (not listed as a regionally restricted feature)

### Infrastructure Cost to Provider

- Providers must maintain a **Databricks Premium workspace** (not free)
- Data remains in the provider's cloud storage (no replication required for Databricks-to-Databricks sharing)
- Provider bears the compute cost for maintaining shares and serving Delta Sharing queries

---

## 5. Marketplace Scale and Growth Context

- **200+ providers** as of Q1 2024, growing to **230+ by Q2 2024**
- **1,900+ listings** in Q1 2024, growing to **2,200+ by Q2 2024**
- Q1 2024 alone added **42 new providers** and **200 new listings**
- Q2 2024 added **47 new providers**
- Notable providers include: Intercontinental Exchange, Shutterstock, HealthVerity, Epsilon
- Growth trajectory suggests **300+ providers** and **3,000+ listings** by early 2026

---

## Summary for Our Business Case

| Factor | Assessment |
|---|---|
| **Take rate** | 0% — Databricks takes nothing |
| **Listing fee** | $0 |
| **Payment handling** | Provider must handle (no built-in billing) |
| **Barrier to entry** | Moderate — need Databricks Premium + Unity Catalog + Partner Program approval |
| **Time to first listing** | Days to weeks (approval) + hours (listing creation if data is ready) |
| **Exclusivity** | None — can list on other platforms simultaneously |
| **Consumer reach** | Databricks-native users + any platform via Delta Sharing (for tables) |
| **Best for** | Reaching data science / ML / AI teams already on Databricks |
| **Key limitation** | No built-in monetization — must manage own billing |
| **Ongoing cost** | Databricks Premium workspace + cloud storage |

---

## Sources

- [Databricks Marketplace Overview (AWS docs)](https://docs.databricks.com/aws/en/marketplace/)
- [List your data product in Databricks Marketplace (AWS docs)](https://docs.databricks.com/aws/en/marketplace/get-started-provider)
- [Databricks Marketplace Provider Policies (AWS docs)](https://docs.databricks.com/aws/en/marketplace/provider-policies)
- [Manage requests for your data product (AWS docs)](https://docs.databricks.com/aws/en/marketplace/manage-requests-provider)
- [Databricks Marketplace Provider Policies (Azure docs)](https://learn.microsoft.com/en-us/azure/databricks/marketplace/provider-policies)
- [List your data product (Azure docs)](https://learn.microsoft.com/en-us/azure/databricks/marketplace/get-started-provider)
- [Databricks Marketplace (product page)](https://www.databricks.com/product/marketplace)
- [Databricks Data Partner Program](https://www.databricks.com/partners/data-partner-program)
- [Top 10 Marketplace Questions, Answered (Databricks Blog)](https://www.databricks.com/blog/top-10-marketplace-questions-answered)
- [42 New Data Providers in Q1 2024 (Databricks Blog)](https://www.databricks.com/blog/databricks-marketplace-welcomes-42-new-data-providers-q1-2024)
- [47 New Data Providers in Q2 2024 (Databricks Blog)](https://www.databricks.com/blog/databricks-marketplace-welcomes-47-new-data-providers-q2-2024)
- [Iceberg Format Support in Delta Sharing (Databricks Blog)](https://www.databricks.com/blog/announcing-first-class-support-iceberg-format-databricks-delta-sharing)
- [Private Exchanges (Databricks Blog)](https://www.databricks.com/blog/unlocking-potential-private-data-sharing-using-databricks-private-exchanges)
- [Guide: Sharing and Marketing Data Products on Databricks (Bobsled)](https://bobsled.com/resources/guide-sharing-data-databricks)
- [Delta Sharing Overview](https://docs.databricks.com/aws/en/delta-sharing/)
