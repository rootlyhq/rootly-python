from typing import Literal, cast

NewAuthorizationDataAttributesAuthorizableType = Literal["Dashboard"]

NEW_AUTHORIZATION_DATA_ATTRIBUTES_AUTHORIZABLE_TYPE_VALUES: set[NewAuthorizationDataAttributesAuthorizableType] = {
    "Dashboard",
}


def check_new_authorization_data_attributes_authorizable_type(
    value: str | None,
) -> NewAuthorizationDataAttributesAuthorizableType | None:
    if value is None:
        return None
    if value in NEW_AUTHORIZATION_DATA_ATTRIBUTES_AUTHORIZABLE_TYPE_VALUES:
        return cast(NewAuthorizationDataAttributesAuthorizableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_AUTHORIZATION_DATA_ATTRIBUTES_AUTHORIZABLE_TYPE_VALUES!r}"
    )
