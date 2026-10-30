# COVID-19 cases (COVID_PT)

`COVID_PT` (코로나19 확진자) is a table in the [Cancer Public Library](index.md). One row is one confirmed COVID-19 case. The people are those on [`RGST`](rgst.md) with a confirmation or a vaccination record from 2020 through 31 August 2023. Vaccinations are on [`COVID_VAC`](covid-vac.md). The row joins to the rest of the library on `SN_KEY`.

Using these variables requires a research-use plan. The variables are listed, each with its own page, in the [variable list](../../variables/public-library/covid_pt.md).

??? info "Source"
    The window and the variables follow data dictionary version 4.0, Table 25 and the COVID-19 overview (September 2026).

## Variables

| Variable | 한글 | Definition |
|---|---|---|
| `CDX_DT` | 확진일자 | Confirmation date, `YYYYMMDD` |
| `REPO_TRANS` | 신고기관권역 | Region of the report: 01 capital area, 02 Chungcheong, 03 Honam, 04 Gyeongbuk, 05 Gyeongnam, 06 Gangwon, 07 Jeju, 99 quarantine |
| `REPO_SIDO` | 신고기관시도 | Province of the report, using the same province codes as `SIDO_CD` on [`BFC`](bfc.md), plus 99 for a quarantine station |
| `INFECT_ROUTE` | 감염경로 | `INT` infection in Korea, `EXT` infection abroad |
