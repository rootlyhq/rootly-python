from typing import Literal

LinkIncidentsDataType = Literal["problems"]

LINK_INCIDENTS_DATA_TYPE_VALUES: set[LinkIncidentsDataType] = {
    "problems",
}


def check_link_incidents_data_type(value: str | None) -> LinkIncidentsDataType | None:
    if value is None:
        return None
    if value in LINK_INCIDENTS_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINK_INCIDENTS_DATA_TYPE_VALUES!r}")
