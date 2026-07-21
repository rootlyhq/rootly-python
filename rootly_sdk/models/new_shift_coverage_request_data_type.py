from typing import Literal, cast

NewShiftCoverageRequestDataType = Literal["shift_coverage_requests"]

NEW_SHIFT_COVERAGE_REQUEST_DATA_TYPE_VALUES: set[NewShiftCoverageRequestDataType] = {
    "shift_coverage_requests",
}


def check_new_shift_coverage_request_data_type(value: str | None) -> NewShiftCoverageRequestDataType | None:
    if value is None:
        return None
    if value in NEW_SHIFT_COVERAGE_REQUEST_DATA_TYPE_VALUES:
        return cast(NewShiftCoverageRequestDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SHIFT_COVERAGE_REQUEST_DATA_TYPE_VALUES!r}")
