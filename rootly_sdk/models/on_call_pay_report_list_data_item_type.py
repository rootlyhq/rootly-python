from typing import Literal, cast

OnCallPayReportListDataItemType = Literal["on_call_pay_reports"]

ON_CALL_PAY_REPORT_LIST_DATA_ITEM_TYPE_VALUES: set[OnCallPayReportListDataItemType] = {
    "on_call_pay_reports",
}


def check_on_call_pay_report_list_data_item_type(value: str | None) -> OnCallPayReportListDataItemType | None:
    if value is None:
        return None
    if value in ON_CALL_PAY_REPORT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(OnCallPayReportListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_PAY_REPORT_LIST_DATA_ITEM_TYPE_VALUES!r}")
