from typing import Literal, cast

ServiceResponseDataType = Literal["services"]

SERVICE_RESPONSE_DATA_TYPE_VALUES: set[ServiceResponseDataType] = {
    "services",
}


def check_service_response_data_type(value: str | None) -> ServiceResponseDataType | None:
    if value is None:
        return None
    if value in SERVICE_RESPONSE_DATA_TYPE_VALUES:
        return cast(ServiceResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_RESPONSE_DATA_TYPE_VALUES!r}")
