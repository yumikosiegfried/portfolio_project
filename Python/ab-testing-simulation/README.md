# A/B Testing: Simulated Marketing Campaign

This project simulates an A/B test measuring the impact of a digital marketing campaign on user conversion.

## Project Overview

- Simulated 10,000 users randomly assigned to treatment/control
- Conversion rate in treatment group increased by 2 percentage points
- Conducted z-test for difference in proportions
- Built a lightweight Streamlit dashboard to explore results

## Folder Structure
ab-testing-simulation/
│
├── app/ # Streamlit app for interactive dashboard
│ └── streamline_app.py # Main dashboard script
│ └── requirements.txt  # Dependencies
├── notebooks/ # Jupyter notebooks for simulation and analysis
│ └── ab_test_simulation.ipynb
│
├── data/ # Data files used or generated
│
├── README.md # Project overview and instructions

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
1. Clone the Repository
git clone https://github.com/your-username/ab-testing-simulation.git
cd ab-testing-simulation/app
2. Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
3. Install Required Packages
See the requirements.txt file under app folder for the versions used to construct this dashboard
4. Run the Dashboard
In the same folder where streamlit_app.py is located, run:
streamlit run streamlit_app.py
Your dashboard should open in your default browser.

## Contact
If you would like to collaborate or provide feedback, please contact me on www.linkedin.com/in/yumiko-siegfried-95b61a232
