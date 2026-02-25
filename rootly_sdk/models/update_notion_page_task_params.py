from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_notion_page_task_params_task_type import (
    UpdateNotionPageTaskParamsTaskType,
    check_update_notion_page_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateNotionPageTaskParams")


@_attrs_define
class UpdateNotionPageTaskParams:
    """
    Attributes:
        file_id (str): The Notion page ID
        task_type (Union[Unset, UpdateNotionPageTaskParamsTaskType]):
        title (Union[Unset, str]): The Notion page title
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when creating page task, if desired
        content (Union[Unset, str]): Custom page content with liquid templating support. When provided, only this
            content will be rendered (no default sections)
        show_timeline_as_table (Union[Unset, bool]):
        show_action_items_as_table (Union[Unset, bool]):
    """

    file_id: str
    task_type: Unset | UpdateNotionPageTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    post_mortem_template_id: Unset | str = UNSET
    content: Unset | str = UNSET
    show_timeline_as_table: Unset | bool = UNSET
    show_action_items_as_table: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        post_mortem_template_id = self.post_mortem_template_id

        content = self.content

        show_timeline_as_table = self.show_timeline_as_table

        show_action_items_as_table = self.show_action_items_as_table

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if content is not UNSET:
            field_dict["content"] = content
        if show_timeline_as_table is not UNSET:
            field_dict["show_timeline_as_table"] = show_timeline_as_table
        if show_action_items_as_table is not UNSET:
            field_dict["show_action_items_as_table"] = show_action_items_as_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("file_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateNotionPageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_notion_page_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        content = d.pop("content", UNSET)

        show_timeline_as_table = d.pop("show_timeline_as_table", UNSET)

        show_action_items_as_table = d.pop("show_action_items_as_table", UNSET)

        update_notion_page_task_params = cls(
            file_id=file_id,
            task_type=task_type,
            title=title,
            post_mortem_template_id=post_mortem_template_id,
            content=content,
            show_timeline_as_table=show_timeline_as_table,
            show_action_items_as_table=show_action_items_as_table,
        )

        update_notion_page_task_params.additional_properties = d
        return update_notion_page_task_params

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
