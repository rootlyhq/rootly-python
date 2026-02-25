from typing import Literal, cast

NewFormFieldPlacementConditionDataAttributesConditioned = Literal["placement", "required"]

NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_CONDITIONED_VALUES: set[
    NewFormFieldPlacementConditionDataAttributesConditioned
] = {
    "placement",
    "required",
}


def check_new_form_field_placement_condition_data_attributes_conditioned(
    value: str | None,
) -> NewFormFieldPlacementConditionDataAttributesConditioned | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_CONDITIONED_VALUES:
        return cast(NewFormFieldPlacementConditionDataAttributesConditioned, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_PLACEMENT_CONDITION_DATA_ATTRIBUTES_CONDITIONED_VALUES!r}"
    )
