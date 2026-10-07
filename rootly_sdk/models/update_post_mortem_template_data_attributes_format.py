from typing import Literal

UpdatePostMortemTemplateDataAttributesFormat = Literal["html", "markdown"]

UPDATE_POST_MORTEM_TEMPLATE_DATA_ATTRIBUTES_FORMAT_VALUES: set[UpdatePostMortemTemplateDataAttributesFormat] = {
    "html",
    "markdown",
}


def check_update_post_mortem_template_data_attributes_format(
    value: str | None,
) -> UpdatePostMortemTemplateDataAttributesFormat | None:
    if value is None:
        return None
    if value in UPDATE_POST_MORTEM_TEMPLATE_DATA_ATTRIBUTES_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_POST_MORTEM_TEMPLATE_DATA_ATTRIBUTES_FORMAT_VALUES!r}"
    )
