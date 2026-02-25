from typing import Literal, cast

UpdateFormFieldDataAttributesValueKind = Literal[
    "catalog_entity", "cause", "environment", "functionality", "group", "incident_type", "inherit", "service", "user"
]

UPDATE_FORM_FIELD_DATA_ATTRIBUTES_VALUE_KIND_VALUES: set[UpdateFormFieldDataAttributesValueKind] = {
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


def check_update_form_field_data_attributes_value_kind(
    value: str | None,
) -> UpdateFormFieldDataAttributesValueKind | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_DATA_ATTRIBUTES_VALUE_KIND_VALUES:
        return cast(UpdateFormFieldDataAttributesValueKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_DATA_ATTRIBUTES_VALUE_KIND_VALUES!r}"
    )
