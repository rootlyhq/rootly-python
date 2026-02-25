from typing import Literal, cast

NewServiceDataType = Literal["services"]

NEW_SERVICE_DATA_TYPE_VALUES: set[NewServiceDataType] = {
    "services",
}


def check_new_service_data_type(value: str | None) -> NewServiceDataType | None:
    if value is None:
        return None
    if value in NEW_SERVICE_DATA_TYPE_VALUES:
        return cast(NewServiceDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SERVICE_DATA_TYPE_VALUES!r}")
