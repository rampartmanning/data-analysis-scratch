# Snowflake Marketplace — Categories

**URL**: https://www.snowflake.com/en/data-cloud/marketplace/
**Scraped**: 2026-02-26
**Method**: WebFetch + Snowflake listing manifest documentation (docs.snowflake.com)

## Category Taxonomy

### Primary Categories (from Listing Manifest Reference)
These are the **exact allowed values** for the `categories` field in Snowflake Marketplace listings. Each listing can have exactly ONE category:

1. BUSINESS
2. CONNECTORS
3. DEMOGRAPHICS
4. ECONOMY
5. ENERGY
6. ENVIRONMENT
7. FINANCIAL
8. GOVERNMENT
9. HEALTH
10. IDENTITY
11. LEGAL
12. LOCAL
13. LOOKUP_TABLES
14. MARKETING
15. MEDIA
16. SECURITY
17. SPORTS
18. TRANSPORTATION
19. TRAVEL
20. WEATHER

### Business Needs (Standard Values)
Listings can also be tagged with one or more "business needs" — these are more granular use-case descriptors:

1. 360-Degree Customer View
2. Accelerating Advertising Revenue
3. Asset Valuation
4. Attribution Analysis
5. Audience Activation
6. Audience Segmentation
7. Blockchain Analysis
8. Contact Data Enrichment
9. Customer Acquisition
10. Customer Onboarding
11. Data Quality and Cleansing
12. Demand Forecasting
13. ESG Investment Analysis
14. Economic Impact Analysis
15. Foot Traffic Analytics
16. Fraud Remediation
17. Fundamental Analysis
18. Identity Resolution
19. Inventory Management
20. Life Sciences Commercialization
21. Location Data Enrichment
22. Location Geocoding
23. Location Planning
24. Machine Learning
25. Market Analysis
26. Patient 360
27. Personalize Customer Experiences
28. Population Health Management
29. Pricing Analysis
30. Quantitative Analysis
31. Real World Data (RWD)
32. Regulatory Reporting
33. Risk Analysis
34. Sentiment Analysis
35. Subscriber Acquisition and Retention
36. Supply Chain

Custom business needs (provider-defined) are also allowed.

### Filter Dimensions Available in UI
- Availability
- Pricing (Free / Free to Try / Paid)
- Categories (the 20 above)
- Business Needs (the 36+ above)
- Cloud Region Availability
- Geographic Coverage
- Legal Terms
- Provider
- Time Frame

### Product Types
- Raw datasets
- Refined/enriched data
- Historical datasets (for ML/forecasting)
- Real-time data streams
- Specialized identity/audience data
- Snowflake Native Apps
- Pre-built data pipelines and transformations
- AI products

## Scale
- ~2,700+ listings
- 670+ providers

## Notes

- **Authoritative source**: The listing manifest reference at `docs.snowflake.com/en/progaccess/listing-manifest-reference` provides the exact enum values
- Category taxonomy is **flat** (20 categories, no hierarchy)
- Business needs provide a **second, more granular layer** of classification (36 standard + custom)
- Each listing gets exactly ONE category but can have MULTIPLE business needs
- The categories map loosely to industries/domains; the business needs map to specific analytics use cases
- Notable categories: LOOKUP_TABLES, CONNECTORS, and LOCAL are unusual — they indicate functional/structural types rather than subject domains
- IDENTITY as a top-level category reflects the importance of identity resolution in the data marketplace
- Source: https://docs.snowflake.com/en/progaccess/listing-manifest-reference
