# Stomach screening, 2007–2008 (CST_RST_0708)

`CST_RST_0708` (위암 검진) is a table in the [Cancer Public Library](index.md). One row is one stomach screening in 2007–2008. The form changed in 2009, so the other period is [`CST_RST_0924`](cst-rst-0924.md).

The record covers the upper gastrointestinal series and endoscopy findings, the biopsy result, and the judgment. The questionnaire for the same screening is [`CQ_RST_0708`](cq-rst-0708.md), and the two join on `SN_KEY` and the examination year `EXMD_BZ_YYYY`.

The people are those on [`RGST`](rgst.md) with a national cancer screening record from 2007 through 2024. When a screening has more than one judgment, the most important one is recorded. Findings can be recorded up to three at a time, in order of severity. Using any screening table requires a research-use plan.

**Who is screened.** Men and women aged 40 or older, every 2 years.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/cst_rst_0708.md).

??? info "Source"
    The description follows the cancer-screening overview and its eligibility table in data dictionary version 4.0 (September 2026).
