# DAS — Business Thesis

## Core Idea

There is unmet demand for **high-quality, reliable, ready-to-use data** on commercial data marketplaces. Public datasets exist in abundance, but they are messy, poorly documented, inconsistently formatted, stale, and require significant effort before they are useful for analytics or ML. The opportunity is to build an **automated data factory** that transforms publicly available data into polished, enriched, continuously refreshed data products — and distribute them where buyers already shop.

## The Problem

Data scientists and analytics teams waste enormous time on data wrangling:

- Public sources are messy (inconsistent schemas, missing values, encoding issues, mixed formats)
- Documentation is absent or outdated
- Delivery formats are whatever the source happened to use (PDFs, HTML tables, shapefiles, XML feeds, flat files)
- Refresh is manual or unreliable — many "open data" portals go months between updates
- There is no geocoding, enrichment, or cross-referencing across sources
- Data is never ML-ready out of the box

## The Business

Build a data products company that takes raw public data and delivers it as **premium, marketplace-ready data products**. The value chain:

```
Raw Public Data → Ingest → Clean → Document → Enrich → Format → Publish → Refresh
```

### Value-Add Layers

| Layer | Description |
|---|---|
| **Messy → Clean** | Schema normalization, deduplication, missing value handling, encoding fixes, type enforcement |
| **Documentation** | Comprehensive data dictionaries, field descriptions, lineage, quality scores, sample queries |
| **Format Diversity** | Ingest anything (PDF, HTML, shapefile, XML, API, etc.) — output in every format buyers want (Parquet, CSV, JSON, Delta, Iceberg, etc.) |
| **Frequent Refresh** | Automated pipelines that detect and pull source updates on a reliable cadence |
| **Geocoding** | Lat/lon enrichment, address standardization, geospatial joins |
| **Field Enrichment** | Cross-reference and augment with related public sources, derived fields, categorizations |
| **ML-Ready Forms** | Feature-engineered tables, train/test splits, embedding-ready text, normalized numerics |
| **Agent-Ready** | Data exposed via MCP servers and tool-friendly APIs so AI agents can discover, query, and reason over datasets programmatically |
| **Quality & Support** | Data quality monitoring, SLAs on freshness, responsive support |

### Unique / Composite Datasets

Beyond cleaning existing public data, there is an opportunity to **aggregate and combine multiple public sources** into new, unique datasets that don't exist anywhere else. Methods include:

- Joining disparate public datasets on common keys (geography, time, entity)
- Web scraping of structured public information
- FOIA requests for government data not yet digitized
- API aggregation from multiple providers
- Any legal method of collection that produces a differentiated product

## Distribution

### Data Marketplaces (Human Buyers)

Enterprise buyers already have procurement workflows on these platforms:

- **AWS Data Exchange**
- **Snowflake Marketplace**
- **Databricks Marketplace**
- Other similar platforms as they emerge

Pricing follows whatever models each marketplace supports natively — the research should clarify what works best on each platform.

### Agent-Ready Distribution (AI Consumers)

The next wave of data consumption is not humans browsing catalogs — it's **AI agents autonomously discovering and using data** to complete tasks. This is a parallel distribution channel that the same cleaned, documented, enriched data products can serve:

- **MCP Servers** — Expose each dataset (or the full catalog) as a Model Context Protocol server. Agents running in Claude, Cursor, or any MCP-compatible host can discover available datasets, read schemas, query rows, and pull slices — all without a human in the loop.
- **Tool-Use APIs** — Lightweight REST or GraphQL endpoints designed for LLM tool-use patterns: structured schemas, predictable pagination, field-level documentation that fits in a system prompt.
- **Semantic Discovery** — Rich metadata and embeddings so agents can search across the catalog by meaning ("find me monthly unemployment data by US county") rather than by knowing exact table names.
- **Context-Window Friendly** — Pre-computed summaries, statistics, and sample rows that let an agent understand a dataset without pulling the entire thing into context.

This matters because:

1. **The same quality work applies** — clean schemas, strong documentation, consistent formats, and enrichment are *exactly* what makes data agent-consumable. No separate product is needed.
2. **New monetization surface** — usage-based pricing per query/call via MCP or API, complementing marketplace subscriptions.
3. **Defensible position** — most public data is not agent-ready today. Being early to expose high-quality data via MCP creates a moat as agent adoption grows.
4. **Compounding value** — agents that find reliable data from a source will be configured to return to it. Trust and consistency drive recurring usage.

## Approach

### Domain-Agnostic

Follow the data, not a vertical. The best public datasets span many domains (government, environmental, economic, transportation, health, etc.). Start where data quality uplift is highest and demand is clearest, then expand.

### Global Scope

No geographic restriction on the data itself. Source from any country or international body where quality public data exists.

### Automated Factory Model

The core technical asset is a **reusable, automated pipeline infrastructure** that can onboard new public data sources quickly:

- Automated ingestion from diverse source formats
- Configurable cleaning and transformation stages
- Automated documentation generation
- Multi-format output targeting
- Scheduled refresh and quality monitoring
- Minimal manual intervention per dataset

The goal is that adding a new data source is a configuration task, not a development project.

### Infrastructure

AWS-preferred for pipeline infrastructure, aligning with AWS Data Exchange as a primary marketplace.

## Launch Plan

### Phase: Research (Current)

- Understand the data marketplace landscape (fees, formats, listing requirements, pricing models, competition)
- Identify high-potential public datasets (quality of raw source × demand × transformation effort)
- Survey what's already listed on marketplaces — find the gaps
- Understand buyer personas and what they actually pay for
- Clarify the competitive moat through research

### Phase: Prototype

- Build automated pipelines for ~10-20 initial datasets
- List on one or two marketplaces
- Stand up an MCP server for the same catalog (agent-ready from day one)
- Validate demand and pricing across both human and agent channels

### Phase: Scale

- Expand catalog
- Add marketplaces
- Build composite/unique datasets
- Expand MCP server capabilities (semantic search, cross-dataset joins)
- Optimize based on sales and usage data from both channels

## Open Questions (To Research)

1. **Marketplace mechanics** — What are the listing requirements, revenue splits, and supported formats for each marketplace?
2. **Competitive landscape** — Who else is doing this? What do they charge? Where are the gaps?
3. **Pricing** — What pricing models work on each platform? What do buyers actually pay for data products?
4. **High-value sources** — Which public datasets have the most transformation potential and buyer demand?
5. **Moat** — Is the moat in quality, freshness, breadth, enrichment, or the full stack? What do buyers value most?
6. **Legal/licensing** — What are the redistribution rights for various public data sources?
7. **Technical architecture** — What's the optimal pipeline architecture for the automated factory model on AWS?
8. **Agent distribution** — What does the MCP server ecosystem look like today? What patterns exist for exposing structured data to AI agents? What's the monetization model for agent-consumed data?
9. **Agent demand signals** — What data are AI agents (coding assistants, research bots, autonomous workflows) most frequently seeking and failing to find today?
