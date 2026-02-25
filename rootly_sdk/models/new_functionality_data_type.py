from typing import Literal, cast

NewFunctionalityDataType = Literal["functionalities"]

NEW_FUNCTIONALITY_DATA_TYPE_VALUES: set[NewFunctionalityDataType] = {
    "functionalities",
}


def check_new_functionality_data_type(value: str | None) -> NewFunctionalityDataType | None:
    if value is None:
        return None
    if value in NEW_FUNCTIONALITY_DATA_TYPE_VALUES:
        return cast(NewFunctionalityDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FUNCTIONALITY_DATA_TYPE_VALUES!r}")
