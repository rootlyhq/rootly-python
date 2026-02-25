from typing import Literal, cast

UpdateServiceDataType = Literal["services"]

UPDATE_SERVICE_DATA_TYPE_VALUES: set[UpdateServiceDataType] = {
    "services",
}


def check_update_service_data_type(value: str | None) -> UpdateServiceDataType | None:
    if value is None:
        return None
    if value in UPDATE_SERVICE_DATA_TYPE_VALUES:
        return cast(UpdateServiceDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SERVICE_DATA_TYPE_VALUES!r}")
