# -*- coding: utf-8 -*-
"""Generate the Variables section from codebook/public-library.json.

The JSON is extracted from data dictionary version 4.0. Edit that file, or
re-extract it, rather than the generated Markdown.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import mkdocs_gen_files

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import importlib
import en_labels  # noqa: E402
import ko_glossary  # noqa: E402

importlib.reload(en_labels)
importlib.reload(ko_glossary)
from ko_glossary import translate  # noqa: E402

OUT = Path("variables")
CODE_SPLIT = re.compile(r"(?:(?<=^)|(?<=[\s,(]))([0-9A-Z*]{1,4}|Y|N)\s*[:：]\s*")

TABLES = [
    ("RGST", "Cancer registration", "암등록", "One registered cancer, 2012–2022.", "datasets/public-library/rgst.md"),
    ("DEATH", "Death", "사망", "One death, 2012–2023.", "datasets/public-library/death.md"),
    ("BFC", "Eligibility and premium", "자격 및 보험료", "One person in one year, 2007–2024.", "datasets/public-library/bfc.md"),
    ("T200", "Claim statement", "명세서 일반내역", "One claim, 2007–2024.", "datasets/public-library/t200.md"),
    ("T300", "Services", "진료내역", "One service line on a claim, 2007–2024.", "datasets/public-library/t300.md"),
    ("T400", "Diagnoses on the claim", "상병내역", "One diagnosis on a claim, 2007–2024.", "datasets/public-library/t400.md"),
    ("T530", "Outpatient prescriptions", "원외처방내역", "One outpatient prescription line, 2007–2024.", "datasets/public-library/t530.md"),
    ("G1E_OBJ", "Checkup target", "일반건강검진 대상자", "One person-year in the checkup target file, 2007–2024.", "datasets/public-library/g1e-obj.md"),
    ("G1Q_0708", "Checkup questionnaire, 2007–2008", "일반건강검진 문진", "One general-checkup questionnaire, 2007–2008.", "datasets/public-library/g1q-0708.md"),
    ("G1Q_0917", "Checkup questionnaire, 2009–2017", "일반건강검진 문진", "One general-checkup questionnaire, 2009–2017.", "datasets/public-library/g1q-0917.md"),
    ("G1Q_1824", "Checkup questionnaire, 2018–2024", "일반건강검진 문진", "One general-checkup questionnaire, 2018–2024.", "datasets/public-library/g1q-1824.md"),
    ("G1E", "Checkup results", "일반건강검진 결과 및 판정", "One general-checkup result, 2007–2024.", "datasets/public-library/g1e.md"),
    ("CQ_RST_0708", "Cancer screening questionnaire, 2007–2008", "암문진", "Common screening questions, 2007–2008.", "datasets/public-library/cq-rst-0708.md"),
    ("CQ_RST_0924", "Cancer screening questionnaire, 2009–2024", "암문진", "Common screening questions, 2009–2024.", "datasets/public-library/cq-rst-0924.md"),
    ("CBR_RST_0708", "Breast screening, 2007–2008", "유방암 검진", "One breast-screening record, 2007–2008.", "datasets/public-library/cbr-rst-0708.md"),
    ("CBR_RST_0924", "Breast screening, 2009–2024", "유방암 검진", "One breast-screening record, 2009–2024.", "datasets/public-library/cbr-rst-0924.md"),
    ("CCR_RST_0708", "Colorectal screening, 2007–2008", "대장암 검진", "One colorectal-screening record, 2007–2008.", "datasets/public-library/ccr-rst-0708.md"),
    ("CCR_RST_0924", "Colorectal screening, 2009–2024", "대장암 검진", "One colorectal-screening record, 2009–2024.", "datasets/public-library/ccr-rst-0924.md"),
    ("CCX_RST_0708", "Cervical screening, 2007–2008", "자궁경부암 검진", "One cervical-screening record, 2007–2008.", "datasets/public-library/ccx-rst-0708.md"),
    ("CCX_RST_0924", "Cervical screening, 2009–2024", "자궁경부암 검진", "One cervical-screening record, 2009–2024.", "datasets/public-library/ccx-rst-0924.md"),
    ("CLV_RST_0708", "Liver screening, 2007–2008", "간암 검진", "One liver-screening record, 2007–2008.", "datasets/public-library/clv-rst-0708.md"),
    ("CLV_RST_0924", "Liver screening, 2009–2024", "간암 검진", "One liver-screening record, 2009–2024.", "datasets/public-library/clv-rst-0924.md"),
    ("CST_RST_0708", "Stomach screening, 2007–2008", "위암 검진", "One stomach-screening record, 2007–2008.", "datasets/public-library/cst-rst-0708.md"),
    ("CST_RST_0924", "Stomach screening, 2009–2024", "위암 검진", "One stomach-screening record, 2009–2024.", "datasets/public-library/cst-rst-0924.md"),
    ("COVID_PT", "COVID-19 cases", "코로나19 확진자", "One confirmed case, 2020 through 31 August 2023.", "datasets/public-library/covid-pt.md"),
    ("COVID_VAC", "COVID-19 vaccination", "코로나19 예방접종", "One vaccination, 17 December 2020 through 31 August 2023.", "datasets/public-library/covid-vac.md"),
]

# Definitions the variable-item cell does not carry on its own. These follow
# the explanation section of dictionary version 4.0.
EXTRA = {
    ("RGST", "AGE"): (
        "Age in full years at the first diagnosis date. The default delivery is "
        "bands: 29 and under, five-year groups from 30 to 84, and 85 and older. "
        "A one-year age requires a research-use plan and committee approval."
    ),
    ("RGST", "TX"): (
        "Five digits for treatment within four months of diagnosis. Each digit is "
        "0 or 1, in order: surgery, chemotherapy, radiation, immunotherapy, hormone "
        "therapy. Surgery and radiation is 10100."
    ),
    ("RGST", "SEER_GRP"): (
        "SEER summary stage. A colorectal in situ code (D01.x) can also be coded 1, localized."
    ),
    ("DEATH", "SAIN1"): (
        "Underlying cause of death in the Korean Standard Classification of Diseases. "
        "Sensitive causes in chapters 1 (A00–B99), 5 (F00–F99), 19 (S00–T98), and 20 "
        "(V01–Y98) are collapsed to a block, such as V59 to V50–V59."
    ),
    ("DEATH", "SAIN2"): (
        "External-cause detail (V01–Y98) when the underlying cause is an injury code "
        "(S00–T98). The same sensitive-cause collapsing applies as for the underlying cause."
    ),
    ("BFC", "CALC_CTRB_VTILE_FD"): (
        "Premium decile from 1 to 10 among the insured population. 0 is a Medical Aid "
        "recipient. People on the same insurance card share a decile."
    ),
    ("BFC", "SIDO_CD"): "Province of residence. This is not on the cancer-registration table.",
    ("COVID_PT", "CDX_DT"): "Date the COVID-19 case was confirmed.",
    ("COVID_VAC", "VACN_YMD"): (
        "Vaccination date. If two doses fall fewer than 21 days apart, only the later dose is kept."
    ),
}


def cell(text) -> str:
    return " ".join(str(text).split()).replace("|", "\\|").replace("<", "&lt;")


def code_labels(label: str) -> tuple[str, str]:
    """Split '국한(Localized)' into the Korean text and the English already in the dictionary."""
    match = re.match(r"^(.+?)\(([^()]+)\)\s*$", label)
    if match and re.search(r"[가-힣]", match.group(1)) and re.search(r"[A-Za-z]", match.group(2)):
        return match.group(1).strip(), match.group(2).strip()
    return label, translate(label)
    return " ".join(str(text).split()).replace("|", "\\|").replace("<", "&lt;")


def parse_codes(note: str) -> tuple[str, list[tuple[str, str]]]:
    parts = CODE_SPLIT.split(note.strip())
    if len(parts) < 3:
        return note.strip(), []
    preamble = parts[0].strip(" ,;※*")
    codes = []
    pairs = iter(parts[1:])
    for code, label in zip(pairs, pairs):
        label = " ".join(label.split()).strip(" ,;")
        codes.append((code, label))
    return preamble, codes


def repair(rows: list[dict]) -> list[dict]:
    """The last stomach-screening row is split across a page. Restore it and the three that follow."""
    out = []
    for row in rows:
        if row["table"] == "CST_RST_0924" and row["name"] == "NCC_ETC":
            out.append({
                **row,
                "name": "CST_BX_NCC_ETC",
                "label_ko": "조직진단 기타_08. 직접기입",
                "note": "(2018~2024) 0: 없음, 1: 있음",
            })
            out.extend([
                {"table": "CST_RST_0924", "seq": 99, "name": "CST_JDG_CST", "label_ko": "위암종합판정",
                 "note": "1: 이상소견없음, 2: 양성질환, 3: 위암의심, 4: 위암, 5: 기타", "page": 147},
                {"table": "CST_RST_0924", "seq": 100, "name": "CST_PHX_CST", "label_ko": "기존 위암환자",
                 "note": "0: 미해당, 1: 해당", "page": 147},
                {"table": "CST_RST_0924", "seq": 101, "name": "CST_CST_FEE_YN", "label_ko": "위암진찰료포함여부",
                 "note": "0: 미포함, 1: 포함", "page": 147},
            ])
        else:
            out.append(row)
    present = {(row["table"], row["name"]) for row in out}
    extras = [
        {"table": "CCX_RST_0924", "seq": 10, "name": "CCX_JDG_CCX", "label_ko": "자궁경부암종합판정",
         "note": "(2009~2017) 1: 이상소견없음, 2: 염증성 또는 감염성 질환, 3: 상피세포 이상, 4: 자궁경부암 의심, 5: 기타 (2018~2024) 1: 이상소견없음, 2: 반응성 소견 및 감염성질환, 3: 비정형 세포이상, 4: 자궁경부암 전구단계 의심, 5: 자궁경부암 의심, 6: 기타",
         "page": 0},
        {"table": "CCX_RST_0924", "seq": 11, "name": "CCX_PHX_CCX", "label_ko": "기존 자궁경부암환자",
         "note": "0: 미해당, 1: 해당", "page": 0},
        {"table": "CCX_RST_0924", "seq": 12, "name": "CCX_CCX_FEE_YN", "label_ko": "자궁경부암 진찰료포함여부",
         "note": "0: 미포함, 1: 포함", "page": 0},
    ]
    for row in extras:
        if (row["table"], row["name"]) not in present:
            out.append(row)
    return out


def load() -> dict[str, list[dict]]:
    rows = json.loads((ROOT / "codebook" / "public-library.json").read_text(encoding="utf-8"))
    rows = repair(rows)
    by = {code: [] for code, *_ in TABLES}
    for row in rows:
        by[row["table"]].append(row)
    for code in by:
        by[code].sort(key=lambda r: r["seq"])
    return by


def render_variable(row: dict, meta: tuple) -> str:
    code, title, title_ko, _unit, _page = meta
    name = row["name"]
    label_ko = row["label_ko"]
    label_en = translate(label_ko)
    preamble, codes = parse_codes(row["note"])
    extra = EXTRA.get((code, name))
    lines = [
        f"[Variables](../../index.md) · [{title}](../{code.lower()}.md)",
        "",
        f"# {name}",
        "",
        f"**{cell(label_ko)}** · {cell(label_en)}",
        "",
        f"- **Dataset** Cancer Public Library (암 공공 라이브러리)",
        f"- **Table** {title} · {title_ko}",
        f"- **File** `{code}`",
        "",
        "## Definition",
        "",
    ]
    if extra:
        lines += [extra, ""]
    elif preamble:
        lines += [cell(translate(preamble)), ""]
    elif not codes:
        lines += [cell(translate(row["note"]) or "See the dictionary note."), ""]
    else:
        lines += [f"{cell(label_en)}.", ""]
    if codes:
        lines += ["## Codes", "", "| Code | 한글 | English |", "|---|---|---|"]
        for value, label in codes:
            ko, en = code_labels(label)
            lines.append(f"| `{cell(value)}` | {cell(ko)} | {cell(en)} |")
        lines.append("")
    lines += [
        "## Dictionary note",
        "",
        cell(row["note"]),
        "",
        "The Korean note is the text in data dictionary version 4.0. The English is a translation for this site.",
        "",
    ]
    return "\n".join(lines)


GROUPS = [
    ("Cancer registration, death, and eligibility", ["RGST", "DEATH", "BFC"]),
    ("Claims", ["T200", "T300", "T400", "T530"]),
    ("General health examination", ["G1E_OBJ", "G1Q_0708", "G1Q_0917", "G1Q_1824", "G1E"]),
    ("Cancer screening", [
        "CQ_RST_0708", "CQ_RST_0924", "CBR_RST_0708", "CBR_RST_0924",
        "CCR_RST_0708", "CCR_RST_0924", "CCX_RST_0708", "CCX_RST_0924",
        "CLV_RST_0708", "CLV_RST_0924", "CST_RST_0708", "CST_RST_0924",
    ]),
    ("COVID-19", ["COVID_PT", "COVID_VAC"]),
]


CLAIMS = {"T200", "T300", "T400", "T530"}


def render_sn_key(meta: tuple) -> str:
    code, title, title_ko, _unit, _page = meta
    lines = [
        "---",
        'title: "SN_KEY"',
        "---",
        "",
        f"[Variables](../../index.md) · [{title}](../{code.lower()}.md)",
        "",
        "# SN_KEY",
        "",
        "**대체식별키** · Person identifier",
        "",
        "- **Dataset** Cancer Public Library (암 공공 라이브러리)",
        f"- **Table** {title} · {title_ko}",
        f"- **File** `{code}`",
        "",
        "## Definition",
        "",
        "Person identifier. This substitute identifier links a row in this table "
        "to the same person in the other Cancer Public Library tables.",
        "",
        "Data dictionary version 4.0, section 10, says the whole file from the five institutions "
        "is linked by `SN_KEY` (대체식별키).",
        "",
    ]
    if code in CLAIMS:
        lines += [
            "Lines of the same claim also join `T200`, `T300`, `T400`, and `T530` on `MID` (명세서조인키).",
            "",
        ]
    if code == "RGST":
        lines += [
            "One person can have more than one cancer-registration row. Those rows share an `SN_KEY`.",
            "",
        ]
    lines += [
        "The quality-control section says each table's substitute identifier is replaced with a new serial number "
        "every time the data are extracted. An `SN_KEY` from one extract does not identify the same person in another extract.",
        "",
    ]
    return "\n".join(lines)


def render_cooperative_staging() -> str:
    rows = [
        ("T_SIZE", "종양의 크기", "Size of the primary tumor, maximum length or diameter"),
        ("EXT", "종양이 퍼진 정도", "Extension of the tumor"),
        ("EXTEVAL", "종양의 크기와 퍼진 정도의 결정 방법", "How size and extension were determined"),
        ("NODES", "침범된 국소림프절", "Regional nodes involved, and the kind and extent of involvement"),
        ("LNPOS", "양성 국소림프절의 개수", "Number of regional nodes positive on pathology"),
        ("LNEXAM", "검사된 국소림프절의 총 개수", "Number of regional nodes examined"),
        ("NODESEVAL", "국소림프절 침범 여부의 결정 방법", "How node involvement was determined"),
        ("METS", "원격전이 부위", "Site of distant metastasis"),
        ("METSEVAL", "원격전이 부위의 결정 방법", "How the metastatic site was determined"),
        ("GRADE", "분화도", "Grade"),
        ("ajcc7_t", "Derived AJCC-7 T", "Derived AJCC 7th edition T"),
        ("ajcc7_n", "Derived AJCC-7 N", "Derived AJCC 7th edition N"),
        ("ajcc7_m", "Derived AJCC-7 M", "Derived AJCC 7th edition M"),
        ("AJCC7_STAGE", "Derived AJCC-7 Stage Grp", "Derived AJCC 7th edition stage group"),
        ("SS2000", "Summary Stage 2000", "Summary Stage 2000"),
        ("AGE", "만 나이", "Age in full years"),
        ("fdx", "초진연월", "Year and month of the first visit, YYYYMM"),
        ("SEX", "성별", "Sex"),
        ("TCODE", "원발부위 코드", "Primary site code"),
        ("MCODE", "조직학적진단명 코드", "Histology code"),
        ("dbyear", "자료등록년도", "Year the record was registered"),
    ]
    lines = [
        "---",
        'title: "Cooperative staging"',
        "---",
        "",
        "[Variables](../index.md)",
        "",
        "# Cooperative staging",
        "",
        "These items are the extra cancer detail on a cooperative-staging sample (협력병기연계 DB). "
        "They are not variables on the customized extract. "
        "A 20 percent site sample uses the same tables as the customized library and does not add this file.",
        "",
        "The names are the output items of the Korea Central Cancer Registry cooperative-staging survey, "
        "as published for stomach cancer. That description says the survey covers stomach, colon, rectum, and breast. "
        "The K-CURE portal also lists liver and lung staging samples. "
        "The sample dictionary version 3.0, announced on 19 June 2025, is the list of columns in a delivered file. "
        "That manual is not among the files this site was built from, so value codes are not repeated here.",
        "",
        "Which samples exist, and for which years, is on the [sample page](../../datasets/public-library/sample.md).",
        "",
        "## Size, nodes, metastasis, and grade",
        "",
        "| Variable | 한글 | English |",
        "|---|---|---|",
    ]
    for name, ko, en in rows:
        lines.append(f"| `{name}` | {ko} | {en} |")
    lines += [
        "",
        "The same survey list also includes derived AJCC 6th edition T, N, M, and stage, "
        "the evaluation flags for those components, a schema number (`SCHEMANO`), "
        "a survey serial number (`SERIAL`), and site-specific factors `SSF1` through `SSF25`.",
        "",
        "## Year of birth",
        "",
        "Year of birth is not an item on this list, and it is not a variable in public-library dictionary version 4.0. "
        "What the registry table carries is `AGE` (진단시 만나이), age in full years at diagnosis, "
        "and `FDX` (최초진단연월일), the date of first diagnosis. "
        "In the customized file, `AGE` is delivered in five-year bands. "
        "A one-year age requires a research-use plan and committee approval. "
        "The survey list has its own `AGE` (만 나이) and `fdx` (초진연월), the year and month of the first visit.",
        "",
        "??? info \"Sources\"",
        "    The item names follow the [stomach cooperative-staging survey](https://www.data.go.kr/data/15058009/openapi.do) "
        "on the public data portal, updated 29 May 2025. "
        "The survey's own description there names stomach, colon, rectum, and breast. "
        "The K-CURE sample list is on the [library overview](https://k-cure.mohw.go.kr/portal/dit/lit/inf/viewDitLitInf.do). "
        "Age banding on `RGST` follows dictionary version 4.0, Table 1.",
        "",
    ]
    return "\n".join(lines)


def render_dataset(meta: tuple, rows: list[dict]) -> str:
    code, title, title_ko, unit, page = meta
    lines = [
        "---",
        f"title: \"{title}\"",
        "---",
        "",
        "[Variables](../index.md)",
        "",
        f"# {title}",
        "",
        f"{title_ko}. File `{code}`. {unit}",
        "",
        f"How the table is defined is on its [dataset page](../../{page}). "
        "Select a variable to see its definition and the meaning of each code.",
        "",
    ]
    if code in {"CQ_RST_0708", "CQ_RST_0924"}:
        suffix = "0708" if code.endswith("0708") else "0924"
        lines += [
            "Dictionary version 4.0 prints this questionnaire once. "
            "The portal catalog delivers it as a separate file for each screening site, "
            f"with the same variables: `CBR_CQ_RST_{suffix}`, `CCR_CQ_RST_{suffix}`, "
            f"`CCX_CQ_RST_{suffix}`, `CLV_CQ_RST_{suffix}`, and `CST_CQ_RST_{suffix}`.",
            "",
        ]
    lines += [
        "| Variable | 한글 | English |",
        "|---|---|---|",
        f"| [`SN_KEY`]({code.lower()}/sn_key.md) | 대체식별키 | Person identifier |",
    ]
    for row in rows:
        lines.append(
            f"| [`{row['name']}`]({code.lower()}/{row['name'].lower()}.md) | {cell(row['label_ko'])} | {cell(translate(row['label_ko']))} |"
        )
    lines.append("")
    return "\n".join(lines)


# Left-hand menu, in the same order and with the same labels as the Datasets page.
# The first three titles stay without a file code. Nested items keep the file code,
# matching the Datasets menu.
SIDEBAR = [
    (None, "RGST", "Cancer registration"),
    (None, "DEATH", "Death"),
    (None, "BFC", "Eligibility and premium"),
    ("Claims", "T200", "Claim statement (T200)"),
    ("Claims", "T300", "Services (T300)"),
    ("Claims", "T400", "Diagnoses (T400)"),
    ("Claims", "T530", "Outpatient prescriptions (T530)"),
    ("General health examination", "G1E_OBJ", "Checkup target (G1E_OBJ)"),
    ("General health examination", "G1Q_0708", "Questionnaire, 2007–2008 (G1Q_0708)"),
    ("General health examination", "G1Q_0917", "Questionnaire, 2009–2017 (G1Q_0917)"),
    ("General health examination", "G1Q_1824", "Questionnaire, 2018–2024 (G1Q_1824)"),
    ("General health examination", "G1E", "Results (G1E)"),
    ("Cancer screening", "CQ_RST_0708", "Questionnaire, 2007–2008 (CQ_RST_0708)"),
    ("Cancer screening", "CQ_RST_0924", "Questionnaire, 2009–2024 (CQ_RST_0924)"),
    ("Cancer screening", "CBR_RST_0708", "Breast, 2007–2008 (CBR_RST_0708)"),
    ("Cancer screening", "CBR_RST_0924", "Breast, 2009–2024 (CBR_RST_0924)"),
    ("Cancer screening", "CCR_RST_0708", "Colorectal, 2007–2008 (CCR_RST_0708)"),
    ("Cancer screening", "CCR_RST_0924", "Colorectal, 2009–2024 (CCR_RST_0924)"),
    ("Cancer screening", "CCX_RST_0708", "Cervical, 2007–2008 (CCX_RST_0708)"),
    ("Cancer screening", "CCX_RST_0924", "Cervical, 2009–2024 (CCX_RST_0924)"),
    ("Cancer screening", "CLV_RST_0708", "Liver, 2007–2008 (CLV_RST_0708)"),
    ("Cancer screening", "CLV_RST_0924", "Liver, 2009–2024 (CLV_RST_0924)"),
    ("Cancer screening", "CST_RST_0708", "Stomach, 2007–2008 (CST_RST_0708)"),
    ("Cancer screening", "CST_RST_0924", "Stomach, 2009–2024 (CST_RST_0924)"),
    ("COVID-19", "COVID_PT", "Cases (COVID_PT)"),
    ("COVID-19", "COVID_VAC", "Vaccination (COVID_VAC)"),
]


def render_index(by: dict[str, list[dict]], *, title: str, link_prefix: str, library_href: str) -> str:
    meta_by = {meta[0]: meta for meta in TABLES}
    lines = [
        f"# {title}",
        "",
        "These are the datasets in the Cancer Public Library (암 공공 라이브러리). "
        "Select a dataset to see its variables. Open a variable to see the definition and the meaning of each code.",
        "",
        "English names and code meanings are translations for this site. "
        "The Korean dictionary note on each variable page is the text of data dictionary version 4.0 (September 2026).",
        "",
        "Each list begins with [`SN_KEY`]("
        f"{link_prefix}rgst/sn_key.md) (대체식별키), the person identifier. "
        "The four claims tables also join to each other on `MID` (명세서조인키).",
        "",
        f"Who is included in the library is on the [library page]({library_href}). "
        "A site sample (표본) and a staging sample (표본 병기) are separate databases, "
        "with their own variable lists.",
        "",
    ]
    for heading, codes in GROUPS:
        lines += [f"## {heading}", ""]
        for code in codes:
            _code, label, title_ko, _unit, _page = meta_by[code]
            n = len(by[code]) + 1
            noun = "variable" if n == 1 else "variables"
            lines.append(
                f"- [{label}]({link_prefix}{code.lower()}.md) · {title_ko} · `{code}` · {n} {noun}"
            )
        lines.append("")
    return "\n".join(lines)


def build_nav() -> mkdocs_gen_files.Nav:
    missing = [meta[0] for meta in TABLES if meta[0] not in {code for _group, code, _label in SIDEBAR}]
    if missing:
        raise SystemExit(f"Sidebar is missing datasets: {', '.join(missing)}")
    nav = mkdocs_gen_files.Nav()
    nav["Variables"] = "index.md"
    nav["Cancer Public Library"] = "public-library/index.md"
    for group, code, label in SIDEBAR:
        key = ("Cancer Public Library", label) if group is None else ("Cancer Public Library", group, label)
        nav[key] = f"public-library/{code.lower()}.md"
    return nav


def main() -> None:
    by = load()
    nav = build_nav()

    with mkdocs_gen_files.open(OUT / "index.md", "w", encoding="utf-8") as f:
        f.write(render_index(
            by,
            title="Variables",
            link_prefix="public-library/",
            library_href="../datasets/public-library/index.md",
        ))
        import gen_samples
        f.write(gen_samples.write_catalogs(
            nav, translate, cell, code_labels, mkdocs_gen_files, OUT,
        ))
    mkdocs_gen_files.set_edit_path(OUT / "index.md", Path("../codebook/public-library.json"))

    library_index = OUT / "public-library" / "index.md"
    with mkdocs_gen_files.open(library_index, "w", encoding="utf-8") as f:
        f.write(render_index(
            by,
            title="Cancer Public Library",
            link_prefix="",
            library_href="../../datasets/public-library/index.md",
        ))
    mkdocs_gen_files.set_edit_path(library_index, Path("../codebook/public-library.json"))

    for meta in TABLES:
        code = meta[0]
        dataset_path = OUT / "public-library" / f"{code.lower()}.md"
        with mkdocs_gen_files.open(dataset_path, "w", encoding="utf-8") as f:
            f.write(render_dataset(meta, by[code]))
        mkdocs_gen_files.set_edit_path(dataset_path, Path("../codebook/public-library.json"))
        sn_key_path = OUT / "public-library" / code.lower() / "sn_key.md"
        with mkdocs_gen_files.open(sn_key_path, "w", encoding="utf-8") as f:
            f.write(render_sn_key(meta))
        mkdocs_gen_files.set_edit_path(sn_key_path, Path("../codebook/public-library.json"))
        for row in by[code]:
            path = OUT / "public-library" / code.lower() / f"{row['name'].lower()}.md"
            with mkdocs_gen_files.open(path, "w", encoding="utf-8") as f:
                f.write(render_variable(row, meta))
            mkdocs_gen_files.set_edit_path(path, Path("../codebook/public-library.json"))

    with mkdocs_gen_files.open(OUT / "SUMMARY.md", "w", encoding="utf-8") as f:
        f.writelines(nav.build_literate_nav())


main()
