from typing import Literal, cast

UnassignRoleFromUserDataType = Literal["incidents"]

UNASSIGN_ROLE_FROM_USER_DATA_TYPE_VALUES: set[UnassignRoleFromUserDataType] = {
    "incidents",
}


def check_unassign_role_from_user_data_type(value: str | None) -> UnassignRoleFromUserDataType | None:
    if value is None:
        return None
    if value in UNASSIGN_ROLE_FROM_USER_DATA_TYPE_VALUES:
        return cast(UnassignRoleFromUserDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNASSIGN_ROLE_FROM_USER_DATA_TYPE_VALUES!r}")
