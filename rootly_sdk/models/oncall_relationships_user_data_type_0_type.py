from typing import Literal, cast

OncallRelationshipsUserDataType0Type = Literal["users"]

ONCALL_RELATIONSHIPS_USER_DATA_TYPE_0_TYPE_VALUES: set[OncallRelationshipsUserDataType0Type] = {
    "users",
}


def check_oncall_relationships_user_data_type_0_type(value: str | None) -> OncallRelationshipsUserDataType0Type | None:
    if value is None:
        return None
    if value in ONCALL_RELATIONSHIPS_USER_DATA_TYPE_0_TYPE_VALUES:
        return cast(OncallRelationshipsUserDataType0Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ONCALL_RELATIONSHIPS_USER_DATA_TYPE_0_TYPE_VALUES!r}"
    )
