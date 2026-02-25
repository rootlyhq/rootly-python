from typing import Literal, cast

UpdateLiveCallRouterDataAttributesCountryCode = Literal["AU", "CA", "DE", "GB", "NL", "NZ", "US"]

UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES: set[UpdateLiveCallRouterDataAttributesCountryCode] = {
    "AU",
    "CA",
    "DE",
    "GB",
    "NL",
    "NZ",
    "US",
}


def check_update_live_call_router_data_attributes_country_code(
    value: str | None,
) -> UpdateLiveCallRouterDataAttributesCountryCode | None:
    if value is None:
        return None
    if value in UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES:
        return cast(UpdateLiveCallRouterDataAttributesCountryCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_COUNTRY_CODE_VALUES!r}"
    )
