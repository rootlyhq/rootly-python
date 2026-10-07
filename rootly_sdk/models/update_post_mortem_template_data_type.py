from typing import Literal

UpdatePostMortemTemplateDataType = Literal["post_mortem_templates"]

UPDATE_POST_MORTEM_TEMPLATE_DATA_TYPE_VALUES: set[UpdatePostMortemTemplateDataType] = {
    "post_mortem_templates",
}


def check_update_post_mortem_template_data_type(value: str | None) -> UpdatePostMortemTemplateDataType | None:
    if value is None:
        return None
    if value in UPDATE_POST_MORTEM_TEMPLATE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_POST_MORTEM_TEMPLATE_DATA_TYPE_VALUES!r}")
