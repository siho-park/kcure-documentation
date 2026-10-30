# Glossary

The portal and the official manuals use Korean administrative terms. This page gives the English used on this site, so that one Korean term keeps one English translation. Claims terms that also appear in the NHIS databases are defined in more detail in the [NHIS glossary](https://siho-park.github.io/nhis-documentation/glossary/).

## The project

| 한글 | English | Notes |
|---|---|---|
| 케이큐어, K-CURE | K-CURE | Korean Clinical Data Utilization Network for Research Excellence |
| 보건복지부 | Ministry of Health and Welfare | |
| 한국보건의료정보원 | Korea Health Information Service (KHIS) | Operates the portal and the central safe-use center |
| 국립암센터 | National Cancer Center | |
| 국가암데이터센터 | National Cancer Data Center (NCDC) | Designated in September 2021. Releases the Cancer Public Library |
| 암관리법 | Cancer Control Act | The statutory basis for the center and the public library |
| 개인정보 보호법 | Personal Information Protection Act | The basis for releasing pseudonymized data |
| 가명처리 | Pseudonymization | The form in which the extracts are released |
| 안심활용센터 | Safe-use center | Closed analysis environment. Also called a safe utilization center |
| 개인정보 이노베이션 존 | Personal-information innovation zone | A more secure analysis room at the National Cancer Center, for data with lighter pseudonymization |
| 가상PC, 가상컴퓨터 | Virtual desktop | The project's analysis computer, opened at a center or remotely |
| 연구활용계획서 | Research-use plan | Required with every application, and to justify restricted variables |
| 보관 중 재사용 | Reuse during storage | Reopening a stored extract, up to seven days at a time |
| 반출심사 | Export review | Review of results before they leave the center |
| 데이터제공심의위원회 | Data-provision review committee | Reviews whether an extract is released |
| 데이터반출심사위원회 | Data-export review committee | Reviews export. The portal names this committee in the public-library timetable |

## The cancer data

| 한글 | English | Notes |
|---|---|---|
| 중앙암등록본부 | Korea Central Cancer Registry (KCCR) | |
| 국가암발생데이터베이스 | Korea National Cancer Incidence Database | The incidence file the public library is built on |
| 암등록 | Cancer registration | |
| 암 공공 라이브러리 | Cancer Public Library | Registry cohort linked to public data |
| 맞춤형 | Customized extract | Researcher-specified variables from the full library |
| 표본 | Site sample | About 20 percent of one cancer site, with a fixed variable list |
| 표본 병기 | Staging sample | About 10 percent of one cancer site, with detailed stage items |
| 병기 | Stage | |
| 협력병기 | Cooperative staging survey | The registry's survey of detailed stage, the source of the staging samples |
| 다중원발암 | Multiple primary cancers | A person with two cancers has two rows on `RGST` |
| 대체식별키 | Person identifier | `SN_KEY`, reassigned at every extraction |
| 명세서조인키 | Claim join key | `MID`, which joins the four claims tables |
| 임상 라이브러리 | Clinical library | Standardized hospital records |
| 특화 데이터 | Specialized data | Hospital-built datasets, often including images |
| 결합 | Linkage, or a combined extract | Person-level link of clinical and public data |
| 전주기 | Full cycle | The portal's term for history before diagnosis, at diagnosis, and after |
| 원발부위 | Primary site | |
| 조직학적 진단 | Histology | Morphology |
| 편측성 | Laterality | |
| 분화도 | Grade | |
| 요약병기 | Summary stage | SEER summary stage: in situ, localized, regional, distant, unknown |
| 국한 | Localized | |
| 국소진행, 영역 | Regional | The profile's English label is regional |
| 원격 | Distant | |
| 진단일, 초진연월일 | Diagnosis date, or date of the first visit | The hospital schema uses the first-visit date. Confirm which date the extract carries |

## Insurance and claims

| 한글 | English | Notes |
|---|---|---|
| 국민건강보험공단 | National Health Insurance Service (NHIS) | Eligibility, premiums, checkups, screening |
| 건강보험심사평가원 | Health Insurance Review and Assessment Service (HIRA) | Claims |
| 질병관리청 | Korea Disease Control and Prevention Agency (KDCA) | COVID-19 confirmation and vaccination |
| 국가데이터처 | National data office | Formerly Statistics Korea (통계청). Date and cause of death |
| 자격 | Eligibility | |
| 직장가입자 | Employee insured | |
| 지역가입자 | Self-employed insured | |
| 의료급여 | Medical Aid | |
| 보험료분위 | Premium decile | Income proxy. 0 is Medical Aid |
| 명세서 | Claim | |
| 진료내역 | Treatment details, or healthcare services | |
| 상병 | Diagnosis | A billing code, except where it is the registry site |
| 주상병 | Primary diagnosis | |
| 부상병 | Secondary diagnosis | |
| 원외처방전 | Outpatient prescription | Drugs dispensed outside the institution |
| 건강검진 | General health examination | |
| 암검진 | National cancer screening | |
