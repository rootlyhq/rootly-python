from typing import Literal, cast

NewStatusPageDataAttributesSamlNameIdentifierFormat = Literal[
    "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
]

NEW_STATUS_PAGE_DATA_ATTRIBUTES_SAML_NAME_IDENTIFIER_FORMAT_VALUES: set[
    NewStatusPageDataAttributesSamlNameIdentifierFormat
] = {
    "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
}


def check_new_status_page_data_attributes_saml_name_identifier_format(
    value: str | None,
) -> NewStatusPageDataAttributesSamlNameIdentifierFormat | None:
    if value is None:
        return None
    if value in NEW_STATUS_PAGE_DATA_ATTRIBUTES_SAML_NAME_IDENTIFIER_FORMAT_VALUES:
        return cast(NewStatusPageDataAttributesSamlNameIdentifierFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_STATUS_PAGE_DATA_ATTRIBUTES_SAML_NAME_IDENTIFIER_FORMAT_VALUES!r}"
    )
