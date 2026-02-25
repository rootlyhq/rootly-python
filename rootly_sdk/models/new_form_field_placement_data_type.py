from typing import Literal, cast

NewFormFieldPlacementDataType = Literal["form_field_placements"]

NEW_FORM_FIELD_PLACEMENT_DATA_TYPE_VALUES: set[NewFormFieldPlacementDataType] = {
    "form_field_placements",
}


def check_new_form_field_placement_data_type(value: str | None) -> NewFormFieldPlacementDataType | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_PLACEMENT_DATA_TYPE_VALUES:
        return cast(NewFormFieldPlacementDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_PLACEMENT_DATA_TYPE_VALUES!r}")
