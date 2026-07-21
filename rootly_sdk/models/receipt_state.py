from typing import Literal, cast

ReceiptState = Literal["done", "failed", "pending"]

RECEIPT_STATE_VALUES: set[ReceiptState] = {
    "done",
    "failed",
    "pending",
}


def check_receipt_state(value: str | None) -> ReceiptState | None:
    if value is None:
        return None
    if value in RECEIPT_STATE_VALUES:
        return cast(ReceiptState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECEIPT_STATE_VALUES!r}")
