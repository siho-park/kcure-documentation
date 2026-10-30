# K-CURE Data Documentation

Welcome. This site is an unofficial guide to the cancer and health data released through [K-CURE](https://k-cure.mohw.go.kr/) (케이큐어), the health and medical data portal of the Korean Ministry of Health and Welfare (보건복지부).

## Motivation

K-CURE is the route to the Korea Central Cancer Registry (중앙암등록본부) linked to claims, screening, and death records. The registry records who was diagnosed, with which cancer, and at what stage. The linked files record the care before and after that diagnosis. A registry diagnosis is a reported cancer, so the combination supports studies that a billing code alone would leave uncertain.

The official documentation is in Korean and spread across portal pages, data catalogs, and a separate data dictionary. This site brings it together in English, with the Korean terms kept beside the English.

It is modeled on the [NHIS Data Documentation](https://siho-park.github.io/nhis-documentation/) and on the documentation that the [Research Data Assistance Center (ResDAC)](https://resdac.org) provides for Medicare data.

## What is on this site

The site has six parts.

- [**Program and data**](overview/index.md) describes the project, the products on the portal, the application, and where the data are analyzed.
- [**Datasets**](datasets/index.md) has one page per table of the Cancer Public Library, and a [sample page](datasets/public-library/sample.md) for the site samples (표본) and staging samples (표본 병기).
- [**Variables**](variables/index.md) lists the variables of every table, first for the customized extract and then for each sample, with a page per variable.
- [**Research notes**](blog/index.md) is a set of posts on working with the data. The first explains [how the tables fit together](blog/posts/01-how-the-kcure-tables-fit-together.md).
- [**Glossary**](glossary.md) translates the Korean terms used on the portal and in the registry.
- [**References**](references.md) lists the profile paper and the official pages these entries follow.

## Where to start

Start with the [Cancer Public Library](datasets/public-library/index.md) page. The registry is the table [`RGST`](datasets/public-library/rgst.md), and claims, screening, and death are the other tables. A study of one cancer site that needs detailed stage, such as tumor size, nodes, and metastasis, should look at the [staging samples](datasets/public-library/sample.md#staging-sample). The research note on [how the tables fit together](blog/posts/01-how-the-kcure-tables-fit-together.md) explains the joins.

## Disclaimer

This site is not affiliated with or endorsed by the Ministry of Health and Welfare, the Korea Health Information Service (한국보건의료정보원), the National Cancer Center (국립암센터), or the National Cancer Data Center (국가암데이터센터). Entries are written from public sources and may contain errors, so check them against the dictionary and the extract that come with an approved project.

## Contributing

Corrections and additions are welcome from anyone who has worked with the data. The easiest way to send them is an email to [sihopark@kdischool.ac.kr](mailto:sihopark@kdischool.ac.kr?subject=K-CURE%20Data%20Documentation). The [contributing page](about/contributing.md) explains what to include.

Maintained by Siho Park, KDI School of Public Policy and Management.
