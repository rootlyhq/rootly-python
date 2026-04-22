from typing import Literal, cast

SlaListDataItemType = Literal["slas"]

SLA_LIST_DATA_ITEM_TYPE_VALUES: set[SlaListDataItemType] = {
    "slas",
}


def check_sla_list_data_item_type(value: str | None) -> SlaListDataItemType | None:
    if value is None:
        return None
    if value in SLA_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(SlaListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLA_LIST_DATA_ITEM_TYPE_VALUES!r}")
