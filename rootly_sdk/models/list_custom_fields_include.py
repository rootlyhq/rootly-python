from typing import Literal

ListCustomFieldsInclude = Literal["options"]

LIST_CUSTOM_FIELDS_INCLUDE_VALUES: set[ListCustomFieldsInclude] = {
    "options",
}


def check_list_custom_fields_include(value: str | None) -> ListCustomFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_CUSTOM_FIELDS_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CUSTOM_FIELDS_INCLUDE_VALUES!r}")
