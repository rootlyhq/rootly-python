from typing import Literal, cast

UpdateFormSetDataType = Literal["form_sets"]

UPDATE_FORM_SET_DATA_TYPE_VALUES: set[UpdateFormSetDataType] = {
    "form_sets",
}


def check_update_form_set_data_type(value: str | None) -> UpdateFormSetDataType | None:
    if value is None:
        return None
    if value in UPDATE_FORM_SET_DATA_TYPE_VALUES:
        return cast(UpdateFormSetDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_SET_DATA_TYPE_VALUES!r}")
