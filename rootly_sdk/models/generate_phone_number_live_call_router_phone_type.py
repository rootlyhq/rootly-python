from typing import Literal, cast

GeneratePhoneNumberLiveCallRouterPhoneType = Literal["local", "mobile", "toll_free"]

GENERATE_PHONE_NUMBER_LIVE_CALL_ROUTER_PHONE_TYPE_VALUES: set[GeneratePhoneNumberLiveCallRouterPhoneType] = {
    "local",
    "mobile",
    "toll_free",
}


def check_generate_phone_number_live_call_router_phone_type(value: str | None) -> GeneratePhoneNumberLiveCallRouterPhoneType | None:
    if value is None:
        return None
    if value in GENERATE_PHONE_NUMBER_LIVE_CALL_ROUTER_PHONE_TYPE_VALUES:
        return cast(GeneratePhoneNumberLiveCallRouterPhoneType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GENERATE_PHONE_NUMBER_LIVE_CALL_ROUTER_PHONE_TYPE_VALUES!r}"
    )
