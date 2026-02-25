from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_notion_page_task_params_task_type import (
    CreateNotionPageTaskParamsTaskType,
    check_create_notion_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_notion_page_task_params_parent_page import CreateNotionPageTaskParamsParentPage


T = TypeVar("T", bound="CreateNotionPageTaskParams")


@_attrs_define
class CreateNotionPageTaskParams:
    """
    Attributes:
        title (str): The Notion page title
        parent_page (CreateNotionPageTaskParamsParentPage): The parent page id and display name
        task_type (Union[Unset, CreateNotionPageTaskParamsTaskType]):
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when creating page task, if desired
        content (Union[Unset, str]): Custom page content with liquid templating support. When provided, only this
            content will be rendered (no default sections)
        mark_post_mortem_as_published (Union[Unset, bool]):  Default: True.
        show_timeline_as_table (Union[Unset, bool]):
        show_action_items_as_table (Union[Unset, bool]):
    """

    title: str
    parent_page: "CreateNotionPageTaskParamsParentPage"
    task_type: Unset | CreateNotionPageTaskParamsTaskType = UNSET
    post_mortem_template_id: Unset | str = UNSET
    content: Unset | str = UNSET
    mark_post_mortem_as_published: Unset | bool = True
    show_timeline_as_table: Unset | bool = UNSET
    show_action_items_as_table: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        parent_page = self.parent_page.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        post_mortem_template_id = self.post_mortem_template_id

        content = self.content

        mark_post_mortem_as_published = self.mark_post_mortem_as_published

        show_timeline_as_table = self.show_timeline_as_table

        show_action_items_as_table = self.show_action_items_as_table

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "parent_page": parent_page,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if content is not UNSET:
            field_dict["content"] = content
        if mark_post_mortem_as_published is not UNSET:
            field_dict["mark_post_mortem_as_published"] = mark_post_mortem_as_published
        if show_timeline_as_table is not UNSET:
            field_dict["show_timeline_as_table"] = show_timeline_as_table
        if show_action_items_as_table is not UNSET:
            field_dict["show_action_items_as_table"] = show_action_items_as_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_notion_page_task_params_parent_page import CreateNotionPageTaskParamsParentPage

        d = dict(src_dict)
        title = d.pop("title")

        parent_page = CreateNotionPageTaskParamsParentPage.from_dict(d.pop("parent_page"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateNotionPageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_notion_page_task_params_task_type(_task_type)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        content = d.pop("content", UNSET)

        mark_post_mortem_as_published = d.pop("mark_post_mortem_as_published", UNSET)

        show_timeline_as_table = d.pop("show_timeline_as_table", UNSET)

        show_action_items_as_table = d.pop("show_action_items_as_table", UNSET)

        create_notion_page_task_params = cls(
            title=title,
            parent_page=parent_page,
            task_type=task_type,
            post_mortem_template_id=post_mortem_template_id,
            content=content,
            mark_post_mortem_as_published=mark_post_mortem_as_published,
            show_timeline_as_table=show_timeline_as_table,
            show_action_items_as_table=show_action_items_as_table,
        )

        create_notion_page_task_params.additional_properties = d
        return create_notion_page_task_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
