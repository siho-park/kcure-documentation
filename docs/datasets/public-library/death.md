# Death

`DEATH` (사망) is a table in the [Cancer Public Library](index.md). One row is one death of a person on [`RGST`](rgst.md), from 2012 through 2023, for 889,536 deaths. A person who was alive at the end of 2023 has no row. The row joins to the rest of the library on `SN_KEY`.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/death.md).

??? info "Source"
    The count, years, and variables follow data dictionary version 4.0, Table 2 and the death-table overview (September 2026).

## Variables

| Variable | 한글 | Definition |
|---|---|---|
| `DREGDATE` | 사망연월일 | Date of death, `YYYYMMDD` |
| `SAIN1` | 사망원인코드1 | Underlying cause, in the Korean Standard Classification of Diseases (KCD). Sensitive causes in chapters 1 (A00–B99), 5 (F00–F99), 19 (S00–T98), and 20 (V01–Y98) are collapsed to a block, such as `V59` to `V50–V59` |
| `SAIN2` | 사망원인코드2 | External-cause detail (`V01–Y98`) when `SAIN1` is an injury code (`S00–T98`). The same sensitive-cause collapsing applies |

Cause-of-death codes follow the statistics-office notice of 1 July 2020 (국가데이터처 고시 제2020-175호).
