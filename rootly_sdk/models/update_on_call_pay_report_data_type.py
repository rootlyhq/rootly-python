from typing import Literal, cast

UpdateOnCallPayReportDataType = Literal["on_call_pay_reports"]

UPDATE_ON_CALL_PAY_REPORT_DATA_TYPE_VALUES: set[UpdateOnCallPayReportDataType] = {
    "on_call_pay_reports",
}


def check_update_on_call_pay_report_data_type(value: str | None) -> UpdateOnCallPayReportDataType | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_PAY_REPORT_DATA_TYPE_VALUES:
        return cast(UpdateOnCallPayReportDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_PAY_REPORT_DATA_TYPE_VALUES!r}")
