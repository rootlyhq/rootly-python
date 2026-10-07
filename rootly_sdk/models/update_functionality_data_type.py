from typing import Literal

UpdateFunctionalityDataType = Literal["functionalities"]

UPDATE_FUNCTIONALITY_DATA_TYPE_VALUES: set[UpdateFunctionalityDataType] = {
    "functionalities",
}


def check_update_functionality_data_type(value: str | None) -> UpdateFunctionalityDataType | None:
    if value is None:
        return None
    if value in UPDATE_FUNCTIONALITY_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FUNCTIONALITY_DATA_TYPE_VALUES!r}")
