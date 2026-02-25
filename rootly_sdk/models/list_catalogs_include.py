from typing import Literal, cast

ListCatalogsInclude = Literal["entities", "fields"]

LIST_CATALOGS_INCLUDE_VALUES: set[ListCatalogsInclude] = {
    "entities",
    "fields",
}


def check_list_catalogs_include(value: str | None) -> ListCatalogsInclude | None:
    if value is None:
        return None
    if value in LIST_CATALOGS_INCLUDE_VALUES:
        return cast(ListCatalogsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CATALOGS_INCLUDE_VALUES!r}")
