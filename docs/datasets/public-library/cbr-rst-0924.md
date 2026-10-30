# Breast screening, 2009–2024 (CBR_RST_0924)

`CBR_RST_0924` (유방암 검진) is a table in the [Cancer Public Library](index.md). One row is one breast screening in 2009–2024. The form changed in 2009, so the other period is [`CBR_RST_0708`](cbr-rst-0708.md).

The record covers mammography findings and the location of each lesion, and the judgment. The questionnaire for the same screening is [`CQ_RST_0924`](cq-rst-0924.md), and the two join on `SN_KEY` and the examination year `EXMD_BZ_YYYY`.

The people are those on [`RGST`](rgst.md) with a national cancer screening record from 2007 through 2024. When a screening has more than one judgment, the most important one is recorded. Findings can be recorded up to three at a time, in order of severity. Using any screening table requires a research-use plan.

**Who is screened.** Women aged 40 or older, every 2 years.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/cbr_rst_0924.md).

??? info "Source"
    The description follows the cancer-screening overview and its eligibility table in data dictionary version 4.0 (September 2026).
