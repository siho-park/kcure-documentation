# Cervical screening, 2007–2008 (CCX_RST_0708)

`CCX_RST_0708` (자궁경부암 검진) is a table in the [Cancer Public Library](index.md). One row is one cervical screening in 2007–2008. The form changed in 2009, so the other period is [`CCX_RST_0924`](ccx-rst-0924.md).

The record covers the Pap smear, including specimen adequacy and the cell findings, and the judgment. The questionnaire for the same screening is [`CQ_RST_0708`](cq-rst-0708.md), and the two join on `SN_KEY` and the examination year `EXMD_BZ_YYYY`.

The people are those on [`RGST`](rgst.md) with a national cancer screening record from 2007 through 2024. When a screening has more than one judgment, the most important one is recorded. Findings can be recorded up to three at a time, in order of severity. Using any screening table requires a research-use plan.

**Who is screened.** Women aged 30 or older through 2014. In 2015, women aged 30 or older, or 20 or older on Medical Aid. From 2016, women aged 20 or older. Every 2 years.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/ccx_rst_0708.md).

??? info "Source"
    The description follows the cancer-screening overview and its eligibility table in data dictionary version 4.0 (September 2026).
