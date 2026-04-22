from typing import Literal, cast

NewOnCallPayReportDataType = Literal["on_call_pay_reports"]

NEW_ON_CALL_PAY_REPORT_DATA_TYPE_VALUES: set[NewOnCallPayReportDataType] = {
    "on_call_pay_reports",
}


def check_new_on_call_pay_report_data_type(value: str | None) -> NewOnCallPayReportDataType | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_PAY_REPORT_DATA_TYPE_VALUES:
        return cast(NewOnCallPayReportDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_PAY_REPORT_DATA_TYPE_VALUES!r}")
