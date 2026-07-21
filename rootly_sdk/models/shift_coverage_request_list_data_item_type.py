from typing import Literal, cast

ShiftCoverageRequestListDataItemType = Literal["shift_coverage_requests"]

SHIFT_COVERAGE_REQUEST_LIST_DATA_ITEM_TYPE_VALUES: set[ShiftCoverageRequestListDataItemType] = {
    "shift_coverage_requests",
}


def check_shift_coverage_request_list_data_item_type(value: str | None) -> ShiftCoverageRequestListDataItemType | None:
    if value is None:
        return None
    if value in SHIFT_COVERAGE_REQUEST_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ShiftCoverageRequestListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SHIFT_COVERAGE_REQUEST_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
