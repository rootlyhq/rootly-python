from typing import Literal, cast

UpdateFormSetConditionDataAttributesComparison = Literal["equal"]

UPDATE_FORM_SET_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES: set[UpdateFormSetConditionDataAttributesComparison] = {
    "equal",
}


def check_update_form_set_condition_data_attributes_comparison(
    value: str | None,
) -> UpdateFormSetConditionDataAttributesComparison | None:
    if value is None:
        return None
    if value in UPDATE_FORM_SET_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES:
        return cast(UpdateFormSetConditionDataAttributesComparison, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_SET_CONDITION_DATA_ATTRIBUTES_COMPARISON_VALUES!r}"
    )
