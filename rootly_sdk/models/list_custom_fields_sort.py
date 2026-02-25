from typing import Literal, cast

ListCustomFieldsSort = Literal["-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"]

LIST_CUSTOM_FIELDS_SORT_VALUES: set[ListCustomFieldsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_custom_fields_sort(value: str | None) -> ListCustomFieldsSort | None:
    if value is None:
        return None
    if value in LIST_CUSTOM_FIELDS_SORT_VALUES:
        return cast(ListCustomFieldsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CUSTOM_FIELDS_SORT_VALUES!r}")
