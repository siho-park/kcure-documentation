"""Keep the dataset menu active on a variable page.

Variable pages are not listed in the sidebar. While one is open, mark its
dataset as the current item so the left-hand menu stays on Variables and
highlights that dataset.
"""
from __future__ import annotations

_marked: list = []


def _walk(items):
    for item in items:
        yield item
        children = getattr(item, "children", None)
        if children:
            yield from _walk(children)


def on_page_context(context, page, config, nav):
    del config
    _marked.clear()
    src = page.file.src_uri.replace("\\", "/")
    parts = src.split("/")
    dataset_src = None
    if len(parts) == 4 and parts[0] == "variables" and parts[1] == "public-library" and parts[3] != "index.md":
        dataset_src = f"variables/public-library/{parts[2]}.md"
    elif len(parts) == 5 and parts[0] == "variables" and parts[1] in {"sample", "staging"}:
        dataset_src = f"variables/{parts[1]}/{parts[2]}.md"
    if dataset_src is None:
        return context
    for item in _walk(nav.items):
        file = getattr(item, "file", None)
        if file is not None and file.src_uri.replace("\\", "/") == dataset_src:
            item.active = True
            _marked.append(item)
            break
    return context


def on_post_page(output, page, config):
    del page, config
    while _marked:
        _marked.pop().active = False
    return output
