# -*- coding: utf-8 -*-
"""Read the portal catalog workbooks into codebook/catalogs.json."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATABASE = ROOT / "database"
OUT = ROOT / "codebook" / "catalogs.json"

PRODUCTS = [
    ("sample", "stomach", "Stomach", "위암 표본", "*표본_위암_*.xlsx"),
    ("sample", "breast", "Breast", "유방암 표본", "*표본_유방암_*.xlsx"),
    ("sample", "colorectal", "Colorectal", "대장암 표본", "*표본_대장암_*.xlsx"),
    ("sample", "liver", "Liver", "간암 표본", "*표본_간암_*.xlsx"),
    ("sample", "lung", "Lung", "폐암 표본", "*표본_폐암_*.xlsx"),
    ("sample", "pancreas", "Pancreas", "췌장암 표본", "*표본_췌장암_*.xlsx"),
    ("staging", "stomach", "Stomach", "위암 표본 병기", "*표본_병기_위암*.xlsx"),
    ("staging", "breast", "Breast", "유방암 표본 병기", "*표본_병기_유방암*.xlsx"),
    ("staging", "colorectal", "Colorectal", "대장암 표본 병기", "*표본_병기_대장암*.xlsx"),
    ("staging", "liver", "Liver", "간암 표본 병기", "*표본_병기_간암*.xlsx"),
    ("staging", "lung", "Lung", "폐암 표본 병기", "*표본_병기_폐암*.xlsx"),
]


def _clean(value) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    return " ".join(str(value).split())


def _header_row(path: Path, sheet: int) -> tuple[int, str]:
    raw = pd.read_excel(path, sheet_name=sheet, header=None, nrows=6)
    banner = ""
    header = 3
    for i in range(min(4, len(raw))):
        text = _clean(raw.iloc[i, 0])
        if text.startswith("※ 상세코드"):
            banner = text
            header = 4
    return header, banner


def _load_variables(path: Path) -> tuple[list[dict], str]:
    header, banner = _header_row(path, 1)
    df = pd.read_excel(path, sheet_name=1, header=header)
    df.columns = [_clean(c) for c in df.columns]
    name_col = next(c for c in df.columns if "변수명" in c)
    label_col = next(c for c in df.columns if "컬럼한글" in c)
    table_col = next(c for c in df.columns if c.startswith("데이터셋명(테이블명)"))
    ko_col = next(c for c in df.columns if "테이블 한글명" in c or c.startswith("데이터셋명(테이블 한글명)"))
    note_col = "설명" if "설명" in df.columns else None
    value_col = "값" if "값" in df.columns else None
    dtype_col = next((c for c in df.columns if "Data Type" in c or c.startswith("형식")), None)
    sub_col = "SUB NO" if "SUB NO" in df.columns else None
    tables: list[dict] = []
    current = None
    for _, row in df.iterrows():
        code = _clean(row[table_col])
        name = _clean(row[name_col])
        if not code or not name or name == "nan":
            continue
        if current is None or current["code"] != code:
            current = {"code": code, "title_ko": _clean(row[ko_col]), "variables": []}
            tables.append(current)
        current["variables"].append({
            "seq": _clean(row[sub_col]) if sub_col else "",
            "name": name,
            "label_ko": _clean(row[label_col]),
            "note": _clean(row[note_col]) if note_col else "",
            "value": _clean(row[value_col]) if value_col else "",
            "dtype": _clean(row[dtype_col]) if dtype_col else "",
        })
    return tables, banner


def _load_codes(path: Path) -> dict[tuple[str, str], list[dict]]:
    header, _banner = _header_row(path, 2)
    df = pd.read_excel(path, sheet_name=2, header=header)
    df.columns = [_clean(c) for c in df.columns]
    out: dict[tuple[str, str], list[dict]] = {}
    for _, row in df.iterrows():
        table = _clean(row.iloc[0])
        name = _clean(row.iloc[1])
        value = _clean(row.iloc[3])
        label = _clean(row.iloc[4])
        if not table or not name or not value:
            continue
        out.setdefault((table, name), []).append({
            "value": value,
            "label": label,
            "start": _clean(row.iloc[6]),
            "end": _clean(row.iloc[7]),
        })
    return out


def main() -> None:
    products = []
    for kind, slug, title, title_ko, pattern in PRODUCTS:
        path = next(DATABASE.glob(pattern))
        tables, banner = _load_variables(path)
        codes = _load_codes(path)
        starts, ends = [], []
        for table in tables:
            for var in table["variables"]:
                var["codes"] = codes.get((table["code"], var["name"]), [])
                for code in var["codes"]:
                    if code["start"].isdigit():
                        starts.append(int(code["start"]))
                    if code["end"].isdigit():
                        ends.append(int(code["end"]))
        nvars = sum(len(t["variables"]) for t in tables)
        products.append({
            "kind": kind,
            "slug": slug,
            "title": title,
            "title_ko": title_ko,
            "source_file": path.name,
            "banner": banner,
            "code_start_min": min(starts) if starts else None,
            "code_end_max": max(ends) if ends else None,
            "tables": tables,
        })
        print(f"{kind:8} {slug:12} tables {len(tables):2} vars {nvars:4} codes {sum(len(v['codes']) for t in tables for v in t['variables']):5} years {min(starts) if starts else '-'}–{max(ends) if ends else '-'}  {path.name}")
    OUT.write_text(json.dumps({"products": products}, ensure_ascii=False), encoding="utf-8")
    print("wrote", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
