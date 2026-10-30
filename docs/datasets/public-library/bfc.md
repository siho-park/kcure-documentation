# Eligibility and premium

`BFC` (자격 및 보험료) is a table in the [Cancer Public Library](index.md). One row is one person in one year, from 2007 through 2024, for people on [`RGST`](rgst.md) who still had health-insurance eligibility on 31 December of that year. The row joins to the rest of the library on `SN_KEY`, and to a claim on `SN_KEY` and the year of care.

Province of residence (`SIDO_CD`) is on this table. The variables are listed, each with its own page, in the [variable list](../../variables/public-library/bfc.md).

??? info "Source"
    The population rule and the variables follow data dictionary version 4.0, Table 3 and the eligibility-table overview (September 2026).

## Variables

| Variable | 한글 | Definition |
|---|---|---|
| `STD_YYYY` | 기준연도 | Year, 2007–2024 |
| `GAIBJA_TYPE` | 가입자구분 | 1 self-employed household head, 2 self-employed household member, 5 employee insured, 6 employee dependent, 7 Medical Aid household head, 8 Medical Aid household member |
| `SIDO_CD` | 실거주주소코드 | Province of residence, in 18 codes: 11 Seoul, 26 Busan, 27 Daegu, 28 Incheon, 29 Gwangju, 30 Daejeon, 31 Ulsan, 36 Sejong, 41 Gyeonggi, 42 Gangwon, 43 Chungbuk, 44 Chungnam, 45 Jeonbuk, 46 Jeonnam, 47 Gyeongbuk, 48 Gyeongnam, 50 Jeju, 51 Gangwon Special Self-Governing Province |
| `CALC_CTRB_VTILE_FD` | 보험료 | Premium decile, 1–10, among the insured population. 0 is a Medical Aid recipient. People on the same insurance card share a decile |
| `CNT_ID_HHHI_FD` | 증인원수 | People on the insurance card: 1, 2, 3, 4, or 5 for five or more |
| `CMPR_DSB_GRADE_ADJ` | 종합장애등급코드 | 0 none, 1 severe (former grades 1–3), 2 mild (former grades 4–6) |
| `MAIN_DSB_TYPE_ADJ` | 주장애유형 | 0 none, 1 physical, 2 brain lesion, 3 visual, 4 hearing, 5 any other disability |

The premium is the annual average, built from the premium charged on the first of each month. A month with no premium on that day is filled with the annual average. Some people, including career soldiers and some long leaves, can still have a missing premium.
