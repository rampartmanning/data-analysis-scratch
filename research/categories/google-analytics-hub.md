# Google Cloud Analytics Hub / BigQuery Public Datasets — Categories

**URL**: https://cloud.google.com/analytics-hub, https://cloud.google.com/bigquery/public-data, https://cloud.google.com/datasets
**Scraped**: 2026-02-26
**Method**: WebFetch (SPA — most Google Cloud pages are client-side rendered; taxonomy compiled from API reference docs, Python SDK reference, and documentation pages)

---

## Scraping Limitation

Google Cloud product pages (analytics-hub, datasets, marketplace) are fully client-side rendered SPAs. WebFetch returns only JavaScript bootstrap/configuration code, not the rendered content. The Google Cloud Console marketplace page (console.cloud.google.com) requires authentication. The taxonomy below was compiled from:
- Python SDK reference: `google.cloud.bigquery_analyticshub_v1.types.Listing.Category` enum
- Analytics Hub documentation (introduction, manage-listings pages)
- BigQuery public data documentation
- Google Cloud Marketplace partner documentation

---

## Category Taxonomy — Analytics Hub Listing Categories

Analytics Hub uses a **flat enum-based category system**. When creating a listing, publishers can select **up to two categories** from the following predefined list. Subscribers can filter listings by these categories.

### Official Category Enum Values

Source: `google.cloud.bigquery_analyticshub_v1.types.Listing.Category` (Python SDK reference)

| # | Enum Value | Display Name (inferred) |
|---|-----------|------------------------|
| 1 | CATEGORY_UNSPECIFIED | (Unspecified / Default) |
| 2 | CATEGORY_OTHERS | Others |
| 3 | CATEGORY_ADVERTISING_AND_MARKETING | Advertising & Marketing |
| 4 | CATEGORY_COMMERCE | Commerce |
| 5 | CATEGORY_CLIMATE_AND_ENVIRONMENT | Climate & Environment |
| 6 | CATEGORY_DEMOGRAPHICS | Demographics |
| 7 | CATEGORY_ECONOMICS | Economics |
| 8 | CATEGORY_EDUCATION | Education |
| 9 | CATEGORY_ENERGY | Energy |
| 10 | CATEGORY_FINANCIAL | Financial |
| 11 | CATEGORY_GAMING | Gaming |
| 12 | CATEGORY_GEOSPATIAL | Geospatial |
| 13 | CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE | Healthcare & Life Science |
| 14 | CATEGORY_MEDIA | Media |
| 15 | CATEGORY_PUBLIC_SECTOR | Public Sector |
| 16 | CATEGORY_RETAIL | Retail |
| 17 | CATEGORY_SPORTS | Sports |
| 18 | CATEGORY_SCIENCE_AND_RESEARCH | Science & Research |
| 19 | CATEGORY_TRANSPORTATION_AND_LOGISTICS | Transportation & Logistics |
| 20 | CATEGORY_TRAVEL_AND_TOURISM | Travel & Tourism |
| 21 | CATEGORY_GOOGLE_EARTH_ENGINE | Google Earth Engine |

**Total user-facing categories: 19** (excluding CATEGORY_UNSPECIFIED and CATEGORY_OTHERS as functional/catch-all values)

---

## Analytics Hub Organizational Structure

Beyond categories, Analytics Hub organizes data through a multi-level hierarchy:

### Data Exchanges
- Top-level containers that group related listings
- Can be **public** (visible to all authenticated Google Cloud users) or **private** (restricted access)
- Created by Analytics Hub Admins

### Listings
- Individual data assets published within a data exchange
- Can be **public** (free or commercial, visible to all) or **private** (shared with specific users/groups)
- Each listing can have up to **2 categories** (per UI documentation) or up to **5 categories** (per API/SDK MutableSequence field)
- Listing metadata includes: display name, description, provider info, publisher info, icon, documentation

### Shared Resource Types
Listings can reference:
- **BigQuery datasets** (tables, views, materialized views, external tables, UDFs, stored procedures, ML models, table snapshots)
- **Pub/Sub topics** (streaming data)

### Discovery & Filtering Dimensions
Subscribers can discover listings by:
- **Category** (from the enum above)
- **Data provider name** (filterable)
- **Description search** (keyword-based)
- **Data exchange** (browse within an exchange)
- **Public vs. private** visibility

### User Roles
- Analytics Hub Admin
- Analytics Hub Publisher
- Analytics Hub Subscriber
- Analytics Hub Viewer

### Geographic Regions
Listings are region-specific. Available regions include:
- Americas
- Asia Pacific
- Europe
- Middle East
- Africa
- Multi-regions (EU, US)
- Omni regions (AWS, Azure cross-cloud)

---

## Google Cloud Marketplace — Dataset Integration

As of 2024-2025, Google Cloud Marketplace datasets are integrated with **BigQuery Sharing** (the rebranded Analytics Hub). Key facts:

- Data products listed on Cloud Marketplace are delivered through BigQuery Sharing (Analytics Hub)
- Providers must first create a listing in BigQuery Sharing, then connect it to a Cloud Marketplace config
- Marketplace configs include product details and pricing (free or subscription)
- Marketplace does not maintain a separate category taxonomy for datasets — it uses the Analytics Hub category system
- Compliance requirement: data products cannot contain personally identifiable sensitive information (per the Protecting Americans' Data from Foreign Adversaries Act of 2024)

### Marketplace Solution Type Filter
The Cloud Marketplace browse page supports a `solution-type:dataset` filter to show only dataset listings (as opposed to SaaS, VM images, Kubernetes apps, etc.)

---

## BigQuery Public Datasets

Google hosts a collection of public datasets in the `bigquery-public-data` project. These are available to all BigQuery users at no storage cost (query costs apply).

### Sample Datasets (in bigquery-public-data:samples)

| Dataset | Domain | Description |
|---------|--------|-------------|
| gsod | Weather | NOAA weather data: precipitation, wind speeds (1929-2010) |
| github_nested | Technology | GitHub repository actions timeline, nested schema (Sept 2012) |
| github_timeline | Technology | GitHub repository actions timeline, flat schema (May 2012) |
| natality | Demographics/Health | US births in 50 states + DC + NYC (1969-2008) |
| shakespeare | Literature | Word index of Shakespeare's works with frequency counts |
| trigrams | Linguistics | English language trigrams from published works (1520-2008) |
| wikipedia | Reference | Complete revision history for all Wikipedia articles (through April 2010) |

### Other Notable Public Datasets
- NIH Chest X-ray dataset (Healthcare)
- The Cancer Imaging Archive (TCIA) dataset (Healthcare/Imaging)
- Google Cloud release notes dataset (Technology/Reference)

### Access Methods
- Cloud Marketplace (primary browsing/discovery)
- BigQuery Console Explorer pane (direct access)
- Analytics Hub / BigQuery Sharing (data exchange)

**Note:** Google does not publish a comprehensive categorized directory of all BigQuery public datasets in their documentation. The full list is only browsable via the Cloud Console UI (client-side rendered, requires authentication) or the Cloud Marketplace. The documentation references "many more" datasets beyond the sample tables listed above.

---

## Industry Verticals Referenced Across Google Cloud Data Products

From the Analytics Hub introduction blog and product documentation, Google highlights these industry verticals for data sharing:

- Financial Services
- Healthcare & Life Sciences
- Manufacturing
- Media & Entertainment
- Public Sector
- Retail
- Supply Chain & Logistics
- Telecommunications

These align closely with the Analytics Hub category enum but are not identical (e.g., "Manufacturing" and "Telecommunications" do not have dedicated category enum values).

---

## Notes

1. **Small, flat taxonomy.** Analytics Hub uses only 19 user-facing categories (plus "Others" and "Unspecified"). This is deliberately minimal compared to Kaggle (~100+ tags) or AWS Data Exchange (~20 categories with subcategories). The design favors simplicity over granularity.

2. **Category limit discrepancy.** The manage-listings documentation states "up to two categories" per listing, while the Python SDK defines the `categories` field as a `MutableSequence` (list) suggesting up to 5. The UI likely enforces a stricter limit than the API.

3. **No subcategories.** The taxonomy is strictly one level deep. There are no nested or hierarchical categories. A healthcare dataset and a genomics dataset would both use `CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE`.

4. **Google Earth Engine is a special category.** `CATEGORY_GOOGLE_EARTH_ENGINE` is the only platform-specific category, suggesting Google Earth Engine datasets are a significant segment of Analytics Hub listings.

5. **Marketplace convergence.** Google Cloud Marketplace dataset listings now route through Analytics Hub (BigQuery Sharing), meaning the Analytics Hub category enum is effectively the taxonomy for all Google Cloud dataset marketplace offerings.

6. **No dataset counts available.** Google does not publicly expose how many datasets exist per category in Analytics Hub. Unlike AWS Data Exchange or Snowflake Marketplace, there is no publicly browsable directory with counts — the Console UI requires authentication.

7. **Comparison to competitor taxonomies.** The Analytics Hub categories map well to industry-standard data marketplace categories. Coverage gaps vs. competitors:
   - No explicit "Telecommunications" category (would fall under "Others")
   - No explicit "Manufacturing" category (would fall under "Others")
   - No explicit "Legal" or "Compliance" category
   - No explicit "Real Estate" or "Property" category
   - No explicit "Insurance" category
   - "Commerce" and "Retail" are separate categories (overlapping in practice)

8. **Relevance to DAS project.** For a data products business targeting Google Cloud, datasets should be tagged with 1-2 of the 19 Analytics Hub categories. The most commercially relevant categories are likely: Financial, Healthcare & Life Science, Geospatial, Demographics, Commerce/Retail, and Advertising & Marketing. The small taxonomy means less discoverability friction but also less differentiation by category alone — description quality and provider reputation matter more.

9. **Client-side rendering challenge.** All Google Cloud product pages (analytics-hub, datasets, marketplace browse) are fully client-side rendered SPAs. Static web fetching cannot extract the rendered content. A headless browser (Puppeteer/Playwright) or authenticated API access would be needed for live scraping of actual listing counts and details.
