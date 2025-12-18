from typing import Literal, cast

ListShiftsInclude = Literal["assignee", "shift_override", "user"]

LIST_SHIFTS_INCLUDE_VALUES: set[ListShiftsInclude] = {
    "assignee",
    "shift_override",
    "user",
}


def check_list_shifts_include(value: str) -> ListShiftsInclude:
    if value in LIST_SHIFTS_INCLUDE_VALUES:
        return cast(ListShiftsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SHIFTS_INCLUDE_VALUES!r}")
