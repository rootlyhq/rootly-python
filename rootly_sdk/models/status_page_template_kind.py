from typing import Literal, cast

StatusPageTemplateKind = Literal["normal", "scheduled"]

STATUS_PAGE_TEMPLATE_KIND_VALUES: set[StatusPageTemplateKind] = {
    "normal",
    "scheduled",
}


def check_status_page_template_kind(value: str | None) -> StatusPageTemplateKind | None:
    if value is None:
        return None
    if value in STATUS_PAGE_TEMPLATE_KIND_VALUES:
        return cast(StatusPageTemplateKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEMPLATE_KIND_VALUES!r}")
