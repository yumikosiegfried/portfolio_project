# A Streamlit app for interactive A/B test simulation and analysis
# Import libraries
import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# ---- Define Helper Functions ----
# Simulate 2 arrays of n elements - one for control group and the other for treatment group
# Control group - binomial(1, p_control)
# Treatment group - binomial(1, p_treatment) where p_treatment is p_control * (1 + expected increase)
def simulate_ab_data(p_control, uplift, n):
    p_treatment = p_control * (1 + uplift/100)
    control = np.random.binomial(1, p_control, n)
    treatment = np.random.binomial(1, p_treatment, n)
    return control, treatment

# Define a function to conduct z-test between the two proportions
# The two proportions are:
# Number of successes in control group / Number of cases in control group = x1/n1 = p1
# Number of successes in treatment group / Number of cases in treatment group = x2/n2 = p2
# Returns z-score, standard error, p1, and p2
def z_test_proportions(x1, n1, x2, n2):
    p1 = x1 / n1
    p2 = x2 / n2
    p_pool = (x1 + x2) / (n1 + n2)
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))  # standard error of the difference
    z = (p2 - p1) / se
    return z, se, p1, p2

# Define a function to calculate minimum detectable effect (MDE) (do power analysis and solve for effect size)
# Need significance level (alpha), statistical power (1-beta), and sample size of each group
# Set default alpha = 0.05 and default 1-beta = 0.8
# Assumes equal sample size in both groups
def calculate_mde(p, n, alpha=0.05, power=0.8):
    z_alpha = norm.ppf(1 - alpha / 2) # z-score at the chosen significance level (2-sided)
    z_beta = norm.ppf(power) # z-score at desired power
    mde = (z_alpha + z_beta) * np.sqrt((2 * p * (1 - p)) / n)
    return mde

# ---- Streamlit UI ----
st.title("A/B Testing Simulation Dashboard")
st.markdown("Simulate randomized A/B test outcomes and assess statistical significance")

# Inputs
col1, col2 = st.columns(2)
with col1:
    p_control = st.slider("Baseline Conversion Rate (Control)", 0.01, 0.5, 0.1, 0.01)
    uplift = st.slider("Expected Uplift (Relative %)", 0, 100, 1, 1)
with col2:
    sample_size = st.slider("Sample Size per Group (e.g., 1000 control + 1000 treatment)", 100, 10000, 1000, 100)

# Choose one-sided vs two-sided test
test_type = st.radio(
    "Select Type of Hypothesis Test",
    ["Two-sided", "One-sided"],
    index=0
)

# Run test
run_test = st.button("Run A/B Test")

if run_test:
    control, treatment = simulate_ab_data(p_control, uplift, sample_size)
    x1, x2 = sum(control), sum(treatment)
    z, se, p1, p2 = z_test_proportions(x1, sample_size, x2, sample_size)

    # Adjust p-value based on test type
    if test_type == "Two-sided":
        p_val = 2 * (1 - norm.cdf(abs(z)))
    else:
        p_val = 1 - norm.cdf(z)

    mde = calculate_mde(p_control, sample_size)

    st.subheader("Results")
    st.metric("Control Conversion Rate", f"{p1:.3f}")
    st.metric("Treatment Conversion Rate", f"{p2:.3f}")
    st.metric("Relative Uplift", f"{((p2 - p1) / p1)*100:.3f}%")
    st.metric("Absolute Uplift", f"{(p2 - p1):.3f}")
    st.metric("Z-statistic", f"{z:.2f}")
    st.metric(r"p-value (Compare against $\alpha = 0.05$ for significance)", f"{p_val:.4f}")
    st.metric(r"MDE (Calculated with $\alpha = 0.05$ and $1 - \beta = 0.8$, two-sided)", f"{mde:.3f}")
    with st.expander("What is Minimum Detectable Effect (MDE)?"):
        st.markdown("""
        MDE represents the **smallest absolute uplift** (difference between control and treatment conversion rates) 
        that this test is likely to detect as statistically significant, 
        given the chosen sample size, baseline conversion rate, alpha, and power.

        - MDE is based on **theoretical assumptions**, not observed outcomes.
        - If the true uplift is smaller than the MDE, the test may not detect it — even if it's real.
        """)

    st.caption(f"Hypothesis Test Type: **{test_type}**")

    # Plot bar chart of conversion rates p1 and p2
    st.subheader("Conversion Rate Comparison")
    fig, ax = plt.subplots()
    bars = ax.bar(["Control", "Treatment"], [p1, p2], color=["skyblue", "salmon"])
    ax.set_ylabel("Conversion Rate")
    ax.set_ylim(0, max(p1, p2) + 0.05)
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.005, f"{yval:.3f}", ha='center', va='bottom')
    st.pyplot(fig)
