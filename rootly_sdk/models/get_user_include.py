from typing import Literal, cast

GetUserInclude = Literal[
    "devices", "email_addresses", "notification_rules", "on_call_role", "phone_numbers", "role", "schedules", "teams"
]

GET_USER_INCLUDE_VALUES: set[GetUserInclude] = {
    "devices",
    "email_addresses",
    "notification_rules",
    "on_call_role",
    "phone_numbers",
    "role",
    "schedules",
    "teams",
}


def check_get_user_include(value: str | None) -> GetUserInclude | None:
    if value is None:
        return None
    if value in GET_USER_INCLUDE_VALUES:
        return cast(GetUserInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_USER_INCLUDE_VALUES!r}")
