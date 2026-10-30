# Cancer screening questionnaire, 2009–2024 (CQ_RST_0924)

`CQ_RST_0924` (암문진) is a table in the [Cancer Public Library](index.md). It holds the questionnaire items shared by every site in the national cancer screening program, for 2009–2024. The other period is [`CQ_RST_0708`](cq-rst-0708.md).

The questionnaire covers symptoms, personal and family history of cancer, earlier screening tests, related conditions, smoking, drinking, and, for women, menstruation and hormone use. The site results for the same period are [`CBR_RST_0924`](cbr-rst-0924.md), [`CCR_RST_0924`](ccr-rst-0924.md), [`CCX_RST_0924`](ccx-rst-0924.md), [`CLV_RST_0924`](clv-rst-0924.md), [`CST_RST_0924`](cst-rst-0924.md), and they join on `SN_KEY` and `EXMD_BZ_YYYY`.

The dictionary prints these items once. The portal catalog delivers them as one file per site, with the same variables: `CBR_CQ_RST_0924`, `CCR_CQ_RST_0924`, `CCX_CQ_RST_0924`, `CLV_CQ_RST_0924`, and `CST_CQ_RST_0924`.

The people are those on [`RGST`](rgst.md) with a national cancer screening record from 2007 through 2024. When a screening has more than one judgment, the most important one is recorded. Findings can be recorded up to three at a time, in order of severity. Using any screening table requires a research-use plan.

The variables are listed, each with its own page, in the [variable list](../../variables/public-library/cq_rst_0924.md).

??? info "Source"
    The description follows the cancer-screening overview in data dictionary version 4.0 (September 2026).
