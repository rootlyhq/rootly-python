from typing import Literal, cast

ListCatalogsSort = Literal["-created_at", "-position", "-updated_at", "created_at", "position", "updated_at"]

LIST_CATALOGS_SORT_VALUES: set[ListCatalogsSort] = {
    "-created_at",
    "-position",
    "-updated_at",
    "created_at",
    "position",
    "updated_at",
}


def check_list_catalogs_sort(value: str | None) -> ListCatalogsSort | None:
    if value is None:
        return None
    if value in LIST_CATALOGS_SORT_VALUES:
        return cast(ListCatalogsSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOGS_SORT_VALUES!r}")
