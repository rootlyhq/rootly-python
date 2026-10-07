from typing import Literal

LiveCallRouterCountryCode = Literal["AU", "CA", "CH", "DE", "GB", "NL", "NZ", "SE", "US"]

LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES: set[LiveCallRouterCountryCode] = {
    "AU",
    "CA",
    "CH",
    "DE",
    "GB",
    "NL",
    "NZ",
    "SE",
    "US",
}


def check_live_call_router_country_code(value: str | None) -> LiveCallRouterCountryCode | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES!r}")
