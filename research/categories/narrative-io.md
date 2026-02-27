# Narrative.io — Categories

**URL**: https://www.narrative.io
**Scraped**: 2026-02-26
**Method**: WebSearch (narrative.io is a Nuxt.js SPA, not directly scrapable via WebFetch)

## Category Taxonomy

Narrative.io is a **programmatic data commerce platform** rather than a traditional browse-and-buy marketplace. Its taxonomy is organized around **data attributes** (columns/fields) rather than dataset topics.

### Core Data Type Categories
Based on knowledge base and search results, Narrative organizes data into these primary types:

1. **Identity Data**
   - Hashed Email addresses
   - Phone Numbers
   - UID2s (Unified ID 2.0)
   - MAIDs (Mobile Advertising IDs)
   - Cookies
   - IP Addresses
   - ID Mapping (cross-device/cross-identifier linkage)

2. **Location / Geolocation Data**
   - Anonymized first-party consented geo-location
   - Latitude/longitude coordinates
   - Store visit / competitor location data
   - Refined polygon geofence data

3. **Purchase / Transaction Data**
   - Purchase history
   - Specific items purchased
   - Item categories
   - Brands
   - Vendors
   - Spending patterns

4. **Demographic Data**
   - Age
   - Gender
   - Income
   - Household composition

5. **Device Data**
   - Device type
   - OS
   - App usage data
   - Mobile device signals

6. **Audience / Behavioral Data**
   - Interest segments
   - Intent signals
   - Behavioral profiles

### Data Commerce Model
Narrative's unique approach:

- **Data Streams** — data is divided into "streams" which are specific sets of attributes pulled from a dataset
- **Attribute-level purchasing** — buyers select specific fields/columns, not whole datasets
- **NQL (Narrative Query Language)** — proprietary query language for cross-provider data selection
- **Data Shops** — turnkey e-commerce storefronts for data sellers
- **Taxonomy Management** — providers create and manage custom taxonomies for their data

### Taxonomy System
- Providers define their own taxonomies via the Taxonomy Management interface
- Tags are used to categorize data and make it discoverable to buyers
- Rosetta Stone identity resolution links data across providers

### Trade Desk Connector Data Types
For advertising activation specifically, Narrative supports:
- Hashed Email
- Phone Number
- UID2s
- MAIDs
- Cookies

## Scale
- Billions of data points available
- Growing provider network
- Focused on programmatic data commerce

## Notes

- **Attribute-first taxonomy** — unlike browse-by-topic marketplaces, Narrative organizes by data attributes (columns/fields)
- This is fundamentally different from AWS/Snowflake/Databricks — those are "browse datasets by category" while Narrative is "query across providers by attribute"
- Strong **identity/AdTech focus** — the core data types reflect advertising and marketing use cases
- Provider-defined taxonomies mean there is no single universal category list
- The NQL query language and attribute-level purchasing are unique differentiators
- Less useful for understanding "what categories of data exist" and more useful for understanding "what attributes/fields data buyers want"
- Sources: https://www.narrative.io/knowledge-base/concepts/data-terms/narrative-data-types, https://www.narrative.io/knowledge-base/concepts/data-terms/what-is-id-mapping-data
