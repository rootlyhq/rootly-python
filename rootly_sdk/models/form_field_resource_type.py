from typing import Literal, cast

FormFieldResourceType = Literal["incident", "problem"]

FORM_FIELD_RESOURCE_TYPE_VALUES: set[FormFieldResourceType] = {
    "incident",
    "problem",
}


def check_form_field_resource_type(value: str | None) -> FormFieldResourceType | None:
    if value is None:
        return None
    if value in FORM_FIELD_RESOURCE_TYPE_VALUES:
        return cast(FormFieldResourceType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_RESOURCE_TYPE_VALUES!r}")
