from typing import Literal, cast

RetrospectiveConfigurationListDataItemType = Literal["retrospective_configurations"]

RETROSPECTIVE_CONFIGURATION_LIST_DATA_ITEM_TYPE_VALUES: set[RetrospectiveConfigurationListDataItemType] = {
    "retrospective_configurations",
}


def check_retrospective_configuration_list_data_item_type(value: str | None) -> RetrospectiveConfigurationListDataItemType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_CONFIGURATION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(RetrospectiveConfigurationListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_CONFIGURATION_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
