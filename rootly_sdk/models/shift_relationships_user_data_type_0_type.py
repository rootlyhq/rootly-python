from typing import Literal, cast

ShiftRelationshipsUserDataType0Type = Literal["users"]

SHIFT_RELATIONSHIPS_USER_DATA_TYPE_0_TYPE_VALUES: set[ShiftRelationshipsUserDataType0Type] = {
    "users",
}


def check_shift_relationships_user_data_type_0_type(value: str | None) -> ShiftRelationshipsUserDataType0Type | None:
    if value is None:
        return None
    if value in SHIFT_RELATIONSHIPS_USER_DATA_TYPE_0_TYPE_VALUES:
        return cast(ShiftRelationshipsUserDataType0Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SHIFT_RELATIONSHIPS_USER_DATA_TYPE_0_TYPE_VALUES!r}")
