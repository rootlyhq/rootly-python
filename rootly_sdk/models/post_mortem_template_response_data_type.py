from typing import Literal, cast

PostMortemTemplateResponseDataType = Literal["post_mortem_templates"]

POST_MORTEM_TEMPLATE_RESPONSE_DATA_TYPE_VALUES: set[PostMortemTemplateResponseDataType] = {
    "post_mortem_templates",
}


def check_post_mortem_template_response_data_type(value: str | None) -> PostMortemTemplateResponseDataType | None:
    if value is None:
        return None
    if value in POST_MORTEM_TEMPLATE_RESPONSE_DATA_TYPE_VALUES:
        return cast(PostMortemTemplateResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TEMPLATE_RESPONSE_DATA_TYPE_VALUES!r}")
