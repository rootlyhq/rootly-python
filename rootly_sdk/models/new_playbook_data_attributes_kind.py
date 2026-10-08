from typing import Literal

NewPlaybookDataAttributesKind = Literal["external_url", "internal_document"]

NEW_PLAYBOOK_DATA_ATTRIBUTES_KIND_VALUES: set[NewPlaybookDataAttributesKind] = {
    "external_url",
    "internal_document",
}


def check_new_playbook_data_attributes_kind(value: str | None) -> NewPlaybookDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_PLAYBOOK_DATA_ATTRIBUTES_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_PLAYBOOK_DATA_ATTRIBUTES_KIND_VALUES!r}")
