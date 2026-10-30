# What the portal releases

The portal's data menu has four products. The cancer registry is part of the first one, the Cancer Public Library, which is the focus of this site.

!!! abstract "At a glance"
    - **[Four products](#the-four-products).** These are the Cancer Public Library, the clinical library, specialized data, and health and medical data.
    - **[The registry](#where-the-registry-is).** National registry records reach a study only through the Cancer Public Library.
    - **[Three databases](#three-databases-in-the-cancer-public-library).** The Cancer Public Library is released as a customized extract, a site sample, or a staging sample, and each is applied for on its own.

??? info "Sources"
    The four products and the counts follow the [portal home page](https://k-cure.mohw.go.kr/) as viewed on 29 October 2026. The definitions follow each product's overview page. Other official pages give different counts, and those are lined up on [Sources and versions](../datasets/sources.md).

## The four products

| Product | 한글 | What it is | Portal summary, 29 Oct 2026 |
|---|---|---|---|
| [Cancer Public Library](../datasets/public-library/index.md) | 암 공공 라이브러리 | Every registered cancer patient, with registry, death, claims, screening, and COVID-19 records linked | About 2.26 million people |
| [Clinical library](../datasets/clinical/index.md) | 임상 라이브러리 | Standardized electronic records from participating hospitals | 6 cancer types, about 500,000 people |
| [Specialized data](../datasets/specialized.md) | 특화 데이터 | Disease-specific datasets built by hospitals, including images | 67 datasets |
| [Health and medical data](../datasets/health.md) | 보건의료 데이터 | Open health files, and a person-level link of nine institutions' data | 9 institutions |

The portal also uses the name [K-CURE library](../datasets/combined.md) (K-CURE 라이브러리) for clinical data, public data, or the two linked together.

## Where the registry is

The Cancer Public Library is built from the Korea Central Cancer Registry. Its cohort is every registered cancer, and the registry items travel with that cohort into every extract. A study that needs incidence, site, histology, or stage, followed by claims or death, applies for this library.

The clinical library has its own registration table, [`cncr_rgst`](../datasets/clinical/cncr-rgst.md), which is each hospital's record of its own patients. The national registry table is [`RGST`](../datasets/public-library/rgst.md).

## Three databases in the Cancer Public Library

| Database | 한글 | Who is in it | Where it is analyzed |
|---|---|---|---|
| [Customized extract](../datasets/public-library/index.md) | 맞춤형 | Every registered cancer, 2012–2022, all sites | In person, at a safe-use center |
| [Site sample](../datasets/public-library/sample.md#site-sample) | 표본 | About 20 percent of one listed site | Remote virtual desktop |
| [Staging sample](../datasets/public-library/sample.md#staging-sample) | 표본 병기 | About 10 percent of one listed site, with detailed stage items | Remote virtual desktop |

The [datasets page](../datasets/index.md) compares their contents, and [Using the data](using.md) describes the two ways of analyzing them.
