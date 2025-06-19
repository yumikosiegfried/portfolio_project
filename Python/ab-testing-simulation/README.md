# A/B Testing: Simulated Marketing Campaign

This project simulates an A/B test measuring the impact of a digital marketing campaign on user conversion.

## Project Overview

- Simulated 10,000 users randomly assigned to treatment/control
- Conversion rate in treatment group increased by 2 percentage points
- Conducted z-test for difference in proportions
- Built a lightweight Streamlit dashboard to explore results

## Folder Structure
```
ab-testing-simulation/
├── app/ # Streamlit app for interactive dashboard
│   ├── streamlit_app.py # Main dashboard script
│   └── requirements.txt # Dependencies
├── notebooks/ # Jupyter notebooks for simulation and analysis
│   └── ab_test_simulation.ipynb
├── data/ # Data files used or generated
└── README.md # Project overview and instructions
```

All code and files are self-contained and reproducible. See the notebook for simulation logic and the `app/` folder for the deployable Streamlit app.

Note: Simulated data are saved in the data folder. To reproduce the result, you can read in the .csv data in data folder instead of rerunning the simulation.

## Methods

- Randomized controlled design
- Z-test for difference in proportions
- Confidence intervals and conversion visualization

## Tools

- Python, Pandas, NumPy, Statsmodels, Streamlit

## Results

- Conversion rate (control): 9.7%
- Conversion rate (treatment): 12.0%
- p-value 0.0002, suggesting statistically significant lift given p = 0.05 threshold

## Future Improvements

- Add logistic regression with covariates
- Explore subgroup effects (e.g., by channel)
- Translate to R using tidyverse and `infer`

## Streamlit Dashboard
The dashboard calculates statistics for a simulated A/B test under different combinations of baseline conversion rates, expected uplift, and sample size per group. The dashboard assumes the sample sizes are equal for the control and treatment groups.
To deploy this dashboard on your own machine, follow the steps below:
1. Clone the repository (https://github.com/yumikosiegfried/portfolio_project)
2. In the terminal, set cd to the cloned repository
3. Create a virtual environment (Optional)
4. Install required libraries: See the requirements.txt file under app folder for Python library versions used for this dashboard. You can install the requirements by entering "pip install -r requirements.txt" in the terminal, or install them manually
5. In the terminal, run the Dashboard by entering "streamlit run Python/ab-testing-simulation/app/streamlit_app.py"
Your dashboard should open in your default browser.

## Contact
If you would like to collaborate or provide feedback, please contact me on www.linkedin.com/in/yumiko-siegfried-95b61a232
