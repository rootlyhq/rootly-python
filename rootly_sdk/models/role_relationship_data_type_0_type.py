from typing import Literal, cast

RoleRelationshipDataType0Type = Literal["roles"]

ROLE_RELATIONSHIP_DATA_TYPE_0_TYPE_VALUES: set[RoleRelationshipDataType0Type] = {
    "roles",
}


def check_role_relationship_data_type_0_type(value: str | None) -> RoleRelationshipDataType0Type | None:
    if value is None:
        return None
    if value in ROLE_RELATIONSHIP_DATA_TYPE_0_TYPE_VALUES:
        return cast(RoleRelationshipDataType0Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_RELATIONSHIP_DATA_TYPE_0_TYPE_VALUES!r}")
