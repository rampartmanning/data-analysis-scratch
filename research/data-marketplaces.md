# Data Marketplaces — Comprehensive Research

**Research Date**: 2026-02-26
**Total Platforms Cataloged**: 127

> **Methodology**: Research compiled from web searches and training knowledge (cutoff ~May 2025).
> Scale figures are approximate and should be verified against current platform pages.
> Some platforms may have changed status, pricing, or ownership since research was conducted.

## Summary

| # | Category | Count |
|---|----------|-------|
| 1 | Cloud & Enterprise Data Marketplaces | 7 |
| 2 | Government & Civic Open Data Portals | 17 |
| 3 | International & Multilateral Organization Data | 9 |
| 4 | Specialized Commercial Data Marketplaces | 18 |
| 5 | AI/ML Dataset Platforms | 11 |
| 6 | Academic & Research Data Repositories | 7 |
| 7 | Data Discovery & Aggregation Platforms | 9 |
| 8 | Decentralized & Blockchain Data Marketplaces | 8 |
| 9 | Sector-Specific Data Providers | 15 |
| 10 | Alternative Data, Web Data & Financial Data Providers | 18 |
| 99 | Other / Uncategorized | 8 |
| | **Total** | **127** |

---

## 1. Cloud & Enterprise Data Marketplaces

### AWS Data Exchange
- **URL**: https://aws.amazon.com/data-exchange/
- **Operator/Parent**: Amazon Web Services (Amazon.com, Inc. - publicly traded: AMZN on Nasdaq)
- **Type**: Both - free and paid datasets available
- **Pricing**: Varies by provider. Options include: subscription-based (monthly/annual), one-time purchase, per-revision pricing, and free tiers. Providers set their own prices. AWS charges data transfer fees separately. Revenue split: AWS retains a percentage o...
- **Data Types**: Financial and economic data, Healthcare and life sciences data, Weather and geospatial data, Satellite and remote sensing imagery, Consumer and marketing analytics, Public sector and government data, Media and entertainment data, Automotive data, ESG and sustainability data, Retail and CPG data, Telecommunications data, Risk and fraud data, Real estate data, Identity and demographic data, Financial data, Healthcare/life sciences data, Geospatial/mapping data, Weather/climate data, Media/entertainment data, Retail/CPG data, Public/open data, ESG data, Satellite imagery, IoT data
- **Industry Focus**: Financial services, Healthcare and pharma, Insurance, Advertising and marketing, Agriculture, Energy, Government and public sector, Retail and e-commerce, Transportation and logistics, Healthcare, Media, Automotive, Retail, Government, Any AWS customer
- **Geographic Focus**: Global - available in multiple AWS regions worldwide
- **Formats**: Amazon S3 objects (any file format), AWS Lake Formation data permissions (table-based sharing), Amazon Redshift data sharing, Amazon S3 Access Grants, API-based access (REST APIs via API Gateway), CSV, Parquet, JSON, Avro, ORC, and other file formats via S3
- **Scale**: Approximately 3,500+ data products from 300+ data providers (as of early 2025, estimated). One of the largest cloud-native data marketplaces.
- **Key Features**:
  - Integrated with AWS ecosystem (S3, Redshift, Lake Formation, Athena, SageMaker, etc.)
  - Automatic data revision notifications and updates
  - Data subscription management with auto-renewal
  - Private offers and custom pricing negotiations between provider and subscriber
  - Data dictionaries and sample data for preview before purchase
- **Provider Requirements**: Providers must register as AWS Marketplace sellers, which requires a valid AWS account, a US bank account (or supported international payment method), W-9/W-8 tax documentation, and agreement to th...
- **Notes**: AWS Data Exchange benefits from the massive AWS customer base. Key advantage is integration with existing AWS infrastructure and billing. Competes with Snowflake Marketplace, Databricks Marketplace, and Google Cloud Analytics Hub. Provider adoption has been steady but the marketplace is less 'dis...

### Azure Data Marketplace (Microsoft Azure Marketplace - Data category) / Azure Open Datasets
- **URL**: https://azuremarketplace.microsoft.com/en-us/marketplace/apps?category=data
- **Operator/Parent**: Microsoft Corporation
- **Type**: Both - Azure Open Datasets are free; Azure Marketplace data products include both free and paid offerings
- **Pricing**: Azure Open Datasets: Free, hosted on Azure and accessible without cost (standard Azure compute/storage costs may apply). Azure Marketplace Data: Varies by provider - subscription, pay-per-use, one-time purchase, free trial, or BYOL (Bring Your Own...
- **Data Types**: Public government datasets (US and international), Demographic and population data, Weather and climate data, Genomics and health data, Transportation and urban mobility data, Safety and public records data, Satellite and geospatial imagery, Financial and economic indicators, Labor and employment statistics, IoT and telemetry data, Machine learning sample datasets
- **Industry Focus**: Government and public sector, Healthcare and life sciences, Financial services, Education and research, Smart cities and IoT, Retail, Manufacturing, Energy
- **Geographic Focus**: Global, with a strong emphasis on US government and public datasets. Azure Open Datasets includes international data from multiple countries.
- **Formats**: Azure Blob Storage (any format), Azure Data Lake Storage Gen2, Parquet, CSV, JSON, TSV, OData feeds, REST APIs, Azure SQL / Synapse Analytics tables, SAS, managed applications, and container-based deployments via Marketplace
- **Scale**: Azure Open Datasets: approximately 100+ curated public datasets. Azure Marketplace (data category): hundreds of data product listings from numerous providers. The broader Azure Marketplace contains tens of thousands of total listings across all categories.
- **Key Features**:
  - Azure Open Datasets: curated, ready-to-use public datasets optimized for Azure ML and analytics
  - Tight integration with Azure ecosystem (Synapse Analytics, Azure ML, Azure Databricks, Power BI)
  - Co-sell programs for providers partnering with Microsoft sales teams
  - Enterprise-grade security and compliance (Azure AD, RBAC)
  - Free trial options for many Marketplace offerings
- **Provider Requirements**: Providers must enroll in the Microsoft Partner Network and register as Azure Marketplace publishers through Partner Center. Requirements include a valid Microsoft account, tax and banking informati...
- **Notes**: Microsoft's data marketplace story is more fragmented than competitors. Azure Open Datasets is a curated collection of free public datasets, while the Azure Marketplace is a broader commercial platform. Microsoft Fabric (launched 2023-2024) is increasingly becoming the unifying analytics layer an...

### Databricks Marketplace
- **URL**: https://www.databricks.com/product/marketplace
- **Operator/Parent**: Databricks Inc. (privately held, founded by Apache Spark creators)
- **Type**: Both - includes free open datasets and paid commercial data products
- **Pricing**: Open marketplace model built on Delta Sharing (open protocol). Free and paid listings available. Providers set their own pricing. Paid listings are handled through direct provider-consumer agreements in many cases. Databricks facilitates discovery...
- **Data Types**: Financial and alternative data, Healthcare and genomics data, Geospatial and mapping data, Climate and weather data, Demographic and socioeconomic data, Machine learning models and notebooks, Solution accelerators and code templates, Open-source datasets, AI/ML training datasets, ESG and sustainability data, Retail and consumer data, Financial data, Healthcare data, Geospatial data, ML models and notebooks, Open source datasets, ESG data, Industry-specific datasets, Solution accelerators, AI/ML models, Datasets for analytics and AI, Notebooks/solutions, Health data
- **Industry Focus**: Financial services, Healthcare and life sciences, Media and entertainment, Manufacturing, Retail, Public sector, Technology and AI/ML, Energy and utilities, Healthcare/life sciences, Retail/CPG, Media, Technology/data science, Data engineering, Data science, AI/ML, Cross-industry analytics
- **Geographic Focus**: Global - available across Databricks deployments on AWS, Azure, and GCP
- **Formats**: Delta Lake tables (Delta Sharing protocol), Notebooks (Jupyter/Databricks notebooks), ML models (MLflow format), Solution accelerators, Parquet, CSV, JSON (underlying Delta Lake formats), Open format via Delta Sharing - accessible from any platform, not just Databricks
- **Scale**: Approximately 1,500+ listings (as of early 2025, estimated). Growing rapidly since GA launch. Includes data products from major providers like Nasdaq, Foursquare, and others.
- **Key Features**:
  - Built on Delta Sharing - an open-source, cross-platform data sharing protocol
  - Works across clouds and platforms (not locked to Databricks)
  - Share data, notebooks, ML models, and solution accelerators
  - Integration with Unity Catalog for governance and access control
  - Recipients do not need a Databricks account to receive shared data (via open Delta Sharing)
- **Provider Requirements**: Providers need a Databricks account with Unity Catalog enabled. They create data products through the Databricks workspace and publish listings to the Marketplace. Requirements include providing me...
- **Status**: Active. Launched in 2022, continuing to grow. Key strategic product for Databricks ecosystem.
- **Notes**: Launched in GA in 2023. Key differentiator is the open-source Delta Sharing protocol, which means data consumers don't need Databricks to access shared data. This openness is a strategic advantage over more proprietary approaches. Also unique in sharing not just data but also ML models, notebooks...

### IBM Data Exchange / IBM Data Asset eXchange (DAX) / IBM Environmental Intelligence Suite Data
- **URL**: https://developer.ibm.com/exchanges/data/
- **Operator/Parent**: IBM Corporation
- **Type**: Primarily free and open-source (IBM Data Asset eXchange). IBM's commercial data offerings are available through IBM Cloud and IBM Environmental Intelligence Suite.
- **Pricing**: IBM Data Asset eXchange (DAX): Free and open-source under permissive licenses (CDLA-Sharing, CDLA-Permissive, Apache 2.0). Datasets are available for download at no cost. IBM's commercial data products (e.g., weather data via The Weather Company /...
- **Data Types**: Natural language processing datasets (text corpora), Computer vision and image datasets, Time series and sensor data, Weather and climate data (via The Weather Company), Geospatial data, Audio and speech datasets, Tabular and structured datasets for ML, Finance and economics datasets, Open-source benchmark datasets for AI/ML
- **Industry Focus**: AI/ML research and development, Weather-dependent industries (agriculture, energy, insurance, logistics), Healthcare and life sciences, Financial services, Government and public sector, Academia and research
- **Geographic Focus**: Global - open datasets are accessible worldwide. Commercial offerings available in IBM Cloud regions.
- **Formats**: CSV, JSON, Parquet, Image formats (JPEG, PNG), Audio formats (WAV, FLAC), Text and document formats, Jupyter notebooks for exploration, Downloadable archives (tar.gz, zip), APIs (REST) for commercial data services, IBM Cloud Object Storage
- **Scale**: IBM Data Asset eXchange: approximately 30-50 curated open datasets (smaller, highly curated collection). IBM's commercial data offerings (Weather Company, etc.) serve thousands of enterprise customers. The scale is more about data quality and curation than breadth of listings.
- **Key Features**:
  - Open-source datasets with permissive licenses (CDLA)
  - Hosted on IBM Developer - accessible without IBM Cloud account
  - Each dataset includes a tutorial notebook for exploration
  - Integration with IBM Watson Studio and IBM Cloud Pak for Data
  - Preview and exploration tools
- **Provider Requirements**: For IBM DAX: IBM curates datasets internally and through partnerships. External contribution is possible through the open-source community (GitHub). For commercial IBM data products: standard IBM p...
- **Notes**: IBM's data marketplace strategy has evolved significantly. The IBM Data Asset eXchange (DAX) focused on free, open-source, AI-ready datasets and is hosted on IBM Developer. It is smaller and more curated than competitors. IBM's major commercial data play is The Weather Company (acquired 2016), wh...

### Oracle Data Marketplace (Oracle Data Cloud - now largely discontinued)
- **URL**: https://www.oracle.com/cx/advertising/
- **Operator/Parent**: Oracle Corporation (publicly traded: ORCL on NYSE)
- **Type**: Both - includes free and paid data product listings
- **Pricing**: Pricing varies by provider. Options include BYOL (Bring Your Own License), pay-as-you-go, and free offerings. Oracle Cloud Marketplace handles billing and licensing. Oracle takes a commission on transactions. Data products are often bundled with O...
- **Data Types**: Business and enterprise data, Financial and risk data, Location and address data, Identity and verification data, Industry-specific reference data, Oracle-optimized datasets and data models, AI/ML training data, ERP and supply chain data enrichment, Was: Consumer audience data, purchase behavior data, demographic data, B2B data (BlueKai, Datalogix, AddThis, Grapeshot), Remaining: Oracle has retained some first-party data capabilities within Oracle CX
- **Industry Focus**: Financial services and banking, Healthcare, Retail, Telecommunications, Government, Manufacturing, Utilities, Was: Advertising/marketing (primary), retail, financial services, Remaining: Oracle CX/marketing cloud customers
- **Geographic Focus**: Global - available across Oracle Cloud regions. Strong presence in enterprise markets in North America, Europe, and Asia Pacific.
- **Formats**: Oracle Database native formats, Oracle Cloud Infrastructure Object Storage, Oracle Analytics Cloud integrations, REST APIs, CSV, JSON, Parquet via OCI Data Integration, Oracle Autonomous Database compatible formats
- **Scale**: The Oracle Cloud Marketplace overall has thousands of listings, but the data-specific category is smaller compared to AWS or Snowflake - estimated hundreds of data-related listings. Oracle's data marketplace is less prominent as a standalone offering compared to competitors.
- **Key Features**:
  - Deep integration with Oracle Cloud Infrastructure and Oracle Database
  - Oracle Cloud Marketplace consolidates data products with SaaS and IaaS offerings
  - Enterprise-grade security and compliance
  - Integration with Oracle Analytics Cloud and Oracle APEX
  - Supports Oracle Autonomous Database for managed data services
- **Provider Requirements**: Providers must register as Oracle Partner Network members and enroll as Oracle Cloud Marketplace publishers. Requirements include an Oracle Cloud account, agreement to the Oracle Marketplace Publis...
- **Status**: Largely Discontinued - Oracle announced in 2024 it would shut down its advertising business/data marketplace, citing GDPR and privacy regulation challenges. Some data capabilities remain within Oracle CX. [Based on training data, may need verification on exact timeline and what remains]
- **Notes**: Oracle's data marketplace is embedded within the broader Oracle Cloud Marketplace rather than being a standalone data exchange. Oracle's strength is in its enterprise database and application ecosystem. The data marketplace capabilities are more tightly coupled with Oracle's existing product suit...

### SAP Data Marketplace
- **URL**: https://www.sap.com/products/technology-platform/datasphere/data-marketplace.html
- **Operator/Parent**: SAP SE
- **Type**: Both - includes free sample/open data and commercial paid data products
- **Pricing**: Integrated into SAP Datasphere (formerly SAP Data Warehouse Cloud). Data products are available via subscription or one-time purchase. Some free/open data products available. Providers set pricing. SAP handles billing through the SAP ecosystem. Co...
- **Data Types**: Business and enterprise operational data, Financial and economic indicators, ESG and sustainability data, Industry benchmarks and KPIs, Geographic and demographic data, Supply chain and logistics data, Master data enrichment (company, product, location), Market research and consumer insights, Regulatory and compliance data
- **Industry Focus**: Manufacturing and industrial, Retail and consumer products, Financial services, Energy and utilities, Healthcare and pharma, Automotive, Public sector, Professional services
- **Geographic Focus**: Global - with a strong presence in Europe (SAP's home market) and enterprise markets worldwide
- **Formats**: SAP Datasphere native tables and views, SAP HANA database formats, CSV and flat files, Open data formats via SAP integration suite, OData services, APIs via SAP Integration Suite / SAP BTP
- **Scale**: Estimated hundreds of data product listings. Growing since SAP Datasphere rebrand and investment. Smaller than AWS or Snowflake marketplaces but highly focused on enterprise and business data.
- **Key Features**:
  - Embedded directly into SAP Datasphere - data products appear as native objects
  - Business semantics and metadata preserved across sharing
  - Integration with SAP Business Technology Platform (BTP)
  - Pre-built data models aligned with SAP's business process expertise
  - Data product governance and lineage tracking
- **Provider Requirements**: Providers must be SAP partners or approved data vendors. They publish data products through SAP Datasphere with metadata, descriptions, licensing terms, and sample data. SAP reviews listings for qu...
- **Notes**: SAP Data Marketplace is uniquely positioned in the enterprise data space because of SAP's dominance in ERP and business applications. The marketplace is tightly integrated with SAP Datasphere, meaning data products can be directly combined with enterprise operational data from SAP systems. This i...

### Snowflake Marketplace
- **URL**: https://www.snowflake.com/en/data-cloud/marketplace/
- **Operator/Parent**: Snowflake Inc. (publicly traded: SNOW on NYSE)
- **Type**: Both - Free and paid listings available. Snowflake account required (which has its own compute costs).
- **Pricing**: Free listings are common (providers use free data to attract customers to their platforms). Paid listings involve provider-set pricing, typically subscription-based. Snowflake facilitates billing through its platform. Providers can monetize via pe...
- **Data Types**: Financial markets and alternative data, Healthcare and medical data, Weather and environmental data, Geospatial and location data, Demographic and consumer data, Government and public sector data, Cybersecurity threat data, Advertising and marketing analytics, Supply chain and logistics data, ESG and sustainability data, Identity resolution data, Retail and point-of-sale data, Snowflake native applications (data apps), Machine learning models and features, Financial market data, Weather/climate data, Geospatial/location data, Healthcare data, Government/public data, Cybersecurity data, ESG/sustainability data, Marketing/advertising data, B2B firmographic data, Economic indicators, Supply chain data, Real estate data, Financial data, Weather data, Government/open data, ESG data, Any structured/semi-structured data
- **Industry Focus**: Financial services and capital markets, Healthcare and life sciences, Retail and CPG, Advertising and media, Technology, Government, Insurance, Manufacturing, Telecommunications, Education, Financial services, Healthcare/life sciences, Retail/CPG, Media/advertising, Cross-industry, Healthcare, Retail, Advertising/marketing
- **Geographic Focus**: Global - available across all Snowflake cloud regions (AWS, Azure, GCP)
- **Formats**: Snowflake-native tables and views (live, no ETL required), Shared databases and schemas, Secure data sharing (zero-copy cloning), Snowflake Native Apps, Data accessed as standard SQL tables
- **Scale**: Approximately 2,000+ listings from 500+ data providers (as of early 2025, estimated). Rapidly growing. Snowflake reports thousands of data shares happening daily across its platform.
- **Key Features**:
  - Live data sharing - no ETL, no data movement, no copying required
  - Near-real-time data updates from providers
  - Secure Data Sharing via Snowflake's unique architecture
  - Data Clean Rooms for privacy-safe data collaboration
  - Snowflake Native Apps - providers can ship code alongside data
- **Provider Requirements**: Providers must have a Snowflake account. To list on the Marketplace, providers apply through the Snowflake Provider Studio. Requirements include agreeing to provider terms, configuring secure data ...
- **Status**: Active and rapidly growing. Key strategic initiative for Snowflake. One of the largest cloud data marketplaces.
- **Notes**: The Snowflake Marketplace is notable because it eliminates the traditional ETL burden of data acquisition - data is shared live within the Snowflake ecosystem. This is a major competitive advantage but also means it only reaches Snowflake customers. Competes with Databricks Marketplace, AWS Data ...

---

## 2. Government & Civic Open Data Portals

### Brazil dados.gov.br
- **URL**: https://dados.gov.br
- **Operator/Parent**: Government of Brazil, Secretariat of Digital Government
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Government Finance & Budget, Health, Education, Economy & Commerce, Environment, Agriculture, Public Safety, Transportation, Science & Technology, Social Programs
- **Industry Focus**: Government & Public Policy, Latin American Market Research, Academic Research, Social Science
- **Geographic Focus**: Brazil (federal, state, and municipal data)
- **Formats**: CSV, JSON, XML, Excel, API (CKAN-based), PDF
- **Scale**: ~10,000+ datasets from federal agencies and some state/municipal sources
- **Key Features**:
  - CKAN-based platform
  - API access
  - Portuguese language (primary) with some metadata in English
  - Integration with Brazil's Transparency Portal
  - Open Data National Plan compliance
- **Licensing**: Open Government Licence - Brazil. Generally free for any use with attribution.
- **Notes**: Brazil has been expanding its open data initiative. The portal is primarily in Portuguese. Complements the Brazilian Transparency Portal (Portal da Transparencia) which focuses on government spending.

### Copernicus Open Access Hub / Copernicus Data Space Ecosystem
- **URL**: https://dataspace.copernicus.eu
- **Operator/Parent**: European Space Agency (ESA) and European Commission, managed by a consortium
- **Type**: Free
- **Pricing**: Completely free. Registration required. Free processing quota available on the Copernicus Data Space Ecosystem.
- **Data Types**: Satellite Imagery (optical, radar, multispectral), Land Monitoring (land cover, vegetation, water), Marine/Ocean Monitoring (sea surface temperature, ocean color, sea level), Atmosphere Monitoring (air quality, ozone, solar radiation), Climate Change Monitoring, Emergency Management, Security (border surveillance, maritime)
- **Industry Focus**: Earth Observation & Remote Sensing, Agriculture & Forestry, Environmental Monitoring, Urban Planning, Marine & Maritime, Insurance & Risk Management, Climate Research, Defense & Security
- **Geographic Focus**: Global (Sentinel satellites provide worldwide coverage)
- **Formats**: SAFE format (Sentinel native), GeoTIFF, NetCDF, GRIB, Cloud Optimized GeoTIFF (COG), Zarr, STAC catalog, OGC Web Services (WMS, WCS, WFS)
- **Scale**: Petabytes of satellite data. Sentinel missions produce ~12+ terabytes of data per day. Full archive available.
- **Key Features**:
  - Sentinel-1 (SAR radar), Sentinel-2 (optical), Sentinel-3 (ocean/land), Sentinel-5P (atmosphere) data
  - Copernicus Data Space Ecosystem (new platform replacing Copernicus Open Access Hub)
  - JupyterLab integration for cloud processing
  - openEO API for data processing
  - STAC-based data discovery
- **Licensing**: Free and open access under the Copernicus data policy. Free for any use including commercial, with attribution.
- **Notes**: Copernicus is the EU's flagship Earth observation program and produces some of the most valuable free satellite data in the world. The transition from the old Open Access Hub to the new Copernicus Data Space Ecosystem (2023) modernized access with cloud-native tools. Sentinel-2 optical imagery is...

### Data.CDC.gov (CDC Open Data)
- **URL**: https://data.cdc.gov
- **Operator/Parent**: Centers for Disease Control and Prevention (CDC), U.S. Department of Health and Human Services
- **Type**: Free
- **Pricing**: Completely free. Powered by Socrata/Tyler Data & Insights platform.
- **Data Types**: Disease Surveillance (infectious diseases, chronic diseases), Vaccination & Immunization Data, Mortality & Death Statistics, Environmental Health, Behavioral Risk Factors (BRFSS), Injury Prevention, Reproductive Health, Chronic Disease Indicators, COVID-19 Data, Foodborne Disease Outbreaks, Smoking & Tobacco Use, STDs & HIV/AIDS
- **Industry Focus**: Public Health, Healthcare & Hospitals, Epidemiology, Pharmaceutical & Biotech, Academic Research, Health Insurance, Government Health Policy
- **Geographic Focus**: United States (national, state, county, and sometimes sub-county levels)
- **Formats**: CSV, JSON, XML, RDF, API (SODA/Socrata API), Excel, GeoJSON
- **Scale**: ~1,000+ datasets on the Socrata portal. Additional data available through CDC WONDER and other CDC data systems.
- **Key Features**:
  - SODA API for all datasets
  - Built-in visualization and mapping tools
  - WONDER (Wide-ranging Online Data for Epidemiologic Research)
  - MMWR data (Morbidity and Mortality Weekly Report)
  - COVID-19 Data Tracker integration
- **Licensing**: U.S. Public Domain (federal government works). Some data has use restrictions for privacy protection (suppression of small cell counts).
- **Notes**: The CDC data portal became especially prominent during the COVID-19 pandemic. It provides some of the most authoritative public health data for the United States. CDC WONDER is a separate but related system for more detailed epidemiological queries. Note: some datasets may have been affected by 2...

### Data.gov (US Federal Open Data)
- **URL**: https://data.gov
- **Operator/Parent**: U.S. General Services Administration (GSA), managed by the Technology Transformation Services (TTS)
- **Type**: Free
- **Pricing**: Completely free. No registration required for browsing or downloading. Some APIs may require an API key (free).
- **Data Types**: Agriculture, Business, Climate, Consumer, Ecosystems, Education, Energy, Finance, Health, Local Government, Manufacturing, Maritime, Ocean, Public Safety, Science & Research, Transportation, Weather
- **Industry Focus**: Government & Public Policy, Healthcare & Public Health, Environmental Science, Transportation & Infrastructure, Agriculture, Energy, Education Research, Financial Regulation, Urban Planning
- **Geographic Focus**: United States (federal, state, and local government data)
- **Formats**: CSV, JSON, XML, RDF, XLS/XLSX, KML/KMZ, Shapefile, GeoJSON, PDF, API endpoints
- **Scale**: ~250,000+ datasets harvested from federal agencies (as of 2024-2025). Note: the actual count fluctuates as agencies add/remove datasets.
- **Key Features**:
  - CKAN-based data catalog
  - Metadata harvesting from hundreds of federal agencies
  - RESTful API for programmatic access to the catalog
  - Geospatial data catalog (integrated with GeoPlatform.gov)
  - Dataset request feature
- **Licensing**: Primarily U.S. Public Domain (federal government works are not subject to copyright). Some datasets from state/local sources may have varying licenses. Open Data Policy (M-13-13) governs federal data sharing.
- **Notes**: Data.gov serves as a centralized catalog/index pointing to datasets hosted across hundreds of federal agencies. Many links redirect to agency-specific portals (e.g., CDC, EPA, USDA). The platform was modernized and migrated to a new infrastructure in 2023-2024. Note: Under the 2025 administration...

### Data.gov.uk (UK Open Data Portal)
- **URL**: https://data.gov.uk
- **Operator/Parent**: UK Government Digital Service (GDS), Cabinet Office
- **Type**: Free
- **Pricing**: Completely free. No registration required for most datasets.
- **Data Types**: Business & Economy, Crime & Justice, Defence, Education, Environment, Government, Government Spending, Health, Mapping, Society, Towns & Cities, Transport
- **Industry Focus**: Government & Public Policy, Urban Planning, Transport & Logistics, Healthcare, Environmental Science, Criminal Justice, Education, Real Estate & Property
- **Geographic Focus**: United Kingdom (England, Scotland, Wales, Northern Ireland)
- **Formats**: CSV, JSON, XML, XLS/XLSX, ODS, RDF, Linked Data, Shapefile, GeoJSON, KML, PDF, WMS/WFS (geospatial services)
- **Scale**: ~55,000-60,000 datasets from ~1,000+ publishers (as of 2024-2025)
- **Key Features**:
  - CKAN-based platform
  - SPARQL endpoint for Linked Data queries
  - Organogram visualization (government structure)
  - Spend data publishing
  - Integration with National Information Infrastructure (NII)
- **Licensing**: Primarily Open Government Licence (OGL) v3.0, which is compatible with CC-BY 4.0. Some datasets use specific licenses from Ordnance Survey, Royal Mail, etc.
- **Notes**: One of the pioneering national open data portals, launched in 2010. Includes data from central government, local authorities, and NHS. Some geospatial data (Ordnance Survey) has moved to separate licensing arrangements. The portal has been through several redesigns and platform updates.

### Japan e-Stat
- **URL**: https://www.e-stat.go.jp/en
- **Operator/Parent**: Statistics Bureau of Japan, Ministry of Internal Affairs and Communications
- **Type**: Free
- **Pricing**: Completely free. No registration required for most data. API access requires registration (free).
- **Data Types**: Population & Demographics, Labour & Wages, Agriculture, Forestry & Fisheries, Industry & Commerce, Economy & Finance, Education, Culture & Science, Health & Welfare, Housing & Land, Transport & Tourism, Energy & Environment, Safety & Disaster Prevention, Government & Elections
- **Industry Focus**: Government & Public Policy, Japan Market Research, Academic Research, International Economics
- **Geographic Focus**: Japan (national, prefectural, and municipal levels)
- **Formats**: CSV, Excel, JSON, XML, API (SDMX-based)
- **Scale**: ~750+ statistical datasets covering virtually all aspects of Japanese society and economy
- **Key Features**:
  - Central portal for all official Japanese government statistics
  - API for programmatic access
  - English interface available
  - Statistical maps/GIS
  - Microdata access (for approved research)
- **Licensing**: Government of Japan terms. Generally free for use with attribution under Japan's Open Data policy.
- **Notes**: e-Stat is the comprehensive portal for all official Japanese government statistics. The English interface makes it accessible to international researchers. Japan has been increasing its commitment to open data in recent years.

### Mexico datos.gob.mx
- **URL**: https://datos.gob.mx
- **Operator/Parent**: Government of Mexico
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Government Finance, Health, Education, Public Safety, Economy, Environment & Natural Resources, Agriculture, Energy, Transportation, Demographics
- **Industry Focus**: Government & Public Policy, Latin American Market Research, Academic Research
- **Geographic Focus**: Mexico (federal and some state-level data)
- **Formats**: CSV, JSON, XML, Excel, API (CKAN-based)
- **Scale**: ~40,000+ datasets from federal agencies
- **Key Features**:
  - CKAN-based platform
  - API access
  - Spanish language interface
  - Sector-organized browsing
  - Integration with Mexican transparency laws
- **Licensing**: Open Data Policy of Mexico. Free for any use with attribution.
- **Notes**: Mexico's open data portal aligns with its transparency and open government commitments. Available primarily in Spanish.

### NASA Earthdata
- **URL**: https://earthdata.nasa.gov
- **Operator/Parent**: NASA Earth Science Data Systems (ESDS) Program
- **Type**: Free
- **Pricing**: Completely free. Free Earthdata account required for downloads.
- **Data Types**: Atmosphere (aerosols, clouds, atmospheric chemistry), Land (land cover, vegetation, fire, surface temperature), Ocean (sea surface temperature, ocean color, sea level), Cryosphere (ice sheets, glaciers, sea ice, snow), Calibrated Radiance & Solar Irradiance, Human Dimensions, Climate Indicators, Terrestrial Hydrosphere (soil moisture, groundwater)
- **Industry Focus**: Earth Science & Climate Research, Remote Sensing & GIS, Agriculture & Forestry, Water Resources Management, Disaster Management, Environmental Monitoring, Weather & Climate Modeling, Academic Research
- **Geographic Focus**: Global (Earth observation data covering the entire planet)
- **Formats**: NetCDF/NetCDF-4, HDF4/HDF5, GeoTIFF, Cloud Optimized GeoTIFF (COG), Zarr, CSV, JSON, GML, Various satellite-specific formats
- **Scale**: Over 60 petabytes of Earth science data across 12 DAACs, growing by several petabytes per year. Thousands of data products from hundreds of satellite missions.
- **Key Features**:
  - 12 Distributed Active Archive Centers (DAACs)
  - Earthdata Search (search and discovery tool)
  - CMR (Common Metadata Repository)
  - Worldview (satellite imagery visualization)
  - Earthdata Cloud (data in AWS cloud)
- **Licensing**: U.S. Public Domain. NASA's Earth science data is freely available with no restrictions on use.
- **Notes**: NASA Earthdata is separate from the main data.nasa.gov portal and is specifically focused on Earth observation data. It is one of the world's largest and most comprehensive repositories of Earth science data. The transition to cloud-based data access (Earthdata Cloud) is making it easier to work ...

### NASA Open Data Portal
- **URL**: https://data.nasa.gov
- **Operator/Parent**: National Aeronautics and Space Administration (NASA), U.S. Government
- **Type**: Free
- **Pricing**: Completely free. NASA's open data policy mandates public access. No registration required for most data.
- **Data Types**: Earth Science (satellite imagery, climate, weather), Space Science (astronomy, astrophysics), Planetary Science, Heliophysics (Sun & solar system), Aeronautics, Life Science & Astrobiology, Engineering & Technology, Software (open-source code), Mission Data & Telemetry, Patents & Spinoff Technologies
- **Industry Focus**: Aerospace & Defense, Earth Science & Climate, Astronomy & Astrophysics, Remote Sensing & GIS, Academic Research, Environmental Monitoring, Agriculture (satellite data), Weather Forecasting
- **Geographic Focus**: Global/Universal (Earth observation is global; space data covers the solar system and beyond)
- **Formats**: CSV, JSON, XML, NetCDF, HDF5, GeoTIFF, FITS (astronomy standard), Shapefile, KML, API, Cloud-optimized formats (COG, Zarr)
- **Scale**: data.nasa.gov catalog lists ~40,000+ datasets. NASA Earthdata system holds petabytes of Earth science data. The full NASA data ecosystem is massive across multiple specialized archives.
- **Key Features**:
  - NASA Earthdata (earthdata.nasa.gov) for Earth science data
  - NASA Open APIs (api.nasa.gov) - APOD, Mars Rover Photos, etc.
  - Worldview interactive satellite imagery viewer
  - Giovanni (geospatial data analysis tool)
  - Exoplanet Archive
- **Licensing**: U.S. Public Domain (federal government works). NASA's Open Data Policy ensures free access. Some datasets generated with international partners may have specific sharing agreements.
- **Notes**: NASA's data ecosystem is vast and distributed across many specialized archives and data centers (DAACs - Distributed Active Archive Centers). data.nasa.gov is the main catalog, but significant data resides in Earthdata, PDS, MAST (astronomy), and other specialized systems. The NASA Open APIs are ...

### NOAA Climate Data (National Centers for Environmental Information)
- **URL**: https://www.ncei.noaa.gov
- **Operator/Parent**: National Oceanic and Atmospheric Administration (NOAA), U.S. Department of Commerce
- **Type**: Free
- **Pricing**: Completely free. No registration required for most data. Some bulk data access may require registration.
- **Data Types**: Climate Data (temperature, precipitation, etc.), Weather Observations (stations, radar, satellite), Oceanic Data (sea surface temperature, ocean currents, salinity), Geophysical Data (seismic, geomagnetic, solar-terrestrial), Paleoclimatology (ice cores, tree rings, sediments), Coastal Data, Marine Ecosystems, Severe Weather Events (storms, hurricanes, tornadoes), Sea Level Data, Snow & Ice Data, Atmospheric Composition
- **Industry Focus**: Climate Science & Research, Weather Forecasting, Agriculture, Insurance & Risk Management, Energy (renewable energy planning), Fisheries & Marine Resources, Environmental Consulting, Disaster Preparedness, Aviation, Shipping & Maritime
- **Geographic Focus**: Global (with especially dense coverage in the United States)
- **Formats**: CSV, NetCDF, HDF5, GeoTIFF, GRIB/GRIB2, JSON, XML, Shapefile, API (Climate Data Online API), THREDDS/OPeNDAP, BUFR
- **Scale**: Tens of petabytes of environmental data. NCEI is the world's largest active archive of weather and climate data. Billions of weather observations from stations worldwide.
- **Key Features**:
  - Climate Data Online (CDO) - search and order historical weather data
  - CDO Web Services API (free API key required)
  - International Best Track Archive (IBTrACS) for tropical cyclones
  - Global Historical Climatology Network (GHCN)
  - Storm Events Database
- **Licensing**: U.S. Public Domain (federal government works). Free for any use. Some international data may have specific terms.
- **Notes**: NOAA NCEI (formerly NCDC, NGDC, and NODC - merged in 2015) is the definitive archive for U.S. and global climate/weather data. The NOAA Big Data Program makes large datasets available on commercial cloud platforms (AWS, Google Cloud, Azure) for free. Essential resource for climate research, agric...

### Official Portal for European Data (data.europa.eu)
- **URL**: https://data.europa.eu
- **Operator/Parent**: European Commission, Publications Office of the European Union
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Agriculture, Fisheries, Forestry & Food, Economy & Finance, Education, Culture & Sport, Energy, Environment, Government & Public Sector, Health, International Issues, Justice, Legal System & Public Safety, Population & Society, Regions & Cities, Science & Technology, Transport
- **Industry Focus**: Government & Public Policy, Agriculture & Food, Energy & Utilities, Environmental Science & Climate, Healthcare, Transport & Mobility, Research & Academia, Urban Planning
- **Geographic Focus**: European Union member states and associated countries (pan-European)
- **Formats**: CSV, JSON, XML, RDF/DCAT-AP, XLS/XLSX, PDF, Shapefile, GeoJSON, SPARQL endpoint, API, HTML, ODS
- **Scale**: ~1,600,000+ datasets harvested from 36+ countries and EU institutions (as of 2024-2025). This is a meta-portal aggregating from national portals.
- **Key Features**:
  - Harvests metadata from national open data portals across EU member states
  - SPARQL endpoint for linked data
  - Data quality dashboard (MQA - Metadata Quality Assessment)
  - DCAT-AP metadata standard
  - Multilingual support (24 EU languages)
- **Licensing**: Varies by source country and publisher. Common licenses include CC-BY 4.0, CC0, national open government licenses. The portal's own content is under CC-BY 4.0.
- **Notes**: Formed by merging the European Data Portal and the EU Open Data Portal in 2021. It is the single point of access to public data from EU institutions and EU member states. Includes the European Data Innovation Board outputs and supports the European Data Strategy.

### Open Data Network (Tyler Data & Insights, formerly Socrata)
- **URL**: https://www.opendatanetwork.com
- **Operator/Parent**: Tyler Technologies (acquired Socrata in 2018, formerly Socrata, Inc.)
- **Type**: Free (data access); platform is commercial SaaS
- **Pricing**: Accessing data through the Open Data Network and individual Socrata-powered portals is free. Tyler Technologies sells the Socrata platform to government agencies as a SaaS product. End users access data for free.
- **Data Types**: Government Finance & Budgets, Public Safety & Crime, Transportation & Infrastructure, Health & Human Services, Education, Housing & Development, Environment, Parks & Recreation, Business Licenses & Permits, 311 Service Requests, Geospatial Data, Election & Voting Data
- **Industry Focus**: Government & Civic Tech, Urban Planning, Public Safety, Journalism & Media, Academic Research, Real Estate, Civic Engagement
- **Geographic Focus**: Primarily United States (federal, state, and local government). Some international government portals also use the platform.
- **Formats**: CSV, JSON, XML, RDF, GeoJSON, Shapefile, KML, API (SODA - Socrata Open Data API), Excel, TSV
- **Scale**: The Open Data Network indexes ~170,000+ datasets across thousands of Socrata/Tyler-powered portals. Individual portals range from hundreds to tens of thousands of datasets.
- **Key Features**:
  - SODA (Socrata Open Data API) - powerful query API with SoQL query language
  - Open Data Network - cross-portal search and comparison
  - Built-in data visualization and charting
  - Embeddable widgets
  - Automatic API endpoint generation for every dataset
- **Licensing**: Varies by portal and dataset. Most government data is public domain or open government license. Each portal sets its own terms.
- **Notes**: Socrata (now Tyler Data & Insights) pioneered government open data platforms. Many major U.S. cities (NYC, Chicago, San Francisco, etc.) and states use Socrata-powered portals. The SODA API is one of the most developer-friendly open data APIs available. The Open Data Network provides a unified se...

### OpenDataSoft
- **URL**: https://www.opendatasoft.com
- **Operator/Parent**: OpenDataSoft SAS (French private company)
- **Type**: Both (freemium for portals; data access is free)
- **Pricing**: The OpenDataSoft platform is a SaaS product sold to organizations (cities, companies, etc.) to build their own data portals. The 'Data Hub' (data.opendatasoft.com) provides free access to datasets published on all OpenDataSoft-powered portals. Ind...
- **Data Types**: Smart City / Urban Data, Transportation & Mobility, Environment & Sustainability, Public Services, Health, Energy & Utilities, Culture & Tourism, Commerce & Economy, Real Estate & Housing, Education, Demographics
- **Industry Focus**: Smart Cities & Local Government, Energy & Utilities, Transportation, Real Estate, Retail & Commerce, Media & Publishing
- **Geographic Focus**: Global (especially strong in Europe, particularly France). Powers portals for cities and organizations worldwide.
- **Formats**: CSV, JSON, GeoJSON, Shapefile, KML, Excel, API (ODS API v2), RDF, iCal, RSS
- **Scale**: Powers 300+ open data portals worldwide. The Data Hub indexes 30,000+ datasets from these portals.
- **Key Features**:
  - Data Hub (data.opendatasoft.com) aggregating 30,000+ datasets
  - RESTful API on every portal (automatically generated)
  - Map and chart visualization widgets
  - Data processing pipeline (geocoding, joins, enrichment)
  - Embeddable visualizations
- **Licensing**: Varies by dataset and portal. Common licenses include Open Licence (France), CC-BY, ODbL. Each portal/dataset specifies its own license.
- **Notes**: OpenDataSoft is primarily a platform provider rather than a data source itself. Many cities (especially in France and Europe) use OpenDataSoft to power their open data portals. The aggregated Data Hub is useful for discovering data across all these portals. Strong in smart city and IoT data.

### Registry of Open Data on AWS
- **URL**: https://registry.opendata.aws
- **Operator/Parent**: Amazon Web Services (AWS), Amazon.com, Inc.
- **Type**: Free (data access); compute costs may apply
- **Pricing**: The data itself is free to access and download. Data is hosted on AWS S3 and other services. Egress/transfer costs may apply for very large downloads outside AWS. If you process data using AWS compute services (EC2, SageMaker, etc.), standard AWS ...
- **Data Types**: Genomics & Life Sciences, Climate & Weather, Satellite Imagery & Geospatial, Machine Learning Training Data, Natural Language Processing, Government & Public Sector, Healthcare, Economics & Finance, Transportation, Agriculture, Astronomy, Materials Science, Environmental Science
- **Industry Focus**: Cloud Computing & Data Engineering, Life Sciences & Genomics, Climate & Earth Science, Machine Learning & AI, Geospatial & Remote Sensing, Healthcare & Biomedical Research
- **Geographic Focus**: Global
- **Formats**: Parquet, CSV, JSON, NetCDF, HDF5, GeoTIFF, Cloud Optimized GeoTIFF (COG), Zarr, FASTQ/BAM/VCF (genomics), DICOM (medical imaging), Various cloud-native formats
- **Scale**: ~500+ curated datasets, many of which are massive (petabyte-scale). Includes landmark datasets like Landsat, Sentinel-2, NEXRAD, 1000 Genomes Project, etc.
- **Key Features**:
  - Data hosted on S3 (fast access within AWS ecosystem)
  - Cloud-native/analysis-ready data formats
  - Integration with AWS analytics services (Athena, EMR, SageMaker)
  - Tutorials and example notebooks
  - Open Data Sponsorship Program (AWS covers hosting costs for qualifying datasets)
- **Licensing**: Varies by dataset. Most are open/public domain or CC-licensed. Each dataset specifies its own license. AWS does not impose additional licensing restrictions.
- **Notes**: The Registry of Open Data on AWS is particularly valuable for large-scale data that would be impractical to download locally. Best used within the AWS cloud ecosystem where you can process data near where it is stored. AWS effectively subsidizes the hosting of many important public datasets as pa...

### South Korea data.go.kr
- **URL**: https://www.data.go.kr
- **Operator/Parent**: Government of South Korea, Ministry of the Interior and Safety
- **Type**: Free
- **Pricing**: Completely free. Registration required for API access (free).
- **Data Types**: Public Administration, Science & Technology, Education, Health & Welfare, Industry & Economy, Transportation, Culture & Tourism, Environment, Agriculture & Food, National Safety
- **Industry Focus**: Government & Public Policy, Korean Market Research, Technology & Smart City, Academic Research
- **Geographic Focus**: South Korea
- **Formats**: CSV, JSON, XML, Excel, API (REST), Linked Open Data
- **Scale**: ~80,000+ datasets and 9,000+ open APIs (among the largest in Asia)
- **Key Features**:
  - Open API hub with thousands of API endpoints
  - Linked Open Data
  - Korean language interface (some English support)
  - Data visualization tools
  - Open Data contests and hackathons
- **Licensing**: Korea Open Government License. Free for any use with attribution.
- **Notes**: South Korea is recognized as one of the world leaders in open data (consistently ranked high in the Open Data Barometer and OECD Open Data Index). The portal is exceptionally comprehensive with strong API infrastructure.

### data.gov.au (Australian Government Open Data Portal)
- **URL**: https://data.gov.au
- **Operator/Parent**: Australian Government, Department of Finance / Digital Transformation Agency
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Business & Industry, Communications, Education, Environment, Finance & Economics, Health & Medicine, Law & Justice, People & Communities, Science & Technology, Security & Defence, Transport & Infrastructure, Water, Agriculture & Forestry
- **Industry Focus**: Government & Public Policy, Environmental Science, Healthcare, Agriculture, Mining & Resources, Academic Research
- **Geographic Focus**: Australia (federal, state/territory, and local government data)
- **Formats**: CSV, JSON, XML, GeoJSON, Shapefile, KML, Excel, WMS/WFS, API (CKAN-based), PDF, ESRI REST
- **Scale**: ~95,000+ datasets from federal, state, and local government sources (as of 2024-2025)
- **Key Features**:
  - CKAN-based platform (using CKAN with government extensions)
  - National Map (nationalmap.gov.au) for geospatial visualization
  - Data.gov.au API (CKAN API)
  - Linked data capabilities
  - Integration with state/territory open data portals
- **Licensing**: Primarily Creative Commons Attribution 4.0 (CC-BY 4.0) under the Australian Government's Open Access and Licensing Framework (AusGOAL). Some datasets use CC-BY-SA or other licenses.
- **Notes**: Australia has been a strong proponent of open data. The portal aggregates data from all levels of government. Notable for strong geospatial data holdings and the National Map visualization tool. Environmental and natural resource data is particularly comprehensive given Australia's geography.

### data.gov.in (India Open Government Data Platform)
- **URL**: https://data.gov.in
- **Operator/Parent**: Government of India, National Informatics Centre (NIC), Ministry of Electronics & Information Technology
- **Type**: Free
- **Pricing**: Completely free. Registration may be required for API access and bulk downloads.
- **Data Types**: Agriculture, Commerce & Industry, Defence, Education, Energy & Power, Environment & Forest, Finance, Food & Public Distribution, Health & Family Welfare, Housing & Urban Affairs, Information & Broadcasting, Labour & Employment, Law & Justice, Panchayati Raj (Local Self-Government), Railways, Rural Development, Science & Technology, Social Justice, Statistics, Telecommunications, Transport, Water Resources, Women & Child Development
- **Industry Focus**: Government & Public Policy, Agriculture, Healthcare, Education, Energy, Transportation & Railways, Rural Development, Academic Research
- **Geographic Focus**: India (national, state, and district level data)
- **Formats**: CSV, JSON, XML, XLS/XLSX, API (RESTful), PDF, ODS
- **Scale**: ~500,000+ resources/catalogs from 150+ government departments (as of 2024-2025). India's portal is one of the largest by catalog count globally, though many entries are individual tables/views rather than distinct datasets.
- **Key Features**:
  - RESTful API for programmatic access
  - Visualizations and dashboards
  - Community participation (data requests, ratings)
  - Sector-wise data catalogs
  - Government-to-Citizen (G2C) data services
- **Licensing**: Government Open Data License - India (GODL). Allows free use, including commercial, with attribution. Compatible with CC-BY 4.0.
- **Notes**: India's open data portal is one of the largest in the world by resource count. The National Data Sharing and Accessibility Policy (NDSAP) mandates government data sharing. Data quality can be variable across different ministries and departments. Strong in agricultural and demographic data given I...

---

## 3. International & Multilateral Organization Data

### Eurostat
- **URL**: https://ec.europa.eu/eurostat
- **Operator/Parent**: European Commission, Eurostat (Statistical Office of the European Union)
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Economy & Finance (GDP, inflation, government finance), Population & Social Conditions, Industry, Trade & Services, Agriculture & Fisheries, International Trade, Transport, Environment & Energy, Science, Technology & Digital Society, Regional Statistics, Quality of Life
- **Industry Focus**: Government & Public Policy, Economics & Finance, Market Research, Academic Research, Business Strategy (European markets)
- **Geographic Focus**: European Union member states, EFTA countries, candidate countries, and some partner countries
- **Formats**: CSV/TSV, JSON, SDMX, Excel, API (JSON and SDMX REST API), Bulk download (TSV and SDMX)
- **Scale**: ~7,500+ datasets covering thousands of indicators. Billions of data points with extensive time series (some going back to the 1950s).
- **Key Features**:
  - Eurostat database with interactive data explorer
  - SDMX REST API
  - Statistics Explained (wiki-like explanations of statistics)
  - Data Browser (new interface)
  - Country profiles
- **Licensing**: Eurostat copyright policy allows free reuse for commercial and non-commercial purposes with attribution (similar to CC-BY).
- **Notes**: Eurostat is the primary source for comparable statistics across EU member states. Data follows harmonized methodologies making cross-country comparison reliable. Essential for anyone doing business or research involving European economies. The new Data Browser interface is a significant improveme...

### FAO Data (FAOSTAT)
- **URL**: https://www.fao.org/faostat
- **Operator/Parent**: Food and Agriculture Organization of the United Nations (FAO)
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Agricultural Production (crops, livestock), Food Balances & Supply, Trade (imports/exports of agricultural commodities), Food Security & Nutrition, Land Use & Irrigation, Agri-Environmental Indicators, Emissions (agriculture-related greenhouse gases), Forestry, Fisheries & Aquaculture, Prices (producer, consumer, trade), Investment (government expenditure on agriculture), Population & Employment in Agriculture
- **Industry Focus**: Agriculture & Food, International Development, Environmental Science, Commodity Trading, Food Policy, Academic Research, NGO & Humanitarian
- **Geographic Focus**: Global (245+ countries and territories)
- **Formats**: CSV, Excel, API (FAOSTAT API / FENIX-based), Bulk download, JSON
- **Scale**: Over 20,000 indicators across 245+ countries/territories. Time series data from 1961 to present for many indicators.
- **Key Features**:
  - FAOSTAT database (comprehensive agricultural statistics)
  - API for programmatic access
  - Interactive data visualization and mapping
  - Country profiles
  - Compare data tool
- **Licensing**: CC BY-NC-SA 3.0 IGO for most FAO data. Free for non-commercial use with attribution. Some datasets have specific terms.
- **Notes**: FAOSTAT is the world's most comprehensive source of food and agriculture statistics. Essential for research on global food security, agricultural trade, and environmental impacts of agriculture. Data quality is high with standardized methodologies, though some developing country data may have gaps.

### Federal Reserve Economic Data (FRED)
- **URL**: https://fred.stlouisfed.org
- **Operator/Parent**: Federal Reserve Bank of St. Louis, U.S. Federal Reserve System
- **Type**: Free
- **Pricing**: Completely free. Free API key available for programmatic access.
- **Data Types**: Monetary & Financial Data (interest rates, money supply), National Accounts (GDP, income, spending), Employment & Labor Markets, Prices & Inflation (CPI, PPI, PCE), International Data (exchange rates, trade), Banking & Financial Institutions, Housing & Real Estate, Production & Business Activity, Population & Demographics, Government Finances (debt, deficits), Academic/Research Data
- **Industry Focus**: Economics & Finance, Banking & Financial Services, Investment & Asset Management, Government & Central Banking, Academic Research, Journalism & Media, Real Estate
- **Geographic Focus**: Primarily United States, with some international economic data
- **Formats**: CSV, JSON, XML, Excel, FRED API (RESTful), ALFRED (vintage/revision data)
- **Scale**: ~800,000+ time series from 100+ sources. One of the most comprehensive free economic data platforms in the world.
- **Key Features**:
  - FRED API (free, robust, well-documented)
  - Interactive charting and graphing
  - GeoFRED (mapping economic data geographically)
  - ALFRED (Archival FRED - historical data revisions)
  - FRASER (historical economic documents)
- **Licensing**: FRED data is free to use. Individual data series have terms from their original sources. Most U.S. government-sourced data is public domain. Attribution to FRED and original source is requested.
- **Notes**: FRED is widely considered the best free tool for U.S. economic and financial data. It aggregates data from BLS, BEA, Census, Treasury, Federal Reserve, and many other sources into a single, easy-to-use platform. The charting and API tools are exceptionally well-designed. Used extensively by econo...

### Humanitarian Data Exchange (HDX)
- **URL**: https://data.humdata.org
- **Operator/Parent**: United Nations Office for the Coordination of Humanitarian Affairs (OCHA), Centre for Humanitarian Data
- **Type**: Free
- **Pricing**: Completely free. Registration required to upload but not to download.
- **Data Types**: Crisis/Emergency Response Data, Population & Demographics (in crisis contexts), Food Security & Nutrition, Health (disease outbreaks, health facilities), Displacement & Migration (refugees, IDPs), Infrastructure (roads, buildings, facilities), Coordination & Logistics, Education, Water, Sanitation & Hygiene (WASH), Protection & Human Rights, Geospatial/Administrative Boundaries, Poverty & Socioeconomic, Climate & Weather Hazards
- **Industry Focus**: Humanitarian Aid & Relief, International Development, Disaster Response & Preparedness, Public Health (crisis contexts), Refugee & Migration Studies, Conflict Analysis, NGO & Nonprofit Sector, Academic Research
- **Geographic Focus**: Global, with emphasis on countries affected by humanitarian crises (Sub-Saharan Africa, Middle East, South/Southeast Asia, etc.)
- **Formats**: CSV, Excel (XLS/XLSX), JSON, GeoJSON, Shapefile, KML, XML, Zipped archives, API (CKAN-based)
- **Scale**: ~20,000+ datasets from 1,500+ organizations covering 250+ locations (as of 2024-2025)
- **Key Features**:
  - CKAN-based platform customized for humanitarian data
  - HDX API for programmatic access
  - Quick Charts (automatic visualization)
  - HDX Connect (data request matching)
  - Humanitarian Exchange Language (HXL) tagging standard
- **Licensing**: Varies by dataset. Common licenses: CC-BY, CC-BY-SA, HDX-specific licenses. Some datasets have humanitarian use restrictions. The platform encourages open licensing.
- **Notes**: HDX is the go-to platform for humanitarian data. It is essential for aid organizations, researchers, and journalists working on crisis response. Data comes from UN agencies, NGOs, governments, and other humanitarian actors. The HXL tagging standard is an innovation for making humanitarian data mo...

### IMF Data
- **URL**: https://data.imf.org
- **Operator/Parent**: International Monetary Fund (IMF)
- **Type**: Free
- **Pricing**: Most data is free. Some specialized databases or early-access data may be restricted to member country officials.
- **Data Types**: Balance of Payments, Direction of Trade Statistics, Government Finance Statistics, International Financial Statistics, World Economic Outlook, Exchange Rates, Commodity Prices, Financial Soundness Indicators, Fiscal Monitor Data, External Debt Statistics, Climate Finance Data
- **Industry Focus**: Economics & Finance, Central Banking & Monetary Policy, International Trade, Government & Public Policy, Academic Research, Investment & Risk Analysis
- **Geographic Focus**: Global (190 member countries)
- **Formats**: CSV, Excel, SDMX (JSON and XML), API (SDMX REST API), PDF reports
- **Scale**: Multiple major databases covering 190 countries with extensive time series. International Financial Statistics alone covers 32,000+ time series.
- **Key Features**:
  - IMF Data Warehouse / IMF Data Portal
  - SDMX REST API
  - DataMapper (interactive visualization tool)
  - World Economic Outlook database (forecasts)
  - Article IV consultation data
- **Licensing**: IMF Terms and Conditions. Data is generally free for research, educational, and journalistic use with attribution. Commercial redistribution may require permission.
- **Notes**: The IMF is the authoritative source for international monetary and financial statistics. Its World Economic Outlook forecasts are among the most watched economic projections globally. Data quality is very high with standardized methodologies across countries.

### OECD Data
- **URL**: https://data.oecd.org
- **Operator/Parent**: Organisation for Economic Co-operation and Development (OECD)
- **Type**: Free (mostly)
- **Pricing**: Most data is freely accessible. Some publications and detailed databases (via OECD.Stat / OECD Data Explorer) may require institutional subscriptions for full access. Individual indicators and standard datasets are free.
- **Data Types**: Agriculture, Development, Economy (GDP, Inflation, Trade, etc.), Education, Energy, Environment, Finance, Government, Health, Innovation & Technology, Jobs & Labour, Society (Income Inequality, Well-being), Tax, Trade, Transport
- **Industry Focus**: Government & Public Policy, Economics & Finance, Education Policy, Healthcare Policy, Tax Policy, International Trade, Labor Markets, Academic Research
- **Geographic Focus**: OECD member countries (38 members as of 2025) plus key partner economies. Primarily developed/advanced economies.
- **Formats**: CSV, SDMX (JSON and XML), Excel, API (RESTful, SDMX-based), Interactive charts/dashboards
- **Scale**: ~800+ datasets covering thousands of indicators across 38+ countries. Billions of data points in the full OECD.Stat system.
- **Key Features**:
  - OECD Data Explorer (new platform replacing OECD.Stat)
  - RESTful API based on SDMX standard
  - Interactive data visualization and charting
  - Country comparisons and rankings
  - Leading economic indicators
- **Licensing**: OECD Terms and Conditions apply. Data can generally be used freely for non-commercial purposes with attribution. Commercial use may require a license. Specific terms vary by dataset.
- **Notes**: The OECD has been transitioning from the older OECD.Stat platform to the new OECD Data Explorer. Data is particularly strong for comparative analysis across developed economies. The OECD produces some of the most cited economic and social indicators (e.g., PISA scores, Better Life Index, leading ...

### UNdata
- **URL**: https://data.un.org
- **Operator/Parent**: United Nations Statistics Division (UNSD)
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Population & Demographics, Economic Statistics (National Accounts, Trade), Social Statistics (Education, Health, Crime), Environment & Energy, Agriculture, Industry, Science & Technology, Tourism, Gender Statistics, Millennium/Sustainable Development Goals, Human Development, Commodity Trade Statistics, National Accounts
- **Industry Focus**: International Development, Government & Public Policy, Academic Research, Demographics & Population Studies, Economics, Environmental Science, Human Rights & Social Justice
- **Geographic Focus**: Global (all UN member states, ~193 countries)
- **Formats**: CSV, XML, Excel, PDF, API (SDMX-based)
- **Scale**: ~60+ databases from 30+ UN system organizations, containing millions of data records across hundreds of indicators
- **Key Features**:
  - Aggregates data from 30+ UN agencies and international organizations
  - UNdata API (based on SDMX standard)
  - Glossary of statistical terms
  - Country profiles
  - SDG Indicators Global Database
- **Licensing**: Generally free for use with attribution to the United Nations. Specific databases may have their own terms. UN Statistical Databases terms of use apply.
- **Notes**: UNdata is a gateway to a wide range of UN statistical databases. It provides a single entry point to search across databases maintained by different UN agencies (FAO, WHO, UNESCO, UNICEF, etc.). Some specialized UN data portals offer more detailed data in their specific domains (e.g., FAOSTAT for...

### WHO Global Health Observatory (GHO)
- **URL**: https://www.who.int/data/gho
- **Operator/Parent**: World Health Organization (WHO)
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Mortality & Burden of Disease, Infectious Diseases (HIV, TB, Malaria, etc.), Non-communicable Diseases, Risk Factors (Tobacco, Alcohol, Obesity, etc.), Health Systems & Financing, Immunization & Vaccines, Maternal & Child Health, Nutrition, Environmental Health, Water & Sanitation, Mental Health, Health Workforce, Essential Medicines, Universal Health Coverage, SDG Health-related Indicators, COVID-19 data
- **Industry Focus**: Public Health, Healthcare, Pharmaceutical & Biotech, Epidemiology, Global Health Policy, Academic Research, NGO & Humanitarian
- **Geographic Focus**: Global (194 WHO member states)
- **Formats**: CSV, JSON, XML, Excel, API (OData-based GHO API), Interactive visualizations
- **Scale**: ~2,300+ indicators across 194 countries with time series data. Covers key global health topics comprehensively.
- **Key Features**:
  - GHO OData API for programmatic access
  - Interactive data visualizations and maps
  - Country health profiles
  - Thematic data pages
  - World Health Statistics annual publication data
- **Licensing**: CC BY-NC-SA 3.0 IGO for most WHO content. Data can be used freely for non-commercial purposes with attribution. Specific datasets may have additional terms.
- **Notes**: The GHO is the WHO's main health data and statistics repository. It is the authoritative source for global health indicators. Data quality is generally high, with standardized methodologies for cross-country comparison. The COVID-19 pandemic significantly expanded WHO's data sharing infrastructure.

### World Bank Open Data
- **URL**: https://data.worldbank.org
- **Operator/Parent**: The World Bank Group (international financial institution)
- **Type**: Free
- **Pricing**: Completely free. Open access policy adopted in 2010. No registration required for most data.
- **Data Types**: Economic Indicators (GDP, GNI, trade, etc.), Poverty & Inequality, Education Statistics, Health, Nutrition & Population, Gender Statistics, Agriculture & Rural Development, Climate Change, Energy & Mining, Environment, Financial Sector, Infrastructure, Private Sector Development, Public Sector & Governance, Science & Technology, Social Protection & Labor, Trade, Urban Development, Water & Sanitation, Debt Statistics
- **Industry Focus**: International Development, Economics & Finance, Public Policy, Healthcare & Public Health, Education, Agriculture, Climate & Environment, Academic Research, NGO & Nonprofit Sector
- **Geographic Focus**: Global (217 economies/countries, with special focus on developing nations)
- **Formats**: CSV, XML, JSON, Excel (XLS/XLSX), API (RESTful), SDMX, Databank online query tool
- **Scale**: ~20,000+ indicators across 217 economies. The Microdata Library contains 5,000+ surveys. Multiple databases including WDI, International Debt Statistics, Doing Business (archived), etc.
- **Key Features**:
  - World Development Indicators (WDI) - flagship dataset
  - RESTful API (v2) for programmatic access
  - DataBank interactive query tool with visualization
  - Time series data spanning decades (1960s-present for many indicators)
  - Country profiles and dashboards
- **Licensing**: Creative Commons Attribution 4.0 (CC-BY 4.0) for most datasets under the Open Data initiative. Some third-party data may have restrictions. Terms of Use require attribution.
- **Notes**: One of the most authoritative sources for international development data. The World Bank's Open Data initiative (launched 2010) was a landmark in making development data freely available. Data quality is generally very high with consistent methodology across countries and years. The DataBank tool...

---

## 4. Specialized Commercial Data Marketplaces

### Acxiom (now a division of IPG / Kinesso)
- **URL**: https://www.acxiom.com
- **Operator/Parent**: Interpublic Group (IPG) - Acxiom was acquired by IPG in 2018 for $2.3B. Now operates under IPG's Kinesso marketing intelligence unit.
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise licensing with custom pricing based on data products, volume, segments, and use case. Data enrichment priced per record. Audience segments priced on CPM basis for advertising. Annual contracts typical.
- **Data Types**: Consumer demographic data, Identity data/identity resolution, Purchase behavior data, Lifestyle/interest data, Financial indicators, Household composition data, Automotive data (vehicle ownership), Real property data, Digital identity data, Audience segments for advertising
- **Industry Focus**: Marketing/advertising, Financial services, Retail/e-commerce, Healthcare marketing, Telecommunications, Automotive marketing, Travel/hospitality, Insurance
- **Geographic Focus**: Primarily US, with operations in UK and several other markets
- **Formats**: Acxiom Real Identity platform, API integrations, Batch file delivery, LiveRamp and other identity graph integrations, Direct activation to advertising platforms, CRM enrichment, Data clean rooms
- **Scale**: Data on 2.5B+ consumers globally, with particularly deep coverage of 300M+ US adults/250M+ US adults with rich attributes. [Based on training data, may need verification]
- **Key Features**:
  - One of the oldest and largest consumer data companies (founded 1969)
  - InfoBase - massive consumer database covering virtually all US households
  - Real Identity - identity resolution platform
  - PersonicX - consumer segmentation system (70+ clusters)
  - Deep data on US consumers - 2,500+ attributes per individual
- **Provider Requirements**: Not a two-sided marketplace. Acxiom aggregates data from public records, surveys, purchase data partnerships, and proprietary collection methods.
- **Status**: Active (as IPG/Kinesso division)
- **Notes**: Acxiom sold its marketing technology platform (now Kinesso) separately from its data business, then was itself acquired by IPG. One of the 'Big 3' consumer data companies alongside Experian and Oracle Data Cloud (now retired). Pioneering company in consumer data compilation. Privacy practices hav...

### Bloomberg Enterprise Data
- **URL**: https://www.bloomberg.com/professional/solution/data-and-content/
- **Operator/Parent**: Bloomberg L.P. (privately held, majority owned by Michael Bloomberg)
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise licensing with custom pricing. Per-user terminal licenses (~$24,000/year per Bloomberg Terminal seat, which includes data). Enterprise data feeds/APIs priced separately based on data products, volume, and distribution rights. Multi-year...
- **Data Types**: Real-time and historical market data (equities, fixed income, commodities, FX, derivatives), Company fundamentals and financial statements, Economic/macro data, ESG data, Alternative data, Credit ratings and risk data, Reference/entity data, News and sentiment data, Regulatory/compliance data, Municipal bond data, Index data, Pricing/valuation data
- **Industry Focus**: Investment banking, Asset management, Hedge funds, Insurance, Central banks, Corporate treasury, Wealth management, Risk management, Compliance/regulatory
- **Geographic Focus**: Global - comprehensive worldwide coverage of financial markets
- **Formats**: Bloomberg Terminal (proprietary desktop), Bloomberg Data License (B-PIPE for real-time, SAPI, Per Security), Bloomberg Enterprise Access Point, REST and proprietary APIs (BLPAPI), Bulk file delivery (CSV, XML), Snowflake integration [Based on training data, may need verification], Cloud delivery (Bloomberg Data License in cloud)
- **Scale**: 325,000+ terminal subscribers. Covers virtually all publicly traded securities globally, millions of fixed income instruments, comprehensive derivatives coverage. Revenue estimated at $12B+ annually. [Based on training data, may need verification]
- **Key Features**:
  - Gold standard in financial data - 325,000+ terminal subscribers globally
  - Unmatched breadth and depth of financial data coverage
  - Bloomberg Terminal is an integrated analytics, communication, and data platform
  - Proprietary data collection and verification processes
  - Real-time data feeds with ultra-low latency options
- **Provider Requirements**: Not a two-sided marketplace. Bloomberg is the data provider. Some third-party data is distributed via Bloomberg (alternative data providers can partner to distribute through Bloomberg Enterprise). ...
- **Notes**: Bloomberg is the dominant force in financial data. The Terminal is ubiquitous in finance. Enterprise Data products allow programmatic access outside the terminal. Pricing is premium but considered essential infrastructure for financial institutions. Competes primarily with Refinitiv/LSEG and S&P ...

### Crunchbase
- **URL**: https://www.crunchbase.com
- **Operator/Parent**: Crunchbase Inc. (San Francisco, CA). Originally part of TechCrunch/AOL, spun out in 2015.
- **Type**: Both - limited free access; paid subscriptions for full data
- **Pricing**: Freemium. Free: basic company profiles. Starter ($29/month), Pro ($49/month), Enterprise (custom). API and data licensing for enterprise/bulk access at higher price points.
- **Data Types**: Startup/company data, Funding rounds and investment data, Investor profiles, M&A data, IPO data, Leadership/people data, Company financials (limited), Industry/technology tags
- **Industry Focus**: Venture capital, Private equity, Startup ecosystem, Sales prospecting, Market research, Competitive intelligence
- **Geographic Focus**: Global, strongest coverage for US tech/startup ecosystem
- **Formats**: Web-based platform, REST API, CSV exports, Salesforce integration, Bulk data licensing, Advanced search and filtering
- **Scale**: Profiles on 1M+ companies, 500K+ people, 200K+ investors. Comprehensive funding data going back decades.
- **Key Features**:
  - Definitive database of startup/VC ecosystem
  - Tracks funding rounds, acquisitions, IPOs globally
  - Company relationship mapping (investors, board members, etc.)
  - Trend analysis for funding by sector/geography
  - Sales intelligence features
- **Status**: Active and profitable. Dominant platform for startup/VC data. Continuously expanding data coverage.
- **Notes**: Crunchbase has evolved from a simple TechCrunch directory to a major data platform. Competes with PitchBook (Morningstar) in private market data, though PitchBook is more comprehensive for institutional use.

### Crunchbase (Data Licensing)
- **URL**: https://www.crunchbase.com
- **Operator/Parent**: Crunchbase, Inc. (independent; originally spun out of AOL/TechCrunch)
- **Type**: Both - Free basic access; paid Pro/Enterprise plans; data licensing for bulk access
- **Pricing**: Tiered SaaS subscription: Free (limited), Starter (~$29/mo), Pro (~$49/mo), Enterprise (custom). Data licensing/API access for bulk commercial use is separately priced (typically $20K-$100K+/year for enterprise data licensing). [Based on training ...
- **Data Types**: Startup/company profiles, Funding rounds and investment data, Investor profiles (VC, PE, angel), Acquisition/M&A data, IPO data, Company leadership/people data, Technology/industry categorization, Company financials (revenue estimates for some), News/events, Diversity/inclusion data for companies
- **Industry Focus**: Venture capital/private equity, Startup ecosystem, Sales/business development (prospecting), Investment banking, Corporate development/M&A, Recruiting, Journalism/media, Academic research
- **Geographic Focus**: Global with strongest coverage in US, Europe, and major startup hubs worldwide
- **Formats**: Web application (search and browse), REST API, Bulk CSV/Excel exports (Pro and Enterprise), Data licensing via flat files or API, Salesforce integration, Snowflake Data Sharing [Based on training data, may need verification], Enterprise data feeds
- **Scale**: Data on 1M+ companies, 200K+ funding rounds, hundreds of thousands of investors. [Based on training data, may need verification]
- **Key Features**:
  - Definitive database of startups, funding, and venture capital
  - Community-contributed and editorially verified data
  - Advanced search/filtering (Pro+)
  - Alerts and saved searches for tracking companies/investors
  - Crunchbase Marketplace (third-party integrations)
- **Provider Requirements**: Not a two-sided data marketplace. Crunchbase collects data through community contributions, partnerships, web crawling, and editorial processes. Companies can claim/update their own profiles.
- **Notes**: Crunchbase is the de facto standard database for startup/VC ecosystem data. Data licensing is a major revenue stream beyond the SaaS product. Competes with PitchBook, CB Insights, and Dealroom in the venture data space. Increasingly positioning as a B2B prospecting tool beyond its startup data ro...

### Demyst
- **URL**: https://www.demyst.com
- **Operator/Parent**: Demyst Data Ltd. (independent, New York-based)
- **Type**: Paid - Enterprise focused
- **Pricing**: Platform subscription plus per-query/per-record data enrichment costs. Enterprise custom pricing. Data costs depend on the providers accessed and volume of enrichment. Platform acts as a single API to multiple data providers.
- **Data Types**: KYC/identity verification data, Business verification data, Credit/financial risk data, Fraud detection data, Property/real estate data, Business firmographic data, Consumer data, Alternative credit data, Compliance/sanctions data, Insurance-relevant data
- **Industry Focus**: Banking/financial services (primary), Insurance, Compliance/RegTech, Lending/credit, Fraud prevention
- **Geographic Focus**: Global, with strong focus on US, UK, Australia, and Asia-Pacific
- **Formats**: Demyst API (unified API to access multiple providers), Demyst Platform (data catalog and discovery), Batch enrichment, Real-time API calls, Cloud deployment, Flat file delivery
- **Scale**: Connects to hundreds of data providers. Serves major banks and financial institutions. [Based on training data, may need verification]
- **Key Features**:
  - Single API gateway to hundreds of external data providers
  - Focus on financial services data needs (KYC, credit, fraud)
  - Data catalog for discovering relevant data sources
  - Compliance-first approach (SOC 2, GDPR-focused)
  - Data quality monitoring and provider comparison
- **Provider Requirements**: Two-sided: Data providers can integrate with Demyst's platform to reach financial services customers. Demyst handles distribution, billing, and compliance. Provider must meet data quality and secur...
- **Notes**: Demyst solves a specific pain point for banks and insurers: instead of managing dozens of data vendor relationships, they provide a single platform to discover, test, and access multiple external data sources. Strong in the financial services data orchestration niche. Less of a marketplace in the...

### Dun & Bradstreet (D&B)
- **URL**: https://www.dnb.com
- **Operator/Parent**: Dun & Bradstreet Holdings, Inc. (publicly traded: DNB on NYSE). Taken private by consortium in 2019, re-IPO'd in 2020.
- **Type**: Both - Limited free lookups; paid for full access and data products
- **Pricing**: Tiered subscription plans. SMB plans start at hundreds/month. Enterprise data licensing custom-priced (typically $50K-$500K+/year depending on scope). API access priced per call or subscription. DUNS number registration is free for businesses.
- **Data Types**: Business firmographic data (company name, address, industry codes), DUNS Number (universal business identifier), Financial data (revenue, employees, financial stress scores), Credit ratings and risk scores (D&B Rating, PAYDEX), Beneficial ownership data, Corporate linkage/hierarchy data, Compliance/regulatory data, Supplier risk data, Contact data (decision-makers), Industry classifications (SIC, NAICS), Small business data
- **Industry Focus**: B2B sales/marketing, Credit/risk management, Supply chain/procurement, Compliance/KYC, Financial services, Government contracting, Insurance underwriting
- **Geographic Focus**: Global - data on 500M+ business entities across 200+ countries
- **Formats**: D&B Direct+ API (REST), D&B Hoovers (online platform for sales/marketing), Batch file delivery (CSV, XML), Salesforce/CRM integrations, D&B Connect (data management platform), Third-party distribution (Snowflake, AWS Data Exchange), Master data enrichment services
- **Scale**: 500M+ business entities globally, 170M+ in detailed database. Used by 90% of Fortune 500. [Based on training data, may need verification]
- **Key Features**:
  - DUNS Number - the universal business identifier used by millions of organizations globally
  - 180+ year history (founded 1841) - longest-operating commercial data provider
  - Global business database covering 500M+ entities
  - Corporate linkage trees (parent-subsidiary relationships)
  - D&B PAYDEX score - leading commercial credit score
- **Provider Requirements**: Not a two-sided marketplace. D&B collects data from trade payment data, public filings, company self-reports, web crawling, and a network of global data partners.
- **Notes**: D&B is the foundational B2B data company. The DUNS Number is effectively a universal business ID (used by governments, lenders, and enterprises globally). Competes with Bureau van Dijk (Moody's), Experian Business, and Equifax Commercial. After going private in 2019 and re-listing in 2020, the co...

### Experian Data Products
- **URL**: https://www.experian.com/business/data
- **Operator/Parent**: Experian plc (publicly traded: EXPN on London Stock Exchange)
- **Type**: Both - Free consumer credit reports (annual); paid business/marketing data products
- **Pricing**: Varied by product line: Consumer credit data (regulated, priced per pull). Marketing data (subscription and per-record enrichment). Business credit data (subscription or per-report). Audience segments (CPM-based). Enterprise licensing custom-priced.
- **Data Types**: Consumer credit data (credit reports, scores), Business credit data, Marketing data (ConsumerView, demographics), Identity verification data, Property/real estate data, Automotive data (VIN, registration), Audience segments for advertising, Fraud prevention data, Email/digital identity data, Health data (claims, patient demographics)
- **Industry Focus**: Financial services/banking, Marketing/advertising, Healthcare, Automotive, Real estate/mortgage, Insurance, Telecommunications, Retail, Government
- **Geographic Focus**: Global - operates in 40+ countries. Major markets: US, UK, Brazil, APAC
- **Formats**: Experian APIs (various product-specific APIs), Bulk data delivery (batch files), Platform integrations (Salesforce, etc.), Experian Marketing Services platform, Direct advertising platform activation, Data clean rooms, Snowflake integration, Experian Ascend analytics platform
- **Scale**: Credit data on 1.4B+ people and 200M+ businesses globally. ConsumerView covers 300M+ US consumers, 126M+ households. Annual revenue ~$7B. [Based on training data, may need verification]
- **Key Features**:
  - One of the three major credit bureaus (with Equifax and TransUnion)
  - ConsumerView - comprehensive marketing database (300M+ US consumers)
  - Mosaic segmentation system (consumer lifestyle segments)
  - CrossCore - fraud and identity platform
  - Experian Ascend - analytics sandbox for credit data
- **Provider Requirements**: Not a two-sided marketplace. Experian is the data provider, collecting from credit furnishers (lenders, utilities), public records, and proprietary sources.
- **Notes**: Experian is a data giant with roots in credit reporting but has expanded significantly into marketing data, identity, and healthcare. The marketing data division (ConsumerView, Mosaic) competes with Acxiom and Oracle Data Cloud. Credit data access is heavily regulated (FCRA in US, similar regulat...

### Foursquare
- **URL**: https://foursquare.com
- **Operator/Parent**: Foursquare Labs, Inc. (independent, privately held). Merged with Factual (location data company) in 2020.
- **Type**: Both - Free tier for developers (limited); paid for commercial/enterprise use
- **Pricing**: Tiered API pricing for Places/location data. Enterprise licensing for advertising/analytics products. Pay-as-you-go API calls for developers. Custom enterprise pricing for large-scale location intelligence, foot traffic, and advertising products.
- **Data Types**: Points of interest (POI) / Places data, Foot traffic / visit data, Location-based audience segments, Movement/mobility patterns, Consumer visit attribution, Geofencing data, Chain/brand location data, Location context/categorization
- **Industry Focus**: Advertising/marketing (location-based advertising), Retail (site selection, competitive analysis), Real estate, Financial services (alternative data), Mapping/navigation apps, Travel/hospitality, CPG, Automotive (connected car)
- **Geographic Focus**: Global - POI data covering 200+ countries; foot traffic data strongest in US
- **Formats**: Foursquare Places API, Foursquare Studio (geospatial visualization, formerly Unfolded), Foursquare Proximity (geofencing SDK), Foursquare Attribution, Bulk data licensing (CSV, JSON, Parquet), Snowflake/AWS Data Exchange, Advertising platform integrations
- **Scale**: 100M+ POI globally, 14B+ user-confirmed check-ins, 500M+ device panel for foot traffic. [Based on training data, may need verification]
- **Key Features**:
  - 100M+ POI globally (one of the largest independent POI databases)
  - First-party location data from Foursquare/Swarm apps plus massive SDK network
  - Foursquare Studio - geospatial analytics and visualization platform (acquired Unfolded/deck.gl)
  - Visit attribution for measuring real-world impact of ads
  - Hex Tiles - proprietary spatial indexing system
- **Provider Requirements**: Not a two-sided marketplace. Foursquare collects location data through its consumer apps (Foursquare City Guide, Swarm), SDK partnerships with thousands of apps, and the former Factual data assets.
- **Notes**: Foursquare pivoted from a consumer check-in app to a B2B location data and technology company. The Factual merger consolidated two major location data players. Foursquare is now one of the largest independent location data companies, competing with SafeGraph/Dewey, Placer.ai, and Near. The acquis...

### Gravy Analytics (formerly UberMedia)
- **URL**: https://gravyanalytics.com
- **Operator/Parent**: Gravy Analytics Inc. (Dulles, VA)
- **Type**: Paid - enterprise/data licensing
- **Pricing**: Enterprise data licensing and SaaS platform. Custom pricing based on data volume, geography, and use case.
- **Data Types**: Consumer location/mobility data, Foot traffic analytics, Audience segments based on real-world behavior, Points of interest visitation data, Event attendance data, Trade area analytics
- **Industry Focus**: Advertising/marketing, Retail analytics, Real estate, Government/public sector, Alternative data for investment
- **Geographic Focus**: Primarily United States
- **Formats**: API access, Data feeds, Platform analytics (AdmitOne), Audience segment activation to ad platforms, Bulk data licensing
- **Scale**: Processes billions of location signals. Covers US retail and commercial locations.
- **Key Features**:
  - Location intelligence from mobile device data
  - Verified visit attribution (confirms actual store visits)
  - Event detection and attendance measurement
  - Consumer audience segments based on real-world behavior
  - Privacy-focused processing of location data
- **Status**: Active. Has been involved in FTC investigations regarding location data privacy practices. Continues to operate but under increased regulatory scrutiny. Suffered a data breach in early 2025.
- **Notes**: Gravy Analytics has faced regulatory and security challenges. The FTC has scrutinized location data companies broadly, and Gravy was part of this examination. A January 2025 data breach exposed consumer location data, raising further privacy concerns. This is representative of broader industry ch...

### Gravy Analytics (now part of Unacast)
- **URL**: https://www.unacast.com
- **Operator/Parent**: Unacast (merged with or acquired Gravy Analytics) [Based on training data, may need verification on exact corporate structure]
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise subscription licensing. Custom pricing based on data products, geography, and use case.
- **Data Types**: Location/mobility data, Foot traffic analytics, Consumer movement patterns, Points of interest visits, Advertising audience segments (location-based), Migration patterns
- **Industry Focus**: Retail, Real estate, Advertising, Financial services, Government/public sector
- **Geographic Focus**: US primarily, some global coverage
- **Formats**: Platform analytics, API access, Bulk data delivery, Advertising platform activation
- **Scale**: Billions of location signals. [Based on training data, may need verification]
- **Key Features**:
  - Location data with strong focus on data quality and verification
  - Consumer movement analytics
  - Advertising audience segments based on real-world behavior
  - Combined assets of Unacast and Gravy Analytics
- **Provider Requirements**: Not a two-sided marketplace. Collects data through SDK partnerships.
- **Status**: Active (as Unacast, following Gravy Analytics integration) [Based on training data, may need verification]
- **Notes**: The location data market has seen significant consolidation. Gravy Analytics and Unacast combining follows the pattern of Foursquare/Factual merger. This space faces increasing privacy regulation scrutiny. [Based on training data, may need verification on current corporate details]

### LiveRamp Data Marketplace
- **URL**: https://liveramp.com/data-marketplace/
- **Operator/Parent**: LiveRamp Holdings, Inc. (publicly traded: RAMP on NYSE)
- **Type**: Paid - enterprise/advertising industry
- **Pricing**: Enterprise licensing and per-segment/per-record pricing. Costs depend on data type, volume, and use case. Typically sold as part of broader LiveRamp platform engagement. CPM-based pricing for audience segments in advertising use cases.
- **Data Types**: Audience/consumer segments, Identity data (deterministic and probabilistic), Purchase behavior data, Demographic data, Interest/intent data, B2B firmographic data, TV viewership data, Automotive/in-market data, Health/wellness segments (privacy-safe), Audience data segments, Consumer demographics, Intent data, Location-based segments, Identity resolution data
- **Industry Focus**: Advertising/marketing (primary), Media/publishing, Retail, Financial services, Automotive, CPG, Healthcare marketing, Digital advertising, Marketing, Audience targeting, Identity resolution, AdTech/MarTech
- **Geographic Focus**: Primarily US, with growing international presence (UK, France, Australia, Japan)
- **Formats**: LiveRamp IdentityLink/RampID integration, Direct activation to 500+ marketing platforms, Data clean room access (via LiveRamp partnerships), API, Cloud-based delivery, Identity resolution (IdentityLink/AbiliTEC), Data marketplace for audience segments, Direct activation to advertising platforms, Clean room collaboration, Cloud-based data connectivity
- **Scale**: Hundreds of data providers, reaching hundreds of millions of US consumers. LiveRamp's identity graph covers 250M+ US adults [Based on training data, may need verification]
- **Key Features**:
  - Built on LiveRamp's identity graph (RampID) - deterministic people-based identity resolution
  - Privacy-safe data collaboration via clean rooms
  - Direct activation to major advertising platforms (Google, Facebook, Trade Desk, etc.)
  - Third-party data providers sell through the marketplace with identity resolution built in
  - Safe Haven technology for privacy-preserving data collaboration
- **Provider Requirements**: Data providers must meet LiveRamp's data quality and privacy standards. Data is onboarded and matched to LiveRamp's identity graph. Revenue share between LiveRamp and providers.
- **Status**: Active. Publicly traded. Evolving from identity resolution to broader data collaboration platform.
- **Notes**: LiveRamp is primarily an identity resolution company; the data marketplace is a key product but sits within the broader identity/connectivity platform. Post-cookie deprecation concerns have actually strengthened LiveRamp's position as a deterministic identity provider. The marketplace is deeply i...

### Lotame
- **URL**: https://www.lotame.com
- **Operator/Parent**: Lotame Solutions, Inc. (independent, privately held, Maryland-based)
- **Type**: Paid
- **Pricing**: SaaS subscription for the DMP/CDP platform. Data marketplace pricing based on CPM for audience segments. Enterprise custom pricing. Platform fees plus data activation costs.
- **Data Types**: Audience data/segments, Behavioral/interest data, Demographic data, Intent data, B2B audience data, Contextual data, Identity data (Panorama ID), Cross-device identity, Second-party data (via data collaboration)
- **Industry Focus**: Advertising/AdTech, Media/publishing, Marketing agencies, CTV/streaming, Retail media
- **Geographic Focus**: Global - operations in US, Europe, APAC, LATAM. Particular strength outside US (often positioned as alternative to larger US-centric platforms)
- **Formats**: Lotame Spherical platform (DMP/CDP), Panorama ID (identity solution for cookieless), Direct activation to 50+ demand-side platforms, Curated marketplaces/PMPs, API access, Data collaboration/clean room tools
- **Scale**: Reaches 4B+ device IDs globally. Marketplace includes billions of audience records. [Based on training data, may need verification]
- **Key Features**:
  - One of the first independent DMPs (data management platforms)
  - Panorama ID - cookieless identity solution (people-based ID)
  - Global data marketplace with audience segments from publishers worldwide
  - Strong in emerging markets and international markets
  - Curation tools for publishers to monetize their data
- **Provider Requirements**: Two-sided: Publishers and data owners can make their audience data available through the Lotame marketplace. Lotame handles identity resolution, audience packaging, and distribution. Revenue share ...
- **Notes**: Lotame is a veteran in the DMP/data marketplace space, now transitioning to a CDP + data collaboration model. Their Panorama ID is their answer to the deprecation of third-party cookies. Strong international presence (often called the leading independent DMP outside the walled gardens). The compa...

### Near (Near Intelligence / Azira)
- **URL**: https://near.com
- **Operator/Parent**: Near Intelligence Inc. Was publicly traded (SPAC in 2022), then faced financial difficulties. Rebranded key assets as Azira. [Based on training data, may need verification - Near went through significant corporate turbulence]
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise subscription licensing. Custom pricing based on markets, data volume, and use case. Platform access plus data licensing fees. [Based on training data, may need verification]
- **Data Types**: Location/mobility data, Foot traffic patterns, Consumer behavioral data, Audience segments (location-based), Demographic data, Points of interest data, Movement/commute patterns, Visit attribution
- **Industry Focus**: Advertising/marketing, Retail (site selection), Real estate, Government/public sector, Urban planning, Financial services, Tourism
- **Geographic Focus**: Global - claimed coverage in 44 countries with particular strength in Southeast Asia, India, Middle East, and US
- **Formats**: Near Platform (cloud-based analytics), API access, Audience activation to advertising platforms, Custom reports and analytics, Bulk data delivery, Data clean rooms
- **Scale**: Claimed 1.6B device IDs, coverage in 44 countries. [Based on training data, may need verification - company faced credibility questions]
- **Key Features**:
  - One of the largest location data companies globally (by geographic coverage)
  - Strong coverage in emerging markets (SE Asia, India, Middle East)
  - Allspark intelligence platform
  - Privacy-focused data collection methodology
  - Combined location intelligence with advertising activation
- **Provider Requirements**: Not a two-sided marketplace. Near collects location data through SDK partnerships and data licensing agreements.
- **Status**: Uncertain/Troubled - Near Intelligence went public via SPAC in 2022, then faced financial difficulties, leadership changes, and questions about data scale claims. Some assets may have been rebranded as Azira. [Based on training data, may need verification - status is actively changing]
- **Notes**: CAUTION: Near Intelligence went through significant corporate turbulence after its SPAC listing. There were reports of financial misstatements, leadership departures, and operational difficulties. The company's future status is uncertain. Some operational assets appear to continue under the Azira...

### Nielsen
- **URL**: https://www.nielsen.com
- **Operator/Parent**: Nielsen Holdings plc. Was publicly traded, then taken private by consortium led by Evergreen Coast Capital and Brookfield Business Partners in 2022 for ~$16B. Nielsen split into two companies: Nielsen (media/audience measurement) and NielsenIQ (consumer/retail data, sold to Advent International).
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise subscription licensing. Custom pricing based on markets, categories, and data granularity. Annual contracts, often multi-year. Costs range from tens of thousands to millions annually depending on scope. Nielsen ratings/audience data is ...
- **Data Types**: TV/video audience measurement (ratings), Digital audience measurement, Audio/podcast measurement, Cross-platform measurement, Advertising effectiveness/ROI data, Consumer panel data (via NielsenIQ - now separate), Retail scanner/POS data (via NielsenIQ - now separate), Sports/esports viewership, Social media content measurement (Gracenote)
- **Industry Focus**: Media/broadcasting, Advertising agencies, Streaming platforms, CPG/FMCG (via NielsenIQ), Retail (via NielsenIQ), Sports/entertainment, Publishing
- **Geographic Focus**: Global - audience measurement in 55+ countries, NielsenIQ in 90+ countries
- **Formats**: Nielsen ONE (cross-platform measurement platform), Nielsen Media Impact (planning tool), APIs and data feeds, Custom reports and analytics, Dashboard/portal access, Gracenote content recognition data, Flat file delivery
- **Scale**: Measures media consumption for hundreds of millions of people globally. Nielsen ratings cover 100% of US TV universe. NielsenIQ covers 90+ markets. [Based on training data, may need verification]
- **Key Features**:
  - Industry-standard TV ratings (Nielsen ratings are the currency of TV advertising)
  - Nielsen ONE - next-gen cross-platform measurement
  - Gracenote - content recognition and metadata
  - People Meter panels for audience measurement
  - NielsenIQ (now separate) - gold standard for CPG/retail market data
- **Provider Requirements**: Not a two-sided marketplace. Nielsen collects measurement data through panels, metering technology, and return-path data partnerships.
- **Status**: Active (private since 2022). IMPORTANT: Nielsen (media measurement) and NielsenIQ (consumer/retail) are now separate companies. [Based on training data, may need verification on latest corporate structure]
- **Notes**: The Nielsen split is important: Nielsen focuses on media audience measurement; NielsenIQ (owned by Advent International) focuses on consumer/retail measurement. Nielsen ratings remain the standard currency for TV ad buying despite competition from Comscore, VideoAmp, and iSpot. The company went t...

### Placer.ai
- **URL**: https://www.placer.ai
- **Operator/Parent**: Placer Labs, Inc. (independent, Israeli-American company)
- **Type**: Both - Free basic dashboard; paid for full analytics and data access
- **Pricing**: Freemium SaaS. Free tier provides limited location analytics. Pro and Enterprise plans priced based on features, locations tracked, and data access. Enterprise custom pricing. Annual contracts for full platform access. [Based on training data, may...
- **Data Types**: Foot traffic/visitation data, Consumer visit patterns, Trade area analytics, Migration/movement patterns, Cross-shopping behavior, Visitor demographics, Void analysis (underserved areas), Retail chain performance data
- **Industry Focus**: Retail (primary), Commercial real estate, Restaurants/food service, Shopping centers/malls, Municipalities/economic development, CPG, Financial services
- **Geographic Focus**: Primarily US
- **Formats**: Placer.ai web platform (interactive dashboards), API access, Reports and exports (CSV, PDF), Custom analytics
- **Scale**: Tracks millions of locations in the US. Used by thousands of retail, CRE, and restaurant companies. [Based on training data, may need verification]
- **Key Features**:
  - Intuitive, consumer-friendly UI for location analytics
  - Free tier drives viral adoption
  - Strong focus on retail/CRE use cases
  - Competitive benchmarking across retail chains
  - Trade area and void analysis
- **Provider Requirements**: Not a two-sided marketplace. Placer.ai collects location data from SDK partnerships and mobile app integrations.
- **Status**: Active - growing rapidly
- **Notes**: Placer.ai has emerged as a strong competitor in the location analytics space, differentiating through a user-friendly interface and freemium model. The free tier has driven strong viral adoption in the commercial real estate and retail industries. Competes with SafeGraph/Dewey, Foursquare, Unacas...

### Precisely Data Experience (formerly Data.World Enterprise / Precisely Data Integrity Suite)
- **URL**: https://www.precisely.com/product/precisely-data-experience
- **Operator/Parent**: Precisely (owned by Clearlake Capital and TA Associates, private equity)
- **Type**: Both - Free community tier; paid for enterprise features
- **Pricing**: Free tier: unlimited public datasets, community features, basic querying. Paid tiers: data.world for Business/Enterprise with private datasets, advanced governance, integrations, collaboration. Enterprise pricing is custom/contact sales.
- **Data Types**: Government & Politics, Health & Healthcare, Environment & Energy, Business & Finance, Education, Science & Research, Social Sciences, Sports, Transportation, Technology, Agriculture, Arts & Culture, Address/location data (address validation, geocoding), Geospatial/boundary data, Property/parcel data, Demographic/consumer data, Points of interest (POI), Risk/insurance data (flood zones, natural hazards), Business firmographic data, Data enrichment datasets, Street-level routing data, Open/public datasets (community-uploaded), Government data, Internal enterprise data (via catalog), Any structured data format, Knowledge graphs
- **Industry Focus**: Data Science & Analytics, Government & Civic Tech, Healthcare, Finance, Research & Academia, Enterprise Data Governance (paid tier), Insurance, Financial services, Real estate, Government, Telecommunications, Retail/CPG, Utilities, Data science/analytics community, Government/public sector, Enterprise data governance, Academic research, Non-profit/social impact
- **Geographic Focus**: Global - data available for 250+ countries and territories, particularly strong in US, UK, Australia
- **Formats**: CSV, TSV, JSON, Excel, RDF, SPARQL queryable, API access, Parquet, Linked Data
- **Scale**: Thousands of enterprise customers. Data covering 250+ countries. Billions of location/address records globally [Based on training data, may need verification]
- **Key Features**:
  - Built-in SQL and SPARQL query engine
  - Data integration/joining across datasets
  - RESTful API and Python/R SDKs
  - Collaborative workspaces (projects)
  - Data cataloging and metadata management
- **Provider Requirements**: Not a two-sided marketplace. Precisely is the primary data provider, offering its own proprietary and licensed datasets through the Data Experience platform.
- **Licensing**: Varies by dataset. Uploaders choose licenses (CC0, CC-BY, PDDL, ODC-BY, etc.). Platform terms of service apply.
- **Notes**: Data.world straddles the line between an open data community (like Kaggle) and an enterprise data catalog (like Alation). The community platform is free and hosts significant open/public data. The enterprise product is a data catalog and governance platform. Different from most platforms on this ...

### Refinitiv / LSEG Data (London Stock Exchange Group Data & Analytics)
- **URL**: https://www.lseg.com/en/data-analytics
- **Operator/Parent**: London Stock Exchange Group (LSEG) - acquired Refinitiv in January 2021 for $27B. Refinitiv was previously the Financial & Risk division of Thomson Reuters.
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise licensing with custom pricing. Per-user desktop licenses (Eikon/Workspace ~$12,000-$22,000/year per seat). Data feeds and APIs priced based on content, volume, and redistribution rights. Multi-year enterprise agreements. Costs range wid...
- **Data Types**: Real-time and historical market data, Company fundamentals and financials, ESG data (one of the largest ESG datasets), Economic data, Deals/M&A data, Ownership/holdings data, Reference data (identifiers, symbology - RIC, SEDOL, etc.), News (Reuters News), Regulatory/compliance data (World-Check for KYC/AML), Fixed income/credit data, Commodities data, FX data (including FX trading venues)
- **Industry Focus**: Investment banking, Asset management, Hedge funds, Corporate treasury, Risk/compliance, Wealth management, Insurance, Central banks/government
- **Geographic Focus**: Global - comprehensive worldwide coverage
- **Formats**: LSEG Workspace (desktop application, formerly Eikon), Refinitiv Real-Time feeds (Elektron), Refinitiv Data Platform APIs (REST, WebSocket, streaming), DataScope (bulk data delivery), Tick History (historical tick data), Snowflake integration, Cloud delivery (AWS, Azure, GCP), Flat files (CSV, XML, JSON)
- **Scale**: 400,000+ customer professionals across 190 countries. Data covering millions of instruments from 400+ exchanges. [Based on training data, may need verification]
- **Key Features**:
  - Second-largest financial data provider globally (behind Bloomberg)
  - World-Check - leading KYC/AML screening database
  - Comprehensive ESG data with 12,000+ companies scored
  - Lipper fund data (mutual fund analytics)
  - I/B/E/S earnings estimates
- **Provider Requirements**: Not a two-sided marketplace. LSEG/Refinitiv is the data provider, aggregating from exchanges, companies, and proprietary collection. Some third-party data distributed via the platform.
- **Status**: Active (operating as LSEG Data & Analytics; Refinitiv branding being phased out)
- **Notes**: The Refinitiv brand is being gradually replaced by LSEG branding following the acquisition. Historically the #2 financial data terminal (Eikon) behind Bloomberg. The LSEG acquisition creates a vertically integrated exchange-data powerhouse. Strong in FX (largest electronic FX trading platform) an...

### S&P Global Market Intelligence
- **URL**: https://www.spglobal.com/marketintelligence/
- **Operator/Parent**: S&P Global Inc. (publicly traded: SPGI on NYSE). Merged with IHS Markit in 2022.
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise subscription licensing. Custom pricing based on products, users, and data scope. Desktop platform (Capital IQ) priced per seat (~$15,000-$24,000/year). Data feeds, APIs, and bulk data priced separately. Total enterprise spend can range ...
- **Data Types**: Company fundamentals and financials (including private companies), Credit ratings (S&P Ratings), M&A/deals data, Private equity/VC data, Debt capital markets data, Industry research and analysis, Supply chain data, Commodities/energy data (Platts, via IHS Markit), Real-time market data, ESG/sustainability data, Economic/country data, Ownership/holders data, Transcripts and filings, Automotive data (via IHS Markit)
- **Industry Focus**: Investment banking, Private equity, Corporate finance, Insurance, Banking/lending, Energy/commodities, Automotive, Government/policy, Academic research
- **Geographic Focus**: Global - comprehensive coverage of public and private companies worldwide
- **Formats**: S&P Capital IQ desktop platform, S&P Capital IQ Pro (next-gen platform), APIs (REST, Excel add-in), Data feeds (XML, CSV, bulk), Snowflake/cloud delivery, Xpressfeed (legacy bulk data), Excel plug-ins
- **Scale**: Data on 68,000+ public companies, millions of private companies. 99% of global market capitalization covered. $13B+ annual revenue for S&P Global overall. [Based on training data, may need verification]
- **Key Features**:
  - Deepest coverage of private company financials globally
  - Comprehensive M&A/deals database (Compustat, Capital IQ)
  - Integrated credit ratings (S&P's own ratings)
  - Platts commodity pricing (from IHS Markit merger)
  - Supply chain relationship mapping
- **Provider Requirements**: Not a two-sided marketplace. S&P Global collects and produces data through proprietary processes, regulatory filings, partnerships, and acquisitions.
- **Notes**: The 2022 merger with IHS Markit made S&P Global a data behemoth, adding commodities (Platts), automotive, and other verticals. Capital IQ is the primary competitor to Bloomberg Terminal and Refinitiv Eikon for financial professionals. Compustat data is the gold standard for academic finance resea...

---

## 5. AI/ML Dataset Platforms

### Appen (formerly Figure Eight / CrowdFlower)
- **URL**: https://appen.com
- **Operator/Parent**: Appen Limited (Sydney, Australia). Publicly traded on ASX (APX). Has faced significant financial challenges.
- **Type**: Paid - enterprise/project-based
- **Pricing**: Project-based and enterprise contracts for data annotation and collection services. Pricing varies by task complexity, volume, and turnaround time. Managed workforce model.
- **Data Types**: Training data for AI/ML, Image/video annotation, Text annotation and classification, Audio transcription and annotation, Search relevance judgments, Content moderation data, Multilingual data collection
- **Industry Focus**: AI/ML training, Search engines, Social media/content moderation, Autonomous vehicles, Virtual assistants/NLP, E-commerce
- **Geographic Focus**: Global - crowd workforce in 170+ countries. Multilingual capabilities.
- **Formats**: Managed data annotation services, Appen Platform for task management, API integration, Custom data collection projects, Various ML-standard output formats
- **Scale**: Global crowd of 1M+ annotators. Major clients include FAANG companies. Revenue of several hundred million USD (though declining).
- **Key Features**:
  - One of the largest AI training data companies globally
  - 1 million+ crowd contributors worldwide
  - Multilingual/multicultural data capabilities
  - Acquired Figure Eight (CrowdFlower) in 2019
  - Government/defense contracts
- **Status**: Active but facing significant challenges. Revenue declining as major tech clients bring labeling in-house. Stock price has dropped substantially from peak. Exploring strategic alternatives as of 2024.
- **Notes**: Appen has been severely impacted by the trend of large tech companies building in-house data labeling operations and by competition from Scale AI. The company has been in a restructuring phase. Historically one of the most important AI training data companies.

### Hugging Face (Platform - broader than just Datasets)
- **URL**: https://huggingface.co
- **Operator/Parent**: Hugging Face Inc. (New York, NY)
- **Type**: Both - free for public usage; Pro and Enterprise tiers for advanced features
- **Pricing**: Hub is free for public models/datasets/spaces. Pro ($9/month), Enterprise Hub (custom). Inference Endpoints, AutoTrain, and Spaces hardware are paid compute services.
- **Data Types**: ML models, Datasets, Interactive demos (Spaces), Model cards/documentation
- **Industry Focus**: AI/ML across all sectors
- **Geographic Focus**: Global
- **Formats**: Git-based model and dataset hosting, Transformers library integration, Inference API, Spaces for interactive demos
- **Scale**: 500,000+ public models. 100,000+ datasets. Millions of users. Dominant ML platform.
- **Key Features**:
  - The GitHub of machine learning
  - Hub for models, datasets, and Spaces
  - Open-source libraries (Transformers, Diffusers, etc.)
  - Community of 500,000+ models and 100,000+ datasets
- **Status**: Active. Valued at $4.5B+ (as of 2023 funding round).
- **Notes**: Already covered in detail under Hugging Face Datasets entry. Included here for completeness as the broader platform context.

### Hugging Face Datasets
- **URL**: https://huggingface.co/datasets
- **Operator/Parent**: Hugging Face Inc. (New York, NY). Venture-backed AI startup valued at ~$4.5B as of 2023.
- **Type**: Both - mostly free community datasets; Hugging Face Pro/Enterprise subscriptions for additional features
- **Pricing**: Community datasets are free to upload and access. Hugging Face Hub is free for public repos. Pro accounts ($9/month) for private datasets and additional compute. Enterprise Hub for organizations with custom pricing. Dataset hosting is free for pub...
- **Data Types**: NLP/text datasets, Computer vision datasets, Audio/speech datasets, Multimodal datasets, Tabular datasets, Reinforcement learning datasets, Any ML/AI training data
- **Industry Focus**: AI/ML research, NLP, Computer vision, Speech/audio AI, Academic research, AI startups
- **Geographic Focus**: Global
- **Formats**: Hugging Face Datasets library (Python), Direct download from Hub, Streaming mode (no full download needed), Parquet/Arrow format (native), CSV, JSON, text, images, audio, Git LFS for large files, Dataset viewer in browser, API access
- **Scale**: 100,000+ public datasets. Millions of monthly users. The de facto standard hub for ML datasets. Hosts some of the most important AI training datasets.
- **Key Features**:
  - Largest open ML dataset hub with 100,000+ datasets
  - Python datasets library for easy loading and processing
  - Dataset cards with documentation, licenses, and usage instructions
  - Streaming mode for processing datasets without full download
  - Dataset viewer for browsing data in the browser
- **Status**: Active and rapidly growing. Dominant platform for ML dataset sharing. Continuously adding features.
- **Notes**: Hugging Face has become the 'GitHub of machine learning' and its Datasets hub is the primary way ML researchers share and access training data. Key datasets hosted include GLUE, SQuAD, Common Voice, LAION, and thousands more. The company's broader platform includes Models, Spaces, and Inference E...

### Kaggle Datasets
- **URL**: https://www.kaggle.com/datasets
- **Operator/Parent**: Kaggle (San Francisco, CA). Acquired by Google in 2017.
- **Type**: Free (with optional paid compute tiers)
- **Pricing**: Datasets are free to browse, download, and use. Kaggle offers free compute (GPU/TPU notebooks with weekly quotas). No premium tier for dataset access specifically. Kaggle competitions may have prize money but participation is free.
- **Data Types**: Machine Learning & AI, Computer Vision / Image Data, Natural Language Processing / Text Data, Tabular / Structured Data, Time Series, Geospatial, Audio, Video, Healthcare & Biomedical, Finance & Economics, Social Science, Sports, Gaming, Government, Education, Environment, Business, Arts & Entertainment, ML/AI training datasets, Tabular/structured data, Image datasets, NLP/text datasets, Time series data, Competition datasets, Diverse community-uploaded data
- **Industry Focus**: Data Science & Machine Learning, Healthcare & Life Sciences, Finance & Fintech, Retail & E-commerce, Technology, Energy, Agriculture, Education, Sports Analytics, Social Science Research, Data science, ML/AI, Education/learning, Competitions, Academic research
- **Geographic Focus**: Global (community-contributed datasets from worldwide sources)
- **Formats**: CSV, JSON, SQLite, Parquet, Images (PNG, JPG, DICOM), Text files, HDF5, Pickle, Excel, TSV, GeoJSON, Audio (WAV, MP3), Video files, Custom/various
- **Scale**: 200,000+ public datasets. 15M+ registered users. One of the largest data science communities globally.
- **Key Features**:
  - Integrated Jupyter notebooks (Kaggle Kernels) with free GPU/TPU
  - Dataset versioning
  - Community discussions and forums per dataset
  - Usability ratings for datasets
  - Kaggle API (Python package) for programmatic download
- **Licensing**: Varies per dataset. Common licenses: CC0, CC-BY 4.0, CC-BY-SA 4.0, CC-BY-NC-SA 4.0, GPL, Apache 2.0, Open Database License, 'Other' (custom). Each dataset specifies its own license. Some competition datasets have restricted licenses.
- **Status**: Active. Continues to grow under Google ownership. Major platform for data science learning and competition.
- **Notes**: Kaggle is the world's largest data science community. While not a government open data portal, it is one of the most popular places to find, share, and work with datasets. Quality varies widely since datasets are community-contributed. Many datasets are mirrors/copies of data from other portals. ...

### LAION (Large-scale Artificial Intelligence Open Network)
- **URL**: https://laion.ai
- **Operator/Parent**: LAION e.V. (non-profit, Germany)
- **Type**: Free - open-source datasets
- **Pricing**: Completely free and open source. Non-profit organization. Funded by donations and compute sponsorships (Stability AI was a major sponsor).
- **Data Types**: Image-text pair datasets for AI training, LAION-5B (5 billion image-text pairs), LAION-400M, Audio datasets (LAION-AI/audio), CLIP embeddings
- **Industry Focus**: AI/ML research, Generative AI (image generation), Computer vision, Multimodal AI
- **Geographic Focus**: Global (web-sourced data)
- **Formats**: Parquet files with URLs and metadata (not images themselves), Hugging Face hosting, Direct download, img2dataset tool for downloading images, Pre-computed CLIP embeddings
- **Scale**: LAION-5B: 5.85 billion image-text pairs. One of the largest open datasets ever created for AI training.
- **Key Features**:
  - Created LAION-5B, one of the largest open image-text datasets
  - Used to train Stable Diffusion and other major generative AI models
  - Open-source and freely available
  - Community-driven research organization
  - CLIP-based filtering and curation
- **Status**: Complicated. The datasets were temporarily taken down in late 2023/early 2024 after reports of CSAM (child sexual abuse material) being found in the dataset. LAION conducted safety reviews and re-released filtered versions. Legal challenges from copyright holders ongoing. The organization continues but faces scrutiny.
- **Notes**: LAION's datasets were foundational for the generative AI revolution (Stable Diffusion). The CSAM discovery and copyright lawsuits (from Getty Images and others) have created significant controversy. Highlights the challenges of large-scale web-scraped datasets.

### Labelbox
- **URL**: https://labelbox.com
- **Operator/Parent**: Labelbox Inc. (San Francisco, CA)
- **Type**: Both - free tier available; paid plans for larger projects
- **Pricing**: Freemium SaaS. Free tier for small projects. Starter, Growth, and Enterprise tiers with increasing labeling volume, team size, and feature access. Pricing starts at hundreds/month.
- **Data Types**: Image labeling/annotation, Video annotation, Text/NLP annotation, Document annotation, Geospatial/satellite imagery annotation, Medical imaging annotation
- **Industry Focus**: Computer vision, NLP/AI, Autonomous vehicles, Defense, Healthcare/medical AI, Agriculture, Geospatial
- **Geographic Focus**: Global
- **Formats**: Cloud-based labeling platform, API, Model-assisted labeling, Export in standard ML formats, Integration with ML frameworks and cloud storage
- **Scale**: Used by enterprises and AI teams globally. Competitor to Scale AI in the labeling space.
- **Key Features**:
  - Collaborative data labeling platform
  - Model-assisted labeling (AI pre-labels, humans review)
  - Catalog - data management and curation
  - Active learning for efficient labeling
  - Workforce management (internal teams + managed services)
- **Status**: Active. Well-funded startup (raised $200M+ total). Growing as AI training data demand increases.
- **Notes**: Labelbox competes with Scale AI, Appen, and others in the data labeling market. Differentiates with a focus on the end-to-end data engine (curation, labeling, model evaluation) rather than just labeling services.

### Papers with Code Datasets
- **URL**: https://paperswithcode.com/datasets
- **Operator/Parent**: Papers with Code (acquired by Meta/Facebook AI Research in 2020)
- **Type**: Free - open index of ML datasets linked to academic papers
- **Pricing**: Completely free. Community-maintained index. Does not host data directly but links to where datasets can be obtained.
- **Data Types**: ML benchmark datasets, Computer vision datasets, NLP datasets, Speech datasets, Medical imaging datasets, Any dataset referenced in ML research papers
- **Industry Focus**: ML/AI research, Academic benchmarking, Computer vision, NLP
- **Geographic Focus**: Global academic and research community
- **Formats**: Web-based catalog/index, Links to original dataset sources, Benchmark leaderboards, Dataset descriptions and paper references
- **Scale**: Indexes thousands of datasets with links to papers and benchmarks. Comprehensive coverage of ML research datasets.
- **Key Features**:
  - Links datasets to research papers and benchmark results
  - Leaderboards showing state-of-the-art results on each dataset
  - Community-maintained and curated
  - Task-based organization (image classification, object detection, etc.)
  - Dataset usage statistics (which papers use which datasets)
- **Status**: Active. Maintained by Meta AI. Continuously updated by community contributions.
- **Notes**: Papers with Code is primarily an index/catalog rather than a data hosting platform. Its unique value is linking datasets to papers, code, and benchmark results in a unified interface. Essential resource for ML researchers choosing datasets and benchmarks.

### Roboflow
- **URL**: https://roboflow.com
- **Operator/Parent**: Roboflow Inc. (Des Moines, IA / distributed)
- **Type**: Both - free tier for public projects; paid plans for private projects and advanced features
- **Pricing**: Freemium. Free: 10,000 source images, 3 projects (public). Starter: ~$249/month. Growth and Enterprise tiers with increasing limits. Roboflow Universe (community datasets) is free to browse and use.
- **Data Types**: Computer vision datasets (labeled images), Object detection datasets, Image classification datasets, Instance segmentation datasets, Semantic segmentation datasets, Keypoint detection datasets
- **Industry Focus**: Computer vision, Manufacturing/quality inspection, Agriculture, Sports analytics, Autonomous vehicles, Retail, Healthcare imaging, Security/surveillance
- **Geographic Focus**: Global
- **Formats**: Roboflow platform (cloud-based annotation and training), Multiple export formats (YOLO, COCO, Pascal VOC, TFRecord, etc.), API access to datasets, Hosted inference API, Roboflow Universe for community datasets, Pre-trained models
- **Scale**: Roboflow Universe hosts 200,000+ public computer vision datasets. Platform used by tens of thousands of developers. Rapidly growing.
- **Key Features**:
  - End-to-end computer vision pipeline (annotate, train, deploy)
  - Roboflow Universe - community repository of 200,000+ public datasets
  - Auto-labeling with foundation models
  - Data augmentation built-in
  - Export to 30+ annotation formats
- **Status**: Active and growing rapidly. Well-funded startup. Has become a leading platform for computer vision development.
- **Notes**: Roboflow is both a dataset marketplace (via Universe) and a full computer vision development platform. The community aspect (Universe) with public datasets is a strong differentiator. Increasingly integrating foundation models (SAM, CLIP) for auto-labeling.

### Scale AI (Scale Data Engine / Scale Catalog)
- **URL**: https://scale.com
- **Operator/Parent**: Scale AI Inc. (San Francisco, CA). Founded by Alexandr Wang. Valued at ~$14B as of 2024.
- **Type**: Paid - enterprise/project-based
- **Pricing**: Enterprise and project-based pricing. Data labeling services priced per task/label. Scale Data Engine platform is enterprise subscription. RLHF and evaluation products are custom-priced. Government contracts are a significant revenue stream.
- **Data Types**: Labeled/annotated data for AI training, Image annotation (bounding boxes, segmentation, etc.), Lidar point cloud annotation, Text/NLP annotation, Audio transcription/annotation, Video annotation, RLHF (human feedback) data, Generative AI evaluation data
- **Industry Focus**: Autonomous vehicles, Defense/government, Generative AI, Robotics, E-commerce, Financial services, Healthcare AI
- **Geographic Focus**: Global - headquartered in US with labeling workforce worldwide
- **Formats**: Cloud platform (Scale Data Engine), API for submitting labeling tasks, Various annotation formats (COCO, KITTI, etc.), Integration with ML frameworks, Scale Catalog for pre-labeled datasets, Custom data pipelines
- **Scale**: One of the highest-valued AI infrastructure companies (~$14B valuation). Hundreds of millions in revenue. Labeled data for most major autonomous vehicle and AI companies.
- **Key Features**:
  - Industry-leading AI data labeling platform
  - Human-in-the-loop data annotation at scale
  - Scale Data Engine for active learning and data curation
  - RLHF services for LLM fine-tuning
  - Government/defense contracts (cleared operations)
- **Status**: Active and rapidly growing. Major government/defense contracts. Expanding from labeling into broader AI infrastructure.
- **Notes**: Scale AI started as a data labeling company but has expanded into a broader AI data platform. Works with major AV companies (Toyota, GM), tech companies, and the US military. The RLHF business for LLM training is a significant growth area.

### UCI Machine Learning Repository
- **URL**: https://archive.ics.uci.edu
- **Operator/Parent**: University of California, Irvine, School of Information and Computer Sciences
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Classification Datasets, Regression Datasets, Clustering Datasets, Time Series, Text/NLP Data, Image Data, Multivariate Data, Sequential Data, Recommender Systems Data
- **Industry Focus**: Machine Learning & AI Research, Data Science Education, Academic Research, Statistics
- **Geographic Focus**: Global (academic dataset repository)
- **Formats**: CSV, Data files (custom text formats), ARFF (Weka), JSON, Various tabular formats
- **Scale**: ~660+ datasets (as of 2024-2025). Focused on quality and citation impact rather than quantity.
- **Key Features**:
  - One of the oldest and most cited ML dataset repositories (since 1987)
  - Well-documented datasets with metadata
  - Standardized dataset descriptions (task type, attribute info, etc.)
  - Recently redesigned website with modern interface
  - API access
- **Licensing**: Varies by dataset. Many are CC-BY 4.0. Donated datasets specify their own terms. The repository encourages open licensing.
- **Notes**: The UCI ML Repository is a cornerstone of machine learning research. Many classic and widely-cited datasets originated here (Iris, Wine, Adult/Census Income, etc.). The recent redesign modernized the platform with better search, APIs, and metadata. Despite its relatively small size compared to Ka...

### arXiv Dataset / Papers with Code
- **URL**: https://paperswithcode.com/datasets
- **Operator/Parent**: Papers with Code (Meta AI / Facebook Research, community-driven)
- **Type**: Free
- **Pricing**: Completely free. Community-curated catalog of ML/AI datasets.
- **Data Types**: Machine Learning Benchmark Datasets, Computer Vision (image classification, object detection, segmentation), Natural Language Processing (text, question answering, translation), Speech & Audio, Reinforcement Learning, Graphs & Networks, Time Series, Tabular Data, Medical/Biomedical, Robotics
- **Industry Focus**: Machine Learning & AI Research, Computer Vision, Natural Language Processing, Academic Research
- **Geographic Focus**: Global
- **Formats**: Varies by dataset - catalog links to original sources, Common formats: Images, Text files, JSON, CSV, HDF5, TFRecord, various
- **Scale**: ~8,000+ datasets cataloged with benchmark results and paper linkages (as of 2024-2025)
- **Key Features**:
  - Links datasets to papers and benchmarks
  - Leaderboards for benchmarks (state-of-the-art results)
  - Task-organized browsing (e.g., image classification, machine translation)
  - Links to code implementations
  - Modality and task filtering
- **Licensing**: Varies by dataset. The catalog itself is community-maintained. Individual datasets have their own licenses.
- **Notes**: Papers with Code is invaluable for ML researchers as it links datasets, papers, code, and benchmark results. It is a discovery/catalog tool - actual datasets are hosted elsewhere. Acquired by Meta (Facebook) but remains open and community-driven.

---

## 6. Academic & Research Data Repositories

### Dryad
- **URL**: https://datadryad.org
- **Operator/Parent**: Dryad Digital Repository (non-profit, headquartered in Durham, NC). Operated by Dryad organization.
- **Type**: Free to access. Publishing fees for depositors (often covered by institutions or journal agreements).
- **Pricing**: Free to access/download. Data Publishing Charges (DPCs) for depositing data: approximately $150 per dataset for institutionally-sponsored depositors, up to $350+ for unsponsored. Many institutions and journals cover costs. Institutional membership...
- **Data Types**: Research data underlying peer-reviewed publications, Tabular data, Genomic/biological data, Ecological data, Any research data tied to publication
- **Industry Focus**: Academic research, Life sciences, Ecology, Evolutionary biology, Biomedical research
- **Geographic Focus**: Global academic community, strong in US and Europe
- **Formats**: Direct file download, REST API, DOI assignment, Integration with journal submission workflows, CC0 (public domain) licensing by default
- **Scale**: Tens of thousands of curated datasets. Primarily focused on data associated with peer-reviewed publications.
- **Key Features**:
  - Tight integration with journal peer review workflows
  - Automated data curation and quality checks
  - CC0 (public domain) licensing for maximum reusability
  - DOI assignment for citations
  - Integration with journal publishers (Wiley, Springer Nature, etc.)
- **Status**: Active. Has evolved from ecology/biology focus to broader research data. Continues to grow through publisher partnerships.
- **Notes**: Dryad differentiates from Zenodo by having a stronger curation/review process and tighter integration with the journal publishing workflow. Default CC0 licensing makes data maximally reusable.

### Dryad Digital Repository
- **URL**: https://datadryad.org
- **Operator/Parent**: Dryad (nonprofit organization)
- **Type**: Both
- **Pricing**: Publishing fee: $150 per data publication (often covered by institutions or journals). Data download/access is completely free. Institutional membership reduces costs.
- **Data Types**: Research Data (primarily life sciences and ecology, but accepts all disciplines), Data underlying scholarly publications, Ecological & Environmental Data, Evolutionary Biology Data, Medical & Health Research Data, Social Science Data
- **Industry Focus**: Academic Research, Ecology & Environmental Science, Life Sciences & Biology, Scholarly Publishing
- **Geographic Focus**: Global (international research community)
- **Formats**: Any format (format-agnostic), Commonly: CSV, Excel, R data files, text files, images, etc.
- **Scale**: ~70,000+ data packages from thousands of journals and researchers
- **Key Features**:
  - DOI minting
  - Curation process (data reviewed before publication)
  - Integration with journal submission workflows
  - CC0 licensing (public domain dedication)
  - FAIR data principles compliance
- **Licensing**: All data in Dryad is published under CC0 (public domain). This is a unique feature - Dryad mandates CC0 for maximum reusability.
- **Notes**: Dryad is distinctive in its requirement that all data be published under CC0 (public domain). This makes Dryad data maximally reusable. The curation process ensures basic data quality. Traditionally focused on life sciences/ecology but now accepts all disciplines. The publishing fee model (rather...

### Figshare
- **URL**: https://figshare.com
- **Operator/Parent**: Digital Science (part of Holtzbrinck Publishing Group, which also owns Springer Nature)
- **Type**: Both - free personal accounts with storage limits; institutional and publisher versions are paid
- **Pricing**: Free personal accounts with 20GB private storage, unlimited public storage. Institutional repository product (Figshare for Institutions) is a paid SaaS product. Publisher integrations also paid. API access is free.
- **Data Types**: Research Data (all disciplines), Figures & Images, Papers & Preprints, Presentations, Code & Software, Media (audio, video), Posters, Filesets, Research datasets, Figures/images, Media/videos, Code/software, Papers/preprints
- **Industry Focus**: Academic Research (all disciplines), Scientific Publishing, Open Science, University Data Management, Academic research, Higher education, Scientific publishing, All research disciplines
- **Geographic Focus**: Global (international research community)
- **Formats**: Any format (format-agnostic repository), Commonly: CSV, Excel, images, PDFs, code, HDF5, etc.
- **Scale**: Millions of research outputs hosted. Used by hundreds of institutions worldwide. One of the most popular research data repositories.
- **Key Features**:
  - DOI minting for all items
  - RESTful API
  - Institutional repositories (figshare for institutions)
  - Embeddable previews (visualizations, 3D models, etc.)
  - Versioning
- **Licensing**: Uploaders choose their license. CC0 and CC-BY are most common. Various options available including CC-BY-NC, CC-BY-SA, MIT, GPL, etc.
- **Status**: Active and well-established. Owned by Digital Science, which provides stable commercial backing.
- **Notes**: Figshare is a popular research data repository, similar to Zenodo but operated by a commercial company (Digital Science). Widely used by universities and publishers for research data management. The institutional product is the primary revenue driver. Individual researchers can publish data for f...

### Harvard Dataverse
- **URL**: https://dataverse.harvard.edu
- **Operator/Parent**: Harvard University, Institute for Quantitative Social Science (IQSS)
- **Type**: Free - open access repository
- **Pricing**: Completely free to deposit and access data. Funded by Harvard University. The Dataverse Project is open-source software that many institutions run independently.
- **Data Types**: Research data from all disciplines, Social science data, Survey data, Geospatial data, Code, Any research data
- **Industry Focus**: Academic research, Social science, All research disciplines
- **Geographic Focus**: Global. Harvard Dataverse is the largest installation, but Dataverse software is used by dozens of institutions worldwide.
- **Formats**: Direct file download, REST API (Search API, Data Access API), Statistical software formats with built-in tabular data ingest, DOI assignment, OAI-PMH harvesting, TwoRavens data exploration tool integration
- **Scale**: Harvard Dataverse alone hosts 100,000+ datasets. Dozens of other institutions run their own Dataverse installations. One of the most widely-used research data repository platforms.
- **Key Features**:
  - Open-source Dataverse software (can be self-hosted by any institution)
  - Network of Dataverse installations worldwide
  - Hierarchical organization (Dataverse > Dataset > File)
  - Tabular data ingest with variable-level metadata
  - Fine-grained access controls including embargoes
- **Status**: Active. Continuous development of the open-source Dataverse software. Major global research data infrastructure.
- **Notes**: The distinction between 'Harvard Dataverse' (the specific installation at Harvard) and 'Dataverse Project' (the open-source software) is important. The software is used by institutions in 40+ countries.

### ICPSR (Inter-university Consortium for Political and Social Research)
- **URL**: https://www.icpsr.umich.edu
- **Operator/Parent**: University of Michigan, Institute for Social Research
- **Type**: Both - some data freely available; full access requires institutional membership
- **Pricing**: Institutional membership model. Member institutions pay annual fees (based on institution size/type) for access to full archive. Some datasets are public access. Individual researchers at non-member institutions may have limited access.
- **Data Types**: Social science survey data, Census and demographic data, Criminal justice data, Health/substance abuse data, Education data, Political behavior data, Economic data, Historical data
- **Industry Focus**: Social science research, Political science, Sociology, Criminology, Public health, Education research, Economics
- **Geographic Focus**: Primarily US data, but includes international datasets. US institutional membership base.
- **Formats**: Statistical software formats (SPSS, Stata, SAS, R), CSV/delimited files, Codebooks and documentation, Online data analysis tools, Restricted-use data via secure access agreements, API access
- **Scale**: Over 16,000 studies with over 250,000 files. 800+ member institutions. One of the world's largest archives of social science data.
- **Key Features**:
  - One of the oldest and most established social science data archives (founded 1962)
  - Extensive metadata and documentation standards
  - Restricted-use data program for sensitive data
  - Data curation and preservation services
  - Training and educational resources
- **Status**: Active and long-established. Continuously growing. A cornerstone of social science research infrastructure.
- **Notes**: ICPSR is arguably the gold standard for curated social science data. Its longevity (60+ years) and institutional membership model provide stable funding. The restricted-use data program is a model for handling sensitive research data.

### OpenAlex
- **URL**: https://openalex.org
- **Operator/Parent**: OurResearch (non-profit). Successor to Microsoft Academic Graph (MAG).
- **Type**: Free - completely open
- **Pricing**: Completely free. Open data. API access is free (with rate limits; premium tier available for higher throughput). Full data snapshot available for download.
- **Data Types**: Academic publication metadata, Citation data, Author profiles, Institution data, Research concepts/topics, Funding data, Open access status
- **Industry Focus**: Academic research, Scientometrics/bibliometrics, Research evaluation, Library science, Science policy
- **Geographic Focus**: Global academic literature
- **Formats**: REST API, Full data snapshot (Amazon S3), OpenAlex API with filtering/grouping, JSON format
- **Scale**: 250M+ works, 100M+ authors, 100K+ institutions. Comprehensive coverage of global scholarly literature.
- **Key Features**:
  - Open replacement for Microsoft Academic Graph (discontinued 2021)
  - Covers 250M+ scholarly works
  - Free API with rich filtering
  - Author disambiguation
  - Institutional affiliation tracking
- **Status**: Active and growing rapidly. Has become the primary open bibliometric data source since MAG shutdown.
- **Notes**: OpenAlex filled a critical gap when Microsoft discontinued MAG. It has quickly become essential infrastructure for scientometric research, competing with proprietary databases like Scopus (Elsevier) and Web of Science (Clarivate).

### Zenodo
- **URL**: https://zenodo.org
- **Operator/Parent**: CERN (European Organization for Nuclear Research), supported by the European Commission via the OpenAIRE project
- **Type**: Free - open access research data repository
- **Pricing**: Completely free for upload and download. Funded by CERN and EU grants. Up to 50GB per dataset (larger by request). No charges for access.
- **Data Types**: Research Data (all scientific disciplines), Publications & Preprints, Software & Code, Images & Figures, Presentations & Posters, Lessons & Educational Materials, Videos, Any research output, Research datasets (any discipline), Publications, Software, Presentations, Posters, Images, Lessons
- **Industry Focus**: Academic Research (all disciplines), Scientific Data Management, Open Science, Software Preservation, Academic research, Scientific data, Open science, All disciplines
- **Geographic Focus**: Global (international research community)
- **Formats**: Any format (Zenodo is format-agnostic), Commonly: CSV, JSON, HDF5, NetCDF, FITS, images, code archives, PDFs, etc.
- **Scale**: Millions of records. One of the largest general-purpose open research data repositories. Growing rapidly as open science mandates increase.
- **Key Features**:
  - DOI minting for every upload (persistent identifiers)
  - GitHub integration (automatic archiving of releases)
  - Versioning support
  - Communities (curated collections by topic/project)
  - OAI-PMH metadata harvesting
- **Licensing**: Uploaders choose their own license (CC0, CC-BY, CC-BY-SA, CC-BY-NC, MIT, Apache, GPL, etc.). Zenodo itself does not impose licensing restrictions.
- **Status**: Active and growing. Major upgrade to new Zenodo platform (based on InvenioRDM) rolled out in 2023-2024.
- **Notes**: Zenodo is a general-purpose open research repository, not specifically a data portal. However, it hosts a significant amount of research datasets and is widely used for data sharing in conjunction with publications. Its DOI minting and CERN backing make it a trusted long-term archive. Particularl...

---

## 7. Data Discovery & Aggregation Platforms

### Datahub.io
- **URL**: https://datahub.io
- **Operator/Parent**: Datopian (formerly Open Knowledge International project)
- **Type**: Free (core datasets)
- **Pricing**: Core datasets are free. Datopian offers commercial data management services. The original DataHub was a CKAN-based catalog; the current version focuses on curated 'core' datasets.
- **Data Types**: Economic Indicators (GDP, CPI, exchange rates), Financial Data (S&P 500, gold prices, etc.), Geographic (country codes, airport codes, etc.), Demographics, Climate & Environment, Reference Data (standards, codes, classifications), Machine Learning Datasets
- **Industry Focus**: Data Science & Analytics, Economics & Finance, Reference Data Management, Academic Research
- **Geographic Focus**: Global
- **Formats**: CSV, JSON, Datapackage (Frictionless Data format), API, Excel
- **Scale**: ~1,000+ core/curated datasets. The platform focuses on quality over quantity.
- **Key Features**:
  - Frictionless Data standards (datapackage.json)
  - Core datasets - curated, high-quality, regularly updated reference datasets
  - Command-line tool for data publishing
  - Data validation and quality checking
  - Version control for data
- **Licensing**: Primarily Open Data Commons Public Domain Dedication and License (PDDL) and Open Data Commons Attribution License (ODC-BY). Some datasets use CC licenses.
- **Notes**: Datahub.io has evolved significantly over time. Originally part of the Open Knowledge Foundation's CKAN ecosystem, it was rebranded and refocused by Datopian. The 'core datasets' collection provides clean, standardized versions of commonly-needed reference data (country codes, currencies, economi...

### Dataiku Data Catalog / Marketplace
- **URL**: https://www.dataiku.com
- **Operator/Parent**: Dataiku SAS (independent, French-American company)
- **Type**: Paid - Part of Dataiku DSS platform
- **Pricing**: Dataiku DSS platform licensing (not a standalone data marketplace). Enterprise pricing based on users and compute. Free community edition available for individuals.
- **Data Types**: Internal data catalog (helps organizations discover their own data), Connections to external data sources, ML models and recipes, Not primarily an external data marketplace
- **Industry Focus**: Enterprise data science/ML, Financial services, Healthcare, Manufacturing, Retail
- **Geographic Focus**: Global
- **Formats**: Dataiku DSS platform, Connects to virtually any data source, Internal data catalog/governance
- **Scale**: 500+ enterprise customers globally. [Based on training data, may need verification]
- **Key Features**:
  - Enterprise AI/ML platform with strong data governance
  - Internal data marketplace/catalog for enterprises
  - Not primarily a data marketplace - included for completeness as it facilitates data sharing within organizations
- **Provider Requirements**: Internal platform - not a two-sided external marketplace.
- **Notes**: Dataiku is primarily an enterprise AI/ML platform, not a data marketplace. Included here because its data catalog and sharing features function as an internal data marketplace within organizations. For actual external data acquisition, users would use the other platforms in this list.

### Datarade
- **URL**: https://datarade.ai
- **Operator/Parent**: Datarade GmbH (independent, Berlin-based startup)
- **Type**: Both - Free to browse and compare; paid to purchase data from listed providers
- **Pricing**: Datarade itself is a discovery/aggregation layer. Pricing is set by individual data providers listed on the platform. Datarade earns revenue through provider subscriptions and lead-generation fees. Data products range from free samples to enterpri...
- **Data Types**: Location data, Financial data, B2B contact/firmographic data, Consumer/demographic data, Geospatial data, Web scraping/crawl data, Alternative data for finance, ESG data, Intent/behavioral data, Healthcare data, Real estate data, Weather data, Social media data, Aggregates listings from 2,000+ data providers across all categories, B2B data, Consumer data, Automotive data
- **Industry Focus**: Financial services, Marketing/advertising, Real estate, Retail, Healthcare, Insurance, Government, Technology, Cross-industry data marketplace/directory, Alternative data for finance, Marketing data, Location intelligence, B2B sales data
- **Geographic Focus**: Global - providers and data covering all major regions
- **Formats**: Varies by provider - CSV, JSON, API, SFTP, cloud delivery (S3, GCS, Azure Blob), Snowflake Data Sharing, Databricks marketplace integration, Direct download, Web-based marketplace/directory for discovering data providers, Matchmaking between buyers and sellers, Not a direct data delivery platform - connects to providers, Provider profiles with data samples and pricing
- **Scale**: 2,000+ listed data providers. Thousands of data products cataloged. Growing as a data commerce intermediary.
- **Key Features**:
  - Aggregator/comparison model - does not own data but connects buyers with 2,000+ data providers
  - Side-by-side data product comparison
  - Free sample requests from providers
  - Provider reviews and ratings
  - RFP/RFI tools for enterprise procurement
- **Provider Requirements**: Providers apply to list products. Datarade vets providers for data quality and legitimacy. Providers pay subscription fees or commission on leads/sales generated through the platform.
- **Status**: Active. Growing as a matchmaking platform for data commerce.
- **Notes**: Often described as the 'Yelp for data' or 'G2 for data products.' Strong SEO presence means many data searches land on Datarade pages. Good starting point for discovery but actual transactions happen off-platform with providers directly in many cases.

### Dawex
- **URL**: https://www.dawex.com
- **Operator/Parent**: Dawex Systems SAS (independent, Paris-based)
- **Type**: Paid - Enterprise platform; Dawex also operates a public data exchange
- **Pricing**: Dawex offers a white-label data exchange technology platform (SaaS licensing to enterprises wanting to build their own data marketplace) plus the Dawex Data Exchange (public marketplace). Enterprise licensing is custom-priced. On the exchange, pri...
- **Data Types**: Industrial/IoT data, Supply chain data, Mobility/transportation data, Agriculture data, Energy data, Financial data, Environmental/sustainability data, Smart city data, Any data the exchange operator chooses to facilitate - B2B data commerce, Industrial data, Automotive data, Agricultural data
- **Industry Focus**: Manufacturing, Automotive, Agriculture, Energy/utilities, Transportation/logistics, Smart cities, Government/public sector, Financial services, Automotive (Gaia-X), Industrial IoT, Government/public sector data sharing
- **Geographic Focus**: Global with strong European/French presence. Active in EU data spaces initiatives (Gaia-X participant).
- **Formats**: API, File transfer (CSV, JSON, XML, Parquet), Streaming, Cloud-to-cloud delivery, White-label marketplace deployment, White-label data exchange platform, API marketplace capabilities, Data product catalog, Secure data exchange protocols, Governance and compliance tools
- **Scale**: Hundreds of organizations using the platform technology; public exchange scale is more modest [Based on training data, may need verification]
- **Key Features**:
  - Data exchange technology provider - enables organizations to create their own branded data marketplace
  - Strong governance and compliance framework (GDPR-focused)
  - Supports data licensing, data sharing, and data trading models
  - Participant in European data space initiatives (Gaia-X, IDSA)
  - Orchestration of data transactions with built-in contract management
- **Provider Requirements**: Providers register and list datasets with metadata, pricing, licensing terms, and usage conditions. Dawex provides governance tooling for access control.
- **Status**: Active. Well-positioned in European data sovereignty ecosystem. Growing with EU data regulations (Data Act, Data Governance Act).
- **Notes**: Dawex positions itself more as data exchange infrastructure/technology than a pure marketplace. Strong alignment with European data sovereignty and Gaia-X initiatives. Important distinction: they sell the marketplace platform technology to enterprises, not just operate one marketplace.

### Google Dataset Search
- **URL**: https://datasetsearch.research.google.com
- **Operator/Parent**: Google LLC (Alphabet Inc.)
- **Type**: Free (search engine; data availability depends on source)
- **Pricing**: The search engine is completely free. It indexes datasets hosted elsewhere, so actual data access depends on the hosting platform (most are free, some may have costs).
- **Data Types**: All types - it is a meta-search engine indexing datasets across the web, Sciences (biology, earth science, physics, etc.), Government & Public Sector, Healthcare & Biomedical, Economics & Finance, Social Sciences, Machine Learning, Geospatial, Environment & Climate
- **Industry Focus**: All industries - serves as a discovery tool across domains
- **Geographic Focus**: Global (indexes datasets from all countries and organizations)
- **Formats**: N/A - Google Dataset Search is a search engine, not a data host. It links to datasets in whatever format the source provides.
- **Scale**: Indexes ~25+ million datasets across the web (as of 2023-2024 estimates). Continuously growing as more sites adopt Schema.org markup.
- **Key Features**:
  - Indexes datasets using Schema.org Dataset markup and DCAT metadata
  - Filters by topic, format, usage rights, and update date
  - Covers government portals, academic repositories, commercial platforms
  - Launched out of beta in 2020
  - Leverages Google's search infrastructure for relevance ranking
- **Licensing**: N/A for the search engine itself. Indexed datasets have their own licenses. Filter available for open/creative commons licensed data.
- **Notes**: Google Dataset Search is a discovery/search tool, not a data host. Think of it as 'Google for datasets.' It is extremely useful for finding datasets you did not know existed. Works best when data publishers mark up their pages with Schema.org structured data. Does not guarantee data quality or ac...

### Harbr (Harbr Data Commerce)
- **URL**: https://www.harbr.com
- **Operator/Parent**: Harbr Ltd (London, UK)
- **Type**: Paid - enterprise B2B platform
- **Pricing**: Enterprise SaaS licensing. Harbr provides the platform infrastructure for organizations to build their own data commerce operations (white-label data marketplace). Pricing is custom/enterprise-tier, not publicly listed.
- **Data Types**: Any data the enterprise client chooses to commercialize, Structured datasets, APIs, Analytics products, Data-as-a-Service products
- **Industry Focus**: Financial services, Media/publishing, Data vendors/aggregators, Government, Enterprise data monetization
- **Geographic Focus**: Global, primarily UK and US enterprise market
- **Formats**: API delivery, File downloads, Cloud-to-cloud transfer, Custom data products with usage tracking, White-label storefronts
- **Scale**: Enterprise clients include financial data firms and media companies. Relatively niche B2B platform. Not a public marketplace - provides infrastructure for clients to build their own.
- **Key Features**:
  - White-label data commerce platform for enterprises
  - Built-in data product management and packaging
  - Usage analytics and metering
  - Access control and entitlements management
  - Revenue tracking and billing integration
- **Status**: Active as of early 2025. Venture-backed startup that has been operating since approximately 2017.
- **Notes**: Harbr is not a marketplace itself but rather a platform for building data commerce operations. Competes with Revelate (formerly known as Data Commerce Cloud by InfoSum), Dawex, and similar B2B data commerce infrastructure providers.

### Knoema
- **URL**: https://knoema.com
- **Operator/Parent**: Knoema Corporation, acquired by Eldridge Industries in 2021
- **Type**: Both - free access to public/open statistical data; premium plans for advanced features and proprietary datasets
- **Pricing**: Freemium. Free tier provides access to public statistical data with basic visualization. Premium/Enterprise tiers provide API access, advanced analytics, custom datasets, and private data management. Post-Eldridge acquisition, some features may ha...
- **Data Types**: Macroeconomic indicators, Statistical data (national/international), Demographics, Industry statistics, Commodity prices, Trade data, Health statistics, Environmental data, Agriculture data
- **Industry Focus**: Economics research, Government/policy, Finance/investment, Consulting, Academic research, International development
- **Geographic Focus**: Global - aggregates data from 200+ countries. Sources include World Bank, IMF, UN, national statistical offices, and proprietary sources.
- **Formats**: Web-based data explorer and visualization tools, REST API, Excel/CSV downloads, Embeddable visualizations and dashboards, Data connector integrations
- **Scale**: Claims billions of data points from thousands of sources covering virtually every country. One of the largest aggregators of public statistical data.
- **Key Features**:
  - Massive aggregation of public statistical data from thousands of sources
  - Unified data schema across disparate sources
  - Data visualization and dashboard tools
  - Time series data with historical depth
  - World Data Atlas - interactive country/topic explorer
- **Status**: Active but somewhat diminished in public visibility post-Eldridge acquisition (2021). The platform remains operational. Eldridge Industries is a diversified holding company owned by Todd Boehly.
- **Notes**: Knoema's primary value is in aggregating, harmonizing, and making accessible vast amounts of public statistical data that would otherwise require visiting dozens of individual source websites. Post-acquisition strategy under Eldridge is not fully transparent.

### Narrative.io
- **URL**: https://www.narrative.io
- **Operator/Parent**: Narrative I/O, Inc. (independent, New York-based)
- **Type**: Both - Free tier available for limited usage; paid plans for full access
- **Pricing**: Subscription-based platform access (Narrative offers a 'Data Shops' self-service product and enterprise plans). Data acquisition costs are separate and based on volume, attributes, and provider pricing. Platform fees plus data costs. Starter plan ...
- **Data Types**: Identity/audience data, Location data, App usage data, Purchase/transaction data, Demographic data, Intent data, B2B data, Device/mobile data, Weather data, Financial data, Consumer/audience data, Identity data, Mobile app data, B2B intent data
- **Industry Focus**: Marketing/advertising (AdTech), Financial services, Data science/analytics, Retail, Real estate, CPG/consumer goods, Digital advertising/marketing, Data monetization, Identity resolution, Audience targeting, Market research
- **Geographic Focus**: Primarily US-focused, with some global data available
- **Formats**: Narrative Data Streaming (NQL - Narrative Query Language), API access, S3 delivery, Snowflake integration, Custom connectors, Flat files (CSV, JSON), Narrative Data Marketplace (self-serve), Data Streaming (real-time), NQL query language for custom data selection, Cloud delivery (S3, Snowflake), APIs, Automated data pipeline creation
- **Scale**: Billions of data points available. Growing provider network. Focused on programmatic data commerce.
- **Key Features**:
  - Proprietary query language (NQL) for cross-provider data querying
  - Data Shops - turnkey e-commerce storefronts for data sellers
  - Rosetta Stone identity resolution across providers
  - Automated data standardization and normalization
  - Attribute-level purchasing (buy specific fields, not whole datasets)
- **Provider Requirements**: Data providers integrate their data into the Narrative platform. The platform handles normalization, deduplication, and compliance. Revenue share model with providers.
- **Status**: Active. Venture-backed. Growing as data clean rooms and privacy-compliant data sharing become more important.
- **Notes**: Key differentiator is the software layer that sits on top of data transactions - allowing buyers to query across multiple providers simultaneously using NQL and purchase at the attribute level rather than buying whole datasets. The 'Data Shops' product lets anyone spin up a branded data storefron...

### Statista
- **URL**: https://www.statista.com
- **Operator/Parent**: Statista GmbH (Hamburg, Germany). Majority owned by Ströer SE & Co. KGaA.
- **Type**: Both - limited free access to some statistics; full access requires paid subscription
- **Pricing**: Subscription-based. Individual plans (Basic, Starter, Professional) starting from roughly $79-$199+/month. Enterprise/Corporate plans with custom pricing. Single-statistic purchases also available. Content licensing for media/publishing.
- **Data Types**: Market research statistics, Industry reports, Company data/dossiers, Consumer surveys, Infographics, Industry forecasts, Country data, Brand/company profiles, eCommerce data
- **Industry Focus**: Market research, Business intelligence, Marketing, Consulting, Media/journalism, Academia, Advertising
- **Geographic Focus**: Global coverage with particularly strong data for US, Europe, and major economies. Offices in Hamburg, New York, London, and other cities.
- **Formats**: Web-based statistics portal, Downloadable charts (PNG, PDF, PPT, XLS), Statista Content & Design service for custom infographics, API access (enterprise), Industry reports (PDF), Outlook data explorer
- **Scale**: 1,000,000+ statistics across 80,000+ topics from 22,500+ sources. Major global platform for business statistics. Over 1 billion annual page views claimed.
- **Key Features**:
  - Massive collection of curated statistics from 22,500+ sources
  - Professional-quality charts and infographics ready for presentation
  - Industry-specific reports and market outlook forecasts
  - Statista Consumer Insights (proprietary survey platform)
  - Statista Global Business Data (company database)
- **Status**: Active and growing. Has expanded aggressively through acquisitions and new product lines. Significant investment in AI and content expansion.
- **Notes**: Statista occupies a unique niche as a 'statistics aggregator and presenter' rather than a traditional data marketplace. Its value is in curation, visualization, and making statistics presentation-ready. Criticized by some researchers for being a secondary source rather than primary data.

---

## 8. Decentralized & Blockchain Data Marketplaces

### Chainlink (Data Feeds / CCIP)
- **URL**: https://chain.link
- **Operator/Parent**: Chainlink Labs (Grand Cayman / distributed team)
- **Type**: Both - reading price feeds is free for consumers; node operators are paid by protocols
- **Pricing**: Oracle network model. Protocols/smart contracts pay LINK tokens to receive verified off-chain data on-chain. Price feeds are sponsored by DeFi protocols. Data providers earn LINK for supplying data to oracle nodes. Custom data feeds are enterprise...
- **Data Types**: Cryptocurrency price feeds, Real-world asset prices, Weather data (via Any API), Sports results, Random number generation (VRF), Cross-chain data (CCIP), Proof of Reserve data
- **Industry Focus**: DeFi, Insurance (parametric), Gaming/NFTs, Cross-chain operations, Enterprise blockchain, Real-world asset tokenization
- **Geographic Focus**: Global (blockchain-based)
- **Formats**: On-chain data feeds (smart contract readable), Chainlink Functions (custom API calls), CCIP (Cross-Chain Interoperability Protocol), Automation (Keepers), Off-chain reporting via Chainlink nodes
- **Scale**: Secures tens of billions of dollars in DeFi value. Hundreds of price feeds across multiple blockchains. LINK is a top-20 cryptocurrency. Used by most major DeFi protocols.
- **Key Features**:
  - Dominant blockchain oracle network
  - Decentralized data feeds securing billions in DeFi TVL
  - CCIP for cross-chain data and token transfers
  - Chainlink Functions for connecting smart contracts to any API
  - Verifiable Random Function (VRF) for provably fair randomness
- **Status**: Active and dominant. Continues expansion with CCIP, Functions, and enterprise adoption. Market-leading oracle solution.
- **Notes**: Chainlink is the bridge between off-chain data and on-chain smart contracts. While not a traditional data marketplace, it is the primary mechanism by which real-world data enters blockchain ecosystems. CCIP expansion into cross-chain is a major strategic initiative.

### Dune Analytics
- **URL**: https://dune.com
- **Operator/Parent**: Dune Analytics (Oslo, Norway / remote)
- **Type**: Both - free tier with public queries; paid plans for private queries and more features
- **Pricing**: Freemium. Free: public queries and dashboards with rate limits. Plus ($349/month), Premium ($custom) with private queries, faster execution, larger result sets, CSV exports, API access.
- **Data Types**: Blockchain/on-chain data (decoded), DeFi protocol analytics, NFT data, Token transfer data, Wallet/address analytics, Cross-chain data (Ethereum, Polygon, Solana, etc.)
- **Industry Focus**: DeFi, Web3/crypto, NFTs, Blockchain analytics, Crypto investment research
- **Geographic Focus**: Global (blockchain data)
- **Formats**: Web-based SQL query interface, Dashboards and visualizations, API access (paid), CSV exports (paid), Embeddable charts, Community-shared queries and dashboards
- **Scale**: Indexes major blockchains completely. Hundreds of thousands of community-created queries and dashboards. Major platform for crypto analytics.
- **Key Features**:
  - Community-driven blockchain analytics platform
  - Write SQL queries against decoded blockchain data
  - Public dashboard sharing (social analytics)
  - Pre-decoded smart contract events and transactions
  - Multi-chain support (Ethereum, Polygon, Solana, Arbitrum, etc.)
- **Status**: Active and well-funded. Raised $69M Series B in 2022. Growing as the primary community blockchain analytics tool.
- **Notes**: Dune has become the go-to platform for blockchain data analysis, similar to what Observable/Mode is for traditional analytics. The community-driven model where queries and dashboards are public creates a powerful network effect.

### Filecoin / Filecoin Data Economy
- **URL**: https://filecoin.io
- **Operator/Parent**: Protocol Labs (San Francisco, CA). Founded by Juan Benet.
- **Type**: Both - storage costs paid in FIL token; data retrieval may be free or paid depending on provider
- **Pricing**: Decentralized storage marketplace. Storage providers compete on price for storage deals. Payment in FIL (Filecoin) tokens. Not a data marketplace per se, but the infrastructure layer for decentralized data commerce. Filecoin Plus program subsidize...
- **Data Types**: Any data (decentralized storage network), Large datasets (designed for cold/warm storage), Public datasets (via Filecoin Plus), NFT/Web3 data, Scientific data archives
- **Industry Focus**: Web3/decentralized storage, Data archival, NFT storage, Scientific data preservation, Enterprise backup
- **Geographic Focus**: Global decentralized network
- **Formats**: IPFS/Filecoin retrieval, Lotus client software, Estuary (simplified upload/retrieval), Web3.storage service, Saturn CDN for fast retrieval
- **Scale**: Exabytes of storage capacity on the network. Thousands of storage providers globally. FIL is a top-50 cryptocurrency by market cap.
- **Key Features**:
  - Largest decentralized storage network
  - Proof of storage (cryptographic verification that data is stored)
  - FIL token incentive mechanism for storage providers
  - IPFS integration for content-addressed storage
  - Filecoin Virtual Machine (FVM) for programmable storage
- **Status**: Active. Continues development with FVM, retrieval market improvements, and enterprise adoption efforts.
- **Notes**: Filecoin is more infrastructure (decentralized storage) than marketplace (data commerce), but its ecosystem includes emerging data marketplace applications. Data DAOs and the Filecoin Plus program represent efforts to build a data economy on top of the storage network.

### Nansen
- **URL**: https://www.nansen.ai
- **Operator/Parent**: Nansen.ai (Singapore)
- **Type**: Paid - subscription plans with limited free features
- **Pricing**: Tiered subscriptions. Free tier with limited features. Pioneer ($150/month), Alpha ($1,500/month), Enterprise (custom). Higher tiers unlock more wallet labels, alerts, and historical data.
- **Data Types**: Blockchain wallet/address labels, On-chain transaction analytics, Smart money tracking, Token holder analysis, NFT analytics, DeFi protocol analytics
- **Industry Focus**: Cryptocurrency investment, DeFi, NFTs, Blockchain analytics, Crypto funds
- **Geographic Focus**: Global (blockchain data)
- **Formats**: Web-based analytics platform, API access, Dashboards and alerts, Smart alerts for wallet activity, Research reports
- **Scale**: Labels millions of blockchain wallets. Covers major blockchains. Growing user base among crypto traders and funds.
- **Key Features**:
  - Proprietary wallet labeling system (identifies exchanges, funds, whales)
  - Smart Money tracking (follow successful traders)
  - Real-time alerts for on-chain activity
  - NFT analytics and floor price tracking
  - Token God Mode (comprehensive token analytics)
- **Status**: Active. Well-funded. Competitive with Arkham Intelligence, Glassnode, and similar blockchain analytics platforms.
- **Notes**: Nansen's key differentiator is its wallet labeling database, which maps blockchain addresses to known entities (exchanges, funds, notable traders). This enables 'smart money' tracking.

### Ocean Protocol
- **URL**: https://oceanprotocol.com
- **Operator/Parent**: Ocean Protocol Foundation (Singapore-based)
- **Type**: Both - free to list, transaction fees apply; OCEAN token used for staking and transactions
- **Pricing**: Decentralized marketplace where data providers set their own prices. Transactions use OCEAN token (ERC-20). Data consumers pay per-access or subscription. Compute-to-data model allows monetization without raw data leaving provider custody.
- **Data Types**: AI/ML training datasets, DeFi and blockchain analytics, IoT sensor data, Weather data, Health data, Mobility data, Any data that providers choose to list
- **Industry Focus**: AI/ML, DeFi, Web3, IoT, Scientific research, Healthcare
- **Geographic Focus**: Global
- **Formats**: Direct download (encrypted), Compute-to-data (data stays in situ, algorithms sent to data), REST API, Smart contract-mediated access via datatokens
- **Scale**: Thousands of datasets listed on Ocean Market. OCEAN token has been a top-200 cryptocurrency by market cap. Active developer community. Total Value Locked has fluctuated with crypto markets.
- **Key Features**:
  - Datatokens - ERC-20 tokens representing access rights to specific datasets
  - Compute-to-Data - privacy-preserving computation where algorithms go to data rather than data to algorithms
  - Deployed on Ethereum mainnet and Polygon (for lower gas fees)
  - Ocean Market - web-based decentralized marketplace UI
  - Data NFTs for representing IP/ownership of datasets
- **Status**: Active. Underwent significant protocol upgrades (Ocean v4 in 2022-2023). Continues development with focus on AI data monetization and Predictoor product.
- **Notes**: One of the pioneering decentralized data marketplace protocols. Founded by Trent McConaghy and Bruce Pon. The compute-to-data feature is a significant differentiator for privacy-sensitive data. Token price highly correlated with broader crypto market.

### Ocean Protocol Predictoor
- **URL**: https://predictoor.ai
- **Operator/Parent**: Ocean Protocol Foundation
- **Type**: Paid - uses OCEAN tokens for predictions
- **Pricing**: Token-based prediction market. Predictoors stake OCEAN tokens on predictions and earn rewards for accuracy. Consumers pay OCEAN for prediction feeds.
- **Data Types**: Cryptocurrency price predictions, Real-time prediction feeds, Financial signal data
- **Industry Focus**: DeFi, Cryptocurrency trading, Quantitative finance
- **Geographic Focus**: Global (blockchain-based)
- **Formats**: On-chain prediction feeds, Subgraph/API access, Integration with trading bots
- **Scale**: Newer product, still building adoption. Part of the broader Ocean Protocol ecosystem.
- **Key Features**:
  - Decentralized prediction feed marketplace
  - Staking mechanism incentivizes accuracy
  - Built on Ocean Protocol infrastructure
  - Targets DeFi/crypto trading use cases
- **Status**: Active/early stage. Launched in 2023 as part of Ocean Protocol ecosystem expansion.
- **Notes**: Predictoor represents Ocean Protocol's pivot toward more specific, monetizable data products rather than a general-purpose data marketplace.

### Streamr
- **URL**: https://streamr.network
- **Operator/Parent**: Streamr Network AG (Zug, Switzerland)
- **Type**: Both - free tier available, paid for premium streams and higher throughput
- **Pricing**: DATA token (ERC-20) used for transactions on the network. Data publishers set prices for their streams. The Streamr Network itself is a decentralized pub/sub messaging network; the marketplace layer sits on top. Broker nodes earn DATA tokens for r...
- **Data Types**: Real-time streaming data, IoT sensor data, Financial market data, Blockchain/crypto data, Machine data, Social media streams, Geolocation data
- **Industry Focus**: IoT, DeFi, Web3, Smart cities, Logistics, Real-time analytics
- **Geographic Focus**: Global
- **Formats**: Real-time pub/sub streams (WebSocket-based), Streamr SDK (JavaScript/TypeScript), REST API, MQTT bridge for IoT devices, Streamr Hub marketplace UI
- **Scale**: Thousands of active streams. Network of broker nodes globally distributed. Community of developers building on the protocol. DATA token is a smaller-cap cryptocurrency.
- **Key Features**:
  - Decentralized real-time data transport layer (pub/sub network)
  - Streamr Hub - marketplace for buying/selling data streams
  - DATA token for payments and network incentives
  - Broker nodes form a peer-to-peer network for data delivery
  - Light nodes for end-user access
- **Status**: Active. Transitioned from centralized to fully decentralized network architecture. Streamr 1.0 milestone achieved. Continues active development.
- **Notes**: Differentiates from Ocean Protocol by focusing specifically on real-time streaming data rather than static datasets. Founded by Henri Pihkala. Originally included the Streamr Marketplace (now Streamr Hub) for data commerce.

### The Graph
- **URL**: https://thegraph.com
- **Operator/Parent**: The Graph Foundation / Edge & Node (founding team company)
- **Type**: Both - free hosted service (being deprecated) and paid decentralized network queries
- **Pricing**: Pay-per-query on the decentralized network using GRT tokens. Indexers earn GRT for serving queries. Curators earn for signaling quality subgraphs. Free hosted service was available but migrating to decentralized network. Query costs are fractions ...
- **Data Types**: Blockchain/on-chain data (indexed), DeFi protocol data, NFT data, DAO governance data, DEX trading data, Smart contract event data
- **Industry Focus**: DeFi, Web3/blockchain, NFTs, DAOs, Blockchain analytics, dApp development
- **Geographic Focus**: Global (blockchain-based)
- **Formats**: GraphQL API (subgraphs), Decentralized query network, Subgraph Studio for development, Graph Explorer for discovery, Supports Ethereum, Polygon, Arbitrum, and many other chains
- **Scale**: Billions of queries served. Thousands of active subgraphs. Core infrastructure for DeFi and Web3 data access.
- **Key Features**:
  - Decentralized indexing protocol for blockchain data
  - GraphQL-based query interface for on-chain data
  - Subgraph model - anyone can deploy indexing schemas
  - GRT token for network economics (staking, curation, queries)
  - Multi-chain support (Ethereum, Polygon, Arbitrum, many more)
- **Status**: Active. Transitioning from centralized hosted service to fully decentralized network. Growing multi-chain support.
- **Notes**: The Graph is often called the 'Google of blockchains' because it indexes and makes queryable on-chain data that would otherwise require running your own blockchain node. Essential infrastructure for Web3 data access.

---

## 9. Sector-Specific Data Providers

### ATTOM Data Solutions
- **URL**: https://www.attomdata.com
- **Operator/Parent**: ATTOM Data Solutions (Irvine, CA). Formed from merger of RealtyTrac, ATTOM, and Home Junction. Owned by private equity.
- **Type**: Paid - enterprise data licensing
- **Pricing**: Data licensing and subscription model. Enterprise contracts for data feeds, bulk data, and API access. Some limited data available through free reports/tools on their website. Custom pricing based on coverage, volume, and use case.
- **Data Types**: Property tax/deed/mortgage data, Foreclosure data, Property characteristics, Sales transaction data, Natural hazard data, Neighborhood/school data, Property valuation estimates, Rental data
- **Industry Focus**: Real estate, Mortgage/lending, Insurance, PropTech, Government, Financial services, Marketing
- **Geographic Focus**: United States - nationwide property data coverage
- **Formats**: Bulk data delivery (FTP, S3), REST API, Cloud data delivery (Snowflake, AWS Data Exchange), Data licensing, Flat files (CSV, pipe-delimited)
- **Scale**: 155M+ US residential and commercial properties. 99%+ county coverage. Billions of data points across property, transaction, and risk categories.
- **Key Features**:
  - Nationwide US property data covering 155M+ properties
  - Former RealtyTrac foreclosure data (long time series)
  - Natural hazard risk data
  - Property tax and assessment data
  - Deed and mortgage transaction data
- **Status**: Active. Continues to expand data coverage and delivery channels.
- **Notes**: ATTOM is one of the major property data aggregators alongside CoreLogic, Black Knight (now ICE Mortgage Technology), and First American. Strong in foreclosure data given RealtyTrac heritage.

### DTN (formerly Data Transmission Network)
- **URL**: https://www.dtn.com
- **Operator/Parent**: DTN LLC. Owned by TBG AG (Swiss holding company, formerly part of DMGT).
- **Type**: Paid - enterprise/commercial subscriptions
- **Pricing**: Enterprise subscriptions and data licensing. Custom pricing based on industry, data products, and delivery needs. Multi-product platform serving multiple verticals.
- **Data Types**: Weather data and forecasts, Agricultural market data, Commodity prices, Energy market data, Transportation/logistics weather, Crop condition data, Precision agriculture data
- **Industry Focus**: Agriculture, Energy/utilities, Aviation, Marine shipping, Transportation/logistics, Commodities trading
- **Geographic Focus**: Global, with particularly strong presence in North America
- **Formats**: Enterprise platforms and dashboards, API access, Data feeds, Mobile apps, Decision support tools, Alerting systems
- **Scale**: Serves thousands of enterprise clients across agriculture, energy, and transportation. Decades of historical weather and market data.
- **Key Features**:
  - Combines weather data with agriculture and energy market intelligence
  - Progressive Farmer brand and content
  - Severe weather alerting for critical operations
  - Precision agriculture decision support
  - Energy trading and risk management data
- **Status**: Active. Continues acquisitions to expand data and analytics capabilities.
- **Notes**: DTN is a veteran player in weather-sensitive industry data. The combination of weather, agriculture, and energy data creates unique cross-industry analytics. Less flashy than Tomorrow.io but deeply embedded in enterprise workflows.

### Definitive Healthcare
- **URL**: https://www.definitivehc.com
- **Operator/Parent**: Definitive Healthcare Corp. (Framingham, MA). Publicly traded on Nasdaq (DH). Taken private by IQVIA in planned 2024 acquisition.
- **Type**: Paid - enterprise subscription with limited free lookups
- **Pricing**: Enterprise SaaS subscriptions. Multi-year contracts typical. Free basic account with limited lookups. Pricing ranges from mid-five-figures to six-figures annually depending on modules and users.
- **Data Types**: Hospital/health system profiles, Physician data, Medical claims data, Clinical trial data, Health insurance data, Employer health benefits data, Medical device purchasing data, Healthcare executive contacts
- **Industry Focus**: Healthcare, Life sciences, Pharmaceutical sales, Medical device companies, Healthcare IT, Health insurance, Healthcare consulting
- **Geographic Focus**: Primarily United States
- **Formats**: Web-based platform/dashboard, API access, Data exports (CSV, Excel), CRM integrations (Salesforce, HubSpot), Analytics and visualization tools, Custom data feeds
- **Scale**: Covers virtually all US hospitals, physician groups, and healthcare facilities. Millions of provider records. Billions of claims records analyzed.
- **Key Features**:
  - Comprehensive US healthcare provider database
  - Claims-based analytics for physician referral patterns
  - Hospital and IDN hierarchy mapping
  - Medical device purchasing intelligence
  - Clinical trial intelligence
- **Status**: Was publicly traded (Nasdaq: DH). IQVIA announced acquisition in late 2024. The platform continues active operations through the acquisition process.
- **Notes**: The IQVIA acquisition would combine Definitive Healthcare's provider intelligence with IQVIA's pharmaceutical data, creating a comprehensive healthcare data powerhouse. Definitive was previously backed by Advent International.

### GenBank / NCBI Databases
- **URL**: https://www.ncbi.nlm.nih.gov
- **Operator/Parent**: National Center for Biotechnology Information (NCBI), National Institutes of Health (NIH), U.S. Government
- **Type**: Free
- **Pricing**: Completely free. No registration required for most access.
- **Data Types**: Genomic Sequences (DNA, RNA), Protein Sequences, Gene Expression Data (GEO), Biomedical Literature (PubMed), Clinical Trials (ClinicalTrials.gov), Genetic Variation (dbSNP, ClinVar, dbVar), 3D Molecular Structures, Taxonomy, Chemical/Compound Data (PubChem), Biosample & BioProject metadata
- **Industry Focus**: Genomics & Bioinformatics, Pharmaceutical & Drug Discovery, Biomedical Research, Clinical Genetics, Agriculture (plant/animal genomics), Public Health, Academic Research
- **Geographic Focus**: Global (international sequence database consortium member)
- **Formats**: FASTA, GenBank flat file, XML (NCBI-specific schemas), JSON, ASN.1, CSV/TSV, SRA formats (sequence read archives), E-utilities API, FTP/HTTPS bulk download, Cloud access (SRA on AWS/GCP/Azure)
- **Scale**: GenBank contains ~250+ million sequences. SRA contains petabytes of sequencing data. PubMed indexes 36+ million citations. PubChem has 110+ million compounds. Collectively the largest biomedical data resource in the world.
- **Key Features**:
  - GenBank (nucleotide sequence database)
  - PubMed (30+ million biomedical citations)
  - Gene Expression Omnibus (GEO)
  - Sequence Read Archive (SRA)
  - BLAST (sequence alignment search tool)
- **Licensing**: Public domain (U.S. government). NCBI databases are freely available with no restrictions on use. International Nucleotide Sequence Database Collaboration (INSDC) policy ensures global open access.
- **Notes**: NCBI is not a single data portal but a collection of interconnected biomedical databases. It is the cornerstone of biomedical and genomic research worldwide. GenBank, along with its partners EMBL-EBI (Europe) and DDBJ (Japan), forms the International Nucleotide Sequence Database Collaboration. Ma...

### Global Biodiversity Information Facility (GBIF)
- **URL**: https://www.gbif.org
- **Operator/Parent**: GBIF Secretariat (international network funded by governments, hosted in Copenhagen, Denmark)
- **Type**: Free
- **Pricing**: Completely free. Registration required for downloading data.
- **Data Types**: Species Occurrence Records, Taxonomic Data (species names, classifications), Specimen Data (museum/herbarium records), Observation Data (citizen science, surveys), Sampling Event Data, Species Checklists, Metadata-only Records
- **Industry Focus**: Biodiversity & Conservation, Ecology & Environmental Science, Academic Research, Agriculture (pest/species monitoring), Pharmaceutical (bioprospecting), Environmental Consulting, Government (environmental policy)
- **Geographic Focus**: Global (data from every continent including Antarctica)
- **Formats**: Darwin Core Archive (DwC-A), CSV, Simple CSV, Species list formats, API (RESTful), GBIF Maps API, Occurrence download (ZIP)
- **Scale**: ~2.6+ billion occurrence records from 85,000+ datasets published by 1,800+ institutions (as of 2024-2025). One of the largest biodiversity databases in the world.
- **Key Features**:
  - Largest biodiversity data network in the world
  - RESTful API for species, occurrences, datasets
  - Interactive occurrence maps
  - Species pages with distribution maps
  - DOI-based data citations for downloaded datasets
- **Licensing**: CC0, CC-BY 4.0, or CC-BY-NC 4.0 depending on data publisher's choice. GBIF encourages CC0 or CC-BY. DOI-based citations ensure academic credit.
- **Notes**: GBIF is the essential infrastructure for global biodiversity research. It aggregates data from natural history museums, citizen science platforms (like iNaturalist), and research surveys worldwide. Used in thousands of peer-reviewed publications annually. The DOI-based download system ensures dat...

### IQVIA (formerly IMS Health / Quintiles IMS)
- **URL**: https://www.iqvia.com
- **Operator/Parent**: IQVIA Holdings Inc. (Durham, NC). Publicly traded on NYSE (IQV).
- **Type**: Paid - enterprise/institutional
- **Pricing**: Enterprise contracts, typically six-to-seven-figure annual subscriptions. Custom pricing based on data modules, geographies, and therapeutic areas. Also provides clinical trial services and technology solutions.
- **Data Types**: Pharmaceutical prescription data, Sales/demand data by drug, Medical claims data, Electronic health record (EHR) data, Clinical trial data, Real-world evidence (RWE), Patient-level data (de-identified), Healthcare provider data
- **Industry Focus**: Pharmaceutical industry, Biotechnology, Life sciences, Healthcare, Government health agencies, Clinical research
- **Geographic Focus**: Global - operates in 100+ countries. Particularly strong in US, Europe, Japan.
- **Formats**: Enterprise data platforms (IQVIA Orchestrated Analytics), Custom data feeds, SAS/statistical software formats, API access, Cloud-based analytics (IQVIA Connected Intelligence), Consulting deliverables
- **Scale**: Analyzes data from 150,000+ data suppliers. Patient-level data on over 1 billion de-identified patient records. $15B+ annual revenue (data, technology, and services combined). 86,000+ employees.
- **Key Features**:
  - World's largest healthcare data and analytics company
  - Covers 85%+ of global pharmaceutical sales data
  - Real-World Evidence (RWE) platform from EHR and claims data
  - Clinical trial design and execution services
  - IQVIA Human Data Science Cloud
- **Status**: Active. One of the largest companies in the healthcare data space. Revenue of ~$15 billion (2023). Actively acquiring (including Definitive Healthcare deal).
- **Notes**: IQVIA is the dominant player in pharmaceutical data. Formed from the merger of IMS Health and Quintiles in 2016. While primarily a data/analytics company, a large portion of revenue comes from clinical trial services (CRO business).

### Lightcast (formerly Emsi Burning Glass)
- **URL**: https://lightcast.io
- **Operator/Parent**: Lightcast (Moscow, ID and Boston, MA). Formed from merger of Emsi and Burning Glass Technologies in 2021, rebranded to Lightcast in 2022.
- **Type**: Paid - enterprise subscriptions. Some free tools (e.g., Open Skills Library).
- **Pricing**: Enterprise SaaS subscriptions. Custom pricing based on modules and user counts. Government/education pricing may differ. Annual contracts typical.
- **Data Types**: Job posting/labor demand data, Skills data and taxonomy, Occupation and wage data, Education program data, Workforce supply data, Compensation benchmarking data, Resume/talent profile data, Career pathway data
- **Industry Focus**: Higher education, Workforce development, Economic development, HR/talent acquisition, Government labor agencies, Corporate learning & development
- **Geographic Focus**: Primarily US, UK, Canada, Australia. Expanding to more countries.
- **Formats**: Web-based analytics platform, API access, Data feeds/bulk data, Open Skills Library (open source), Custom reports and dashboards, Excel/CSV exports
- **Scale**: Processes billions of job postings historically. Covers millions of employer profiles. Used by thousands of educational institutions and employers.
- **Key Features**:
  - Real-time job posting analytics from millions of scraped postings
  - Open Skills Library (open source skills taxonomy)
  - Skills-based workforce analytics
  - Labor market supply-demand gap analysis
  - Career pathway mapping
- **Status**: Active and dominant in labor market analytics. Post-merger integration complete. Continues to expand internationally.
- **Notes**: The Emsi + Burning Glass merger created the dominant player in labor market/skills data analytics. Particularly important for higher education institutions aligning programs with employer demand. Competes with Revelio Labs, LinkedIn Economic Graph, and government BLS data.

### OpenStreetMap (OSM)
- **URL**: https://www.openstreetmap.org
- **Operator/Parent**: OpenStreetMap Foundation (nonprofit, UK-based)
- **Type**: Free
- **Pricing**: Completely free. Community-maintained open geographic data.
- **Data Types**: Geographic/Geospatial Data, Roads & Transportation Networks, Buildings & Structures, Land Use & Land Cover, Points of Interest (POIs), Administrative Boundaries, Water Features, Natural Features, Public Transport Routes, Addresses
- **Industry Focus**: Mapping & Geospatial, Transportation & Logistics, Urban Planning, Navigation & Location Services, Humanitarian Aid (HOT - Humanitarian OpenStreetMap Team), Real Estate, Telecommunications, Academic Research
- **Geographic Focus**: Global (worldwide coverage, quality varies by region)
- **Formats**: OSM XML / PBF (native format), Shapefile (via exports/Geofabrik), GeoJSON, GeoPackage, API (OSM API, Overpass API for queries), Tile images (raster/vector tiles), Planet file (full database dump)
- **Scale**: ~10+ billion nodes, 1+ billion ways, 15+ million relations. Over 9 million registered contributors. One of the largest collaborative geospatial databases in the world.
- **Key Features**:
  - Community-edited (Wikipedia model for maps)
  - Overpass API (powerful geospatial query language)
  - Regular planet file dumps (complete database)
  - Regional extracts (Geofabrik, BBBike)
  - Nominatim (geocoding/address search)
- **Licensing**: Open Data Commons Open Database License (ODbL) 1.0. Free to use, share, and adapt with attribution and share-alike requirements.
- **Notes**: OpenStreetMap is the largest open geospatial dataset in the world. While not a traditional 'data portal,' it is an essential open data resource. Quality varies significantly by region (excellent in Western Europe and major cities, sparser in rural developing areas). Many commercial products and s...

### Reonomy
- **URL**: https://www.reonomy.com
- **Operator/Parent**: Reonomy (New York, NY). Acquired by Altus Group in 2022.
- **Type**: Paid - subscription-based platform
- **Pricing**: SaaS subscription. Plans typically start in the hundreds per month for individual users. Enterprise pricing for teams and API access. Free trial available.
- **Data Types**: Commercial real estate (CRE) property data, Ownership information, Debt/mortgage data, Transaction history, Tenant data, Zoning information, Building permits, Tax assessment data
- **Industry Focus**: Commercial real estate, CRE lending, Property insurance, CRE investment, Brokerage
- **Geographic Focus**: United States - comprehensive national CRE coverage
- **Formats**: Web-based property search and analysis platform, REST API, Data exports (CSV/Excel), CRM integrations, Map-based visual interface
- **Scale**: Covers 50M+ commercial and residential properties in the US. Millions of commercial property records with ownership data.
- **Key Features**:
  - AI-powered property data platform for commercial real estate
  - Entity resolution linking properties to true owners
  - Comprehensive ownership/debt data for CRE
  - Sales comps and transaction analysis
  - Building-level data (tenants, permits, etc.)
- **Status**: Acquired by Altus Group (TSX: AIF) in 2022. Operating as part of Altus Group's analytics division. Active.
- **Notes**: Altus Group is a major CRE analytics and valuation company. The acquisition combined Reonomy's data platform with Altus's appraisal and analytics business. Competes with CoStar, REIS, Real Capital Analytics.

### Replica
- **URL**: https://replicahq.com
- **Operator/Parent**: Replica (San Francisco, CA). Spun out of Alphabet/Sidewalk Labs.
- **Type**: Paid - government/enterprise subscriptions
- **Pricing**: SaaS subscriptions primarily for government agencies and transportation planners. Custom pricing. Some data accessible via partnerships with academic researchers.
- **Data Types**: Population mobility data, Trip origin-destination data, Mode of transportation data, Land use data, Economic activity patterns, Traffic volume estimates, Demographic movement patterns
- **Industry Focus**: Urban planning, Transportation planning, Government/public sector, Infrastructure investment, Real estate development, Economic development
- **Geographic Focus**: United States - growing metro area coverage
- **Formats**: Web-based analytics platform (Replica Places), Data exports, API access, Map-based visualization, Zone-to-zone trip tables
- **Scale**: Covers most major US metro areas. Used by dozens of state DOTs and metropolitan planning organizations.
- **Key Features**:
  - Synthetic population modeling using privacy-preserving techniques
  - Generates synthetic trip-level data from aggregated inputs
  - Combines mobile device data, census data, and other sources
  - Privacy-preserving - creates synthetic populations rather than tracking individuals
  - Spun out of Alphabet's Sidewalk Labs (Google lineage)
- **Status**: Active and growing. Has raised significant venture funding. Expanding geographic and data coverage.
- **Notes**: Replica's approach of creating synthetic populations is a notable privacy-preserving innovation. The Sidewalk Labs/Alphabet heritage gave it early credibility and resources. Competes with StreetLight Data and traditional travel demand models.

### Revelio Labs
- **URL**: https://www.reveliolabs.com
- **Operator/Parent**: Revelio Labs Inc. (New York, NY)
- **Type**: Paid - enterprise subscriptions
- **Pricing**: Enterprise SaaS and data licensing. Custom pricing. Data available via direct feeds, API, or platform access.
- **Data Types**: Workforce composition data, Employee headcount by company, Employee skill profiles, Hiring/attrition rates, Compensation data, Workforce demographics, Workforce sentiment, Job posting analytics
- **Industry Focus**: Investment management/hedge funds, Corporate strategy, HR/talent analytics, Consulting, Private equity due diligence, Economic research
- **Geographic Focus**: Primarily US, growing international coverage
- **Formats**: Web-based analytics platform, API access, Data feeds (for quant/alt data use cases), Cloud delivery (Snowflake, S3), Custom research deliverables
- **Scale**: Tracks hundreds of millions of professional profiles. Coverage of most large public and private companies in the US.
- **Key Features**:
  - Workforce intelligence from public profile data (LinkedIn-derived)
  - Company-level headcount and skill composition tracking
  - Alternative data product for investors tracking workforce changes
  - Hiring/attrition signals as investment indicators
  - Workforce diversity and composition analytics
- **Status**: Active. Well-funded startup growing rapidly. Strong position in alternative data for investors and corporate workforce analytics.
- **Notes**: Revelio Labs occupies the intersection of labor/workforce data and alternative data for investment. Founded by academic labor economists, which gives it analytical rigor. Competes with Lightcast in workforce analytics and with Thinknum/Yipit in alternative data.

### StreetLight Data
- **URL**: https://www.streetlightdata.com
- **Operator/Parent**: StreetLight Data Inc. (San Francisco, CA). Acquired by Jacobs Engineering Group in 2022.
- **Type**: Paid - subscription/project-based
- **Pricing**: SaaS subscriptions and project-based licensing. Government and enterprise pricing. Annual subscriptions or per-analysis pricing. Custom enterprise agreements.
- **Data Types**: Vehicle movement/traffic data, Bicycle and pedestrian counts, Origin-destination trip data, Freight/truck movement data, Speed/travel time data, VMT (vehicle miles traveled) estimates
- **Industry Focus**: Transportation planning, Traffic engineering, Government/DOTs, Urban planning, Real estate, Retail analytics
- **Geographic Focus**: United States and Canada primarily
- **Formats**: Web-based analytics platform (StreetLight InSight), Data exports (CSV), GIS-compatible outputs, API, AADT (Annual Average Daily Traffic) estimates, Map visualizations
- **Scale**: Processes trillions of location data points. Covers all US roads. Used by hundreds of government agencies and planning firms.
- **Key Features**:
  - Processes location-based services (LBS) data from mobile devices at massive scale
  - Machine-learning-calibrated traffic and mobility metrics
  - No hardware deployment needed (fully data-driven vs. sensor-based counting)
  - Historical data available (back several years)
  - Bike and pedestrian mode-specific analytics
- **Status**: Active. Acquired by Jacobs Engineering Group in 2022. Continues to operate as a product within Jacobs.
- **Notes**: StreetLight pioneered the use of mobile device location data for transportation planning, reducing the need for expensive physical traffic counters. The Jacobs acquisition provides access to a large engineering/planning client base.

### Tomorrow.io (formerly ClimaCell)
- **URL**: https://www.tomorrow.io
- **Operator/Parent**: Tomorrow.io (Boston, MA). Rebranded from ClimaCell in 2021.
- **Type**: Both - free tier for basic weather API; paid plans for advanced features and data
- **Pricing**: Freemium API model. Free tier: 500 calls/day. Paid plans: Growth, Business, Enterprise with increasing call volumes, features, and data resolution. Enterprise pricing is custom. Also developing proprietary weather satellite constellation.
- **Data Types**: Weather forecast data (hyperlocal), Historical weather data, Severe weather alerts, Air quality data, Road weather conditions, Pollen/allergen data, Solar/wind energy weather data, Satellite weather data
- **Industry Focus**: Aviation, Logistics/transportation, Construction, Agriculture, Insurance, Events management, Defense/military, Energy
- **Geographic Focus**: Global coverage with minute-by-minute resolution
- **Formats**: REST API (Weather API), Dashboard/platform (Tomorrow.io Platform), Map tiles, Webhook alerts, SDK integrations, Satellite imagery (from proprietary constellation)
- **Scale**: Global coverage. Hundreds of millions of API calls served. Backed by over $400M in venture funding. Building satellite constellation for proprietary data.
- **Key Features**:
  - Hyperlocal weather forecasting using non-traditional data sources
  - MicroWeather technology - uses wireless signal attenuation for precipitation detection
  - Building proprietary weather satellite constellation (Tomorrow-R satellites launched)
  - Weather intelligence platform (not just data, but decision support)
  - Minute-by-minute precipitation nowcasting
- **Status**: Active and growing. Well-funded startup. Launching proprietary weather satellites to differentiate data quality.
- **Notes**: Tomorrow.io is disrupting the traditional weather data market dominated by The Weather Company (IBM) and DTN. The satellite constellation is a significant long-term investment in proprietary data generation.

### Veraset
- **URL**: https://www.veraset.com
- **Operator/Parent**: Veraset Inc. (San Francisco, CA). Spun out of SafeGraph.
- **Type**: Both - free for academic/non-profit research; paid commercial licensing
- **Pricing**: Free access for academic and non-profit researchers (major differentiator). Commercial licensing for enterprise customers with custom pricing.
- **Data Types**: Human mobility/movement data, Device-level location data (de-identified), Visit patterns, Trip origin-destination, Dwell time data
- **Industry Focus**: Academic research, Public health, Urban planning, Transportation, Commercial real estate, Government/public sector
- **Geographic Focus**: United States, with international expansion
- **Formats**: Cloud delivery (AWS S3, Snowflake), Bulk data files, Movement panel data
- **Scale**: Tracks tens of millions of devices in the US. Daily-updating panel data.
- **Key Features**:
  - Spun out of SafeGraph to focus on mobility/movement data
  - Free academic/research access (continuing SafeGraph tradition)
  - Privacy-preserving de-identification
  - Daily-updating movement data
  - Used extensively in COVID-19 and public health research
- **Status**: Active. Growing academic and commercial client base.
- **Notes**: Veraset inherits SafeGraph's popular academic data access program but focuses specifically on mobility/movement data rather than POI data. Critical data source for academic research on human mobility and public health.

### Zillow Data Products (ZTRAX / Zillow Research)
- **URL**: https://www.zillow.com/research/data/
- **Operator/Parent**: Zillow Group Inc. (Seattle, WA). Publicly traded (Nasdaq: ZG/Z).
- **Type**: Both - Zillow Research data is free; ZTRAX (transaction/assessment data) was free for researchers but access has been restricted
- **Pricing**: Zillow Research data (Zillow Home Value Index, rental indices) is freely downloadable. ZTRAX (Zillow Transaction and Assessment Dataset) was provided free to academic researchers but has become harder to access. Zillow API (now via Bridge API) for...
- **Data Types**: Home value indices (ZHVI), Rental price indices (ZRI), Real estate transaction data (ZTRAX), Property assessment data, For-sale listing data, Market heat indices, Days on market data
- **Industry Focus**: Real estate, Housing economics, Urban planning, Academic research, Investment/finance, Government/policy
- **Geographic Focus**: United States (comprehensive coverage)
- **Formats**: CSV downloads (research data), API access, Bulk data (ZTRAX - by application), Web-based data tools/visualizations
- **Scale**: Covers 100M+ US properties. ZTRAX contains hundreds of millions of transaction records. Research data covers all US metros/states.
- **Key Features**:
  - Zillow Home Value Index (ZHVI) - widely cited housing market metric
  - Granular geographic coverage (ZIP, city, county, metro, state, national)
  - ZTRAX - one of the most comprehensive US property transaction databases
  - Time series data going back decades
  - Regular monthly/quarterly updates
- **Status**: Active. Zillow Research data freely available. ZTRAX access has become more restricted over time. Zillow sunsetted some public APIs in favor of Bridge Interactive platform.
- **Notes**: Zillow shut down its iBuying business (Zillow Offers) in 2021, but data products continue. ZTRAX was a uniquely valuable research resource; its restricted access has been lamented by academic researchers.

---

## 10. Alternative Data, Web Data & Financial Data Providers

### Advan Research
- **URL**: https://www.advanresearch.com
- **Operator/Parent**: Advan Research Corporation (independent) [Based on training data, may need verification]
- **Type**: Paid - Enterprise/institutional only
- **Pricing**: Enterprise subscription. Custom pricing for institutional clients. [Based on training data, may need verification]
- **Data Types**: Foot traffic data for public companies, Consumer visitation analytics, Location intelligence for equities research
- **Industry Focus**: Hedge funds, Asset management, Equity research, Investment banking
- **Geographic Focus**: US primarily
- **Formats**: Platform/dashboard, API, Data feeds, Flat files
- **Scale**: Tracks thousands of retail chains across US [Based on training data, may need verification]
- **Key Features**:
  - Foot traffic data specifically designed for equity investors
  - Ticker-mapped location data (mapped to publicly traded companies)
  - Historical data for backtesting investment strategies
  - Daily/weekly foot traffic estimates for retail chains
- **Provider Requirements**: Not a two-sided marketplace.
- **Status**: Active [Based on training data, may need verification]
- **Notes**: Advan is a specialized location data provider focused specifically on the investment community. Their data is mapped to public company tickers, making it directly usable for equity analysis and trading strategies. Representative of the growing niche of alternative data providers serving Wall Street.

### BattleFin
- **URL**: https://www.battlefin.com
- **Operator/Parent**: BattleFin LLC (New York, NY)
- **Type**: Paid - enterprise/institutional
- **Pricing**: Event-based and platform-based. BattleFin runs invitation-only alternative data conferences (Discovery Days) connecting data providers with buy-side firms. Also operates BattleFin Ensemble platform for data discovery. Conference attendance and pla...
- **Data Types**: Alternative data discovery platform - aggregates metadata about hundreds of alternative data providers, Satellite imagery, Web scraping data, Transaction data, Social sentiment, Geolocation data, App usage data
- **Industry Focus**: Hedge funds, Asset management, Quantitative finance, Investment research, Alternative data
- **Geographic Focus**: Primarily US and Europe (financial centers)
- **Formats**: Discovery platform (BattleFin Ensemble) for searching alternative data providers, Events/conferences for data provider-buyer matchmaking, Not a direct data delivery platform but a marketplace/discovery layer
- **Scale**: Catalogs hundreds of alternative data providers. Events attract major hedge funds and asset managers. Niche but influential in alternative data ecosystem.
- **Key Features**:
  - Alternative data discovery and evaluation platform
  - Invitation-only Discovery Day events connecting data sellers with hedge funds
  - BattleFin Ensemble platform for cataloging and searching data providers
  - Data evaluation and due diligence services
  - Focus specifically on alternative data for investment
- **Status**: Active. Has been a key connector in the alternative data ecosystem since approximately 2013.
- **Notes**: BattleFin is more of a marketplace facilitator/discovery platform than a direct data provider. It helps institutional investors find and evaluate alternative data sources. The Discovery Day events are considered important networking venues in the alt data space.

### Battlefin / Eagle Alpha
- **URL**: https://www.battlefin.com
- **Operator/Parent**: BattleFin Group (independent). Eagle Alpha is a separate but related company in the alternative data discovery space.
- **Type**: Paid / By invitation for events; platform access varies
- **Pricing**: BattleFin operates alternative data discovery events/conferences plus a data intelligence platform. Eagle Alpha offers an alternative data discovery and evaluation platform (subscription-based). [Based on training data, may need verification]
- **Data Types**: Alternative data discovery and evaluation, Financial alternative data (all types), Data provider matching/curation
- **Industry Focus**: Hedge funds, Asset management, Investment banking, Quantitative finance
- **Geographic Focus**: Global, US-focused
- **Formats**: Discovery platform, Events/conferences, Data evaluation services, Curated introductions to data providers
- **Scale**: Network of hundreds of alternative data providers and thousands of institutional data buyers [Based on training data, may need verification]
- **Key Features**:
  - Alternative data discovery events connecting data buyers and sellers
  - Data provider evaluation and curation
  - Community of alternative data professionals
  - BattleFin Alternative Data conferences
- **Provider Requirements**: Data providers apply to present at events or list on platform. Curated/vetted for relevance to institutional investors.
- **Status**: Active [Based on training data, may need verification]
- **Notes**: BattleFin and Eagle Alpha serve the alternative data ecosystem primarily as discovery and matching platforms rather than transactional marketplaces. They help institutional investors find and evaluate alternative data providers. The BattleFin conferences (ensemble, discovery day) are important ne...

### Bright Data (formerly Luminati Networks)
- **URL**: https://brightdata.com
- **Operator/Parent**: Bright Data Ltd. (independent, Israeli company, formerly Luminati Networks Ltd.)
- **Type**: Paid - usage-based pricing
- **Pricing**: Pay-as-you-go and subscription plans. Proxy services priced per GB of traffic ($5-$25+/GB depending on proxy type). Web scraping/data collection priced per request or per record. Ready-made datasets priced per dataset or subscription. Plans range ...
- **Data Types**: Web-scraped data (any public website), E-commerce data (pricing, products, reviews), Social media data, SERP/search engine data, Real estate listing data, Travel/airline/hotel pricing data, Job listing data, News/media data, Financial data (from public web sources), Ready-made datasets (pre-collected), Web-scraped data (any website), E-commerce product/pricing data, Travel/hospitality data, Real estate listings data, Job postings data, Financial data, Ready-made datasets
- **Industry Focus**: E-commerce (price monitoring, market intelligence), Ad verification, Brand protection, Market research, Financial services (alternative data), Travel/hospitality, Cybersecurity, Academic research, SEO/digital marketing, E-commerce intelligence, Financial research
- **Geographic Focus**: Global - proxy network covers 195+ countries; data collection from websites worldwide
- **Formats**: Bright Data Web Scraper IDE (visual scraping tool), Proxy APIs (HTTP/HTTPS, SOCKS), Data Collector (automated scraping), Ready-made datasets (JSON, CSV, Excel), Bright Data Scraping Browser (headless browser), API access, SERP API, Web Unlocker (anti-bot bypass), Ready-made datasets (JSON, CSV), Web Scraper IDE (custom scraping), Proxy network (residential, datacenter, mobile, ISP), Browser automation tools, Snowflake/cloud delivery for datasets
- **Scale**: 72M+ residential IPs, millions of datacenter IPs. Serves 20,000+ customers including Fortune 500 companies. [Based on training data, may need verification]
- **Key Features**:
  - Largest proxy network globally (72M+ residential IPs)
  - Proxy types: Residential, datacenter, ISP, mobile
  - Web Scraper IDE - no-code/low-code web scraping tool
  - Ready-made datasets for popular data categories
  - Web Unlocker - automated anti-bot bypass
- **Provider Requirements**: Not a traditional two-sided data marketplace. Bright Data provides the infrastructure for web data collection. Residential proxy network sources IPs from opt-in users via SDK partnerships.
- **Status**: Active and profitable. Major player in web data collection. Has faced regulatory and ethical scrutiny over proxy network practices.
- **Notes**: Bright Data (formerly Luminati) is the largest commercial proxy and web data collection platform. Controversial history due to the residential proxy network model (shares bandwidth from consumer devices via SDK in apps like HolaVPN). Has invested heavily in compliance and repositioned as a legiti...

### Common Crawl
- **URL**: https://commoncrawl.org
- **Operator/Parent**: Common Crawl Foundation (501(c)(3) non-profit, San Francisco)
- **Type**: Free - entirely open and free to use
- **Pricing**: Free. Data is hosted on AWS S3 (as part of AWS Open Data Program, so no egress fees). The foundation is funded by donations and grants. Users may incur AWS compute costs if processing data in the cloud.
- **Data Types**: Web crawl data (raw HTML), Extracted text content, Metadata (HTTP headers, URLs), WAT (metadata), WET (text), WARC (raw) formats
- **Industry Focus**: AI/ML training, NLP research, Web research, Academic research, Search engine development, Data science
- **Geographic Focus**: Global web - crawls billions of pages across all languages and countries
- **Formats**: WARC files (Web Archive format - full raw crawl), WET files (extracted text only), WAT files (metadata only), Hosted on AWS S3 for direct access, Columnar index for URL-level lookups
- **Scale**: Each monthly crawl contains 3-5+ billion web pages. Total archive spans 10+ years of monthly crawls. Hundreds of petabytes of total data. Used to train many of the world's largest language models.
- **Key Features**:
  - One of the largest freely available web crawl datasets
  - Monthly crawls containing billions of pages (3-5 billion pages per crawl)
  - Petabytes of historical crawl data available
  - Used as foundation for major AI models and datasets (C4, OSCAR, The Pile)
  - Hosted free on AWS Open Data Program
- **Status**: Active. Continues monthly crawls. One of the most important open data resources for AI development.
- **Notes**: Common Crawl data was foundational for training GPT-3, BERT, T5, and many other major language models. The C4 (Colossal Clean Crawled Corpus) dataset used for T5 was derived from Common Crawl. Critical infrastructure for AI research.

### Crux Informatics
- **URL**: https://www.cruxinformatics.com
- **Operator/Parent**: Crux Informatics, Inc. (independent, backed by Two Sigma founders)
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise subscription for data operations platform. Custom pricing based on data volume, complexity, and number of data pipelines managed.
- **Data Types**: Alternative data for finance (various types), Data operations/pipeline management, External data ingestion and delivery, Reference data, Market data
- **Industry Focus**: Hedge funds/quantitative finance (primary), Asset management, Investment banking
- **Geographic Focus**: Global (data sources worldwide)
- **Formats**: Crux platform (managed data operations), Cloud delivery (S3, GCS, Azure), Snowflake delivery, API access, Managed data pipelines
- **Scale**: Manages data pipelines for major financial institutions. [Based on training data, may need verification]
- **Key Features**:
  - Managed data operations - Crux handles the engineering of ingesting, cleaning, and delivering external data
  - Founded by Two Sigma (major quant hedge fund) leadership
  - Focuses on the 'plumbing' of external data rather than being a marketplace
  - Data quality monitoring and pipeline reliability
  - Reduces operational burden of managing multiple data vendor feeds
- **Provider Requirements**: Not a two-sided marketplace. Crux manages data operations for existing data vendor relationships.
- **Status**: Active [Based on training data, may need verification]
- **Notes**: Crux solves the operational challenge of managing alternative data pipelines rather than being a marketplace for discovering data. Founded out of the Two Sigma ecosystem, it understands the pain points of quantitative firms managing dozens of alternative data feeds.

### Databento
- **URL**: https://databento.com
- **Operator/Parent**: Databento Inc. (Palo Alto, CA)
- **Type**: Paid - usage-based
- **Pricing**: Usage-based pricing (pay per query/byte). No minimum commitments. Real-time market data priced per symbol/per month. Historical data priced by data volume. Significantly cheaper than traditional market data providers.
- **Data Types**: Real-time market data (equities, futures, options), Historical tick data, Level 2/order book data, Trades and quotes (TAQ), Options data, Cryptocurrency market data
- **Industry Focus**: Quantitative trading, Algorithmic trading, Market research, Financial data science, Hedge funds
- **Geographic Focus**: US markets primarily (CME, Nasdaq, NYSE, CBOE, etc.). Expanding.
- **Formats**: REST API, Real-time WebSocket feeds, Python/C++/Rust client libraries, Historical data downloads, DBN (Databento Binary) format for efficiency, CSV export
- **Scale**: Covers major US exchanges. Growing data coverage and exchange partnerships.
- **Key Features**:
  - Modern, developer-friendly market data API
  - Usage-based pricing disrupting traditional market data licensing
  - Sub-second historical data access
  - Normalized data across exchanges
  - No minimum commitments or long-term contracts
- **Status**: Active. Well-funded startup disrupting the market data industry. Y Combinator alumni.
- **Notes**: Databento is disrupting the traditional market data industry (Bloomberg, Refinitiv, ICE) with modern API-first design and transparent usage-based pricing. Particularly popular with quantitative traders and smaller hedge funds.

### Eagle Alpha
- **URL**: https://eaglealpha.com
- **Operator/Parent**: Eagle Alpha Ltd (Dublin, Ireland)
- **Type**: Paid - enterprise/institutional
- **Pricing**: Enterprise SaaS and advisory. Provides a data discovery platform (Eagle Alpha Data Marketplace) plus advisory services for alternative data sourcing. Custom enterprise pricing.
- **Data Types**: Alternative data aggregation/discovery, ESG data, Web traffic data, App data, Social media data, Satellite data, Transaction data, Job postings data, Reviews/sentiment
- **Industry Focus**: Asset management, Hedge funds, Private equity, Corporate strategy, Alternative data
- **Geographic Focus**: Global, primarily serving US and European financial institutions
- **Formats**: Data marketplace/catalog platform, Advisory and consulting services, Data procurement support, API connections to vetted data providers, Custom data sourcing
- **Scale**: Catalogs and evaluates hundreds of alternative data providers. Serves institutional investors globally. Published influential annual alternative data surveys.
- **Key Features**:
  - Curated marketplace of vetted alternative data providers
  - Advisory services for data strategy and procurement
  - Data vendor due diligence and evaluation
  - ESG data specialization
  - Regular research reports on alternative data trends
- **Status**: Active as of 2024. Has been growing as the alternative data market expands. Privately held.
- **Notes**: Similar to BattleFin in connecting data providers with financial buyers, but Eagle Alpha has a stronger advisory/consulting component. Publishes annual alternative data surveys that are widely cited in the industry.

### Enigma (Enigma Technologies)
- **URL**: https://www.enigma.com
- **Operator/Parent**: Enigma Technologies, Inc. (independent, New York-based)
- **Type**: Paid (some free public data tools previously available)
- **Pricing**: Enterprise subscription and per-record API pricing. Custom pricing for bulk data licensing. [Based on training data, may need verification]
- **Data Types**: Small business data, Business identity/verification data, Revenue estimation data, Business financial health data, Government registration/licensing data, Public records data
- **Industry Focus**: Banking/lending (small business lending), Insurance, Financial services, Government, Compliance/KYC
- **Geographic Focus**: US primarily
- **Formats**: Enigma API, Platform/dashboard access, Bulk data delivery, Integration with lending/underwriting platforms
- **Scale**: Data on millions of US small businesses. [Based on training data, may need verification]
- **Key Features**:
  - Specializes in small business data (a notoriously difficult category)
  - Links public records across government sources to build comprehensive business profiles
  - Revenue estimation for small businesses (where financials are not publicly available)
  - Strong in small business lending use cases
  - Public data aggregation and linking expertise
- **Provider Requirements**: Not a two-sided marketplace. Enigma aggregates public records and builds proprietary data products.
- **Notes**: Enigma fills an important gap - small business data is notoriously incomplete and fragmented. They aggregate public records from thousands of government sources to build comprehensive small business profiles. Particularly valuable for lenders who need to underwrite small businesses that lack the ...

### Explorium
- **URL**: https://www.explorium.ai
- **Operator/Parent**: Explorium Ltd. (independent, Israeli-American company)
- **Type**: Paid (with free trial/demo available)
- **Pricing**: SaaS subscription based on data volume and features. Enterprise custom pricing. The platform connects to thousands of external data signals, so pricing reflects both platform access and data enrichment volume.
- **Data Types**: External data discovery and enrichment (thousands of signals), B2B firmographic data, Technographic data, Web presence/traffic data, Social media signals, Financial data, Consumer demographic data, Job market/hiring data, Geospatial data, Industry-specific signals, External data aggregation for ML/AI, Business firmographic data, Web traffic data, Government/public records, Intent data
- **Industry Focus**: Financial services (credit risk, fraud), Insurance (underwriting, claims), B2B marketing/sales, E-commerce, Healthcare, Real estate, Financial services, Insurance, B2B marketing, Credit risk, Fraud detection, Customer analytics
- **Geographic Focus**: Global data enrichment capabilities, company based in US and Israel
- **Formats**: Explorium platform (cloud-based), API for automated enrichment, Batch processing, Integrations with ML platforms (Databricks, SageMaker), CSV/data frame outputs, Feature store integration, Platform-based external data discovery and enrichment, API, Integration with ML pipelines and BI tools, Feature engineering platform, Snowflake/cloud delivery
- **Scale**: Access to thousands of external data sources, billions of data points. Serves hundreds of enterprise customers. [Based on training data, may need verification]
- **Key Features**:
  - Automated external data discovery - AI finds relevant external signals for your use case
  - Signal discovery engine - automatically tests thousands of external data features
  - Feature engineering automation
  - Pre-built connectors to thousands of data sources
  - ML-ready feature store
- **Provider Requirements**: Not a traditional two-sided marketplace. Explorium aggregates external data from various sources (licensed, public, and partnered) and uses AI to match relevant signals to customer use cases.
- **Status**: Active. Venture-backed (raised $75M+). Growing as external data for AI becomes more important.
- **Notes**: Explorium's key innovation is automated external data discovery - rather than manually searching for relevant datasets, their AI engine automatically identifies which external data signals improve your ML models or analytics. This is different from a traditional marketplace where you browse and b...

### Nasdaq Data Link (formerly Quandl)
- **URL**: https://data.nasdaq.com
- **Operator/Parent**: Nasdaq, Inc. (publicly traded: NDAQ on Nasdaq)
- **Type**: Both - Many free datasets; premium/alternative data requires paid subscription
- **Pricing**: Freemium. Core financial data is free with usage limits. Premium/alternative datasets are separately priced by their providers (subscription-based, ranging from hundreds to tens of thousands per month). Nasdaq Data Link takes a revenue share from ...
- **Data Types**: Financial market data (equities, futures, options), Alternative data (web traffic, sentiment, satellite, etc.), Economic/macro data, Commodity data, Real estate data (Zillow via Quandl), Cryptocurrency data, Fund holdings data, Consumer/corporate alternative data, ESG data, Financial market data, Economic/macroeconomic data, Alternative data, Real estate data, Demographic data
- **Industry Focus**: Quantitative finance/hedge funds, Asset management, Academic research, Data science, Algorithmic trading, Risk management, Quantitative finance, Investment management, Economic research, Financial modeling
- **Geographic Focus**: Primarily US financial data, with some global coverage depending on dataset
- **Formats**: REST API, Python/R packages (direct data access), CSV/JSON/XML downloads, Excel add-in, Bulk data downloads, Nasdaq Data Link platform (web-based), REST API (Nasdaq Data Link API), Python, R, Excel libraries, CSV/JSON downloads, Direct integration with quant platforms (QuantConnect, Zipline)
- **Scale**: Hundreds of datasets from dozens of providers. Millions of time series. Hundreds of thousands of users. [Based on training data, may need verification]
- **Key Features**:
  - One of the earliest alternative data platforms for finance
  - Easy-to-use API with native Python/R libraries
  - Free tier makes it accessible for students, researchers, and small firms
  - Two-sided marketplace for alternative data providers to reach quant finance audience
  - Strong community of quantitative analysts and data scientists
- **Provider Requirements**: Two-sided marketplace: Data providers can apply to list premium datasets. Nasdaq vets data quality and relevance to the finance/investment community. Revenue share model with providers.
- **Status**: Active as Nasdaq Data Link. Integrated into Nasdaq's broader data business. API and data products continue to operate.
- **Notes**: Quandl was a pioneer in the alternative data for finance space. Nasdaq acquisition gave it institutional credibility and distribution. The platform is particularly popular with quant researchers and smaller hedge funds who need cost-effective alternative data access. The free datasets (FRED econo...

### Neudata
- **URL**: https://www.neudata.co
- **Operator/Parent**: Neudata Ltd. (independent, London-based)
- **Type**: Paid - Subscription for buy-side firms
- **Pricing**: Annual subscription for the scouting platform. Pricing based on firm size and number of users. [Based on training data, may need verification]
- **Data Types**: Alternative data scouting/discovery (not the data itself), Data provider profiles and evaluations, Data product reviews and assessments
- **Industry Focus**: Hedge funds, Asset management, Quantitative finance, Private equity
- **Geographic Focus**: Global alternative data landscape
- **Formats**: Neudata Scout platform (web-based), Research reports on data providers, Alerts on new data products
- **Scale**: Tracks 2,000+ data providers, used by hundreds of institutional investors [Based on training data, may need verification]
- **Key Features**:
  - Largest alternative data scouting/discovery platform
  - Tracks 2,000+ alternative data providers
  - Independent evaluations and reviews of data products
  - New data product alerts
  - Analyst team that evaluates data providers
- **Provider Requirements**: Not a transactional marketplace. Neudata scouts and evaluates data providers independently. Providers do not pay to be listed (maintaining independence).
- **Notes**: Neudata is the leading independent alternative data scouting platform. Think of it as an analyst/research firm that evaluates alternative data providers, not a marketplace where you buy data. Very influential in the alt data ecosystem as hedge funds rely on Neudata's evaluations to find new data ...

### PitchBook
- **URL**: https://pitchbook.com
- **Operator/Parent**: PitchBook Data Inc. (Seattle, WA). Acquired by Morningstar Inc. in 2016.
- **Type**: Paid - enterprise subscription
- **Pricing**: Enterprise subscriptions. Annual contracts typically $20,000-$50,000+ per seat depending on features and data access. Academic pricing available through university subscriptions.
- **Data Types**: Private company valuations, VC/PE deal data, M&A transaction data, Fund performance data, LP (limited partner) data, Company financials, Cap table data, Industry/sector analytics
- **Industry Focus**: Venture capital, Private equity, Investment banking, Corporate development, Academic research (finance), LP/institutional investors
- **Geographic Focus**: Global, comprehensive coverage of US, Europe, Asia-Pacific private markets
- **Formats**: Web-based platform, Excel plugin, PDF reports, API (PitchBook Data API), Salesforce integration, Data feeds for quantitative analysis
- **Scale**: Covers 3M+ companies, 1.5M+ deals, 300K+ investors. Gold standard for private market data. Morningstar subsidiary.
- **Key Features**:
  - Most comprehensive private market data platform
  - Detailed company profiles with estimated valuations
  - Fund-level performance benchmarking
  - Deal comparables and multiples
  - 1,800+ researchers maintaining data quality
- **Status**: Active and dominant. Continues to expand coverage and features under Morningstar ownership.
- **Notes**: PitchBook is the institutional-grade private market data platform, while Crunchbase serves a broader/lighter-weight market. The Morningstar acquisition created a powerful public+private market data combination.

### Polygon.io
- **URL**: https://polygon.io
- **Operator/Parent**: Polygon.io Inc. (Raleigh, NC)
- **Type**: Both - free basic tier; paid plans for real-time and higher-volume access
- **Pricing**: Tiered API subscriptions. Free (Basic): delayed data, limited calls. Starter ($29/month), Developer ($79/month), Advanced ($199/month), Business ($custom). Real-time data available on paid tiers.
- **Data Types**: Stock market data (US equities), Options data, Forex data, Cryptocurrency data, Reference data (tickers, company info), News/sentiment
- **Industry Focus**: FinTech development, Algorithmic trading, Financial app development, Quantitative analysis
- **Geographic Focus**: Primarily US financial markets
- **Formats**: REST API, WebSocket real-time streaming, Client libraries (Python, Go, JavaScript, etc.), JSON format, Flat files for historical data
- **Scale**: Covers all US stocks, options, forex, and crypto. Serves thousands of developers and FinTech applications.
- **Key Features**:
  - Developer-friendly financial data APIs
  - Real-time and historical market data
  - WebSocket streaming for live data
  - Generous free tier for development
  - Simple REST API design
- **Status**: Active and growing. Popular alternative to more expensive traditional market data feeds.
- **Notes**: Polygon.io makes financial market data accessible to developers and startups who can't afford Bloomberg or direct exchange feeds. Part of the democratization of financial data alongside Databento and Alpha Vantage.

### Similarweb
- **URL**: https://www.similarweb.com
- **Operator/Parent**: Similarweb Ltd. (publicly traded: SMWB on NYSE)
- **Type**: Both - free browser extension and limited web lookups; paid platform subscriptions
- **Pricing**: Freemium SaaS. Free tier provides limited website analytics. Paid plans: Starter, Professional, Team, Enterprise. Enterprise data licensing for bulk access. Starting at hundreds/month for individual plans, enterprise is custom. [Based on training ...
- **Data Types**: Website traffic data (visits, engagement, sources), App analytics (downloads, usage, engagement), Digital market intelligence, Audience demographics, Search/keyword data, Referral/advertising intelligence, Industry benchmarks, Conversion and funnel data, Website traffic estimates, Digital audience data, Referral and advertising data, App analytics (mobile intelligence), Shopper Intelligence (eCommerce), Stock intelligence (investment signals)
- **Industry Focus**: Digital marketing, Competitive intelligence, Investment/finance (digital alternative data), E-commerce, Media/publishing, Management consulting, Venture capital, eCommerce, Investment research, Sales intelligence, SEO/SEM, Advertising
- **Geographic Focus**: Global - estimates for websites and apps worldwide
- **Formats**: Similarweb platform (web-based dashboards), REST API, Data exports (CSV, Excel), Custom data feeds for enterprise, Salesforce integration, Excel plugin, Web-based analytics platform, Chrome browser extension, CSV/Excel exports, Data feeds for enterprise, Similarweb Digital Data product for financial services
- **Scale**: Estimates traffic for 100M+ websites. Data from panel of hundreds of millions of devices, ISP partnerships, and direct measurement. Major global digital intelligence provider.
- **Key Features**:
  - Leading digital competitive intelligence platform
  - Website traffic estimation for virtually any domain
  - App intelligence across iOS and Android
  - Benchmark any company's digital presence against competitors
  - Shopper Intelligence (e-commerce specific analytics)
- **Provider Requirements**: Not a two-sided marketplace. Similarweb collects data through browser extensions, ISP partnerships, web crawling, and proprietary estimation algorithms.
- **Status**: Active. Publicly traded since 2021. Has made several acquisitions to expand product line. Revenues growing but company has faced profitability challenges typical of growth-stage SaaS.
- **Notes**: Similarweb is the leading provider of digital competitive intelligence data. Their website traffic estimation is widely used across industries. The investment/finance vertical is a growing focus (competing with Thinknum in providing digital signals for investors). The free tier is very popular an...

### Thinknum
- **URL**: https://www.thinknum.com
- **Operator/Parent**: Thinknum Inc. (independent, later acquired by M Science, which itself was acquired by Vontobel [Based on training data, may need verification])
- **Type**: Paid - Enterprise only (some limited free data available)
- **Pricing**: Enterprise subscription licensing. Custom pricing based on data products, number of users, and use case. Annual contracts. Pricing typically in the tens of thousands per year for institutional clients. [Based on training data, may need verification]
- **Data Types**: Alternative data derived from public web sources, Job listings data (hiring trends), Employee reviews and sentiment (Glassdoor-derived), Product pricing data, App store data (rankings, reviews), Social media metrics, Web traffic data, Patent filings data, Government contracts data, SEC filing analytics, Store location/opening/closing data, Online inventory levels
- **Industry Focus**: Hedge funds/quantitative investing, Asset management, Private equity, Investment banking, Equity research, Corporate strategy, Venture capital
- **Geographic Focus**: Primarily US with some global coverage depending on data type
- **Formats**: Thinknum web platform (interactive dashboards), REST API, Bulk data downloads (CSV), Excel add-in, Python library, Snowflake delivery [Based on training data, may need verification]
- **Scale**: Tracks 400K+ companies, billions of data points. Serves hundreds of institutional clients. [Based on training data, may need verification]
- **Key Features**:
  - Pioneer in web-derived alternative data for finance
  - Tracks 400K+ companies through web data signals
  - Comprehensive job listing data for tracking hiring trends
  - Product pricing tracking across major retailers
  - Company-level dashboards with multiple alternative data signals
- **Provider Requirements**: Not a two-sided marketplace. Thinknum collects data through web scraping and public web monitoring.
- **Status**: Active [Based on training data, may need verification - check current status following M Science acquisition]
- **Notes**: Thinknum was an early mover in the alternative data space, systematically collecting public web data and structuring it for institutional investors. The platform excels at tracking companies through non-traditional signals like job postings, product pricing, and app rankings. The M Science connec...

### Thinknum Alternative Data
- **URL**: https://www.thinknum.com
- **Operator/Parent**: Thinknum Inc. (New York, NY)
- **Type**: Paid - enterprise/institutional
- **Pricing**: Enterprise subscriptions for hedge funds and institutional investors. Custom pricing. Data available via platform, API, and bulk delivery.
- **Data Types**: Job listings data (by company), Social media follower counts, App store rankings and reviews, Web traffic estimates, Car inventory data, Product pricing/availability, Store location/closure data, Patent filings, SEC filings analysis, Google Trends data
- **Industry Focus**: Hedge funds, Asset management, Alternative data for investment, Equity research, Private equity due diligence
- **Geographic Focus**: Primarily US companies tracked, with growing international coverage
- **Formats**: Web-based analytics platform, REST API, Bulk data delivery (S3, SFTP), Excel plugin, Snowflake integration, Python SDK
- **Scale**: Tracks 500K+ companies across dozens of web-scraped data types. Used by hundreds of investment firms.
- **Key Features**:
  - Web-scraped alternative data covering 500K+ companies
  - Tracks publicly observable digital signals (job postings, social media, app data)
  - Historical time series for all tracked metrics
  - Company-level granularity for investment analysis
  - Dashboard and visualization tools
- **Status**: Active. Well-established in the alternative data space for investment.
- **Notes**: Thinknum focuses on web-scraped alternative data that can serve as leading indicators for investment decisions. For example, tracking a company's job postings can signal expansion or contraction before it shows in financial results.

### data.ai (formerly App Annie)
- **URL**: https://www.data.ai
- **Operator/Parent**: data.ai Inc. (San Francisco, CA). Rebranded from App Annie in 2022. Acquired by Sensor Tower in 2024.
- **Type**: Both - limited free tier (app rankings, basic estimates); paid subscriptions for detailed analytics
- **Pricing**: Tiered SaaS subscriptions. Free tier for basic app store data. Paid plans (Intelligence, Connect) for detailed download/revenue estimates, usage analytics, advertising analytics. Enterprise pricing is custom and can be $50K-$200K+/year for compreh...
- **Data Types**: Mobile app store data (downloads, revenue, rankings), App usage and engagement metrics, Mobile advertising data, App audience demographics, Cross-app usage, Mobile market share data, App performance metrics
- **Industry Focus**: Mobile app development, Mobile gaming, Digital advertising, Venture capital/investment, Market research, Competitive intelligence
- **Geographic Focus**: Global - covers iOS App Store and Google Play across all countries
- **Formats**: Web-based analytics dashboard, REST API, CSV/Excel exports, Custom reports, Data connectors to BI tools
- **Scale**: Tracks millions of apps across iOS and Google Play. Estimates for 150+ countries. Previously the largest independent mobile analytics provider.
- **Key Features**:
  - Industry-standard mobile app market data
  - Download and revenue estimates for millions of apps
  - Usage and engagement analytics from panel data
  - Advertising analytics (creative, spend, network analysis)
  - App Store Optimization (ASO) tools
- **Status**: Acquired by Sensor Tower in late 2024. The data.ai brand may be merged into Sensor Tower's platform. The combined entity creates the dominant mobile app intelligence provider.
- **Notes**: The SEC settlement in 2021 was related to misleading investors about how the company was using consumers' personal data from its consumer-facing apps to fuel its analytics products. After the Sensor Tower acquisition, the competitive landscape changed significantly.

---

## 99. Other / Uncategorized

### CARTO Data Observatory
- **URL**: https://carto.com/spatial-data-catalog
- **Operator/Parent**: CARTO (formerly CartoDB), headquartered in New York/Madrid
- **Type**: Both - some free/open datasets accessible; premium datasets require CARTO subscription or additional licensing
- **Pricing**: Part of CARTO platform subscription. Data Observatory provides curated geospatial and spatial datasets that can be accessed through the CARTO platform. Some datasets are free (open data), others are premium from third-party providers at additional...
- **Data Types**: Geospatial data, Demographics, Points of interest (POI), Boundaries (administrative, postal), Financial data (spatially indexed), Mobility data, Environmental data, Human mobility patterns
- **Industry Focus**: Location intelligence, Retail site selection, Urban planning, Logistics, Real estate, Marketing/advertising, Government
- **Geographic Focus**: Global coverage, strong in US and Europe
- **Formats**: Integrated into CARTO platform (cloud-native), SQL access via CARTO's data warehouse connections (BigQuery, Snowflake, Redshift, Databricks), Spatial Data Catalog browsing interface, No raw file downloads - accessed through platform
- **Scale**: Thousands of curated spatial datasets from dozens of providers. Covers 190+ countries for some dataset categories.
- **Key Features**:
  - Curated spatial data catalog with thousands of datasets
  - Seamless integration with CARTO's spatial analytics platform
  - Data enrichment workflows - enrich your own data with Observatory data
  - Cloud-native architecture working with major data warehouses
  - Partnerships with data providers like Mastercard, Vodafone, SafeGraph/Dewey successors
- **Status**: Active. CARTO has evolved from a mapping tool to a full spatial analytics platform. The Data Observatory / Spatial Data Catalog is a key product differentiator.
- **Notes**: Renamed from 'Data Observatory' to 'Spatial Data Catalog' in recent product updates. Particularly strong for enriching location-based business data with demographics, POI, and mobility information.

### Canada Open Government Portal
- **URL**: https://open.canada.ca
- **Operator/Parent**: Government of Canada, Treasury Board of Canada Secretariat
- **Type**: Free
- **Pricing**: Completely free. No registration required.
- **Data Types**: Agriculture & Food, Arts, Music & Literature, Economics & Industry, Education & Training, Form Descriptions, Government & Politics, Health & Safety, History & Archaeology, Information & Communications, Labour, Language & Linguistics, Law, Military, Nature & Environment, Persons, Processes & Procedures, Science & Technology, Society & Culture, Transport
- **Industry Focus**: Government & Public Policy, Natural Resources & Environment, Healthcare, Agriculture, Transportation, Academic Research
- **Geographic Focus**: Canada (federal government data; some provincial data)
- **Formats**: CSV, JSON, XML, GeoJSON, Shapefile, KML, Excel, PDF, HTML, FGDB, API (CKAN-based)
- **Scale**: ~90,000+ datasets from federal departments and agencies (as of 2024-2025)
- **Key Features**:
  - CKAN-based platform
  - Bilingual (English and French)
  - Open Maps for geospatial data
  - Proactive Disclosure (government spending, contracts, travel)
  - Open Information (completed Access to Information requests)
- **Licensing**: Open Government Licence - Canada. Very permissive, allows commercial and non-commercial use with attribution.
- **Notes**: Canada is recognized as a global leader in open government data. The portal includes not just datasets but also proactive disclosure information (government contracts, travel expenses, etc.) and completed access to information requests. Strong geospatial data holdings through Natural Resources Ca...

### Flatfile
- **URL**: https://flatfile.com
- **Operator/Parent**: Flatfile Inc. (Denver, CO)
- **Type**: Both - free tier; paid plans for higher volume
- **Pricing**: Freemium. Free tier for basic data import. Paid plans based on records imported. Not a data marketplace but a data onboarding/import tool.
- **Data Types**: Data import/onboarding tool - handles CSV, Excel, and other file imports, Not a data marketplace
- **Industry Focus**: SaaS companies, Data onboarding, ETL/data integration
- **Geographic Focus**: Global
- **Formats**: Embeddable data importer widget, API, Webhook-based data delivery
- **Scale**: Used by thousands of SaaS companies for data onboarding.
- **Key Features**:
  - Intelligent data import/onboarding for SaaS applications
  - Data validation and transformation during import
  - Embeddable in any web application
  - NOT a data marketplace - included here for completeness but this is a data infrastructure tool
- **Status**: Active. Well-funded startup.
- **Notes**: Flatfile is not a data marketplace but rather a data onboarding tool. Included here as it sometimes appears in data commerce discussions but should not be classified as a marketplace.

### Google Cloud Analytics Hub
- **URL**: https://cloud.google.com/analytics-hub
- **Operator/Parent**: Google Cloud (Alphabet Inc. - publicly traded: GOOGL on Nasdaq)
- **Type**: Both - many free public datasets via Google BigQuery Public Datasets; Analytics Hub supports both free and commercial data exchanges
- **Pricing**: Analytics Hub itself has no additional licensing fee - standard BigQuery costs apply (storage and query costs). Google BigQuery Public Datasets: free to query up to 1 TB/month in the free tier, then standard BigQuery pricing. For commercial data e...
- **Data Types**: Public datasets (census, weather, transportation, etc.), Financial and market data, Healthcare and biomedical data, Geospatial and mapping data (Google Maps Platform data), Advertising and marketing analytics, Climate and environmental data, Genomics data (via Google Genomics), COVID-19 and public health data, Blockchain and cryptocurrency data, News and media data, Satellite imagery (Google Earth Engine), Public datasets (Google Public Datasets Program), Financial data, Geographic/geospatial data, Healthcare data, Weather/climate data, Government/census data, Advertising/marketing data, Google Trends data
- **Industry Focus**: Technology and digital advertising, Financial services, Healthcare and life sciences, Government and public policy, Academia and research, Retail and e-commerce, Media and publishing, Any Google Cloud customer, Data science/analytics, Healthcare, Public sector
- **Geographic Focus**: Global - available in all Google Cloud regions. BigQuery Public Datasets lean toward US-centric sources but include significant international data.
- **Formats**: BigQuery native tables and views (SQL-queryable), Linked datasets (live, zero-copy sharing within BigQuery), BigQuery supports ingestion of CSV, JSON, Avro, Parquet, ORC, Data accessed via standard SQL through BigQuery, Analytics Hub shared datasets, Pub/Sub for streaming data
- **Scale**: BigQuery Public Datasets: 200+ datasets. Analytics Hub: growing number of commercial and internal listings (exact count not widely published). Google Dataset Search indexes millions of datasets across the web (but is a search engine, not a marketplace).
- **Key Features**:
  - Analytics Hub: governed, secure data sharing within and across organizations
  - Zero-copy data sharing (linked datasets - no data duplication)
  - BigQuery Public Datasets: 200+ free public datasets ready to query
  - Data Clean Rooms for privacy-preserving analytics
  - Google Dataset Search: a search engine to find datasets across the internet
- **Provider Requirements**: For Analytics Hub: providers need a Google Cloud account with BigQuery. They create 'exchanges' (public or private) and publish 'listings' containing shared datasets. Providers configure access pol...
- **Status**: Active (GA since 2022)
- **Notes**: Google's approach to data sharing is centered on BigQuery and Analytics Hub. Unlike AWS Data Exchange, Analytics Hub focuses on zero-copy sharing within the BigQuery ecosystem. Google Dataset Search is a separate, complementary product - it's a search engine for discovering datasets across the we...

### Measured (formerly known in alternative data circles)
- **URL**: https://www.measured.com
- **Operator/Parent**: Measured, Inc. (independent) [Based on training data, may need verification]
- **Type**: Paid - Enterprise only
- **Pricing**: Enterprise subscription. Custom pricing based on use case and data products.
- **Data Types**: Marketing attribution data, Media measurement data, Incrementality testing data
- **Industry Focus**: Marketing/advertising measurement, E-commerce, DTC brands
- **Geographic Focus**: US primarily
- **Formats**: Platform/dashboard, API, Reports
- **Scale**: Niche platform serving hundreds of brands [Based on training data, may need verification]
- **Key Features**:
  - Incrementality measurement for marketing
  - Marketing mix modeling
  - Attribution across channels
- **Provider Requirements**: Not a two-sided data marketplace.
- **Status**: Active [Based on training data, may need verification]
- **Notes**: Included for completeness as a specialized data/measurement platform. More of a measurement/analytics platform than a data marketplace per se.

### New York City Open Data
- **URL**: https://opendata.cityofnewyork.us
- **Operator/Parent**: City of New York, Mayor's Office of Data Analytics (MODA), NYC Open Data Team
- **Type**: Free
- **Pricing**: Completely free. Powered by Socrata/Tyler Data & Insights platform. Mandated by Local Law 11 of 2012.
- **Data Types**: 311 Service Requests, Building & Property Data, Business & Economic Data, City Government Operations, Education, Environment & Sustainability, Health & Social Services, Housing & Development, Public Safety (NYPD, FDNY), Transportation (Taxi, Subway, Citibike), City Budget & Finance
- **Industry Focus**: Urban Planning, Real Estate & Property, Transportation & Mobility, Public Safety, Civic Tech, Journalism, Academic Research, Data Science Education
- **Geographic Focus**: New York City (five boroughs)
- **Formats**: CSV, JSON, XML, GeoJSON, Shapefile, KML, API (SODA API), Excel, RDF
- **Scale**: ~3,000+ datasets from 100+ city agencies
- **Key Features**:
  - SODA API for every dataset
  - One of the largest and most comprehensive city-level open data portals
  - Legally mandated (NYC Open Data Law)
  - Built-in visualization tools
  - Annual Open Data Report
- **Licensing**: Public domain / NYC Open Data Terms of Use. Free for any use.
- **Notes**: NYC Open Data is widely considered one of the best city-level open data portals in the world. Its taxi/rideshare trip data, 311 service requests, and NYPD data are among the most analyzed open datasets globally. Frequently used in data science courses and tutorials. The legal mandate ensures ongo...

### SafeGraph (now part of Dewey)
- **URL**: https://www.deweydata.io
- **Operator/Parent**: Dewey (SafeGraph was acquired/merged into Dewey). SafeGraph was originally independent, founded by Auren Hoffman.
- **Type**: Both - Dewey offers free academic access to some datasets; commercial licensing for business use
- **Pricing**: Subscription-based access through Dewey platform. Tiered pricing based on datasets and volume. Academic/research pricing available (previously SafeGraph offered free academic access). Commercial pricing varies by dataset and use case.
- **Data Types**: Points of interest (POI) data, Foot traffic/visit patterns data, Spend/transaction patterns, Geospatial/place data, Consumer mobility data, Business listings/firmographic data, Brand affinity data, Foot traffic/visit patterns, Store/location data, Geospatial data, Mobility data, Spend/transaction data (from partners)
- **Industry Focus**: Real estate (site selection), Financial services (alternative data), Retail/CPG, Government/public policy, Academic research, Urban planning, Advertising/marketing, Hedge funds/investment firms, Location intelligence, Retail analytics, Real estate, Alternative data for finance
- **Geographic Focus**: Primarily US, with some global POI coverage (SafeGraph had data for 220+ countries for POI)
- **Formats**: Dewey platform (cloud-based access), Snowflake Data Sharing, AWS Data Exchange, Bulk file downloads (CSV, Parquet), API access, Databricks integration, Cloud delivery (Snowflake, Databricks, AWS S3), CSV downloads, Dewey marketplace platform
- **Scale**: ~11 million POI in the US, global POI covering 220+ countries. Foot traffic data derived from tens of millions of mobile devices [Based on training data, may need verification]
- **Key Features**:
  - Industry-leading POI dataset with detailed place attributes
  - Foot traffic patterns with visit counts, dwell times, visitor home locations
  - Consumer spending patterns data
  - Strong academic community and research program
  - Widely used in COVID-19 mobility research
- **Provider Requirements**: Not a traditional two-sided marketplace. SafeGraph/Dewey aggregates data from mobile SDKs, partnerships, and proprietary collection. Dewey platform may host some third-party datasets as well.
- **Status**: Transitional. SafeGraph restructured into Dewey (data marketplace) and parts were acquired by other companies. The exact current state of the transition should be verified.
- **Notes**: SafeGraph was a prominent location data company founded by Auren Hoffman. It gained widespread visibility during COVID-19 for mobility data. The transition to Dewey represents a broader data platform play. SafeGraph's POI data was considered among the best in the industry. The free academic acces...

### U.S. Census Bureau Data
- **URL**: https://data.census.gov
- **Operator/Parent**: U.S. Census Bureau, U.S. Department of Commerce
- **Type**: Free
- **Pricing**: Completely free. API key required for API access (free, instant).
- **Data Types**: Decennial Census (population counts every 10 years), American Community Survey (ACS - demographics, socioeconomic), Economic Census & Surveys, Population Estimates & Projections, Housing Data, Income & Poverty, Employment & Labor, Education Attainment, Health Insurance Coverage, Race & Ethnicity, Migration & Commuting, Business Patterns (County/ZIP), International Trade, Government Finances, Geographic/Boundary Data (TIGER)
- **Industry Focus**: Government & Public Policy, Real Estate & Housing, Retail & Market Research, Healthcare, Education, Urban Planning & Demographics, Political Science & Redistricting, Marketing & Advertising, Academic Research, Logistics & Transportation
- **Geographic Focus**: United States (national, state, county, city, census tract, block group, ZIP code levels)
- **Formats**: CSV, JSON, API (RESTful Census API), Shapefile/TIGER Line, GeoJSON, KML, FTP bulk downloads, Microdata (PUMS)
- **Scale**: Hundreds of datasets covering the entire U.S. population. The Census API provides access to billions of data points across multiple surveys and geographies.
- **Key Features**:
  - data.census.gov - primary data access platform (replaced American FactFinder)
  - Census API with hundreds of endpoints
  - TIGER/Line geographic boundary files
  - American Community Survey (annual demographic estimates)
  - Public Use Microdata Samples (PUMS)
- **Licensing**: U.S. Public Domain. Title 13 protections ensure individual confidentiality, but aggregated data is freely available.
- **Notes**: The Census Bureau is the primary source for U.S. demographic and economic data. The 2020 Decennial Census data has been fully released. The American Community Survey (ACS) provides annual updates on demographics. Data is available at extremely granular geographic levels (down to census blocks). E...

---

## Analysis & Observations

### Key Trends

1. **Zero-copy data sharing** is replacing file-based exchange (Snowflake, Databricks Delta Sharing, Google Analytics Hub)
2. **Data Clean Rooms** emerging as privacy-preserving collaboration feature across cloud marketplaces
3. **Open protocols** (Delta Sharing) challenging proprietary lock-in
4. **ESG and sustainability data** becoming a major category across all marketplaces
5. **Alternative data** for finance remains the highest-value commercial niche
6. **Decentralized/blockchain** data marketplaces exist but have not achieved mainstream adoption
7. **AI/ML dataset platforms** (Hugging Face) growing rapidly as training data demand explodes
8. **Government open data** is massive in volume but inconsistent in quality and freshness — prime territory for value-add
9. **Consolidation** ongoing — many niche players being acquired (SafeGraph→Dewey, Quandl→Nasdaq, Factual→Foursquare, Thinknum→M Science)
10. **Data-as-a-Service** subscription models dominating over one-time purchases

### Gaps & Opportunities

1. **Quality gap in open data**: Government portals have massive datasets but poor documentation, inconsistent formats, and unreliable refresh — exactly the DAS value proposition
2. **Format gap**: Most sources offer 1-2 formats; few provide the full spectrum (Parquet, Delta, Iceberg, CSV, JSON) that modern data teams need
3. **Enrichment gap**: Raw public data rarely includes geocoding, cross-referencing, or derived fields
4. **ML-readiness gap**: Almost no public data source provides ML-ready forms (feature-engineered, normalized, split)
5. **Documentation gap**: Metadata is the weakest link across nearly all sources
6. **Freshness gap**: Many valuable datasets are updated quarterly or annually when monthly or weekly would be feasible
7. **Agent-readiness gap**: No major marketplace currently offers MCP or tool-use-friendly interfaces for AI agents

### Relevance to DAS Thesis

**As distribution channels** (where to sell):
- **Tier 1**: AWS Data Exchange (largest, AWS-aligned infrastructure), Snowflake Marketplace (zero-copy sharing, large buyer base), Databricks Marketplace (open protocol)
- **Tier 2**: Datarade (discovery/matchmaking), Azure Marketplace, Google Analytics Hub
- **Future**: MCP servers for agent consumption (no one doing this yet — first-mover opportunity)

**As data sources** (where to get raw material):
- **High-value government portals**: data.gov, Census Bureau, NOAA, EU Open Data, data.gov.uk — massive, messy, high transformation potential
- **International organizations**: World Bank, UN, OECD, WHO, IMF — authoritative but need format/enrichment work
- **Niche free sources**: HDX (humanitarian), GBIF (biodiversity), OpenStreetMap (geospatial), FRED (economic), NASA/Copernicus (satellite)
- **Aggregation opportunities**: Combining Census + NOAA + economic data into composite location-intelligence datasets
