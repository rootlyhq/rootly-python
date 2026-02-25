from typing import Literal, cast

NewOnCallRoleDataType = Literal["on_call_roles"]

NEW_ON_CALL_ROLE_DATA_TYPE_VALUES: set[NewOnCallRoleDataType] = {
    "on_call_roles",
}


def check_new_on_call_role_data_type(value: str | None) -> NewOnCallRoleDataType | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_TYPE_VALUES:
        return cast(NewOnCallRoleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_TYPE_VALUES!r}")
