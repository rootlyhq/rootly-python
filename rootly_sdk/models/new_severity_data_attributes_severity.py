from typing import Literal, cast

NewSeverityDataAttributesSeverity = Literal["critical", "high", "low", "medium"]

NEW_SEVERITY_DATA_ATTRIBUTES_SEVERITY_VALUES: set[NewSeverityDataAttributesSeverity] = {
    "critical",
    "high",
    "low",
    "medium",
}


def check_new_severity_data_attributes_severity(value: str | None) -> NewSeverityDataAttributesSeverity | None:
    if value is None:
        return None
    if value in NEW_SEVERITY_DATA_ATTRIBUTES_SEVERITY_VALUES:
        return cast(NewSeverityDataAttributesSeverity, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SEVERITY_DATA_ATTRIBUTES_SEVERITY_VALUES!r}")
