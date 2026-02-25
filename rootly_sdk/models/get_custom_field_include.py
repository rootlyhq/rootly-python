from typing import Literal, cast

GetCustomFieldInclude = Literal["options"]

GET_CUSTOM_FIELD_INCLUDE_VALUES: set[GetCustomFieldInclude] = {
    "options",
}


def check_get_custom_field_include(value: str | None) -> GetCustomFieldInclude | None:
    if value is None:
        return None
    if value in GET_CUSTOM_FIELD_INCLUDE_VALUES:
        return cast(GetCustomFieldInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CUSTOM_FIELD_INCLUDE_VALUES!r}")
