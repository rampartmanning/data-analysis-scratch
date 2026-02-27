# Kaggle Repackaging Candidates

**Date**: 2026-02-27
**Method**: Kaggle CLI API — sorted by votes across thesis-aligned domains, filtered for CC0-equivalent licensing + staleness + enrichment potential
**Purpose**: Identify popular but under-maintained Kaggle datasets that can be repackaged as premium data products on paid marketplaces (AWS Data Exchange, Snowflake, Databricks)

---

## Selection Criteria

| Criterion | Signal |
|---|---|
| **License** | **CC0, CC-BY, DbCL, World Bank Open only** — must allow unrestricted commercial redistribution. No NC (Non-Commercial) or other restrictive licenses. |
| **Popularity** | High votes and downloads = proven demand |
| **Staleness** | Last updated >2 years ago = maintenance gap we can fill |
| **Enrichment potential** | Raw source exists, can add: schema normalization, geocoding, freshness, cross-referencing, ML-ready features |
| **Marketplace fit** | Enterprise buyers want this domain (finance, energy, environment, health, transportation, macro-economic, etc.) |

---

## 25 Candidates

### 1. Huge Stock Market Dataset (US Stocks & ETFs)

| Field | Value |
|---|---|
| **Kaggle ref** | `borismarjanovic/price-volume-data-for-all-us-stocks-etfs` |
| **URL** | https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs |
| **Votes / Downloads / Views** | 4,608 / 141k / 1.2M |
| **Last updated** | 2017-11-16 (8+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~516 MB |
| **Domain** | Finance |

**What it is**: Full historical daily OHLCV (open/high/low/close/volume) for all US-listed stocks and ETFs.

**Why it's a candidate**: 1.2M views. 8 years stale. Stock price data is high-value, refreshable from public sources (Yahoo Finance, SEC EDGAR). Enterprise buyers (hedge funds, fintech, analytics teams) pay for clean, current market data.

**Enrichment opportunity**:
- Daily auto-refresh pipeline from public sources
- Add sector/industry classification, market cap tiers
- Add corporate actions (splits, dividends) as separate table
- Add earnings dates, fundamental ratios
- Parquet + Delta Lake output formats
- Train/test split helper columns for ML

---

### 2. World Happiness Report

| Field | Value |
|---|---|
| **Kaggle ref** | `unsdsn/world-happiness` |
| **URL** | https://www.kaggle.com/datasets/unsdsn/world-happiness |
| **Votes / Downloads / Views** | 4,454 / 387k / 2.0M |
| **Last updated** | 2019-11-27 (6+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~38 KB |
| **Domain** | Social Science / Economics |

**What it is**: Country-level happiness scores and explanatory factors (GDP per capita, social support, life expectancy, freedom, generosity, corruption) from the UN SDSN.

**Why it's a candidate**: Nearly 2M views and 387k downloads. 6+ years stale despite the report being published annually. Small data, huge enrichment surface.

**Enrichment opportunity**:
- Annual auto-refresh (source report published each March)
- Merge all years into single time-series with consistent schema
- Join with World Bank indicators (GDP, population, Gini)
- Add ISO country codes, region/continent, lat/lon centroids
- Year-over-year change columns, rankings
- Cross-reference with WHO health data, education indices

---

### 3. Netflix Movies and TV Shows

| Field | Value |
|---|---|
| **Kaggle ref** | `shivamb/netflix-shows` |
| **URL** | https://www.kaggle.com/datasets/shivamb/netflix-shows |
| **Votes / Downloads / Views** | 9,721 / 721k / 3.9M |
| **Last updated** | 2021-09-27 (4+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~1.4 MB |
| **Domain** | Entertainment / Media |

**What it is**: Complete catalog of Netflix titles — movies and TV shows with cast, directors, ratings, release year, duration, country, genre.

**Why it's a candidate**: Kaggle's 2nd most popular dataset (3.9M views, 721k downloads). 4+ years stale. Streaming content metadata is valuable for media analytics, content strategy, and recommendation research.

**Enrichment opportunity**:
- Expand to multi-platform (Netflix + Disney+ + Hulu + Prime Video + HBO)
- Auto-refresh from public APIs (TMDb, OMDb, JustWatch)
- Add IMDb ratings, Rotten Tomatoes scores, box office data
- Add content availability by country/region
- Genre taxonomy normalization across platforms
- Viewing trend indicators, content age analysis

---

### 4. Trending YouTube Video Statistics

| Field | Value |
|---|---|
| **Kaggle ref** | `datasnaek/youtube-new` |
| **URL** | https://www.kaggle.com/datasets/datasnaek/youtube-new |
| **Votes / Downloads / Views** | 5,876 / 298k / 2.2M |
| **Last updated** | 2019-06-03 (6+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~211 MB |
| **Domain** | Digital Media / Marketing |

**What it is**: Daily trending video data across multiple countries — views, likes, dislikes, comments, tags, category, channel for trending YouTube videos.

**Why it's a candidate**: 2.2M views. Digital marketing and social media analytics is a growing enterprise data need. 6+ years stale but YouTube Data API v3 is public and provides this data.

**Enrichment opportunity**:
- Daily auto-refresh from YouTube Data API
- Expand country coverage
- Add channel-level metadata (subscriber count, total uploads)
- Sentiment analysis on comments
- Trend velocity scoring, virality metrics
- Cross-platform comparison (YouTube vs TikTok trending)

---

### 5. New York City Airbnb Open Data

| Field | Value |
|---|---|
| **Kaggle ref** | `dgomonov/new-york-city-airbnb-open-data` |
| **URL** | https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data |
| **Votes / Downloads / Views** | 3,093 / 237k / 1.4M |
| **Last updated** | 2019-08-12 (6+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~2.6 MB |
| **Domain** | Real Estate / Hospitality |

**What it is**: Airbnb listing data for NYC — price, location, room type, availability, reviews, host info.

**Why it's a candidate**: 1.4M views. Airbnb/short-term rental data is valuable for real estate investors, hospitality analytics, urban planning. Inside Airbnb continues publishing quarterly snapshots for many cities worldwide.

**Enrichment opportunity**:
- Expand from NYC to 50+ major cities globally (Inside Airbnb is CC0)
- Quarterly auto-refresh
- Add neighborhood demographics (census), walk score, transit access
- Price per sqft normalization, seasonal pricing patterns
- Occupancy rate estimation from review frequency
- Geocoded with H3 hex indices for spatial analysis

---

### 6. Hotel Booking Demand

| Field | Value |
|---|---|
| **Kaggle ref** | `jessemostipak/hotel-booking-demand` |
| **URL** | https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand |
| **Votes / Downloads / Views** | 2,668 / 206k / 1.4M |
| **Last updated** | 2020-02-13 (6 years stale) |
| **License** | CC-BY-4.0 |
| **Size** | ~1.3 MB |
| **Domain** | Hospitality / Revenue Management |

**What it is**: ~119k hotel booking records from two hotels (resort + city hotel) — booking dates, lead time, guest demographics, room type, cancellations, ADR, market segment.

**Why it's a candidate**: 1.4M views, 206k downloads. Revenue management and demand forecasting data is highly valuable for hospitality industry. CC-BY allows commercial use with attribution.

**Enrichment opportunity**:
- Expand with additional hotel booking datasets
- Add seasonal/event calendar features (holidays, conferences, weather)
- Cancellation prediction features
- Dynamic pricing benchmarking metrics
- Join with destination-level tourism statistics
- Format as time-series for demand forecasting models

---

### 7. House Sales in King County, USA

| Field | Value |
|---|---|
| **Kaggle ref** | `harlfoxem/housesalesprediction` |
| **URL** | https://www.kaggle.com/datasets/harlfoxem/housesalesprediction |
| **Votes / Downloads / Views** | 2,303 / 240k / 1.3M |
| **Last updated** | 2016-08-25 (9+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~798 KB |
| **Domain** | Real Estate |

**What it is**: ~21k house sales in King County (Seattle area) with price, bedrooms, bathrooms, sqft, condition, grade, year built, zip code, lat/lon.

**Why it's a candidate**: 1.3M views, 240k downloads — massive demand for real estate pricing data. 9+ years stale. County assessor and MLS data is publicly available in many US jurisdictions.

**Enrichment opportunity**:
- Expand to multiple metro areas (county assessor data is public in many US counties)
- Auto-refresh from public records
- Add school district ratings, crime rates, walkability
- Mortgage rate context (30-yr fixed at time of sale)
- Price per sqft, appreciation rates, comp analysis features
- Geocoded with census tract demographics

---

### 8. Hourly Energy Consumption (PJM)

| Field | Value |
|---|---|
| **Kaggle ref** | `robikscube/hourly-energy-consumption` |
| **URL** | https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption |
| **Votes / Downloads / Views** | 1,110 / 110k / 563k |
| **Last updated** | 2018-08-30 (7+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~12 MB |
| **Domain** | Energy |

**What it is**: Hourly power consumption from PJM Interconnection (major US grid operator, 13 states). Multiple regional sub-zones.

**Why it's a candidate**: Energy data is high-value for utilities, traders, climate tech, ESG. 7+ years stale, but PJM publishes hourly data publicly and continuously.

**Enrichment opportunity**:
- Auto-refresh from PJM Data Miner API
- Expand to other ISOs (ERCOT, CAISO, MISO, NYISO, ISO-NE)
- Add weather correlation (temperature, humidity per zone)
- Add LMP pricing data alongside consumption
- Seasonal decomposition, peak/off-peak flags
- Time-series forecasting features (lag, rolling, calendar)

---

### 9. S&P 500 Stock Data

| Field | Value |
|---|---|
| **Kaggle ref** | `camnugent/sandp500` |
| **URL** | https://www.kaggle.com/datasets/camnugent/sandp500 |
| **Votes / Downloads / Views** | 1,119 / 104k / 598k |
| **Last updated** | 2018-02-10 (8 years stale) |
| **License** | CC0-1.0 |
| **Size** | ~20 MB |
| **Domain** | Finance |

**What it is**: Daily OHLCV data for S&P 500 constituent stocks. Individual CSV per ticker.

**Why it's a candidate**: 598k views, 104k downloads, 8 years stale. S&P 500 is the benchmark index — clean, current data has enormous enterprise demand.

**Enrichment opportunity**:
- Daily auto-refresh from public sources
- Track index constituency changes over time
- Add GICS sector/industry classification
- Add market cap, P/E, dividend yield
- Total return calculations (adjusted for dividends/splits)
- Portfolio analysis and backtesting features

---

### 10. Hourly Energy Demand, Generation & Weather (Spain)

| Field | Value |
|---|---|
| **Kaggle ref** | `nicholasjhana/energy-consumption-generation-prices-and-weather` |
| **URL** | https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather |
| **Votes / Downloads / Views** | 416 / 41k / 229k |
| **Last updated** | 2019-10-10 (6+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~4 MB |
| **Domain** | Energy / ESG |

**What it is**: 4 years of hourly data combining energy demand, generation by source (nuclear, wind, solar, hydro), spot prices, and weather for Spain.

**Why it's a candidate**: Energy transition data is high-demand for ESG, trading, and policy. The concept of combining generation mix + prices + weather is extremely valuable — but only Spain, only through 2019.

**Enrichment opportunity**:
- Expand to full EU (ENTSO-E Transparency Platform is public)
- Add US markets (EIA, PJM, CAISO)
- Extend to present day
- Carbon intensity calculations per generation hour
- Renewable penetration % and forecasting features
- Cross-country comparison tables

---

### 11. Air Quality Data in India (2015-2020)

| Field | Value |
|---|---|
| **Kaggle ref** | `rohanrao/air-quality-data-in-india` |
| **URL** | https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india |
| **Votes / Downloads / Views** | 633 / 86k / 409k |
| **Last updated** | 2020-07-28 (5+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~76 MB |
| **Domain** | Environment |

**What it is**: Daily air quality metrics (PM2.5, PM10, NO2, SO2, CO, O3, AQI) for stations across India, 2015-2020.

**Why it's a candidate**: Air quality is a growing ESG/regulatory data need. 409k views, 86k downloads. 5+ years stale, but India's CPCB publishes continuously.

**Enrichment opportunity**:
- Extend to global coverage (OpenAQ aggregates 300+ sources)
- Auto-refresh from CPCB, EPA AirNow, EEA, OpenAQ APIs
- Add WHO guideline exceedance flags
- Geocode stations with city/district/state hierarchy
- Population exposure estimates (station x census)
- Health impact scoring

---

### 12. Historical Hourly Weather Data (2012-2017)

| Field | Value |
|---|---|
| **Kaggle ref** | `selfishgene/historical-hourly-weather-data` |
| **URL** | https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data |
| **Votes / Downloads / Views** | 520 / 51k / 242k |
| **Last updated** | 2017-12-28 (8+ years stale) |
| **License** | DbCL-1.0 |
| **Size** | ~13 MB |
| **Domain** | Weather |

**What it is**: Hourly weather observations (temperature, humidity, pressure, wind) for 36 major cities, 2012-2017.

**Why it's a candidate**: Weather is a foundational cross-domain dataset — finance, agriculture, energy, insurance, logistics all need it. 8+ years stale with only 36 cities.

**Enrichment opportunity**:
- Expand from 36 to 500+ cities globally
- Extend time range to present (NOAA ISD is free, hourly, global)
- Add derived features: heat index, wind chill, degree days (HDD/CDD)
- Add airport/station metadata with lat/lon
- Join with air quality (EPA AQI) data
- Parquet partitioned by city/year

---

### 13. World Development Indicators (World Bank)

| Field | Value |
|---|---|
| **Kaggle ref** | `kaggle/world-development-indicators` |
| **URL** | https://www.kaggle.com/datasets/kaggle/world-development-indicators |
| **Votes / Downloads / Views** | 1,691 / 72k / 454k |
| **Last updated** | 2017-05-01 (9 years stale) |
| **License** | World Bank Open License (commercial OK with attribution) |
| **Size** | ~387 MB |
| **Domain** | Macro-Economics |

**What it is**: 1,000+ annual indicators of economic development from hundreds of countries. GDP, trade, health expenditure, infrastructure.

**Why it's a candidate**: Authoritative source, 9 years stale on Kaggle, but World Bank API has current data. Perfect "stale mirror of live source" pattern.

**Enrichment opportunity**:
- Auto-refresh from World Bank API
- Pre-compute cross-country comparison tables
- Time-series features (growth rates, moving averages, trend indicators)
- Consistent ISO country coding with geocoding
- Curated subsets for popular use cases
- Parquet partitioned by country/year

---

### 14. 120 Years of Olympic History

| Field | Value |
|---|---|
| **Kaggle ref** | `heesoo37/120-years-of-olympic-history-athletes-and-results` |
| **URL** | https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results |
| **Votes / Downloads / Views** | 2,470 / 226k / 980k |
| **Last updated** | 2018-06-15 (7+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~5.7 MB |
| **Domain** | Sports |

**What it is**: ~270k athlete records from 1896-2016 Olympics — name, sex, age, height, weight, team, NOC, sport, event, medal.

**Why it's a candidate**: 980k views, 226k downloads. 7+ years stale — missing 2020 Tokyo and 2024 Paris Olympics. Sports analytics data has strong commercial demand from broadcasters, sponsors, betting platforms.

**Enrichment opportunity**:
- Add 2020, 2024 (and forward) Games
- Auto-refresh after each Olympic cycle
- Add country GDP/population for medals-per-capita analysis
- Athlete career tracking across Games
- Sport-level analytics (record progressions, competitiveness indices)
- Join with host city economic impact data

---

### 15. Amazon Fine Food Reviews

| Field | Value |
|---|---|
| **Kaggle ref** | `snap/amazon-fine-food-reviews` |
| **URL** | https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews |
| **Votes / Downloads / Views** | 2,422 / 252k / 1.2M |
| **Last updated** | 2017-05-01 (9 years stale) |
| **License** | CC0-1.0 |
| **Size** | ~254 MB |
| **Domain** | E-Commerce / NLP |

**What it is**: ~568k food reviews from Amazon — review text, summary, score, helpfulness votes, product/user IDs, timestamps (through 2012).

**Why it's a candidate**: 1.2M views, 252k downloads. Product review/sentiment data is valuable for brand intelligence, market research, NLP benchmarking. 9 years stale.

**Enrichment opportunity**:
- Expand to broader product categories beyond food
- Add product metadata (brand, category hierarchy, price range)
- Pre-computed sentiment scores, topic models
- Embedding vectors for semantic search
- Review quality scoring
- Time-series aggregation (brand sentiment over time)

---

### 16. Credit Card Customers

| Field | Value |
|---|---|
| **Kaggle ref** | `sakshigoyal7/credit-card-customers` |
| **URL** | https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers |
| **Votes / Downloads / Views** | 2,437 / 138k / 1.0M |
| **Last updated** | 2020-11-19 (5+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~388 KB |
| **Domain** | Banking / Financial Services |

**What it is**: ~10k credit card customer records — demographics, card category, credit limit, revolving balance, transaction counts, utilization, months inactive, contacts, churn flag.

**Why it's a candidate**: 1M views, 138k downloads. Customer churn and credit risk data is core to banking analytics. Well-structured for ML classification use cases.

**Enrichment opportunity**:
- Combine with additional banking/fintech customer datasets
- Add synthetic data augmentation for larger training sets
- Feature engineering for churn prediction (interaction terms, ratios)
- Pre-built ML baselines with documented performance
- Benchmarking leaderboard data

---

### 17. Customer Personality Analysis

| Field | Value |
|---|---|
| **Kaggle ref** | `imakash3011/customer-personality-analysis` |
| **URL** | https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis |
| **Votes / Downloads / Views** | 2,910 / 232k / 1.1M |
| **Last updated** | 2021-08-22 (4+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~63 KB |
| **Domain** | Marketing / Retail |

**What it is**: ~2.2k customer records with demographics, purchase history across categories, campaign response, channel behavior, complaints.

**Why it's a candidate**: 1.1M views, 232k downloads. Customer segmentation is a core enterprise analytics use case — marketing teams pay for this kind of benchmarking data.

**Enrichment opportunity**:
- Combine with additional customer segmentation datasets
- Pre-built RFM (recency, frequency, monetary) features
- Cluster labels and persona profiles
- Campaign ROI calculation features
- Cross-reference with industry benchmarks

---

### 18. FitBit Fitness Tracker Data

| Field | Value |
|---|---|
| **Kaggle ref** | `arashnic/fitbit` |
| **URL** | https://www.kaggle.com/datasets/arashnic/fitbit |
| **Votes / Downloads / Views** | 2,620 / 194k / 958k |
| **Last updated** | 2024-03-02 (1 year stale) |
| **License** | CC0-1.0 |
| **Size** | ~45 MB |
| **Domain** | Health / Wearables |

**What it is**: 30 FitBit users' data — daily activity, steps, heart rate, sleep, calories, intensities over 31 days.

**Why it's a candidate**: 958k views, 194k downloads. Wearable/health tracking data is high-demand in digital health, wellness, insurance analytics. Small but representative sample.

**Enrichment opportunity**:
- Aggregate with other public wearable datasets
- Add derived health metrics (resting heart rate trends, sleep quality scores)
- Circadian rhythm analysis features
- Activity classification and anomaly detection features
- Benchmark tables against clinical ranges
- Time-series optimized formats

---

### 19. New York Stock Exchange

| Field | Value |
|---|---|
| **Kaggle ref** | `dgawlik/nyse` |
| **URL** | https://www.kaggle.com/datasets/dgawlik/nyse |
| **Votes / Downloads / Views** | 1,399 / 107k / 574k |
| **Last updated** | 2017-02-22 (9 years stale) |
| **License** | CC0-1.0 |
| **Size** | ~32 MB |
| **Domain** | Finance |

**What it is**: NYSE-listed company data — daily prices, fundamentals (revenue, earnings, assets), and S&P 500 constituent info.

**Why it's a candidate**: 574k views, 107k downloads. Combines price data with fundamental data — rare on Kaggle. 9 years stale. Pairs with candidates #1 and #9 for a comprehensive financial data product.

**Enrichment opportunity**:
- Auto-refresh from SEC EDGAR (fundamentals), public price sources
- Expand from NYSE to full US market
- Add quarterly earnings, guidance, analyst estimates
- Financial ratio calculations (P/E, EV/EBITDA, ROE)
- Sector comparison benchmarks
- Screening and ranking features

---

### 20. Used Cars Dataset (Craigslist)

| Field | Value |
|---|---|
| **Kaggle ref** | `austinreese/craigslist-carstrucks-data` |
| **URL** | https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data |
| **Votes / Downloads / Views** | 1,623 / 113k / 767k |
| **Last updated** | 2021-05-06 (4+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~275 MB |
| **Domain** | Automotive / Pricing |

**What it is**: ~426k used vehicle listings from Craigslist — price, manufacturer, model, year, condition, odometer, paint color, type, region, state, lat/lon.

**Why it's a candidate**: 767k views, 113k downloads. Used car pricing data is valuable for dealers, insurers, lenders, and consumer apps. 4+ years stale.

**Enrichment opportunity**:
- Expand to multi-source (Craigslist + Facebook Marketplace + public auctions)
- Add KBB/NADA fair market value comparisons
- VIN decoding for trim/features
- Depreciation curve modeling
- Regional price variation analysis
- Geocoded with metro area classification

---

### 21. California Housing Prices

| Field | Value |
|---|---|
| **Kaggle ref** | `camnugent/california-housing-prices` |
| **URL** | https://www.kaggle.com/datasets/camnugent/california-housing-prices |
| **Votes / Downloads / Views** | 1,613 / 291k / 1.1M |
| **Last updated** | 2017-11-24 (8+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~409 KB |
| **Domain** | Real Estate |

**What it is**: 1990 California census block-level housing data — median house value, income, rooms, bedrooms, population, households, ocean proximity, lat/lon.

**Why it's a candidate**: 1.1M views, 291k downloads — one of the most-downloaded ML benchmark datasets. 8+ years stale. California housing is perennial interest.

**Enrichment opportunity**:
- Update with current census/ACS data (2020 census, annual ACS)
- Expand to all US states
- Add time-series dimension (multiple census years)
- School ratings, crime, walkability enrichment
- Zillow ZHVI integration for current valuations
- Parcel-level detail where public assessor data allows

---

### 22. 2015 Flight Delays and Cancellations

| Field | Value |
|---|---|
| **Kaggle ref** | `usdot/flight-delays` |
| **URL** | https://www.kaggle.com/datasets/usdot/flight-delays |
| **Votes / Downloads / Views** | 1,150 / 163k / 728k |
| **Last updated** | 2017-02-09 (9 years stale) |
| **License** | CC0-1.0 |
| **Size** | ~200 MB |
| **Domain** | Aviation / Transportation |

**What it is**: All 2015 US domestic flights — ~5.8M records with departure/arrival times, delays, cancellations, diversions, airline, origin/destination airports.

**Why it's a candidate**: 728k views, 163k downloads. Official USDOT data, 9 years stale on Kaggle. BTS (Bureau of Transportation Statistics) publishes this monthly for free. Aviation analytics valuable for airlines, travel, logistics, insurance.

**Enrichment opportunity**:
- Extend to 2015-present (BTS releases monthly)
- Auto-refresh pipeline from BTS On-Time Performance data
- Add airport metadata (city, state, lat/lon, hub classification)
- Weather at departure/arrival for delay attribution
- Route-level aggregations and reliability scores
- Airline performance benchmarking
- Connection risk modeling

---

### 23. Water Potability

| Field | Value |
|---|---|
| **Kaggle ref** | `adityakadiwal/water-potability` |
| **URL** | https://www.kaggle.com/datasets/adityakadiwal/water-potability |
| **Votes / Downloads / Views** | 1,673 / 122k / 707k |
| **Last updated** | 2021-04-25 (4+ years stale) |
| **License** | CC0-1.0 |
| **Size** | ~257 KB |
| **Domain** | Environment / Public Health |

**What it is**: ~3.3k water samples with 9 quality parameters (pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, turbidity) and potability label.

**Why it's a candidate**: 707k views, 122k downloads. Water quality is an important ESG, public health, and infrastructure theme. Classification-ready with clear enrichment path.

**Enrichment opportunity**:
- Expand with EPA water quality monitoring data (STORET/WQX — public)
- Add geographic context (water source, treatment plant, service area)
- WHO/EPA standard threshold comparisons
- Time-series monitoring data from public utilities
- Cross-reference with health outcome data
- Infrastructure age/investment context

---

### 24. US Census Demographic Data

| Field | Value |
|---|---|
| **Kaggle ref** | `muonneutrino/us-census-demographic-data` |
| **URL** | https://www.kaggle.com/datasets/muonneutrino/us-census-demographic-data |
| **Votes / Downloads / Views** | 365 / 35k / 225k |
| **Last updated** | 2019-03-03 (7 years stale) |
| **License** | CC0-1.0 |
| **Size** | ~11 MB |
| **Domain** | Demographics |

**What it is**: County and census-tract level demographic data — population, income, poverty, employment, commute, race/ethnicity from ACS.

**Why it's a candidate**: 225k views. Census/ACS data is the backbone of location intelligence, market sizing, and policy analysis. 7 years stale on Kaggle, but Census Bureau publishes ACS annually.

**Enrichment opportunity**:
- Auto-refresh from Census API (annual ACS releases)
- Add time-series (multiple ACS years for trend analysis)
- Add geographic boundaries (GeoJSON/GeoParquet)
- Join with housing, crime, health, education datasets
- Pre-computed market sizing features (TAM by geography)
- H3 hex indexing for spatial joins

---

### 25. Goodreads Books

| Field | Value |
|---|---|
| **Kaggle ref** | `jealousleopard/goodreadsbooks` |
| **URL** | https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks |
| **Votes / Downloads / Views** | 1,975 / 88k / 539k |
| **Last updated** | 2020-03-09 (6 years stale) |
| **License** | CC0-1.0 |
| **Size** | ~637 KB |
| **Domain** | Publishing / Media |

**What it is**: ~10k books with title, author, rating, ratings count, reviews count, pages, publisher, language, ISBN.

**Why it's a candidate**: 539k views, 88k downloads. Book/publishing metadata is valuable for publishers, libraries, content recommendation. 6 years stale.

**Enrichment opportunity**:
- Expand to 1M+ titles via Open Library API (public, CC0)
- Add genre/subject classification (BISAC codes)
- Add pricing data (Amazon, BookDepository)
- Bestseller list history (NYT API)
- Author metadata (nationality, birth year, other works)
- Recommendation graph features (also-read, similar-to)

---

## Summary Table

| # | Dataset | Votes | Downloads | Last Updated | License | Domain |
|---|---|---|---|---|---|---|
| 1 | US Stocks & ETFs (OHLCV) | 4,608 | 141k | 2017-11 | CC0 | Finance |
| 2 | World Happiness Report | 4,454 | 387k | 2019-11 | CC0 | Social/Econ |
| 3 | Netflix Movies & TV Shows | 9,721 | 721k | 2021-09 | CC0 | Entertainment |
| 4 | Trending YouTube Videos | 5,876 | 298k | 2019-06 | CC0 | Digital Media |
| 5 | NYC Airbnb Open Data | 3,093 | 237k | 2019-08 | CC0 | Real Estate |
| 6 | Hotel Booking Demand | 2,668 | 206k | 2020-02 | CC-BY-4.0 | Hospitality |
| 7 | House Sales King County | 2,303 | 240k | 2016-08 | CC0 | Real Estate |
| 8 | Hourly Energy (PJM) | 1,110 | 110k | 2018-08 | CC0 | Energy |
| 9 | S&P 500 Stock Data | 1,119 | 104k | 2018-02 | CC0 | Finance |
| 10 | Energy Demand+Gen (Spain) | 416 | 41k | 2019-10 | CC0 | Energy |
| 11 | Air Quality India | 633 | 86k | 2020-07 | CC0 | Environment |
| 12 | Historical Hourly Weather | 520 | 51k | 2017-12 | DbCL | Weather |
| 13 | World Development Indicators | 1,691 | 72k | 2017-05 | WB Open | Macro-Econ |
| 14 | 120 Years of Olympics | 2,470 | 226k | 2018-06 | CC0 | Sports |
| 15 | Amazon Fine Food Reviews | 2,422 | 252k | 2017-05 | CC0 | E-Commerce/NLP |
| 16 | Credit Card Customers | 2,437 | 138k | 2020-11 | CC0 | Banking |
| 17 | Customer Personality Analysis | 2,910 | 232k | 2021-08 | CC0 | Marketing |
| 18 | FitBit Fitness Tracker | 2,620 | 194k | 2024-03 | CC0 | Health/Wearables |
| 19 | NYSE Stocks + Fundamentals | 1,399 | 107k | 2017-02 | CC0 | Finance |
| 20 | Used Cars (Craigslist) | 1,623 | 113k | 2021-05 | CC0 | Automotive |
| 21 | California Housing Prices | 1,613 | 291k | 2017-11 | CC0 | Real Estate |
| 22 | US Flight Delays (USDOT) | 1,150 | 163k | 2017-02 | CC0 | Aviation |
| 23 | Water Potability | 1,673 | 122k | 2021-04 | CC0 | Environment |
| 24 | US Census Demographics | 365 | 35k | 2019-03 | CC0 | Demographics |
| 25 | Goodreads Books | 1,975 | 88k | 2020-03 | CC0 | Publishing |

**Combined totals**: ~57k votes, ~4.3M downloads across all 25 candidates.

---

## License Summary

All 25 candidates use commercially permissive licenses:

| License | Count | Commercial Use |
|---|---|---|
| CC0-1.0 (Public Domain) | 22 | Unrestricted |
| CC-BY-4.0 | 1 | Yes, with attribution |
| DbCL-1.0 | 1 | Yes, with attribution |
| World Bank Open | 1 | Yes, with attribution |

No NC (Non-Commercial) or restrictive licenses in this list.

---

## Recommended Product Families

These 25 cluster into **8 product families** sharing pipeline infrastructure:

### 1. Financial Markets (#1, #9, #19)
US stocks, S&P 500, NYSE fundamentals. Common sources: Yahoo Finance, SEC EDGAR. Single pipeline covers price + fundamentals.

### 2. Real Estate & Housing (#5, #7, #21)
Airbnb, house sales, housing prices. Common enrichment: census, school ratings, geocoding. Expandable to many metro areas.

### 3. Energy & Grid (#8, #10)
PJM consumption, Spain generation mix. Common sources: ISO/RTO APIs, ENTSO-E. Expandable to global markets.

### 4. Weather & Environment (#11, #12, #23)
Air quality, hourly weather, water quality. Common sources: NOAA, EPA, OpenAQ. Core enrichment layer for other products.

### 5. Global Indicators (#2, #13, #14)
Happiness, World Bank indicators, Olympics. Common join key: country/year. UN/World Bank APIs.

### 6. Hospitality & Travel (#6, #22)
Hotel bookings, flight delays. Common sources: BTS, tourism boards. Valuable for travel industry analytics.

### 7. Consumer & Commerce (#3, #4, #15, #16, #17, #20, #25)
Netflix, YouTube, Amazon reviews, credit cards, customers, used cars, books. The largest family — common theme is consumer behavior data.

### 8. Demographics & Health (#18, #24)
FitBit, census. Common enrichment: geographic, health benchmarks.

---

## Next Steps

1. **Marketplace gap analysis**: Check which of these 25 topics already have competing products on AWS Data Exchange, Snowflake Marketplace, and Databricks Marketplace
2. **Source verification**: For each candidate, confirm the original public data source is still active and accessible for auto-refresh
3. **Effort estimation**: Rank by build effort (small/clean datasets vs. large/complex pipelines)
4. **Priority scoring**: Combine demand signal, competitive gap, and build effort into a priority stack-rank for the prototype phase
