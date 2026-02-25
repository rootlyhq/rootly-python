from typing import Literal, cast

RetrospectiveStepListDataItemType = Literal["retrospective_steps"]

RETROSPECTIVE_STEP_LIST_DATA_ITEM_TYPE_VALUES: set[RetrospectiveStepListDataItemType] = {
    "retrospective_steps",
}


def check_retrospective_step_list_data_item_type(value: str | None) -> RetrospectiveStepListDataItemType | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_STEP_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(RetrospectiveStepListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_STEP_LIST_DATA_ITEM_TYPE_VALUES!r}")
