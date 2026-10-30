# Sample

The portal releases two kinds of sample, and each one is a separate database, applied for and delivered on its own. A **site sample** (표본) is about 20 percent of one cancer site. A **staging sample** (표본 병기) is about 10 percent of one site, and its registration table comes from the registry's staging survey (협력병기). 병기 means stage.

!!! abstract "At a glance"
    - **[Site sample](#site-sample).** Six sites, with the same registration items as the customized extract (summary stage, histology, treatment) and a shorter list of claims columns.
    - **[Staging sample](#staging-sample).** Five sites, whose registration table adds tumor size, nodes, metastasis, grade, and TNM stage, depending on the site.
    - **[Other tables](#other-tables).** Death, eligibility, claims, and checkups are the same in both kinds of sample. Screening is included only for the sample's own site, and COVID-19 is absent.
    - **[Age and dates](#age-and-dates).** Neither kind lists year of birth. `AGE` is age at diagnosis in five-year bands, and the diagnosis date is given as year and month.
    - **[Access](#site-sample).** Both are analyzed remotely, on a virtual desktop, and delivered about one month after review.

??? info "Sources"
    The sites and the 20 percent and 10 percent figures follow the portal's [K-CURE library overview](https://k-cure.mohw.go.kr/portal/dit/lit/inf/viewDitLitInf.do). The tables and variables follow the data catalogs on the [catalog page](https://k-cure.mohw.go.kr/portal/dac/clc/ctg/viewClcCtgPub.do), downloaded 30 October 2026. The library overview also names kidney and prostate samples, and the catalog page has no workbook for them.

The variable lists are under [Variables](../../variables/index.md), for the [site samples](../../variables/index.md#site-samples) and the [staging samples](../../variables/index.md#staging-samples). Where the samples are analyzed is on [Using the data](../../overview/using.md#access-mode-by-dataset).

## Site sample (표본) {#site-sample}

A site sample's registration table keeps the registry items of the customized extract: SEER summary stage (`SEER_GRP`), treatment (`TX`), and basis of diagnosis (`METHOD`). It stores the full histology code `MCODE`, where the customized extract stores a 17-group code (`MCODE_GRP`). It omits `MULTI_9911`, the flag for a cancer diagnosed in 1999–2011.

| Sample | 한글 | Diagnoses | Tables |
|---|---|---|---|
| [Stomach](../../variables/sample/stomach.md) | 위암 표본 | 2012–2021 | 16, including stomach screening |
| [Breast](../../variables/sample/breast.md) | 유방암 표본 | 2012–2021 | 16, including breast screening |
| [Colorectal](../../variables/sample/colorectal.md) | 대장암 표본 | 2012–2021 | 16, including colorectal screening |
| [Liver](../../variables/sample/liver.md) | 간암 표본 | 2012–2021 | 16, including liver screening |
| [Lung](../../variables/sample/lung.md) | 폐암 표본 | 2012–2021 | 12, without screening |
| [Pancreas](../../variables/sample/pancreas.md) | 췌장암 표본 | 2012–2021 | 12, without screening |

## Staging sample (표본 병기) {#staging-sample}

A staging sample replaces the registration table with the staging-survey record. For stomach, breast, and colorectal cancer, that record has tumor size, nodes, metastasis, grade, and AJCC TNM stage, and it omits `SEER_GRP`, `TX`, and the ICD-10 code. Liver and lung have their own stage items.

| Sample | 한글 | Registration table | Stage detail |
|---|---|---|---|
| [Stomach](../../variables/staging/stomach.md) | 위암 표본 병기 | `CS_GC_RGST`, 40 variables | Tumor size, nodes, metastasis, grade, AJCC TNM |
| [Breast](../../variables/staging/breast.md) | 유방암 표본 병기 | `CS_BC_RGST`, 55 variables | Tumor size, nodes, metastasis, grade, AJCC TNM, and breast-specific factors |
| [Colorectal](../../variables/staging/colorectal.md) | 대장암 표본 병기 | `CS_CC_RGST`, 41 variables | Tumor size, nodes, metastasis, grade, AJCC TNM |
| [Liver](../../variables/staging/liver.md) | 간암 표본 병기 | `CS_LV_RGST`, 11 variables | Height, weight, AFP, clinical TNM and stage |
| [Lung](../../variables/staging/lung.md) | 폐암 표본 병기 | `CS_LC_RGST`, 32 variables | Smoking, histology, EGFR, ALK, imaging and pathologic TNM |

Diagnoses run from 2012 through 2021, and lung starts in 2014. For stomach, breast, and colorectal, the catalog refers to the Korea Central Cancer Registry's cooperative-staging user guide (협력병기 조사자료 이용자 안내서) for the detailed codes. The code tables on the variable pages are the codes the catalog itself lists.

## Other tables

The other tables are the same in a site sample and a staging sample of the same cancer. They are the same kinds of record as in the customized extract, with fewer columns.

- **Eligibility** omits the number of people on the insurance card.
- **Claim statement** omits several fields, including the cost amounts.
- **Services and outpatient prescriptions** omit unit price and amount.
- **Checkups** are included for every site. The questionnaire for recent years is `G1Q_1823`, so these files run through 2023.
- **Screening** is included only for the sample's own site, in files that run through 2023 (`0923`). Lung and pancreas have no screening table.
- **COVID-19** is absent.

The catalogs do not list `SN_KEY`. The claims tables list `MID`.

## Age and dates

Neither kind of sample lists year of birth. `AGE` is age at diagnosis, in five-year bands. `FDX` is the year and month of first diagnosis, where the customized extract gives the full date. `DBYEAR` (자료등록연도) on a staging table is the year the record was registered.
