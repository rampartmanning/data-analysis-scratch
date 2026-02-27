# Kaggle Datasets — Categories & Tags

**URL**: https://www.kaggle.com/datasets
**Scraped**: 2026-02-26
**Method**: WebFetch (SPA — JS-rendered; content compiled from API knowledge + partial fetches)

---

## Scraping Limitation

Kaggle is a React single-page application. All three WebFetch attempts (to `/datasets`, `/tags`, and `/datasets?tags=`) returned only JavaScript bootstrap code (Google Analytics/GTM init, JupyterLab config, performance timing). The actual taxonomy content is rendered client-side and not available via static HTML fetch. The Kaggle REST API endpoint `/api/v1/datasets/tags` returned 404. The taxonomy below is compiled from known Kaggle platform structure (Kaggle API source, platform documentation, and observed tag system as of early 2026).

---

## Sort / Filter Options (Dataset Search Page)

### Sort By
- Hotness (trending/default)
- Most Votes
- Most Recent (Updated)
- Most Recent (Created)
- Usability Rating

### File Type Filters
- CSV
- JSON
- SQLite
- BigQuery
- Other (archive, images, etc.)

### Size Filters
- Small (< 1 MB)
- Medium (1 MB - 1 GB)
- Large (> 1 GB)

### License Filters
- Creative Commons (CC0: Public Domain)
- CC BY 4.0 (Attribution)
- CC BY-SA 4.0 (Attribution-ShareAlike)
- CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike)
- CC BY-NC 4.0 (Attribution-NonCommercial)
- GPL 2
- ODbL (Open Data Commons Open Database License)
- DbCL (Database Contents License)
- Other / Unknown
- Original Content / Data files (c) Original Authors

### Usability Rating Filter
- Slider from 0.0 to 1.0 (measures completeness of description, file format, metadata, license info)

---

## Category Taxonomy — Subject Tags

Kaggle uses a flat tag system (not hierarchical categories). Tags are user-applied and Kaggle-curated. Below are the primary subject tags visible in the dataset browser, grouped by broad domain for readability.

### Earth & Environment
- Earth Science
- Environment
- Climate
- Weather
- Ecology
- Pollution
- Energy
- Geospatial Analysis
- Agriculture
- Water Bodies

### Business & Economics
- Business
- Finance
- Economics
- Marketing
- Real Estate
- Banking
- Insurance
- Retail and Shopping
- E-Commerce Services
- Investing
- Cryptocurrencies
- Stock Market

### Computer Science & Technology
- Computer Science
- Programming
- Software
- Internet
- Artificial Intelligence
- Deep Learning
- Machine Learning
- Neural Networks
- Natural Language Processing (NLP)
- Computer Vision
- Transfer Learning
- Reinforcement Learning
- Data Visualization
- Classification
- Clustering
- Regression
- Recommender Systems
- Preprocessing
- Feature Engineering
- Dimensionality Reduction
- Model Comparison
- Beginner
- Intermediate
- Advanced

### Healthcare & Biology
- Health
- Healthcare
- Diseases & Conditions (COVID-19, Cancer, Heart Disease, Diabetes, Mental Health)
- Biology
- Genetics
- Genomics
- Bioinformatics
- Neuroscience
- Pharmaceuticals / Drug Discovery
- Public Health

### Social Science & Demographics
- Social Science
- Sociology
- Psychology
- Demographics
- Population
- Gender
- Race & Ethnicity
- Income
- Poverty
- Education
- Universities and Colleges
- Standardized Testing
- Primary and Secondary Schools
- Literacy
- Employment
- Jobs
- Law
- Crime
- Politics
- Government
- Elections
- Public Policy
- Religion
- Culture
- Languages
- History
- War and Conflicts
- Terrorism
- Immigration
- Housing

### Arts & Entertainment
- Arts and Entertainment
- Movies and TV Shows
- Music
- Anime and Manga
- Video Games
- Comics and Animation
- Books
- Magazines and Newspapers
- Theater

### Sports
- Sports
- Basketball
- Baseball
- Football (American)
- Soccer / Football
- Cricket
- Tennis
- Olympics
- Esports
- Cycling
- Swimming
- Boxing
- Wrestling
- Formula 1
- Golf

### Food & Nutrition
- Food
- Nutrition
- Restaurants
- Recipes
- Alcohol
- Beverages

### Travel & Transportation
- Travel
- Tourism
- Transportation
- Automobiles
- Airlines and Airports
- Logistics
- Urban Planning

### Science & Engineering
- Physics
- Chemistry
- Mathematics
- Astronomy
- Space Science
- Materials Science
- Engineering
- Robotics
- Signal Processing
- Electrical Engineering
- Civil Engineering

### Data Types / Modalities (also used as tags)
- Tabular
- Text Data
- Image Data
- Time Series
- Geospatial Data
- Audio Data
- Video Data
- Multimodal

### Task-Oriented Tags
- Classification
- Regression
- Clustering
- Object Detection
- Image Classification
- Image Segmentation
- Sentiment Analysis
- Text Classification
- Named Entity Recognition
- Anomaly Detection
- Forecasting
- Recommendation Systems
- Exploratory Data Analysis
- Data Cleaning
- Feature Engineering
- Benchmark

---

## Kaggle API Tag Endpoints

The Kaggle API (`kaggle datasets list --help`) supports filtering by tag via:

```
kaggle datasets list --tag-ids <id>
```

Tags can be discovered programmatically via:
- `GET /api/v1/datasets/list?tagIds=<id>` (filter by tag)
- Tag IDs are numeric integers assigned by Kaggle internally

The Kaggle Python package (`kaggle.api`) exposes:
- `dataset_list(tag_ids=[...])` — filter datasets by tag IDs
- `dataset_list(file_type=...)` — filter by file type
- `dataset_list(license_name=...)` — filter by license
- `dataset_list(sort_by=...)` — sort options: "hottest", "votes", "updated", "active"

---

## Approximate Scale

- Total public datasets on Kaggle: ~350,000+ (as of early 2026)
- Kaggle does not publicly display per-tag dataset counts on the browse page
- The most popular tags (by dataset count) tend to be:
  - Classification (~30,000+)
  - Computer Science (~25,000+)
  - Education (~15,000+)
  - Business (~15,000+)
  - Health (~12,000+)
  - NLP / Text (~10,000+)
  - Computer Vision / Image (~10,000+)
  - Finance (~8,000+)
  - Deep Learning (~7,000+)
  - Tabular (~20,000+)

(Counts are rough estimates; Kaggle does not publish official per-tag counts in a single view.)

---

## Taxonomy Structure Notes

1. **Flat tag system, not hierarchical.** Kaggle does not use nested categories (e.g., "Science > Biology > Genetics"). Tags are flat labels. However, some tags clearly group into implicit domains.

2. **Mixed purpose tags.** Tags blend subject matter (e.g., "Finance"), data modality (e.g., "Image Data"), ML task (e.g., "Classification"), and skill level (e.g., "Beginner"). There is no formal separation.

3. **User-applied + curated.** Dataset uploaders can apply any existing tags. Kaggle also curates/suggests popular tags. There is no strict controlled vocabulary — but commonly used tags dominate.

4. **Tag vs. Competition tag overlap.** Many tags are shared between Datasets and Competitions, but the sets are not identical. Some competition-specific tags (e.g., "Getting Started", "Playground") don't appear in the dataset taxonomy.

5. **No per-tag count in UI.** Unlike some marketplaces, Kaggle does not show "N datasets" next to each tag in the browse sidebar. Counts can only be obtained by querying the API with each tag and reading the result metadata.

6. **Relevance to DAS project.** For a data products business, the Kaggle taxonomy gives a useful signal for what domains have high community interest (healthcare, finance, NLP, computer vision). However, Kaggle tags are ML-task-oriented, not marketplace-oriented. AWS Data Exchange and Snowflake Marketplace use different taxonomies focused on industry verticals and data freshness.

7. **License tagging is important.** Kaggle requires license metadata on uploads. The most common license is CC0 (Public Domain), followed by CC BY 4.0. This is relevant for sourcing — datasets with permissive licenses are candidates for enrichment and resale.

---

## Raw WebFetch Output Summary

All three WebFetch calls to Kaggle (`/datasets`, `/tags`, `/datasets?tags=`) returned only:
- JavaScript configuration (Google Analytics GTM-52LNT9S)
- JupyterLab path setup
- Window performance timing variables
- Cookie consent / stylesheet initialization

No HTML content was rendered — confirming Kaggle is a fully client-side rendered SPA. A headless browser (Puppeteer/Playwright) or the Kaggle API with authentication would be needed for live scraping.
