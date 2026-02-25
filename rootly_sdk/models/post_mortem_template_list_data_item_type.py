from typing import Literal, cast

PostMortemTemplateListDataItemType = Literal["post_mortem_templates"]

POST_MORTEM_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES: set[PostMortemTemplateListDataItemType] = {
    "post_mortem_templates",
}


def check_post_mortem_template_list_data_item_type(value: str | None) -> PostMortemTemplateListDataItemType | None:
    if value is None:
        return None
    if value in POST_MORTEM_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(PostMortemTemplateListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TEMPLATE_LIST_DATA_ITEM_TYPE_VALUES!r}")
