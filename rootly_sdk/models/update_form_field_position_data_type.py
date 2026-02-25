from typing import Literal, cast

UpdateFormFieldPositionDataType = Literal["form_field_positions"]

UPDATE_FORM_FIELD_POSITION_DATA_TYPE_VALUES: set[UpdateFormFieldPositionDataType] = {
    "form_field_positions",
}


def check_update_form_field_position_data_type(value: str | None) -> UpdateFormFieldPositionDataType | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_POSITION_DATA_TYPE_VALUES:
        return cast(UpdateFormFieldPositionDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_POSITION_DATA_TYPE_VALUES!r}")
