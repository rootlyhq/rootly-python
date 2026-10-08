from typing import Literal

VerifiedDomainSource = Literal["manual", "migration", "oauth_auto"]

VERIFIED_DOMAIN_SOURCE_VALUES: set[VerifiedDomainSource] = {
    "manual",
    "migration",
    "oauth_auto",
}


def check_verified_domain_source(value: str | None) -> VerifiedDomainSource | None:
    if value is None:
        return None
    if value in VERIFIED_DOMAIN_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VERIFIED_DOMAIN_SOURCE_VALUES!r}")
