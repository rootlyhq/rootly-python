from typing import Literal, cast

UpdateStatusPageDataAttributesAuthenticationMethod = Literal["none", "password", "saml"]

UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_AUTHENTICATION_METHOD_VALUES: set[
    UpdateStatusPageDataAttributesAuthenticationMethod
] = {
    "none",
    "password",
    "saml",
}


def check_update_status_page_data_attributes_authentication_method(
    value: str | None,
) -> UpdateStatusPageDataAttributesAuthenticationMethod | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_AUTHENTICATION_METHOD_VALUES:
        return cast(UpdateStatusPageDataAttributesAuthenticationMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_AUTHENTICATION_METHOD_VALUES!r}"
    )
