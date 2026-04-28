from typing import Literal, cast

ListOncallsInclude = Literal["escalation_policy", "schedule", "user"]

LIST_ONCALLS_INCLUDE_VALUES: set[ListOncallsInclude] = {
    "escalation_policy",
    "schedule",
    "user",
}


def check_list_oncalls_include(value: str | None) -> ListOncallsInclude | None:
    if value is None:
        return None
    if value in LIST_ONCALLS_INCLUDE_VALUES:
        return cast(ListOncallsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ONCALLS_INCLUDE_VALUES!r}")
