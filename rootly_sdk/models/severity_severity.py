from typing import Literal

SeveritySeverity = Literal["critical", "high", "low", "medium"]

SEVERITY_SEVERITY_VALUES: set[SeveritySeverity] = {
    "critical",
    "high",
    "low",
    "medium",
}


def check_severity_severity(value: str | None) -> SeveritySeverity | None:
    if value is None:
        return None
    if value in SEVERITY_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEVERITY_SEVERITY_VALUES!r}")
