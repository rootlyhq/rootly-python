from typing import Literal, cast

PostMortemTemplateFormat = Literal["html", "markdown"]

POST_MORTEM_TEMPLATE_FORMAT_VALUES: set[PostMortemTemplateFormat] = {
    "html",
    "markdown",
}


def check_post_mortem_template_format(value: str | None) -> PostMortemTemplateFormat | None:
    if value is None:
        return None
    if value in POST_MORTEM_TEMPLATE_FORMAT_VALUES:
        return cast(PostMortemTemplateFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TEMPLATE_FORMAT_VALUES!r}")
