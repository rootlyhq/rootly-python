from typing import Literal, cast

UpdateFormSetConditionDataType = Literal["form_set_conditions"]

UPDATE_FORM_SET_CONDITION_DATA_TYPE_VALUES: set[UpdateFormSetConditionDataType] = {
    "form_set_conditions",
}


def check_update_form_set_condition_data_type(value: str | None) -> UpdateFormSetConditionDataType | None:
    if value is None:
        return None
    if value in UPDATE_FORM_SET_CONDITION_DATA_TYPE_VALUES:
        return cast(UpdateFormSetConditionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_SET_CONDITION_DATA_TYPE_VALUES!r}")
