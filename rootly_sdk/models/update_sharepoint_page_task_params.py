from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_sharepoint_page_task_params_task_type import (
    UpdateSharepointPageTaskParamsTaskType,
    check_update_sharepoint_page_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSharepointPageTaskParams")


@_attrs_define
class UpdateSharepointPageTaskParams:
    """
    Attributes:
        file_id (str): The SharePoint file ID
        task_type (Union[Unset, UpdateSharepointPageTaskParamsTaskType]):
        title (Union[Unset, str]): The SharePoint document title
        content (Union[Unset, str]): The SharePoint document content
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when updating document, if desired
    """

    file_id: str
    task_type: Unset | UpdateSharepointPageTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    content: Unset | str = UNSET
    post_mortem_template_id: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        content = self.content

        post_mortem_template_id = self.post_mortem_template_id

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
        if content is not UNSET:
            field_dict["content"] = content
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("file_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateSharepointPageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_sharepoint_page_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        update_sharepoint_page_task_params = cls(
            file_id=file_id,
            task_type=task_type,
            title=title,
            content=content,
            post_mortem_template_id=post_mortem_template_id,
        )

        update_sharepoint_page_task_params.additional_properties = d
        return update_sharepoint_page_task_params

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
