# Checkup results (G1E)

`G1E` (일반건강검진 결과 및 판정) is a table in the [Cancer Public Library](index.md). One row is the measured results of one general health examination, from 2007 through 2024. The questionnaire for the same examination is on [`G1Q_0708`](g1q-0708.md), [`G1Q_0917`](g1q-0917.md), or [`G1Q_1824`](g1q-1824.md), depending on the year, and joins on `SN_KEY` and `EXMD_BZ_YYYY`.

The people are those on [`RGST`](rgst.md) with a general health examination record from 2007 through 2024. Using any checkup table requires a research-use plan.

## What is measured

- Body: height, weight, waist, body mass index, and blood pressure.
- Urine: glucose, protein, and occult blood.
- Blood: hemoglobin, fasting glucose, total, HDL, and LDL cholesterol, triglycerides, creatinine, eGFR, AST, ALT, and GGT.

Body measures are top- and bottom-coded:

| Variable | Released as |
|---|---|
| Height (`G1E_HGHT`) | 150 or less, then each centimeter from 151 to 179, then 180 or more |
| Weight (`G1E_WGHT`) | 40 or less, then each kilogram from 41 to 99, then 100 or more |
| Body mass index (`G1E_BMI`) | 18.5 or less, then one decimal from 18.6 to 29.9, then 30 or more |
| Waist (`G1E_WSTC`) | 60 or less, then each centimeter from 61 to 89, then 90 or more |

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/g1e.md).

## Who is examined

The general health examination follows the schedule below, so most people have a record every other year at most.

| Insurance type | Who is examined | How often |
|---|---|---|
| Self-employed insured, household head | Everyone | Every 2 years |
| Self-employed insured, household member | Aged 20 or older | Every 2 years |
| Employee insured | Everyone | Every 2 years, or every year for a non-office worker |
| Employee dependent | Aged 20 or older | Every 2 years |
| Medical Aid, household head | Aged 19–64 | Every 2 years, from 2012 |
| Medical Aid, household member | Aged 40–64 | Every 2 years, from 2012 |

??? info "Source"
    The description follows the health-examination overview and its pseudonymization table in data dictionary version 4.0 (September 2026).
