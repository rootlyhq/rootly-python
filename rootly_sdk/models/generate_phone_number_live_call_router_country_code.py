from typing import Literal, cast

GeneratePhoneNumberLiveCallRouterCountryCode = Literal["AU", "CA", "DE", "GB", "NL", "NZ", "US"]

GENERATE_PHONE_NUMBER_LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES: set[GeneratePhoneNumberLiveCallRouterCountryCode] = {
    "AU",
    "CA",
    "DE",
    "GB",
    "NL",
    "NZ",
    "US",
}


def check_generate_phone_number_live_call_router_country_code(
    value: str | None,
) -> GeneratePhoneNumberLiveCallRouterCountryCode | None:
    if value is None:
        return None
    if value in GENERATE_PHONE_NUMBER_LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES:
        return cast(GeneratePhoneNumberLiveCallRouterCountryCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GENERATE_PHONE_NUMBER_LIVE_CALL_ROUTER_COUNTRY_CODE_VALUES!r}"
    )
