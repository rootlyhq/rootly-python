from typing import Literal, cast

UpdateLiveCallRouterDataAttributesPhoneType = Literal["local", "mobile", "toll_free"]

UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PHONE_TYPE_VALUES: set[UpdateLiveCallRouterDataAttributesPhoneType] = {
    "local",
    "mobile",
    "toll_free",
}


def check_update_live_call_router_data_attributes_phone_type(
    value: str | None,
) -> UpdateLiveCallRouterDataAttributesPhoneType | None:
    if value is None:
        return None
    if value in UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PHONE_TYPE_VALUES:
        return cast(UpdateLiveCallRouterDataAttributesPhoneType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_PHONE_TYPE_VALUES!r}"
    )
