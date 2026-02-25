from typing import Literal, cast

NewAuthorizationDataAttributesGranteeType = Literal["Team", "User"]

NEW_AUTHORIZATION_DATA_ATTRIBUTES_GRANTEE_TYPE_VALUES: set[NewAuthorizationDataAttributesGranteeType] = {
    "Team",
    "User",
}


def check_new_authorization_data_attributes_grantee_type(
    value: str | None,
) -> NewAuthorizationDataAttributesGranteeType | None:
    if value is None:
        return None
    if value in NEW_AUTHORIZATION_DATA_ATTRIBUTES_GRANTEE_TYPE_VALUES:
        return cast(NewAuthorizationDataAttributesGranteeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_AUTHORIZATION_DATA_ATTRIBUTES_GRANTEE_TYPE_VALUES!r}"
    )
