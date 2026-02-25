from typing import Literal, cast

UpdateFormFieldPlacementConditionDataAttributesConditioned = Literal["placement", "required"]

UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_CONDITIONED_VALUES: set[
    UpdateFormFieldPlacementConditionDataAttributesConditioned
] = {
    "placement",
    "required",
}


def check_update_form_field_placement_condition_data_attributes_conditioned(
    value: str | None,
) -> UpdateFormFieldPlacementConditionDataAttributesConditioned | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_CONDITIONED_VALUES:
        return cast(UpdateFormFieldPlacementConditionDataAttributesConditioned, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_CONDITIONED_VALUES!r}"
    )
