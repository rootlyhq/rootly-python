from typing import Literal, cast

NewFormSetConditionDataType = Literal["form_set_conditions"]

NEW_FORM_SET_CONDITION_DATA_TYPE_VALUES: set[NewFormSetConditionDataType] = {
    "form_set_conditions",
}


def check_new_form_set_condition_data_type(value: str | None) -> NewFormSetConditionDataType | None:
    if value is None:
        return None
    if value in NEW_FORM_SET_CONDITION_DATA_TYPE_VALUES:
        return cast(NewFormSetConditionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_SET_CONDITION_DATA_TYPE_VALUES!r}")
