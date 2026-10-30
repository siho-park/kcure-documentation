# -*- coding: utf-8 -*-
"""Variable pages for the portal's site-sample and staging-sample catalogs."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "codebook" / "catalogs.json"

_HANGUL = re.compile(r"[가-힣]")
_PREFIX = re.compile(r"^(?:SMPL|CS)_[A-Z]{2}_(.+)$")
_CQ = re.compile(r"^([A-Z]+)_CQ_RST_(\d+)$")
_RST = re.compile(r"^([A-Z]+)_RST_(\d+)$")

SITES = {
    "CBR": "Breast",
    "CCR": "Colorectal",
    "CCX": "Cervical",
    "CLV": "Liver",
    "CST": "Stomach",
}
CORE = {
    "RGST": "Cancer registration",
    "DEATH": "Death",
    "BFC": "Eligibility and premium",
    "T200": "Claim statement",
    "T300": "Services",
    "T400": "Diagnoses",
    "T530": "Outpatient prescriptions",
    "G1E_OBJ": "Checkup target",
    "G1Q_0708": "Checkup questionnaire, 2007–2008",
    "G1Q_0917": "Checkup questionnaire, 2009–2017",
    "G1Q_1823": "Checkup questionnaire, 2018–2023",
    "G1E": "Checkup results",
}


def logical_name(code: str) -> str:
    match = _PREFIX.match(code)
    return match.group(1) if match else code


def table_title(code: str) -> str:
    logical = logical_name(code)
    if logical in CORE:
        return CORE[logical]
    match = _CQ.match(logical)
    if match:
        site = SITES.get(match.group(1), match.group(1))
        years = "2007–2008" if match.group(2) == "0708" else "2009–2023"
        return f"{site} screening questionnaire, {years}"
    match = _RST.match(logical)
    if match:
        site = SITES.get(match.group(1), match.group(1))
        years = "2007–2008" if match.group(2) == "0708" else "2009–2023"
        return f"{site} screening results, {years}"
    return logical


def _english(text: str, translate) -> str:
    gloss = translate(text) if text else ""
    if gloss and not _HANGUL.search(gloss):
        return gloss
    return ""


def _year_sentence(codes: list[dict]) -> str:
    starts = {c["start"] for c in codes if c.get("start")}
    ends = {c["end"] for c in codes if c.get("end")}
    if len(starts) == 1 and len(ends) == 1:
        return f"The catalog records these codes as valid from {next(iter(starts))} through {next(iter(ends))}."
    return ""


def render_variable(product: dict, table: dict, var: dict, translate, cell, code_labels) -> str:
    kind_ko = "표본" if product["kind"] == "sample" else "표본 병기"
    heading = "sample" if product["kind"] == "sample" else "staging sample"
    label_en = _english(var["label_ko"], translate)
    note_en = _english(var["note"], translate) if var["note"] and var["note"] != var["label_ko"] else ""
    lines = [
        "---",
        f'title: "{var["name"]}"',
        "---",
        "",
        f"[Variables](../../../index.md) · [{product['title']} {heading}](../../{product['slug']}.md)",
        "",
        f"# {var['name']}",
        "",
        f"**{cell(var['label_ko'])}**" + (f" · {cell(label_en)}" if label_en else ""),
        "",
        f"- **Dataset** {product['title']} {heading} ({product['title_ko']})",
        f"- **Table** {table_title(table['code'])} · {cell(table['title_ko'])}",
        f"- **File** `{table['code']}`",
    ]
    if var.get("dtype"):
        lines.append(f"- **Type** `{cell(var['dtype'])}`")
    lines += ["", "## Definition", ""]
    if note_en:
        lines += [note_en, ""]
    elif label_en:
        lines += [f"{cell(label_en)}.", ""]
    else:
        lines += [cell(var["label_ko"]), ""]
    codes = var.get("codes") or []
    if codes:
        years_differ = len({(c.get("start"), c.get("end")) for c in codes}) > 1
        header = "| Code | 한글 | English | Years |" if years_differ else "| Code | 한글 | English |"
        rule = "|---|---|---|---|" if years_differ else "|---|---|---|"
        lines += ["## Codes", "", header, rule]
        for code in codes:
            ko, en = code_labels(code["label"])
            if _HANGUL.search(en):
                en = ""
            row = f"| `{cell(code['value'])}` | {cell(ko)} | {cell(en)} |"
            if years_differ:
                row = f"| `{cell(code['value'])}` | {cell(ko)} | {cell(en)} | {cell(code.get('start', ''))}–{cell(code.get('end', ''))} |"
            lines.append(row)
        lines.append("")
        sentence = _year_sentence(codes)
        if sentence and not years_differ:
            lines += [sentence, ""]
    lines += ["## Catalog note", ""]
    note = var["note"] or var["label_ko"]
    lines.append(cell(note))
    if var.get("value") and var["value"] != note:
        lines += ["", cell(var["value"])]
    lines += [
        "",
        f"The Korean text is from the portal data catalog for this {kind_ko} database, "
        f"downloaded 30 October 2026 (`{product['source_file']}`). "
        "The English is a translation for this site. "
        "The catalog says that code values beyond this sheet are on the Health Insurance Review and Assessment Service open-data system.",
        "",
    ]
    return "\n".join(lines)


def render_product(product: dict, translate, cell) -> str:
    heading = "sample" if product["kind"] == "sample" else "staging sample"
    other_kind = "staging" if product["kind"] == "sample" else "sample"
    other_heading = "staging sample" if other_kind == "staging" else "sample"
    nvars = sum(len(table["variables"]) for table in product["tables"])
    lines = [
        "---",
        f'title: "{product["title"]} {heading}"',
        "---",
        "",
        "[Variables](../index.md)",
        "",
        f"# {product['title']} {heading}",
        "",
        f"{product['title_ko']}. {len(product['tables'])} tables, {nvars} variables in the portal catalog.",
        "",
    ]
    if product["kind"] == "sample":
        lines += [
            "This is a site sample (표본). It is its own database: one cancer site, with the tables listed below. "
            f"The [staging sample](../staging/{product['slug']}.md) of the same site, where the catalog has one, is a separate database. "
            "How the two differ is on the [sample page](../../datasets/public-library/sample.md).",
            "",
            "The registration table keeps summary stage (`SEER_GRP`) and the histology code `MCODE`. "
            "Death, eligibility, claims, and the checkup use the same kind of row as the customized library, with fewer columns. "
            "There is no COVID-19 table. A screening table appears here only for a site the catalog includes, and only for this site. "
            "The checkup and screening year files in this catalog run through 2023.",
            "",
            "Year of birth is not a variable. `AGE` is age at diagnosis.",
            "",
        ]
    else:
        lines += [
            "This is a staging sample (표본 병기). 병기 means stage. "
            f"It is a separate database from the [site sample](../sample/{product['slug']}.md). "
            "Death, eligibility, claims, the checkup, and screening, where this catalog includes them, match the site sample. "
            "The registration table is the staging-survey record for this site. "
            "How the two databases differ is on the [sample page](../../datasets/public-library/sample.md).",
            "",
            "`DBYEAR` (자료등록연도) is the year the record was registered. It is not the year of birth. "
            "`AGE` is age at diagnosis. `FDX` on this table is the year and month of the first diagnosis.",
            "",
        ]
    if product.get("banner"):
        lines += [cell(product["banner"]), ""]
    if product.get("code_start_min") and product.get("code_end_max"):
        lines += [
            f"On the code sheet, recorded validity runs from {product['code_start_min']} through {product['code_end_max']}.",
            "",
        ]
    lines += [
        "The catalog does not list `SN_KEY`. Claim lines list `MID`.",
        "",
    ]
    for table in product["tables"]:
        lines += [
            f"## {table_title(table['code'])}",
            "",
            f"{cell(table['title_ko'])}. File `{table['code']}`.",
            "",
            "| Variable | 한글 | English |",
            "|---|---|---|",
        ]
        for var in table["variables"]:
            label_en = _english(var["label_ko"], translate)
            href = f"{product['slug']}/{table['code'].lower()}/{var['name'].lower()}.md"
            lines.append(
                f"| [`{var['name']}`]({href}) | {cell(var['label_ko'])} | {cell(label_en)} |"
            )
        lines.append("")
    return "\n".join(lines)


def write_catalogs(nav, translate, cell, code_labels, mkdocs_gen_files, out: Path) -> str:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    products = data["products"]
    # Drop a staging link from a site sample when that site has no staging catalog.
    staging_slugs = {p["slug"] for p in products if p["kind"] == "staging"}
    index_lines = [
        "## Site samples (표본) {#site-samples}",
        "",
        "Each of these is its own database, a fraction of one cancer site. "
        "The variable list is the portal catalog, not the customized-library dictionary. "
        "A [staging sample](staging/stomach.md) is a separate database. "
        "The difference is on the [sample page](../datasets/public-library/sample.md).",
        "",
    ]
    for product in products:
        if product["kind"] != "sample":
            continue
        nvars = sum(len(table["variables"]) for table in product["tables"])
        index_lines.append(
            f"- [{product['title']} sample](sample/{product['slug']}.md) · {product['title_ko']} · {len(product['tables'])} tables · {nvars} variables"
        )
    index_lines += [
        "",
        "## Staging samples (표본 병기) {#staging-samples}",
        "",
        "병기 means stage. Each staging sample is a separate database from the site sample of the same cancer. "
        "The registration table carries that site's stage items.",
        "",
    ]
    for product in products:
        if product["kind"] != "staging":
            continue
        nvars = sum(len(table["variables"]) for table in product["tables"])
        index_lines.append(
            f"- [{product['title']} staging sample](staging/{product['slug']}.md) · {product['title_ko']} · {len(product['tables'])} tables · {nvars} variables"
        )
    index_lines.append("")

    for product in products:
        group = "Site samples (표본)" if product["kind"] == "sample" else "Staging samples (표본 병기)"
        label = product["title"]
        folder = "sample" if product["kind"] == "sample" else "staging"
        nav[(group, label)] = f"{folder}/{product['slug']}.md"
        page = out / folder / f"{product['slug']}.md"
        text = render_product(product, translate, cell)
        if product["kind"] == "sample" and product["slug"] not in staging_slugs:
            text = text.replace(
                f"The [staging sample](../staging/{product['slug']}.md) of the same site, where the catalog has one, is a separate database. ",
                "The catalog has no staging sample for this site. ",
            )
        with mkdocs_gen_files.open(page, "w", encoding="utf-8") as handle:
            handle.write(text)
        mkdocs_gen_files.set_edit_path(page, Path("../codebook/catalogs.json"))
        for table in product["tables"]:
            for var in table["variables"]:
                path = out / folder / product["slug"] / table["code"].lower() / f"{var['name'].lower()}.md"
                with mkdocs_gen_files.open(path, "w", encoding="utf-8") as handle:
                    handle.write(render_variable(product, table, var, translate, cell, code_labels))
                mkdocs_gen_files.set_edit_path(path, Path("../codebook/catalogs.json"))
    return "\n".join(index_lines)
