from typing import Literal

ListFormFieldsInclude = Literal["options", "positions"]

LIST_FORM_FIELDS_INCLUDE_VALUES: set[ListFormFieldsInclude] = {
    "options",
    "positions",
}


def check_list_form_fields_include(value: str | None) -> ListFormFieldsInclude | None:
    if value is None:
        return None
    if value in LIST_FORM_FIELDS_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_FORM_FIELDS_INCLUDE_VALUES!r}")
