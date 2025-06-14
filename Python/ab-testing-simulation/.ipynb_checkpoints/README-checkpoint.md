# A/B Testing: Simulated Marketing Campaign

This project simulates an A/B test measuring the impact of a digital marketing campaign on user conversion.

## Project Overview

- Simulated 10,000 users randomly assigned to treatment/control
- Conversion rate in treatment group increased by 2 percentage points
- Conducted z-test for difference in proportions
- Built a lightweight Streamlit dashboard to explore results

## Methods

- Randomized controlled design
- Z-test for difference in proportions
- Confidence intervals and conversion visualization

## Tools

- Python, Pandas, NumPy, Statsmodels, Streamlit

## Results

- Conversion rate (control): ~10%
- Conversion rate (treatment): ~12%
- p-value < 0.05, suggesting statistically significant lift

## Future Improvements

- Add logistic regression with covariates
- Explore subgroup effects (e.g., by channel)
- Translate to R using tidyverse and `infer`
