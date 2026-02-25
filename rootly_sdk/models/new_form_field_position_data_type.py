from typing import Literal, cast

NewFormFieldPositionDataType = Literal["form_field_positions"]

NEW_FORM_FIELD_POSITION_DATA_TYPE_VALUES: set[NewFormFieldPositionDataType] = {
    "form_field_positions",
}


def check_new_form_field_position_data_type(value: str | None) -> NewFormFieldPositionDataType | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_POSITION_DATA_TYPE_VALUES:
        return cast(NewFormFieldPositionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_POSITION_DATA_TYPE_VALUES!r}")
