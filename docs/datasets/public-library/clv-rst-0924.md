# Liver screening, 2009–2024 (CLV_RST_0924)

`CLV_RST_0924` (간암 검진) is a table in the [Cancer Public Library](index.md). One row is one liver screening in 2009–2024. The form changed in 2009, so the other period is [`CLV_RST_0708`](clv-rst-0708.md).

The record covers the liver ultrasound findings, alpha-fetoprotein, and the judgment. The 2009–2024 file also has ALT and the hepatitis B and C tests. The questionnaire for the same screening is [`CQ_RST_0924`](cq-rst-0924.md), and the two join on `SN_KEY` and the examination year `EXMD_BZ_YYYY`.

The people are those on [`RGST`](rgst.md) with a national cancer screening record from 2007 through 2024. When a screening has more than one judgment, the most important one is recorded. Findings can be recorded up to three at a time, in order of severity. Using any screening table requires a research-use plan.

**Who is screened.** Men and women aged 40 or older in the high-risk group for liver cancer in the previous two years, every 6 months. A person treated for liver cancer is deferred until the year before their insurance special-calculation period ends.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/clv_rst_0924.md).

??? info "Source"
    The description follows the cancer-screening overview and its eligibility table in data dictionary version 4.0 (September 2026).
