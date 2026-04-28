from typing import Literal, cast

OnCallPayReportPayType = Literal["daily", "hourly"]

ON_CALL_PAY_REPORT_PAY_TYPE_VALUES: set[OnCallPayReportPayType] = {
    "daily",
    "hourly",
}


def check_on_call_pay_report_pay_type(value: str | None) -> OnCallPayReportPayType | None:
    if value is None:
        return None
    if value in ON_CALL_PAY_REPORT_PAY_TYPE_VALUES:
        return cast(OnCallPayReportPayType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_PAY_REPORT_PAY_TYPE_VALUES!r}")
