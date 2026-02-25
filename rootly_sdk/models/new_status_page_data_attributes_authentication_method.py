from typing import Literal, cast

NewStatusPageDataAttributesAuthenticationMethod = Literal["none", "password", "saml"]

NEW_STATUS_PAGE_DATA_ATTRIBUTES_AUTHENTICATION_METHOD_VALUES: set[NewStatusPageDataAttributesAuthenticationMethod] = {
    "none",
    "password",
    "saml",
}


def check_new_status_page_data_attributes_authentication_method(
    value: str | None,
) -> NewStatusPageDataAttributesAuthenticationMethod | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_DATA_ATTRIBUTES_AUTHENTICATION_METHOD_VALUES:
        return cast(NewStatusPageDataAttributesAuthenticationMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_DATA_ATTRIBUTES_AUTHENTICATION_METHOD_VALUES!r}"
    )
