# General checkup target (G1E_OBJ)

`G1E_OBJ` (일반건강검진 대상자) is a table in the [Cancer Public Library](index.md). One row is one person in one examination year, from 2007 through 2024. It has two variables besides `SN_KEY`: the examination year (`EXMD_BZ_YYYY`) and the work type (`WKG_TYPE_CD`, 근무구분코드), which decides whether an employee is examined every year.

The questionnaire answers are on [`G1Q_0708`](g1q-0708.md), [`G1Q_0917`](g1q-0917.md), and [`G1Q_1824`](g1q-1824.md), and the measured results are on [`G1E`](g1e.md). All of them join on `SN_KEY` and `EXMD_BZ_YYYY`.

The people are those on [`RGST`](rgst.md) with a general health examination record from 2007 through 2024. Using any checkup table requires a research-use plan.

!!! note "Eligible years or examined years"
    The dictionary defines the people in every checkup table as registered patients with an examination record. It does not say whether `G1E_OBJ` also lists the years in which a person was eligible and skipped the examination. In the NHIS customized database, a table of the same name lists the eligible population. Within an extract, comparing the years on `G1E_OBJ` with the years on `G1E` for the same person settles the question. The National Cancer Data Center (data@ncc.re.kr) can also confirm it.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/g1e_obj.md).

## Who is examined

| Insurance type | Who is examined | How often |
|---|---|---|
| Self-employed insured, household head | Everyone | Every 2 years |
| Self-employed insured, household member | Aged 20 or older | Every 2 years |
| Employee insured | Everyone | Every 2 years, or every year for a non-office worker |
| Employee dependent | Aged 20 or older | Every 2 years |
| Medical Aid, household head | Aged 19–64 | Every 2 years, from 2012 |
| Medical Aid, household member | Aged 40–64 | Every 2 years, from 2012 |

??? info "Source"
    The description follows the health-examination overview in data dictionary version 4.0 (September 2026).
