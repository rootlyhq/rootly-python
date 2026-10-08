from typing import Literal

CustomFieldResourceType = Literal["incident", "problem"]

CUSTOM_FIELD_RESOURCE_TYPE_VALUES: set[CustomFieldResourceType] = {
    "incident",
    "problem",
}


def check_custom_field_resource_type(value: str | None) -> CustomFieldResourceType | None:
    if value is None:
        return None
    if value in CUSTOM_FIELD_RESOURCE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_RESOURCE_TYPE_VALUES!r}")
