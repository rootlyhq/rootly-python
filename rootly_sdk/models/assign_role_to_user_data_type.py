from typing import Literal, cast

AssignRoleToUserDataType = Literal["incidents"]

ASSIGN_ROLE_TO_USER_DATA_TYPE_VALUES: set[AssignRoleToUserDataType] = {
    "incidents",
}


def check_assign_role_to_user_data_type(value: str | None) -> AssignRoleToUserDataType | None:
    if value is None:
        return None
    if value in ASSIGN_ROLE_TO_USER_DATA_TYPE_VALUES:
        return cast(AssignRoleToUserDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSIGN_ROLE_TO_USER_DATA_TYPE_VALUES!r}")
