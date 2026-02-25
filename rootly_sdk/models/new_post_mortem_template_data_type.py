from typing import Literal, cast

NewPostMortemTemplateDataType = Literal["post_mortem_templates"]

NEW_POST_MORTEM_TEMPLATE_DATA_TYPE_VALUES: set[NewPostMortemTemplateDataType] = {
    "post_mortem_templates",
}


def check_new_post_mortem_template_data_type(value: str | None) -> NewPostMortemTemplateDataType | None:
    if value is None:
        return None
    if value in NEW_POST_MORTEM_TEMPLATE_DATA_TYPE_VALUES:
        return cast(NewPostMortemTemplateDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_POST_MORTEM_TEMPLATE_DATA_TYPE_VALUES!r}")
