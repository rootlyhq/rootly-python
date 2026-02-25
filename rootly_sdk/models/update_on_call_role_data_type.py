from typing import Literal, cast

UpdateOnCallRoleDataType = Literal["on_call_roles"]

UPDATE_ON_CALL_ROLE_DATA_TYPE_VALUES: set[UpdateOnCallRoleDataType] = {
    "on_call_roles",
}


def check_update_on_call_role_data_type(value: str | None) -> UpdateOnCallRoleDataType | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_TYPE_VALUES:
        return cast(UpdateOnCallRoleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_TYPE_VALUES!r}")
