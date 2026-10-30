# Cancer registration

`RGST` (암등록) is the registry table of the [Cancer Public Library](index.md). One row is one registered cancer, diagnosed from 2012 through 2022, for 2,923,903 rows. A person with two cancers has two rows with the same `SN_KEY`, which joins the row to death, claims, screening, and the other tables.

??? info "Source"
    Variable names, codes, and the row count follow data dictionary version 4.0 (September 2026), Table 1 and the registry-table overview.

## Variables

`RGST` has ten variables besides `SN_KEY`. Each has its own page in the [variable list](../../variables/public-library/rgst.md).

| Variable | 한글 | Definition |
|---|---|---|
| `SEX` | 성별 | 1 man, 2 woman |
| `AGE` | 진단시 만나이 | Age in full years at the first diagnosis date, in bands: 29 and under, five-year groups from 30 to 84, and 85 and older. One-year age requires a research-use plan and committee approval |
| `ICD10` | 국제질병분류코드 | Site in ICD-10, without the decimal (`C161` for C16.1) |
| `TCODE` | 원발부위코드 | Primary site in ICD-O-3 topography, without the decimal |
| `MCODE_GRP` | 조직학적진단그룹 | Histology in 17 ICD-O-3 groups. A finer grouping requires a research-use plan |
| `FDX` | 최초진단연월일 | Date of first diagnosis, `YYYYMMDD` |
| `TX` | 치료 | Treatment within four months of diagnosis, as five digits of 0 or 1: surgery, chemotherapy, radiation, immunotherapy, hormone therapy. Surgery and radiation is `10100` |
| `METHOD` | 최종진단방법 | Most definitive basis of diagnosis. 0 death certificate only, 1 clinical, 2 clinical test, 3 surgery or autopsy without histology, 4 special biochemical or immunological test, 5 cytology or hematology, 6 histology of a metastasis, 7 histology of the primary site, 8 autopsy |
| `SEER_GRP` | 요약병기 | SEER summary stage. 0 carcinoma in situ, 1 localized (국한), 2 regional (국소), 7 distant (원격), 9 unknown. A colorectal in situ code (`D01.x`) can also be coded 1, localized |
| `MULTI_9911` | '99–'11년 암진단 여부 | `Y` if the person had a cancer diagnosed in 1999–2011, otherwise `N` |

Province of residence is on the eligibility table, [`BFC`](bfc.md), as `SIDO_CD`. Date and cause of death are on [`DEATH`](death.md).

## Registry diagnoses and claims diagnoses

A claims diagnosis is the code a provider billed, which can be a suspected cancer, a rule-out, or a cancer treated years earlier. `RGST` records a cancer the registry confirmed, with a date, a site, and a stage. A cohort defined from `RGST` therefore avoids the false positives and missed cases of a claims-based definition.

`TX` summarizes treatment within four months. The procedures, drugs, and dates are on the claims tables [`T200`](t200.md), [`T300`](t300.md), [`T400`](t400.md), and [`T530`](t530.md).

## Detailed stage

`SEER_GRP` is the only stage variable on the customized `RGST`. Tumor size, nodes, metastasis, grade, and TNM stage are in the [staging samples](sample.md#staging-sample) (표본 병기), for stomach, breast, colorectal, liver, and lung.
