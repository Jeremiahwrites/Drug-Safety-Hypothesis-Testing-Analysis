# 💊 Drug Safety Hypothesis Testing Analysis

## 📌 Project Overview

This project analyzes clinical trial data from **GlobalXYZ pharmaceutical company** to evaluate the safety profile of a new drug. The dataset contains demographic information, blood markers, and recorded adverse effects from both **Drug** and **Placebo** groups.

The goal is to determine whether:

* The drug increases adverse effects
* The number of adverse effects differs by treatment group
* There are demographic differences (age) between groups

---

## 📊 Dataset Description

| Column            | Description                                           |
| ----------------- | ----------------------------------------------------- |
| `sex`             | Gender of participant                                 |
| `age`             | Age of participant                                    |
| `week`            | Week of trial observation                             |
| `trx`             | Treatment group (Drug / Placebo)                      |
| `wbc`             | White blood cell count                                |
| `rbc`             | Red blood cell count                                  |
| `adverse_effects` | Whether at least one adverse effect occurred (Yes/No) |
| `num_effects`     | Number of adverse effects per participant             |

---

## 🧪 Hypothesis Tests Performed

### 1️⃣ Proportion of Adverse Effects (Z-test)

**Question:**
Is there a difference in the proportion of adverse effects between Drug and Placebo groups?

* **Test Used:** Two-sample proportion z-test
* **p-value:** `0.9639`

### 📌 Insight:

There is **no statistically significant difference** in adverse effect proportions between the Drug and Placebo groups.

👉 Interpretation:

> The drug does not increase the likelihood of experiencing at least one adverse effect.

---

### 2️⃣ Number of Adverse Effects (Chi-square Test)

**Question:**
Is the number of adverse effects independent of treatment group?

* **Test Used:** Chi-square test of independence
* **p-value:** `0.6150`

### 📌 Insight:

There is **no significant association** between treatment type and the number of adverse effects experienced.

👉 Interpretation:

> The severity (count) of adverse effects is not influenced by whether a participant received the drug or placebo.

---

### 3️⃣ Age Distribution Difference (Mann–Whitney U Test)

**Question:**
Is there a difference in age distribution between Drug and Placebo groups?

* **Test Used:** Mann–Whitney U test (two-sided)
* **p-value:** `0.2570`

### 📌 Insight:

No statistically significant difference in age distribution between the two groups.

👉 Interpretation:

> Randomization was successful — both groups are comparable in age.

---

## 📈 Summary of Findings

| Analysis                  | Test           | p-value | Conclusion     |
| ------------------------- | -------------- | ------- | -------------- |
| Adverse effect proportion | Z-test         | 0.9639  | No difference  |
| Number of adverse effects | Chi-square     | 0.6150  | No association |
| Age distribution          | Mann–Whitney U | 0.2570  | No difference  |

---

## 🧠 Key Insights

### ✅ 1. Drug Safety Profile is Stable

No evidence suggests the drug increases:

* likelihood of adverse effects
* number of adverse reactions

---

### ✅ 2. Balanced Trial Groups

Age distribution is statistically similar across groups, confirming:

* Proper randomization
* Reduced demographic bias

---

### ✅ 3. Strong Evidence of Independence

Both:

* adverse occurrence
* adverse severity

are independent of treatment assignment.

---

## 🧪 Final Conclusion

> Based on statistical testing, the drug does **not show a significant increase in adverse effects compared to placebo**, and the trial groups are demographically well-balanced.

This supports a **favorable safety profile** for further evaluation.

---

## 🛠️ Tools Used

* Python 🐍
* Pandas
* SciPy (`proportions_ztest`, `chi2_contingency`)
* Pingouin (`mwu`)

---

## 📌 Author Note

This analysis focuses strictly on statistical inference to ensure reproducibility, transparency, and unbiased evaluation of drug safety outcomes.

---

