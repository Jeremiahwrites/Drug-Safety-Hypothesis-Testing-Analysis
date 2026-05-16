# Import packages
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import chi2_contingency
import pingouin as pg

#proportion of adverse effects
# Load the dataset
drug_safety = pd.read_csv(r"c:\Users\USER1\Downloads\drug_safety.csv")

#create contigency summary
summary = drug_safety.groupby('trx')['adverse_effects'].agg(total='count', adverse=lambda x: (x == "Yes").sum())

# Counts of adverse effects
counts = summary["adverse"].values

# Total number of observations in each group
nobs = summary["total"].values

# Perform two-sample proportion z-test
stat, two_sample_p_value = proportions_ztest(count=counts, nobs=nobs)

# Display the p-value
print('two_sample_p_value:',two_sample_p_value)

#number of effects
# Create contingency table
contingency_table = pd.crosstab(
    drug_safety["trx"],
    drug_safety["num_effects"]
)

# Perform Chi-square test of independence
chi2, num_effects_p_value, dof, expected = chi2_contingency(contingency_table)

# Display p-value
print('num_effects_p_value:',num_effects_p_value)

#Significant difference
# Split age by treatment groups
drug_age = drug_safety[drug_safety["trx"] == "Drug"]["age"]
placebo_age = drug_safety[drug_safety["trx"] == "Placebo"]["age"]

# Mann–Whitney U test (Pingouin)
test_result = pg.mwu(
    x=drug_age,
    y=placebo_age,
    alternative="two-sided"
)

# Extract p-value
age_group_effects_p_value = test_result["p-val"].values[0]

print('age_group_effects_p_value:',age_group_effects_p_value)