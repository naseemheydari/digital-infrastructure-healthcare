# Digital Infrastructure & Preventive Healthcare Engagement

## Overview

This project explores the relationship between state-level digital infrastructure and preventive healthcare engagement across the United States.

Using data from the CDC Behavioral Risk Factor Surveillance System (BRFSS) and the National Telecommunications and Information Administration (NTIA) Internet Use Survey, the analysis examines whether states with greater digital access and technology use also demonstrate different patterns of preventive healthcare engagement.

The study focuses on 2019, 2021, and 2023 and evaluates relationships between measures of digital connectivity—including home internet use, broadband access, device use, email use, and video calling—and healthcare measures such as routine checkups, access to a personal healthcare provider, flu vaccination, exercise, and cholesterol screening.

Because the analysis is observational and conducted at the state level, the results identify associations rather than causal effects.

---

## Research Question

**Do states with better digital infrastructure show higher rates of preventive healthcare utilization and healthcare engagement?**

The project also explores geographic patterns, changes over time, and potential differences in how individual dimensions of digital access relate to healthcare behaviors.

---

## Data Sources

### CDC Behavioral Risk Factor Surveillance System (BRFSS)

BRFSS provides state-level survey data on health behaviors, preventive care, and healthcare access.

The analysis used data from:

- **2019:** 418,268 records × 342 variables
- **2021:** 438,693 records × 303 variables
- **2023:** 433,323 records × 350 variables

Healthcare measures examined included:

- Routine checkup in the past year
- Access to a personal healthcare provider
- Flu vaccination
- Physical activity
- Cholesterol screening

Official data source: [CDC BRFSS Annual Survey Data](https://www.cdc.gov/brfss/annual_data/annual_data.htm)

### NTIA Internet Use Survey

The NTIA Internet Use Survey provides information about internet access, device use, household connectivity, and online activities across U.S. states.

The source dataset contained **835 records × 348 variables**, with observations spanning 1994–2023. The analysis selected measures corresponding to 2019, 2021, and 2023 to align with the BRFSS data.

Digital infrastructure measures included:

- Home internet use
- Email use
- Video/voice calling capability
- PC or tablet use
- Mobile phone use
- Wired broadband access

Official data source: [NTIA Internet Use Survey Datasets](https://www.ntia.gov/page/download-ntia-internet-use-survey-datasets)

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

BRFSS identifies states using numeric FIPS codes, while NTIA uses state abbreviations.

A state mapping was used to reconcile the identifiers, and the datasets were joined on:

- State
- Year

The resulting analytical dataset contained **146 state-year observations and 15 variables**, including healthcare and digital infrastructure measures.

---

## Analysis

The project used exploratory and statistical analysis to investigate relationships between digital infrastructure and healthcare engagement.

Methods included:

- Summary statistics
- Distribution analysis
- Outlier detection
- Scatter plots
- Pearson correlation analysis
- Linear regression
- High-vs.-low digital infrastructure comparisons
- Geographic analysis
- Temporal analysis across 2019, 2021, and 2023

---

## Key Findings

The analysis found that the relationship between digital infrastructure and healthcare engagement was not uniform across healthcare measures.

Some of the strongest observed correlations included:

- **Email use ↔ Exercise:** r = 0.740
- **PC/Tablet use ↔ Exercise:** r = 0.639
- **Broadband access ↔ Exercise:** r = 0.580
- **Video calling ↔ Personal doctor access:** r = -0.747

Overall, digital infrastructure showed stronger positive relationships with some health behaviors, particularly exercise, while some measures showed negative relationships with traditional healthcare access.

The geographic analysis also revealed regional variation in both digital infrastructure and healthcare engagement.

These findings should be interpreted as **associations rather than causal relationships**.

---

## Visualizations

### Digital Infrastructure vs. Healthcare Engagement

Scatter plots were used to examine direct relationships between digital infrastructure measures and healthcare outcomes. Overall, many relationships showed substantial variation across states, demonstrating that digital access alone does not fully explain healthcare engagement.

<!-- Visualization will be added here -->

### Correlation & Regression Analysis

Correlation and regression analyses were used to quantify relationships between selected digital infrastructure and healthcare measures.

<!-- Visualization will be added here -->

### Geographic Patterns

Choropleth maps were developed to compare state-level digital infrastructure and preventive healthcare engagement across the United States.

<!-- Visualization will be added here -->

---

## Limitations

Several limitations are important when interpreting the results:

- The analysis is observational and cannot establish causation.
- State-level aggregation can hide substantial within-state variation.
- Demographic and socioeconomic variables were not included as controls in the final state-level models.
- The 2019–2023 study period overlaps with the COVID-19 pandemic, which significantly disrupted healthcare utilization.
- Simple linear regression may not capture nonlinear relationships or interactions between variables.

Future work could incorporate individual-level microdata, demographic controls, county-level or urban/rural analysis, longer longitudinal periods, and direct measures of telehealth adoption.

---

## Technologies & Methods

**Programming:** Python, pandas, NumPy

**Analysis:** Statistical Analysis, Pearson Correlation, Linear Regression, Hypothesis Testing, Survey Data Processing

**Data:** Data Cleaning, Data Transformation, Data Integration, Survey-Weighted Aggregation

**Visualization:** Choropleth Maps, Heatmaps, Scatter Plots, Geographic Visualization

---

## My Contribution

This project was completed collaboratively as part of **SIADS 593: Milestone I** in the University of Michigan Master of Applied Data Science program.

My primary contribution was developing the project's data visualizations, including **choropleth maps, heatmaps, and scatter plots**. I focused on transforming the analytical results into clear visual representations of geographic patterns and relationships between digital infrastructure and preventive healthcare engagement.

I also contributed to the development and communication of the final project report.

---

## Project Context

- **Program:** Master of Applied Data Science
- **Institution:** University of Michigan
- **Course:** SIADS 593 – Milestone I
- **Project Type:** Collaborative Data Science Project
