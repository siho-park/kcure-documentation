# Hospital cancer registration

`cncr_rgst` is the cancer-registration table in the [clinical library](index.md). Participating hospitals map a registration into this table. Its key is the hospital, the hospital patient number, the date of the first visit, and a registration sequence. The columns include primary site, laterality, histology, grade, a SEER code, stage, and treatment, stored with the hospital's own identifiers.

The national registry extract is [`RGST`](../public-library/rgst.md) in the Cancer Public Library. `cncr_rgst` is the hospital file. Its columns are not the column list for a public-library extract.

??? info "Source"
    The schema is the public [ClinicalLibrary repository](https://github.com/k-cure/ClinicalLibrary), in the cancer-registration folder.
