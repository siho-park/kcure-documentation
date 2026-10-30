# COVID-19 vaccination (COVID_VAC)

`COVID_VAC` (코로나19 예방접종) is a table in the [Cancer Public Library](index.md). One row is one vaccination. The dates run from 17 December 2020 through 31 August 2023, for people on [`RGST`](rgst.md). Confirmations are on [`COVID_PT`](covid-pt.md). The row joins to the rest of the library on `SN_KEY`.

Using these variables requires a research-use plan. If two doses fall fewer than 21 days apart, only the later dose is kept. Dose numbers are released as the Korea Disease Control and Prevention Agency collected them. A dose given abroad can appear without the earlier doses, and the dose number for an abroad vaccination is not filled in. Counts from this table can differ from the agency's published daily totals.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/covid_vac.md).

??? info "Source"
    The window and the variables follow data dictionary version 4.0, Table 26 and the vaccination-variable notes (September 2026).

## Variables

| Variable | 한글 | Definition |
|---|---|---|
| `VACN_YMD` | 접종일자 | Vaccination date, `YYYYMMDD` |
| `VACN_TME` | 접종차수 | 1 first dose, 2 second, 3 third, 4 fourth, 5 the 2022 winter dose, 6 an extra dose from May 2023 for an immunocompromised person or someone aged 65 or older who had the winter dose, 99 vaccinated abroad |
| `VACN_NM` | 접종백신명 | 01 AstraZeneca, 02 Pfizer-BioNTech, 03 Moderna, 04 Janssen, 05 Novavax, 06 SKYCovione, 07 Pfizer bivalent, 08 Moderna bivalent, 99 vaccinated abroad |
