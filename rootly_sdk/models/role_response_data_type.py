from typing import Literal, cast

RoleResponseDataType = Literal["roles"]

ROLE_RESPONSE_DATA_TYPE_VALUES: set[RoleResponseDataType] = {
    "roles",
}


def check_role_response_data_type(value: str | None) -> RoleResponseDataType | None:
    if value is None:
        return None
    if value in ROLE_RESPONSE_DATA_TYPE_VALUES:
        return cast(RoleResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_RESPONSE_DATA_TYPE_VALUES!r}")
