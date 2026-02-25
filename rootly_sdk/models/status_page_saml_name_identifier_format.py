from typing import Literal, cast

StatusPageSamlNameIdentifierFormat = Literal[
    "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
]

STATUS_PAGE_SAML_NAME_IDENTIFIER_FORMAT_VALUES: set[StatusPageSamlNameIdentifierFormat] = {
    "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
    "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
}


def check_status_page_saml_name_identifier_format(value: str | None) -> StatusPageSamlNameIdentifierFormat | None:
    if value is None:
        return None
    if value in STATUS_PAGE_SAML_NAME_IDENTIFIER_FORMAT_VALUES:
        return cast(StatusPageSamlNameIdentifierFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SAML_NAME_IDENTIFIER_FORMAT_VALUES!r}")
