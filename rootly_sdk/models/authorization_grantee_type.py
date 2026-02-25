from typing import Literal, cast

AuthorizationGranteeType = Literal["Team", "User"]

AUTHORIZATION_GRANTEE_TYPE_VALUES: set[AuthorizationGranteeType] = {
    "Team",
    "User",
}


def check_authorization_grantee_type(value: str | None) -> AuthorizationGranteeType | None:
    if value is None:
        return None
    if value in AUTHORIZATION_GRANTEE_TYPE_VALUES:
        return cast(AuthorizationGranteeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUTHORIZATION_GRANTEE_TYPE_VALUES!r}")
