from typing import Literal, cast

NewPostMortemTemplateDataAttributesFormat = Literal["html", "markdown"]

NEW_POST_MORTEM_TEMPLATE_DATA_ATTRIBUTES_FORMAT_VALUES: set[NewPostMortemTemplateDataAttributesFormat] = {
    "html",
    "markdown",
}


def check_new_post_mortem_template_data_attributes_format(value: str | None) -> NewPostMortemTemplateDataAttributesFormat | None:
    if value is None:
        return None
    if value in NEW_POST_MORTEM_TEMPLATE_DATA_ATTRIBUTES_FORMAT_VALUES:
        return cast(NewPostMortemTemplateDataAttributesFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_POST_MORTEM_TEMPLATE_DATA_ATTRIBUTES_FORMAT_VALUES!r}"
    )
