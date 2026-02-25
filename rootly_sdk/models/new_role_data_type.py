from typing import Literal, cast

NewRoleDataType = Literal["roles"]

NEW_ROLE_DATA_TYPE_VALUES: set[NewRoleDataType] = {
    "roles",
}


def check_new_role_data_type(value: str | None) -> NewRoleDataType | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_TYPE_VALUES:
        return cast(NewRoleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_TYPE_VALUES!r}")
