from typing import Literal, cast

ReceiptReason = Literal["deduplicated", "no_route_matched", "suppressed", "validation_error"]

RECEIPT_REASON_VALUES: set[ReceiptReason] = {
    "deduplicated",
    "no_route_matched",
    "suppressed",
    "validation_error",
}


def check_receipt_reason(value: str | None) -> ReceiptReason | None:
    if value is None:
        return None
    if value in RECEIPT_REASON_VALUES:
        return cast(ReceiptReason, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECEIPT_REASON_VALUES!r}")
