from typing import Literal, cast

GetFormFieldInclude = Literal["options", "positions"]

GET_FORM_FIELD_INCLUDE_VALUES: set[GetFormFieldInclude] = {
    "options",
    "positions",
}


def check_get_form_field_include(value: str | None) -> GetFormFieldInclude | None:
    if value is None:
        return None
    if value in GET_FORM_FIELD_INCLUDE_VALUES:
        return cast(GetFormFieldInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_FORM_FIELD_INCLUDE_VALUES!r}")
