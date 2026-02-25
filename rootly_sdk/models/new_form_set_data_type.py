from typing import Literal, cast

NewFormSetDataType = Literal["form_sets"]

NEW_FORM_SET_DATA_TYPE_VALUES: set[NewFormSetDataType] = {
    "form_sets",
}


def check_new_form_set_data_type(value: str | None) -> NewFormSetDataType | None:
    if value is None:
        return None
    if value in NEW_FORM_SET_DATA_TYPE_VALUES:
        return cast(NewFormSetDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_SET_DATA_TYPE_VALUES!r}")
