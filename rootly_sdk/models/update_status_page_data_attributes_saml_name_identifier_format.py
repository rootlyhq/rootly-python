from typing import Literal, cast

UpdateStatusPageDataAttributesSamlNameIdentifierFormat = Literal[
    "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
]

UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SAML_NAME_IDENTIFIER_FORMAT_VALUES: set[
    UpdateStatusPageDataAttributesSamlNameIdentifierFormat
] = {
    "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
}


def check_update_status_page_data_attributes_saml_name_identifier_format(
    value: str | None,
) -> UpdateStatusPageDataAttributesSamlNameIdentifierFormat | None:
    if value is None:
        return None
    if value in UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SAML_NAME_IDENTIFIER_FORMAT_VALUES:
        return cast(UpdateStatusPageDataAttributesSamlNameIdentifierFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_STATUS_PAGE_DATA_ATTRIBUTES_SAML_NAME_IDENTIFIER_FORMAT_VALUES!r}"
    )
