from typing import Literal, cast

FormSetConditionResponseDataType = Literal["form_set_conditions"]

FORM_SET_CONDITION_RESPONSE_DATA_TYPE_VALUES: set[FormSetConditionResponseDataType] = {
    "form_set_conditions",
}


def check_form_set_condition_response_data_type(value: str | None) -> FormSetConditionResponseDataType | None:
    if value is None:
        return None
    if value in FORM_SET_CONDITION_RESPONSE_DATA_TYPE_VALUES:
        return cast(FormSetConditionResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_SET_CONDITION_RESPONSE_DATA_TYPE_VALUES!r}")
