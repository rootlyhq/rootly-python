from typing import Literal, cast

VerifiedDomainResponseDataType = Literal["verified_domains"]

VERIFIED_DOMAIN_RESPONSE_DATA_TYPE_VALUES: set[VerifiedDomainResponseDataType] = {
    "verified_domains",
}


def check_verified_domain_response_data_type(value: str | None) -> VerifiedDomainResponseDataType | None:
    if value is None:
        return None
    if value in VERIFIED_DOMAIN_RESPONSE_DATA_TYPE_VALUES:
        return cast(VerifiedDomainResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VERIFIED_DOMAIN_RESPONSE_DATA_TYPE_VALUES!r}")
