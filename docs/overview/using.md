# Using the data

Researchers never take the Cancer Public Library home. A customized extract is analyzed in person at a safe-use center, and a sample is analyzed on a remote virtual desktop. In both cases, results leave only after they pass export review (반출심사). Applying is a separate step, described on [Applying for data](access.md).

!!! abstract "At a glance"
    - **[Where](#access-mode-by-dataset).** A customized extract opens only at a safe-use center, and a site sample or a staging sample opens remotely from the researcher's own computer.
    - **[How long](#period-of-use-and-fees).** An approval lasts two years from the start of analysis: up to one year of analysis and up to one year of storage.
    - **[Fees](#period-of-use-and-fees).** The platform fee is charged by days, weeks, and months of use, and storage is free for the first three months.
    - **[Reuse during storage](#reuse-during-storage).** A stored extract can be reopened for up to seven days at a time, booked at least two weeks ahead.
    - **[Centers](#safe-use-centers).** There is a central center in Seoul, a center at the National Cancer Center in Goyang, and seven regional centers, and the statistical software differs by center.
    - **[Results](#results-and-linkage).** Results leave only after export review, and researchers cannot link another person-level file.

??? info "Sources"
    Access modes, fees, and the period of use follow data dictionary version 4.0 (September 2026, pages 4–6 of the overview). Remote access for the staging samples follows the National Cancer Center [press release of August 2023](https://ncc.re.kr/prBoardView1.ncc?nwsId=8916). The virtual-desktop drive, software, and reservations follow the portal [FAQ](https://k-cure.mohw.go.kr/portal/bbs/faq/viewFaq.do). The centers follow the portal's [safe-use center page](https://k-cure.mohw.go.kr/portal/pfm/kif/use/viewPfmKifUse.do) and its [English version](https://k-cure.mohw.go.kr/portal/cmm/htm/engSafeCenterIntro.do). The rule against further linkage follows Choi and colleagues.[^choi]

## Access mode by dataset

| Dataset | 한글 | Access mode | Where the analysis runs | Time from the review date |
|---|---|---|---|---|
| [Customized extract](../datasets/public-library/index.md) | 맞춤형 | In person | A designated safe-use center (안심활용센터), or the personal-information innovation zone at the National Cancer Center | About three months |
| [Site sample](../datasets/public-library/sample.md#site-sample) | 표본 | Remote | A virtual desktop (가상PC) assigned to the project, reached from the researcher's own computer | About one month |
| [Staging sample](../datasets/public-library/sample.md#staging-sample) | 표본 병기 | Remote | A virtual desktop (가상PC) assigned to the project, reached from the researcher's own computer | About one month |

The dictionary lists both an analysis room and a virtual computer for a customized extract, and a virtual computer alone for a sample. The portal FAQ says the project's source data are on the D drive of its virtual desktop (VDI).

The portal does not say whether remote access uses a VPN or which client software it needs. Those are questions for k-cure@khis.kr.

The personal-information innovation zone (개인정보 이노베이션 존) is a more secure room at the National Cancer Center, with fingerprint and entry authentication and CCTV. Researchers there can analyze data with lighter pseudonymization. Applying for the zone needs extra documents, listed on [Applying for data](access.md#documents).

## Period of use and fees

An approval lasts two years from the start of analysis: up to one year of analysis, then up to one year of storage. Using the same data after either limit requires a new application and review.

The analysis-platform fee is half an analysis-room fee and half a virtual-computer fee. The room fee is paid to the center the researcher chooses, and regional centers can set their own room fees. Both are charged by the length of use:

| Period of use | Fee |
|---|---|
| 6 days or fewer | 50,000 won per day |
| 1 week or more | 225,000 won per week, plus 50,000 won per remaining day |
| 1 month or more | 700,000 won per month, plus 225,000 won per remaining week and 50,000 won per remaining day |

Storage is free for three months and then costs 10,000 won per month, up to twelve months.

A GPU server is available at the National Cancer Data Center's center and by remote access. It runs only a Python Jupyter environment and costs twice the virtual-computer fee. Ask the data provision staff first whether it is available. The fee for the innovation zone is set separately.

## Reuse during storage

Within the approval period, a stored extract can be reopened (보관 중 재사용).

- Each reuse lasts up to seven days. For a sample, weekends count toward the seven days. For a customized extract, only weekdays count.
- Agree the start date with the National Cancer Center data provision staff at least two weeks ahead, and file a use request on the portal so the center visit can be scheduled.
- From the second reuse on, attach evidence such as a journal's revision or rejection email.
- The same fees and reductions apply as for the analysis platform.

## Safe-use centers

A safe-use center provides the data and a closed analysis environment for scientific and academic work. Regional centers let researchers outside Seoul use the data. A visit requires an approval and a reservation, which is made through the K-CURE portal or the [Health and Medical Big Data Platform](https://hcdl.mohw.go.kr).

| Center | 한글 | Location |
|---|---|---|
| Central Safe Utilization Center | 안심활용중앙센터 | Korea Health Information Service, 11th floor, 39 Sejong-daero, Jung-gu, Seoul |
| National Cancer Data Center | 국가암데이터센터 | 7th floor, research building, National Cancer Center, Goyang |
| Keimyung University Dongsan Hospital | 계명대학교 동산의료원 | Regional |
| Wonju Severance Christian Hospital | 원주세브란스기독병원 | Regional |
| Chungnam National University Hospital | 충남대학교병원 | Regional |
| Pusan National University Hospital | 부산대학교병원 | Regional |
| Hwasun Chonnam National University Hospital | 화순전남대학교병원 | Regional |
| Konyang University Hospital | 건양대학교병원 | Regional |
| Yonsei University Health System | 연세대학교 의료원 | Regional |

### Software

Every center has document tools (Hangul, Excel, Word, PowerPoint). Statistical software differs by center.

| Center | Statistical software |
|---|---|
| Central center | SAS, R, SPSS, Stata, Python |
| National Cancer Data Center | SAS, R, Python |

A study that depends on a particular package should confirm it with k-cure@khis.kr for the center that will hold the extract.

### Hours

The National Cancer Data Center's center is open on weekdays from 08:30 to 16:30. The central center is open on weekdays and closed for lunch from 12:00 to 13:00, and it is also closed on public holidays, Labor Day, and the Korea Health Information Service anniversary (24 September). Its opening hours differ across the portal's pages, so check them before booking.

??? note "Central-center hours by source"
    | Source | Central center |
    |---|---|
    | Korean center page | Weekdays 10:00–17:00, closed 12:00–13:00 |
    | English center page | Weekdays 09:00–18:00, closed 12:00–13:00 |
    | Portal FAQ | Weekdays 09:00–18:00 |

## Results and linkage

Results leave through export review (반출심사). The [contributing page](../about/contributing.md) explains what that means for anything published from an extract, including notes sent to this site.

Each person has one non-identifying number, shared across the tables, and researchers cannot link any further person-level data themselves. Another linkage has to be built by an institution authorized under the Personal Information Protection Act. A study that needs a file the library lacks should be designed as a linkage project from the start.

[^choi]: Choi DW, et al. Data Resource Profile: The Cancer Public Library Database in South Korea. *Cancer Research and Treatment*. 2024;56(4):1014-1026. [doi:10.4143/crt.2024.207](https://doi.org/10.4143/crt.2024.207)
