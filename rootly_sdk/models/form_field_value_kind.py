from typing import Literal, cast

FormFieldValueKind = Literal[
    "catalog_entity", "cause", "environment", "functionality", "group", "incident_type", "inherit", "service", "user"
]

FORM_FIELD_VALUE_KIND_VALUES: set[FormFieldValueKind] = {
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


def check_form_field_value_kind(value: str | None) -> FormFieldValueKind | None:
    if value is None:
        return None
    if value in FORM_FIELD_VALUE_KIND_VALUES:
        return cast(FormFieldValueKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_VALUE_KIND_VALUES!r}")
