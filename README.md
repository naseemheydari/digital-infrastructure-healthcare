# Digital Infrastructure & Preventive Healthcare Engagement

## Overview

This project explores the relationship between state-level digital infrastructure and preventive healthcare engagement across the United States.

Using data from the CDC Behavioral Risk Factor Surveillance System (BRFSS) and the National Telecommunications and Information Administration (NTIA) Internet Use Survey, the analysis examines whether states with greater digital access and technology use also demonstrate different patterns of preventive healthcare engagement.

The study focuses on **2019, 2021, and 2023** and evaluates relationships between measures of digital connectivity—including home internet use, broadband access, device use, email use, and video calling—and healthcare measures such as routine checkups, access to a personal healthcare provider, flu vaccination, exercise, and cholesterol screening.

Because the analysis is observational and conducted at the state level, the results identify **associations rather than causal effects**.

---

## Full Project Report

For the complete methodology, analysis, visualizations, results, limitations, and discussion:

**[View Full Project Report (PDF)](./Project_Report.pdf)**

---

## Research Question

**Do states with better digital infrastructure show higher rates of preventive healthcare utilization and healthcare engagement?**

The project also explores geographic patterns, changes over time, and differences in how individual dimensions of digital access relate to healthcare behaviors.

---

## Data Sources

### CDC Behavioral Risk Factor Surveillance System (BRFSS)

BRFSS provides state-level survey data on health behaviors, preventive care, and healthcare access.

The analysis used:

- **2019:** 418,268 records × 342 variables
- **2021:** 438,693 records × 303 variables
- **2023:** 433,323 records × 350 variables

Healthcare measures examined included:

- Routine checkup in the past year
- Access to a personal healthcare provider
- Flu vaccination
- Physical activity
- Cholesterol screening

Official source: [CDC BRFSS Annual Survey Data](https://www.cdc.gov/brfss/annual_data/annual_data.htm)

### NTIA Internet Use Survey

The NTIA Internet Use Survey provides information about internet access, device use, household connectivity, and online activities across U.S. states.

The source dataset contained **835 records × 348 variables**, with observations spanning 1994–2023. The analysis selected measures corresponding to 2019, 2021, and 2023 to align with the BRFSS data.

Digital infrastructure measures included:

- Home internet use
- Email use
- Video/voice calling
- PC or tablet use
- Mobile phone use
- Wired broadband access

Official source: [NTIA Internet Use Survey Datasets](https://www.ntia.gov/page/download-ntia-internet-use-survey-datasets)

---

## Data Preparation & Integration

The analysis required harmonizing multiple years of large survey datasets before state-level comparisons could be performed.

### BRFSS Processing

BRFSS variable names and definitions can change across survey years. Variables were standardized across 2019, 2021, and 2023 using mapping dictionaries and codebook verification.

Missing-value codes such as "Don't know" and "Refused" were converted to missing values, and BRFSS survey weights were used to calculate weighted state-level percentages.

The three years of BRFSS data were then combined into a state-year dataset.

### NTIA Processing

Selected digital infrastructure variables were filtered to the corresponding 2019, 2021, and 2023 survey periods.

The NTIA dataset required reshaping because state observations were originally distributed across columns. The data were transformed into state-variable-year observations and then pivoted into a state-level analytical dataset.

### Dataset Integration

BRFSS identifies states using numeric FIPS codes, while NTIA uses state abbreviations. A state mapping was used to reconcile the identifiers, and the datasets were joined by state and year.

The resulting analytical dataset contained **146 state-year observations and 15 variables**, including healthcare and digital infrastructure measures.

---

## Analysis

The project used exploratory and statistical analysis to investigate relationships between digital infrastructure and healthcare engagement.

Methods included:

- Summary statistics and distribution analysis
- Outlier detection
- Scatter plots
- Pearson correlation analysis
- Linear regression
- High-vs.-low digital infrastructure comparisons
- Geographic analysis using choropleth maps
- Temporal analysis across 2019, 2021, and 2023

---

## Key Findings

The relationship between digital infrastructure and healthcare engagement was **not uniform across healthcare measures**.

Some of the strongest observed correlations included:

- **Email use ↔ Exercise:** r = 0.740
- **PC/Tablet use ↔ Exercise:** r = 0.639
- **Broadband access ↔ Exercise:** r = 0.580
- **Video calling ↔ Personal doctor access:** r = -0.747

Digital infrastructure showed positive associations with some health behaviors, particularly exercise, while some digital measures were negatively associated with personal healthcare provider access.

Geographic analysis also revealed regional variation in both digital infrastructure and healthcare engagement.

These findings represent **state-level associations and should not be interpreted as evidence of causation**.

---

## Visualizations

The project used multiple visualization techniques to communicate geographic patterns and statistical relationships, including:

- Choropleth maps
- Correlation heatmaps
- Scatter plots
- Regression plots
- Distribution plots
- Temporal trend visualizations

The complete visual analysis is available in the **[Full Project Report](./Project_Report.pdf)** and the analysis notebooks below.

---

## Project Notebooks

The analysis workflow is organized into three Jupyter notebooks:

1. **[Data Cleaning & Integration](./notebooks/01_data_cleaning.ipynb)**  
   Loads and harmonizes BRFSS and NTIA data, handles missing values and survey weights, performs state-level aggregation, and integrates the datasets.

2. **[Exploratory Data Analysis](./notebooks/02_exploratory_analysis.ipynb)**  
   Examines distributions, outliers, geographic patterns, scatter plots, and temporal trends across the study period.

3. **[Correlation & Regression Analysis](./notebooks/03_correlation_regression_analysis.ipynb)**  
   Performs Pearson correlation analysis, group comparisons, linear regression, correlation heatmaps, and geographic visualization.

---

## Processed Data

The repository includes the state-level datasets produced during the data preparation pipeline:

- **[BRFSS State-Level Dataset](./data/processed/brfss_state_level.csv)**
- **[Merged BRFSS + NTIA Dataset](./data/processed/merged_brfss_ntia.csv)**

Large raw BRFSS datasets are not stored in this repository. They can be obtained from the official CDC source linked above.

---

## Repository Structure

```text
digital-infrastructure-healthcare/
│
├── data/
│   └── processed/
│       ├── brfss_state_level.csv
│       └── merged_brfss_ntia.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_correlation_regression_analysis.ipynb
│
├── src/
│   ├── cleaning_utils.py
│   ├── config.py
│   └── data_utils.py
│
├── Project_Report.pdf
├── requirements.txt
└── README.md
