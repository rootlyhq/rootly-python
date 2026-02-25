from typing import Literal, cast

NewLiveCallRouterDataAttributesCountryCode = Literal["AU", "CA", "DE", "GB", "NL", "NZ", "US"]

NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES: set[NewLiveCallRouterDataAttributesCountryCode] = {
    "AU",
    "CA",
    "DE",
    "GB",
    "NL",
    "NZ",
    "US",
}


def check_new_live_call_router_data_attributes_country_code(
    value: str | None,
) -> NewLiveCallRouterDataAttributesCountryCode | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES:
        return cast(NewLiveCallRouterDataAttributesCountryCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES!r}"
    )
