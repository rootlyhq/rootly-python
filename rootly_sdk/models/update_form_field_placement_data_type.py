from typing import Literal, cast

UpdateFormFieldPlacementDataType = Literal["form_field_placements"]

UPDATE_FORM_FIELD_PLACEMENT_DATA_TYPE_VALUES: set[UpdateFormFieldPlacementDataType] = {
    "form_field_placements",
}


def check_update_form_field_placement_data_type(value: str | None) -> UpdateFormFieldPlacementDataType | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_PLACEMENT_DATA_TYPE_VALUES:
        return cast(UpdateFormFieldPlacementDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_PLACEMENT_DATA_TYPE_VALUES!r}")
