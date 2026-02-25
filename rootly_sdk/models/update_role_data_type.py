from typing import Literal, cast

UpdateRoleDataType = Literal["roles"]

UPDATE_ROLE_DATA_TYPE_VALUES: set[UpdateRoleDataType] = {
    "roles",
}


def check_update_role_data_type(value: str | None) -> UpdateRoleDataType | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_TYPE_VALUES:
        return cast(UpdateRoleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_TYPE_VALUES!r}")
