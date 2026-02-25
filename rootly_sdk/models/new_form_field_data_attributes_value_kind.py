from typing import Literal, cast

NewFormFieldDataAttributesValueKind = Literal[
    "catalog_entity", "cause", "environment", "functionality", "group", "incident_type", "inherit", "service", "user"
]

NEW_FORM_FIELD_DATA_ATTRIBUTES_VALUE_KIND_VALUES: set[NewFormFieldDataAttributesValueKind] = {
    "catalog_entity",
    "cause",
    "environment",
    "functionality",
    "group",
    "incident_type",
    "inherit",
    "service",
    "user",
}


def check_new_form_field_data_attributes_value_kind(value: str | None) -> NewFormFieldDataAttributesValueKind | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_DATA_ATTRIBUTES_VALUE_KIND_VALUES:
        return cast(NewFormFieldDataAttributesValueKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_DATA_ATTRIBUTES_VALUE_KIND_VALUES!r}")
