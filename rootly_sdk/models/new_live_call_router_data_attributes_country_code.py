from typing import Literal

NewLiveCallRouterDataAttributesCountryCode = Literal["AU", "CA", "CH", "DE", "GB", "NL", "NZ", "SE", "US"]

NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES: set[NewLiveCallRouterDataAttributesCountryCode] = {
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


def check_new_live_call_router_data_attributes_country_code(
    value: str | None,
) -> NewLiveCallRouterDataAttributesCountryCode | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES!r}"
    )
