# Combined library (K-CURE 라이브러리)

The portal uses "K-CURE library" for three arrangements of the same two sources: the clinical library alone, the Cancer Public Library alone, and the two linked at the person level.

??? info "Source"
    The three-way definition follows the portal's [K-CURE library overview](https://k-cure.mohw.go.kr/portal/dit/lit/inf/viewDitLitInf.do).

| Arrangement | What a study gets |
|---|---|
| Clinical | Hospital charts, standardized, for participating hospitals |
| Public | The national registry cohort, with claims, screening, death, and, in current builds, COVID-19 |
| Clinical and public | Both, on the people who can be linked |

The third arrangement is the one that puts chart-level stage, pathology, and results next to the national claims and death records. It is requested on the combined-data path (결합 데이터 신청), not by applying for the two libraries separately and merging them. Researchers do not hold the key that would make that merge possible. Linkage is done inside the project, as described on the [project page](../overview/project.md).

The library overview also describes the public-library samples on the same page. Those samples are public data only. They are documented on the [sample page](public-library/sample.md).

This site does not yet have a separate description of how a combined extract is reviewed, which hospitals can be linked, or how often a registered patient matches a contributing hospital. Those facts belong here once an official guide or an approved project records them.
