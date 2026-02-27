# Databricks Marketplace — Categories

**URL**: https://marketplace.databricks.com/
**Scraped**: 2026-02-26
**Method**: WebFetch of docs + WebSearch (marketplace.databricks.com is a JS SPA, not directly scrapable)

## Category Taxonomy

### Product / Asset Types
Databricks Marketplace organizes listings first by what TYPE of asset it is:

1. **Datasets** — tabular data delivered as Unity Catalog tables
2. **Non-tabular data** — delivered via Databricks Volumes (files, images, etc.)
3. **Databricks Notebooks** — code/analysis notebooks
4. **Solution Accelerators** — clonable Git repos with pre-built solutions
5. **Machine Learning (AI) Models** — pre-trained ML models (MLflow format)
6. **Model Context Protocol (MCP) Servers** — AI agent tool servers

### Industry / Domain Categories (from marketplace browse filters)
Based on provider listings and blog posts, the following industry categories are used:

- Advertising & Marketing
- Financial Services / Financial & Economic Analysis
- Healthcare & Life Sciences
- Geospatial & Real Estate
- Manufacturing
- Media & Entertainment
- Retail & CPG
- Technology & Software
- Communications
- Public Sector / Government

### Pricing Categories
- Free
- Paid

### Listing Access Models
- **Public marketplace listings** — visible to all
- **Private exchange listings** — visible only to invited consumers
- **Instant access** — upon request and terms agreement
- **Provider approval required** — with transaction completion

### Data Access Methods
- Unity Catalog-enabled workspaces (native Databricks)
- External platforms (Power BI, pandas, Apache Spark via Delta Sharing)
- Non-Unity Catalog workspaces (legacy)

## Scale
- ~1,500+ listings (as of early 2025, growing)
- 150+ providers

## Notes

- The marketplace is a **JS SPA** — direct scraping returned only bootstrap code; categories were reconstructed from documentation, blog posts, and web search
- Databricks uses a **dual taxonomy**: asset type (dataset vs. notebook vs. model) AND industry/domain category
- The asset type dimension is unique among data marketplaces — competitors focus mainly on data, while Databricks also shares code, models, and solution accelerators
- **Delta Sharing** (open protocol) is the key differentiator — consumers don't need a Databricks account
- The industry categories are not formally documented as an enum (unlike Snowflake's manifest reference)
- Category list may be incomplete — the actual marketplace UI likely has more filter values than what appears in documentation
- Source: https://docs.databricks.com/aws/en/marketplace/
