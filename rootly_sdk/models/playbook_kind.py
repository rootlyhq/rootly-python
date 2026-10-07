from typing import Literal

PlaybookKind = Literal["external_url", "internal_document"]

PLAYBOOK_KIND_VALUES: set[PlaybookKind] = {
    "external_url",
    "internal_document",
}


def check_playbook_kind(value: str | None) -> PlaybookKind | None:
    if value is None:
        return None
    if value in PLAYBOOK_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_KIND_VALUES!r}")
