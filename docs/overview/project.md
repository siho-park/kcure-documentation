# The K-CURE project

K-CURE (Korean Clinical Data Utilization Network for Research Excellence, 케이큐어) is a Ministry of Health and Welfare project that links the cancer registry to other public health data and to hospital records, and lets approved studies analyze the result inside a closed environment. Its public face is the [K-CURE portal](https://k-cure.mohw.go.kr/).

!!! abstract "At a glance"
    - **[Purpose](#what-the-project-does).** The project puts registry, insurance, screening, and death records on one person identifier, so a study can follow a registered cancer from screening to death.
    - **[Who runs it](#who-operates-it).** The National Cancer Data Center builds and releases the Cancer Public Library, and the Korea Health Information Service runs the portal and the central safe-use center.
    - **[Legal basis](#legal-basis).** The Cancer Control Act and the Personal Information Protection Act allow the release of pseudonymized data for research.
    - **[Contacts](#who-operates-it).** Questions about the Cancer Public Library go to data@ncc.re.kr, and questions about the portal and the centers go to k-cure@khis.kr.

??? info "Sources"
    This page follows the portal's [service overview](https://k-cure.mohw.go.kr/portal/pfm/kif/inf/viewPfmKifInf.do), the [National Cancer Data Center](https://www.cancerdata.re.kr/main/publicData/publicDataList) description of its designation, data dictionary version 4.0 (September 2026), and the data resource profile by Choi and colleagues.[^choi] The profile names the Korea Health Information Service as the party that builds the linkage table, and the portal overview describes the Ministry as receiving the linkage keys. Both say the released file carries only a project-specific person number.

## What the project does

Each source holds one part of a cancer patient's history. The Korea Central Cancer Registry (중앙암등록본부) records who was diagnosed, with which cancer, and at what stage. The National Health Insurance Service (국민건강보험공단, NHIS) and the Health Insurance Review and Assessment Service (건강보험심사평가원, HIRA) record eligibility, checkups, screening, and claims. The national data office (국가데이터처) records deaths, and the Korea Disease Control and Prevention Agency (질병관리청) records COVID-19 cases and vaccinations.

K-CURE links these files on one person identifier, under the rules for pseudonymized data. The linked file stays in a closed analysis environment, and only reviewed results leave it.

## Who operates it

| Role | 한글 | What it does |
|---|---|---|
| Ministry of Health and Welfare | 보건복지부 | Runs the project |
| National Cancer Data Center | 국가암데이터센터 | Builds, reviews, and releases the Cancer Public Library. Hosted by the National Cancer Center (국립암센터). Contact: data@ncc.re.kr, 031-920-2597 |
| Korea Central Cancer Registry | 중앙암등록본부 | Supplies the registry file on which the library is built |
| Korea Health Information Service | 한국보건의료정보원 | Operates the portal and the central safe-use center. Contact: k-cure@khis.kr |
| Participating hospitals | 참여기관 | Contribute standardized records to the clinical library |

Fee payment for the Cancer Public Library also goes through data@ncc.re.kr.

## Legal basis

Two laws allow the release.

- The Cancer Control Act (암관리법), article 9-2, establishes the cancer-data program. Under it, the National Cancer Data Center collects records held by public institutions, processes them internally, and provides them for public-interest research.
- The Personal Information Protection Act (개인정보 보호법) allows pseudonymized data to be used for statistics and scientific research without individual consent.

Each source institution creates a linkage key from the resident registration number, and a linkage table joins those keys. The released file carries one project-specific person number, `SN_KEY` (대체식별키). Researchers cannot attach another person-level file themselves.

## What the name covers

The portal uses "K-CURE" for the project, the website, and a [library that combines clinical and public data](../datasets/combined.md). On this site, K-CURE means the project and the portal, and each released database is named on its own page.

[^choi]: Choi DW, et al. Data Resource Profile: The Cancer Public Library Database in South Korea. *Cancer Research and Treatment*. 2024;56(4):1014-1026. [doi:10.4143/crt.2024.207](https://doi.org/10.4143/crt.2024.207)
