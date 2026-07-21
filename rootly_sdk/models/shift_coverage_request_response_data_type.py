from typing import Literal, cast

ShiftCoverageRequestResponseDataType = Literal["shift_coverage_requests"]

SHIFT_COVERAGE_REQUEST_RESPONSE_DATA_TYPE_VALUES: set[ShiftCoverageRequestResponseDataType] = {
    "shift_coverage_requests",
}


def check_shift_coverage_request_response_data_type(value: str | None) -> ShiftCoverageRequestResponseDataType | None:
    if value is None:
        return None
    if value in SHIFT_COVERAGE_REQUEST_RESPONSE_DATA_TYPE_VALUES:
        return cast(ShiftCoverageRequestResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SHIFT_COVERAGE_REQUEST_RESPONSE_DATA_TYPE_VALUES!r}")
