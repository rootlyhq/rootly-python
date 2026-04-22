from typing import Literal, cast

OnCallPayReportStatus = Literal["downloaded", "generated", "processing"]

ON_CALL_PAY_REPORT_STATUS_VALUES: set[OnCallPayReportStatus] = {
    "downloaded",
    "generated",
    "processing",
}


def check_on_call_pay_report_status(value: str | None) -> OnCallPayReportStatus | None:
    if value is None:
        return None
    if value in ON_CALL_PAY_REPORT_STATUS_VALUES:
        return cast(OnCallPayReportStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_PAY_REPORT_STATUS_VALUES!r}")
