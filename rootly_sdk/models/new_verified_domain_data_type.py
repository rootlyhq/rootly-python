from typing import Literal

NewVerifiedDomainDataType = Literal["verified_domains"]

NEW_VERIFIED_DOMAIN_DATA_TYPE_VALUES: set[NewVerifiedDomainDataType] = {
    "verified_domains",
}


def check_new_verified_domain_data_type(value: str | None) -> NewVerifiedDomainDataType | None:
    if value is None:
        return None
    if value in NEW_VERIFIED_DOMAIN_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_VERIFIED_DOMAIN_DATA_TYPE_VALUES!r}")
