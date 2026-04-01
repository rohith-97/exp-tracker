import streamlit as st
import numpy as np
from expi import analyze_experiment, confidence_interval

st.title("📊 Experiment Decision Engine")

control_input = st.text_input("Control group", "1,2,3,4,5")
treatment_input = st.text_input("Treatment group", "2,3,4,5,6")

if st.button("Analyze"):

    control = np.array([float(x) for x in control_input.split(",")])
    treatment = np.array([float(x) for x in treatment_input.split(",")])

    mean_c, mean_t, diff, p_value = analyze_experiment(control, treatment)
    ci_low, ci_high = confidence_interval(control, treatment)

    st.write(f"Control Mean: {mean_c:.2f}")
    st.write(f"Treatment Mean: {mean_t:.2f}")
    st.write(f"Difference: {diff:.2f}")
    st.write(f"P-value: {p_value:.4f}")

    if p_value < 0.05:
        st.success("Statistically significant → Ship")
    else:
        if diff > 0:
            st.warning("Positive trend but not significant → Collect more data")
        else:
            st.error("No improvement → Do not ship")

    st.write(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")

    if ci_low > 0:
        st.success("Confident positive effect")
    elif ci_high < 0:
        st.error("Confident negative effect")
    else:
        st.warning("CI crosses 0 → High uncertainty")

    if len(control) < 30 or len(treatment) < 30:
        st.warning("Sample size too small → Results unreliable")