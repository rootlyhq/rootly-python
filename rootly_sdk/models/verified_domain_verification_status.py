from typing import Literal, cast

VerifiedDomainVerificationStatus = Literal["expired", "failing", "pending", "verified"]

VERIFIED_DOMAIN_VERIFICATION_STATUS_VALUES: set[VerifiedDomainVerificationStatus] = {
    "expired",
    "failing",
    "pending",
    "verified",
}


def check_verified_domain_verification_status(value: str | None) -> VerifiedDomainVerificationStatus | None:
    if value is None:
        return None
    if value in VERIFIED_DOMAIN_VERIFICATION_STATUS_VALUES:
        return cast(VerifiedDomainVerificationStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VERIFIED_DOMAIN_VERIFICATION_STATUS_VALUES!r}")
