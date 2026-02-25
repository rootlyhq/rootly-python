from typing import Literal, cast

AuthorizationAuthorizableType = Literal["Dashboard"]

AUTHORIZATION_AUTHORIZABLE_TYPE_VALUES: set[AuthorizationAuthorizableType] = {
    "Dashboard",
}


def check_authorization_authorizable_type(value: str | None) -> AuthorizationAuthorizableType | None:
    if value is None:
        return None
    if value in AUTHORIZATION_AUTHORIZABLE_TYPE_VALUES:
        return cast(AuthorizationAuthorizableType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUTHORIZATION_AUTHORIZABLE_TYPE_VALUES!r}")
