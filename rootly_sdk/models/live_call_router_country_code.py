from typing import Literal, cast

LiveCallRouterCountryCode = Literal["AU", "CA", "DE", "GB", "NL", "NZ", "US"]

LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES: set[LiveCallRouterCountryCode] = {
    "AU",
    "CA",
    "DE",
    "GB",
    "NL",
    "NZ",
    "US",
}


def check_live_call_router_country_code(value: str | None) -> LiveCallRouterCountryCode | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES:
        return cast(LiveCallRouterCountryCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES!r}")
