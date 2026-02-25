from typing import Literal, cast

UpdateSeverityDataAttributesSeverity = Literal["critical", "high", "low", "medium"]

UPDATE_SEVERITY_DATA_ATTRIBUTES_SEVERITY_VALUES: set[UpdateSeverityDataAttributesSeverity] = {
    "critical",
    "high",
    "low",
    "medium",
}


def check_update_severity_data_attributes_severity(value: str | None) -> UpdateSeverityDataAttributesSeverity | None:
    if value is None:
        return None
    if value in UPDATE_SEVERITY_DATA_ATTRIBUTES_SEVERITY_VALUES:
        return cast(UpdateSeverityDataAttributesSeverity, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SEVERITY_DATA_ATTRIBUTES_SEVERITY_VALUES!r}")
