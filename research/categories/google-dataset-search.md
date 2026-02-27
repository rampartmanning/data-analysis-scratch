# Google Dataset Search — Categories

**URL**: https://datasetsearch.research.google.com
**Scraped**: 2026-02-26
**Method**: WebSearch + WebFetch of Google News Initiative guide (the search tool itself is a JS SPA, not scrapable)

## Category Taxonomy

Google Dataset Search is a **meta-search engine**, not a marketplace. It indexes datasets across the web using Schema.org/DCAT metadata. Its taxonomy is expressed through search filters rather than browse categories.

### Filter Dimensions

#### Topic
- Social Sciences
- Life Sciences
- (Additional topics likely available — the filter is populated dynamically from indexed dataset metadata; these two are the ones documented in guides)

#### Download Format
- Table
- Text
- Image
- Other

#### Usage Rights
- Commercial use
- Noncommercial use

#### Last Updated
- Past month
- Past year
- Past three years

#### Free
- Toggle: show only free datasets

### Underlying Schema
Google Dataset Search indexes based on **Schema.org Dataset markup** and **DCAT metadata** that publishers add to their pages. The taxonomy is therefore emergent — it reflects what publishers tag, not a predefined category list.

Key Schema.org properties indexed:
- `name` — dataset name
- `description` — dataset description
- `keywords` — topic tags
- `creator` / `publisher` — who created it
- `license` — usage rights
- `distribution` — download format, URL
- `temporalCoverage` — time range
- `spatialCoverage` — geographic coverage
- `dateModified` — last updated
- `variableMeasured` — what the data measures

## Scale
- ~25+ million datasets indexed across the web
- Indexes from government portals, academic repositories, commercial platforms, and any site with Schema.org markup

## Notes

- **Not a marketplace** — Google Dataset Search is a discovery/search engine, not a place to buy or download data
- The filter taxonomy is **extremely minimal** compared to actual marketplaces (only ~5 filter dimensions)
- Topic filter appears to have very few values — likely just broad disciplinary categories
- The real "taxonomy" is Schema.org metadata — what publishers choose to tag
- Most useful for understanding what **search terms** people use to find datasets, rather than for category intelligence
- No dataset counts per category are visible
- Launched 2018, exited beta 2020
- Value for DAS: less useful for category taxonomy mining than actual marketplaces, but useful for understanding discoverability and SEO for data products
- Source: https://newsinitiative.withgoogle.com/resources/trainings/dataset-search-quickstart-guide/
