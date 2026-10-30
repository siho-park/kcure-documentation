# Clinical library (임상 라이브러리)

The clinical library is a separate database from the Cancer Public Library. It is standardized electronic medical record data from hospitals that participate in K-CURE. It holds the clinical detail the public library does not: pathology, laboratory results, imaging, drugs as ordered in the hospital, and follow-up recorded in the chart. It covers the patients of those hospitals, not every registered cancer patient in Korea.

??? info "Sources"
    Definitions follow the portal's [clinical-library overview](https://k-cure.mohw.go.kr/portal/dit/clb/inf/viewClbInfo.do). Counts that disagree with that page are taken from the [portal home page](https://k-cure.mohw.go.kr/) on 29 October 2026 and from the portal FAQ. The schema is the public [ClinicalLibrary repository](https://github.com/k-cure/ClinicalLibrary).

## Two databases

The overview splits the library in two.

- **Baseline DB.** Common clinical data, not limited to one disease, mapped from each hospital's clinical data warehouse. The overview says the model has 6 groups and 39 tables and borrows the OMOP common data model. The FAQ says 15 hospitals contribute to Baseline.
- **Cancer clinical library (암 임상 라이브러리).** Cancer-specific items, standardized with the relevant clinical societies and then implemented by the participating hospitals. Each cancer has its own schema, arranged in five groups: patient, diagnosis, tests, treatment, and follow-up (환자, 진단, 검사, 치료, 추적관찰), with subgroups that differ by cancer.

The overview also says the clinical library as a whole was planned to cover cancer from 2022 through 2025, and respiratory and cardiovascular disease. This page is about the cancer portion.

## How many cancers, and how many people

The official pages do not agree, and this site does not pick a winner.

| Source | What it says |
|---|---|
| Portal home page, 29 October 2026 | 6 cancer types, about 500,000 people |
| Clinical-library overview | 10 cancers, and a plan to build the library with 18 hospitals |
| K-CURE library overview | 1.65 million people in standardized clinical data |
| Portal FAQ, written as the state in 2022 | Stomach and breast were built. The plan was colorectal and liver by 2023, pancreas, lung, and prostate by 2024, and cervix, kidney, and hematologic cancers by 2025 |
| Same FAQ, on hospitals | Baseline, 15 hospitals. Breast, 11 hospitals. Stomach, 6 hospitals |

The ten cancers named in that 2022 plan are stomach (위암), breast (유방암), colorectal (대장암), liver (간암), pancreas (췌장암), lung (폐암), prostate (전립선암), cervix (자궁경부암), kidney (신장암), and hematologic cancers (혈액암). The home page's "6 cancer types" is the current advertisement. Which six, and whether the later cancers in the plan were finished, is not stated on the pages above. The application catalog is the place to see what can be requested.

Each hospital decides on the request for its own patients. An approval does not extend to hospitals that did not review it.

## Tables

The portal points to [github.com/k-cure/ClinicalLibrary](https://github.com/k-cure/ClinicalLibrary) for the schemas. The repository holds the cancer clinical library, a standard vocabulary, common codes, a cancer-registration table, a statistics database, the Baseline OMOP schema, and a quality-management folder, plus a guide PDF for hospitals building the library. The FAQ says a new schema version goes to participating hospitals first and is published after the build that uses it.

The hospital registration table is [`cncr_rgst`](cncr-rgst.md). The Baseline model's 39 tables, and the tables inside each cancer schema, each belong on their own page once that schema is transcribed. They are not listed here in advance of that schema.

## What it does not replace

A clinical-library cohort is the patients whose hospitals contributed charts. Survival, incidence, and treatment patterns from it do not describe Korea. The national cohort, with stage and morphology but without chart-level results, is the [Cancer Public Library](../public-library/index.md). A study that needs both on the same people is a [combined](../combined.md) application.
