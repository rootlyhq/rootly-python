from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_quip_page_task_params_task_type import (
    CreateQuipPageTaskParamsTaskType,
    check_create_quip_page_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateQuipPageTaskParams")


@_attrs_define
class CreateQuipPageTaskParams:
    """
    Attributes:
        title (str): The page title
        task_type (Union[Unset, CreateQuipPageTaskParamsTaskType]):
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when creating page, if desired
        parent_folder_id (Union[Unset, str]): The parent folder id
        content (Union[Unset, str]): The page content
        template_id (Union[Unset, str]): The Quip file ID to use as a template
        mark_post_mortem_as_published (Union[Unset, bool]):  Default: True.
    """

    title: str
    task_type: Unset | CreateQuipPageTaskParamsTaskType = UNSET
    post_mortem_template_id: Unset | str = UNSET
    parent_folder_id: Unset | str = UNSET
    content: Unset | str = UNSET
    template_id: Unset | str = UNSET
    mark_post_mortem_as_published: Unset | bool = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        post_mortem_template_id = self.post_mortem_template_id

        parent_folder_id = self.parent_folder_id

        content = self.content

        template_id = self.template_id

        mark_post_mortem_as_published = self.mark_post_mortem_as_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if parent_folder_id is not UNSET:
            field_dict["parent_folder_id"] = parent_folder_id
        if content is not UNSET:
            field_dict["content"] = content
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if mark_post_mortem_as_published is not UNSET:
            field_dict["mark_post_mortem_as_published"] = mark_post_mortem_as_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateQuipPageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_quip_page_task_params_task_type(_task_type)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        parent_folder_id = d.pop("parent_folder_id", UNSET)

        content = d.pop("content", UNSET)

        template_id = d.pop("template_id", UNSET)

        mark_post_mortem_as_published = d.pop("mark_post_mortem_as_published", UNSET)

        create_quip_page_task_params = cls(
            title=title,
            task_type=task_type,
            post_mortem_template_id=post_mortem_template_id,
            parent_folder_id=parent_folder_id,
            content=content,
            template_id=template_id,
            mark_post_mortem_as_published=mark_post_mortem_as_published,
        )

        create_quip_page_task_params.additional_properties = d
        return create_quip_page_task_params

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
