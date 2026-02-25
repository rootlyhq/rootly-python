from typing import Literal, cast

ListUsersSort = Literal["-created_at", "-updated_at", "created_at", "updated_at"]

LIST_USERS_SORT_VALUES: set[ListUsersSort] = {
    "-created_at",
    "-updated_at",
    "created_at",
    "updated_at",
}


def check_list_users_sort(value: str | None) -> ListUsersSort | None:
    if value is None:
        return None
    if value in LIST_USERS_SORT_VALUES:
        return cast(ListUsersSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_USERS_SORT_VALUES!r}")
