from typing import Literal, cast

OnCallRoleResponseDataType = Literal["on_call_roles"]

ON_CALL_ROLE_RESPONSE_DATA_TYPE_VALUES: set[OnCallRoleResponseDataType] = {
    "on_call_roles",
}


def check_on_call_role_response_data_type(value: str | None) -> OnCallRoleResponseDataType | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_RESPONSE_DATA_TYPE_VALUES:
        return cast(OnCallRoleResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_RESPONSE_DATA_TYPE_VALUES!r}")
