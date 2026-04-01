from scipy import stats
import numpy as np

import numpy as np

def confidence_interval(control, treatment):
    control = np.array(control)
    treatment = np.array(treatment)

    diff = np.mean(treatment) - np.mean(control)
    
    se = np.sqrt(np.var(control)/len(control) + np.var(treatment)/len(treatment))
    
    ci_low = diff - 1.96 * se
    ci_high = diff + 1.96 * se

    print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
    interpret_ci(ci_low, ci_high)

def interpret_ci(ci_low, ci_high):
    if ci_low > 0:
        print("📈 Confident positive effect")
    elif ci_high < 0:
        print("📉 Confident negative effect")
    else:
        print("⚠️ Confidence interval crosses 0 → High uncertainty")

def sample_size_hint(control, treatment):
    n_control = len(control)
    n_treatment = len(treatment)

    print(f"Sample sizes → Control: {n_control}, Treatment: {n_treatment}")

    if n_control < 30 or n_treatment < 30:
        print("📉 Sample size too small → Results unreliable")
    else:
        print("📊 Sample size reasonable, uncertainty likely due to variance")

def analyze_experiment(control, treatment, alpha=0.05):
    control = np.array(control)
    treatment = np.array(treatment)
    
    
    t_stat, p_stat = stats.ttest_ind(control, treatment)

    mean_control = np.mean(control)
    mean_treatment = np.mean(treatment)
    diff = mean_treatment - mean_control
    return mean_control, mean_treatment, diff, p_stat

    

control = [1,2,3,4,5]
treatment = [2,3,4,5,6]

analyze_experiment(control, treatment)
confidence_interval(control, treatment)
sample_size_hint(control, treatment)