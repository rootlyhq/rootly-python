from typing import Literal, cast

OnCallRoleRelationshipDataType0Type = Literal["on_call_roles"]

ON_CALL_ROLE_RELATIONSHIP_DATA_TYPE_0_TYPE_VALUES: set[OnCallRoleRelationshipDataType0Type] = {
    "on_call_roles",
}


def check_on_call_role_relationship_data_type_0_type(value: str | None) -> OnCallRoleRelationshipDataType0Type | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_RELATIONSHIP_DATA_TYPE_0_TYPE_VALUES:
        return cast(OnCallRoleRelationshipDataType0Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_RELATIONSHIP_DATA_TYPE_0_TYPE_VALUES!r}"
    )
