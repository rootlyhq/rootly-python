from typing import Literal, cast

ApiKeyKind = Literal["organization", "personal", "team"]

API_KEY_KIND_VALUES: set[ApiKeyKind] = {
    "organization",
    "personal",
    "team",
}


def check_api_key_kind(value: str | None) -> ApiKeyKind | None:
    if value is None:
        return None
    if value in API_KEY_KIND_VALUES:
        return cast(ApiKeyKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_KEY_KIND_VALUES!r}")
