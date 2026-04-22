from typing import Literal, cast

OnCallPayReportResponseDataType = Literal["on_call_pay_reports"]

ON_CALL_PAY_REPORT_RESPONSE_DATA_TYPE_VALUES: set[OnCallPayReportResponseDataType] = {
    "on_call_pay_reports",
}


def check_on_call_pay_report_response_data_type(value: str | None) -> OnCallPayReportResponseDataType | None:
    if value is None:
        return None
    if value in ON_CALL_PAY_REPORT_RESPONSE_DATA_TYPE_VALUES:
        return cast(OnCallPayReportResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_PAY_REPORT_RESPONSE_DATA_TYPE_VALUES!r}")
