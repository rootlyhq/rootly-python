from typing import Literal, cast

AuditsListDataItemType = Literal["audits"]

AUDITS_LIST_DATA_ITEM_TYPE_VALUES: set[AuditsListDataItemType] = {
    "audits",
}


def check_audits_list_data_item_type(value: str | None) -> AuditsListDataItemType | None:
    if value is None:
        return None
    if value in AUDITS_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AuditsListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUDITS_LIST_DATA_ITEM_TYPE_VALUES!r}")
