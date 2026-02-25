from typing import Literal, cast

ListUsersInclude = Literal[
    "devices", "email_addresses", "notification_rules", "on_call_role", "phone_numbers", "role", "schedules", "teams"
]

LIST_USERS_INCLUDE_VALUES: set[ListUsersInclude] = {
    "devices",
    "email_addresses",
    "notification_rules",
    "on_call_role",
    "phone_numbers",
    "role",
    "schedules",
    "teams",
}


def check_list_users_include(value: str | None) -> ListUsersInclude | None:
    if value is None:
        return None
    if value in LIST_USERS_INCLUDE_VALUES:
        return cast(ListUsersInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_USERS_INCLUDE_VALUES!r}")
