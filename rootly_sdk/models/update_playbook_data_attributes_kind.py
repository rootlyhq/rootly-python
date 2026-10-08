from typing import Literal

UpdatePlaybookDataAttributesKind = Literal["external_url", "internal_document"]

UPDATE_PLAYBOOK_DATA_ATTRIBUTES_KIND_VALUES: set[UpdatePlaybookDataAttributesKind] = {
    "external_url",
    "internal_document",
}


def check_update_playbook_data_attributes_kind(value: str | None) -> UpdatePlaybookDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_PLAYBOOK_DATA_ATTRIBUTES_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PLAYBOOK_DATA_ATTRIBUTES_KIND_VALUES!r}")
