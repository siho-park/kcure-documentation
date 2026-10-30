# Datasets

The Cancer Public Library (암 공공 라이브러리) starts from the national cancer registry and attaches death, eligibility, claims, checkups, screening, and COVID-19 records to the same people. It is released as three separate databases: a customized extract, a site sample, and a staging sample.

!!! abstract "At a glance"
    - **[Three databases](#three-databases).** A customized extract covers every registered cancer from 2012 to 2022. A site sample covers about 20 percent of one cancer site, and a staging sample covers about 10 percent of one site, with detailed stage.
    - **[Tables](#tables-in-the-customized-extract).** The customized extract has 26 tables, all joined on the person identifier `SN_KEY`.
    - **[One row per cancer](#tables-in-the-customized-extract).** A row of `RGST` is one registered cancer, so a person with two cancers has two rows.
    - **[Other products](#other-products).** The clinical library, specialized data, and health data are separate databases with their own documentation.

??? info "Sources"
    The table list follows data dictionary version 4.0 (September 2026). The samples follow the portal's data catalogs, downloaded 30 October 2026, and the [K-CURE library overview](https://k-cure.mohw.go.kr/portal/dit/lit/inf/viewDitLitInf.do). Where official figures differ, they are lined up on [Sources and versions](sources.md).

## Three databases

| | Customized extract | Site sample | Staging sample |
|---|---|---|---|
| 한글 | 맞춤형 | 표본 | 표본 병기 |
| Who is included | Every registered cancer, 2012–2022, all sites. About 2.92 million registrations | About 20 percent of one site, diagnosed 2012–2021 | About 10 percent of one site, diagnosed 2012–2021. Lung starts in 2014 |
| Sites | Every site the registry recorded | Stomach, breast, colorectal, liver, lung, pancreas | Stomach, breast, colorectal, liver, lung |
| Stage | SEER summary stage | SEER summary stage | Tumor size, nodes, metastasis, grade, and TNM, depending on the site |
| Variables | Requested by the study | A fixed, shorter list | A fixed list, with a staging-survey registration table |
| Where it is analyzed | In person, at a safe-use center | Remote virtual desktop | Remote virtual desktop |
| Documentation | [Cancer Public Library](public-library/index.md) | [Sample page](public-library/sample.md#site-sample) | [Sample page](public-library/sample.md#staging-sample) |

A study of thyroid, cervical, hematologic, or any other unlisted cancer, or of several sites together, needs a customized extract. Access and timing are on [Using the data](../overview/using.md).

## Tables in the customized extract

Each table has its own page, and its variables are listed under [Variables](../variables/index.md). The years of each table are on the [library page](public-library/index.md#tables).

| Table | Code | One row is |
|---|---|---|
| [Cancer registration](public-library/rgst.md) | `RGST` | One registered cancer, including SEER summary stage |
| [Death](public-library/death.md) | `DEATH` | One death |
| [Eligibility and premium](public-library/bfc.md) | `BFC` | One person in one year |
| [Claim statement](public-library/t200.md) | `T200` | One claim |
| [Services](public-library/t300.md) | `T300` | One service line on a claim |
| [Diagnoses](public-library/t400.md) | `T400` | One diagnosis on a claim |
| [Outpatient prescriptions](public-library/t530.md) | `T530` | One outpatient prescription line |
| [Checkup target](public-library/g1e-obj.md) | `G1E_OBJ` | One person in one examination year |
| [Checkup questionnaire](public-library/g1q-0708.md) | `G1Q_0708`, `G1Q_0917`, `G1Q_1824` | One questionnaire, in three files because the form changed |
| [Checkup results](public-library/g1e.md) | `G1E` | One examination result |
| [Cancer screening questionnaire](public-library/cq-rst-0708.md) | `CQ_RST_0708`, `CQ_RST_0924` | One screening questionnaire, common items |
| [Breast screening](public-library/cbr-rst-0708.md) | `CBR_RST_0708`, `CBR_RST_0924` | One breast screening |
| [Colorectal screening](public-library/ccr-rst-0708.md) | `CCR_RST_0708`, `CCR_RST_0924` | One colorectal screening |
| [Cervical screening](public-library/ccx-rst-0708.md) | `CCX_RST_0708`, `CCX_RST_0924` | One cervical screening |
| [Liver screening](public-library/clv-rst-0708.md) | `CLV_RST_0708`, `CLV_RST_0924` | One liver screening |
| [Stomach screening](public-library/cst-rst-0708.md) | `CST_RST_0708`, `CST_RST_0924` | One stomach screening |
| [COVID-19 cases](public-library/covid-pt.md) | `COVID_PT` | One confirmed case |
| [COVID-19 vaccination](public-library/covid-vac.md) | `COVID_VAC` | One vaccination |

Every table carries `SN_KEY` (대체식별키), the person identifier. The four claims tables also join to each other on `MID` (명세서조인키), the claim number. A row of `RGST` is one registered cancer, so a person with two cancers has two rows with the same `SN_KEY`.

## Published counts

The portal's visualization menu also publishes counts computed from the library. They are charts, so they have no variable list.

| Chart | 한글 | What is counted | Years |
|---|---|---|---|
| [New cancer cases](https://k-cure.mohw.go.kr/portal/dvz/pbl/ocr/viewDvzPblOcr.do) | 암 발생자 수 | People newly diagnosed, by site, year, age, province, and summary stage | 2012–2022 |
| [Deaths](https://k-cure.mohw.go.kr/portal/dvz/pbl/dth/viewDvzPblDth.do) | 암 환자 사망자 수 | Those people found in the death records, by site, year of death, and age | 2012–2023 |
| [Survivors](https://k-cure.mohw.go.kr/portal/dvz/pbl/svl/viewDvzPblSvl.do) | 암 환자 생존자 수 | Those people with no death record, by site, year, age, province, and survival time | 2012–2023 |

## Other products

These are separate databases, described briefly on their own pages.

- The [clinical library](clinical/index.md) (임상 라이브러리) holds standardized charts from participating hospitals. Its registration table, [`cncr_rgst`](clinical/cncr-rgst.md), is each hospital's own record.
- The [combined library](combined.md) (K-CURE 라이브러리) links the clinical library to the Cancer Public Library for people in both.
- [Specialized data](specialized.md) (특화 데이터) are 67 hospital-built datasets, often images or a single hospital's cohort.
- [Health and medical data](health.md) (보건의료 데이터) are open files from the Ministry and a person-level link of nine institutions.

Eligibility, premiums, and claims also appear in the [NHIS research databases](https://siho-park.github.io/nhis-documentation/), for a population sample. Their names and codes can differ, so read codes from the K-CURE dictionary for the extract in hand.
