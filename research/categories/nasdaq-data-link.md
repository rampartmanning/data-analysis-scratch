# Nasdaq Data Link (Quandl) — Categories

**URL**: https://data.nasdaq.com
**Scraped**: 2026-02-26
**Method**: WebSearch + WebFetch (data.nasdaq.com is a JS SPA, not directly scrapable)

## Category Taxonomy

### Organization Model
Nasdaq Data Link organizes data into **databases** (collections from a single provider) rather than topic categories. Each database covers a specific domain. The platform uses three classification axes:

1. **Asset Class** — what financial instrument/domain the data covers
2. **Data Type** — what kind of measurement/metric
3. **Region** — geographic coverage

### Known Databases (Free)

| Database Code | Name | Description |
|---------------|------|-------------|
| WIKIP | Wiki EOD Stock Prices | Free US equity end-of-day data |
| FRED | Federal Reserve Economic Data | US economic indicators (growth, employment, inflation, manufacturing) |
| ZILLOW | Zillow Real Estate Data | Market indices, rental, sales, inventories for US geographies |
| MULTPL | S&P 500 Ratios | Shiller PE, earnings yield, dividend yield |
| USTREASURY | US Treasury | Yield curves, real yield curves, bill rates |
| ODA | Open Data for Africa | African economic indicators |
| WORLDBANK | World Bank | Global development indicators |
| UN | United Nations | UN statistical data |
| EUREKA | Eureka Hedge Fund Index | Hedge fund performance indices |
| ML | Merrill Lynch | Bond indices |

### Known Databases (Premium)

| Database Code | Name | Description |
|---------------|------|-------------|
| QDL | Nasdaq Data Link proprietary | Nasdaq's own data products |
| SHARADAR | Sharadar | US equity fundamentals, prices, and metrics |
| MER | Marex | Commodity and financial data |
| WB | World'vest Base | Investment data |
| SF1 | Sharadar Fundamentals | US company fundamentals |
| SFB | Sharadar Fund Holdings | Fund holdings data |
| AR | Alternative data | Various alternative data feeds |

### Implied Topic Categories
Based on available databases, these topic areas are covered:

1. **Equity Markets** — stock prices, fundamentals, ratios
2. **Fixed Income** — bonds, treasury yields, interest rates
3. **Economic Indicators** — GDP, employment, inflation, manufacturing
4. **Real Estate** — housing prices, rental data, market indices
5. **Commodities** — commodity prices, futures
6. **Foreign Exchange** — currency data
7. **Alternative Data** — ESG, sentiment, web traffic, satellite
8. **Demographics/Social** — population, education, health (via World Bank, UN)
9. **Fund/Hedge Fund Performance** — fund returns, indices

## Scale
- 250+ databases
- Millions of time series
- 400+ data sources indexed
- Hundreds of thousands of users

## Notes

- Taxonomy is **database-centric** rather than category-centric — you browse by provider/database, not by topic
- This is a **finance-first** marketplace — most databases relate to financial data, economic indicators, or alternative data for investment
- The free databases (FRED, WIKIP, ZILLOW, World Bank) serve as top-of-funnel; premium databases are the revenue model
- Originally Quandl (acquired by Nasdaq in 2018), rebranded to Nasdaq Data Link in 2021
- The API is one of the most developer-friendly in the financial data space (native Python, R, Excel libraries)
- No formal category taxonomy published — organization is by database/publisher, not by subject matter
- Sources: https://data.nasdaq.com, https://docs.data.nasdaq.com
