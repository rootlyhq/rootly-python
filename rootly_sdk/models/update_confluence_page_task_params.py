from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_confluence_page_task_params_task_type import (
    UpdateConfluencePageTaskParamsTaskType,
    check_update_confluence_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_confluence_page_task_params_template import UpdateConfluencePageTaskParamsTemplate


T = TypeVar("T", bound="UpdateConfluencePageTaskParams")


@_attrs_define
class UpdateConfluencePageTaskParams:
    """
    Attributes:
        file_id (str): The Confluence page ID
        task_type (Union[Unset, UpdateConfluencePageTaskParamsTaskType]):
        title (Union[Unset, str]): The Confluence page title
        content (Union[Unset, str]): The Confluence page content
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when updating page, if desired
        template (Union[Unset, UpdateConfluencePageTaskParamsTemplate]): The Confluence template to use
    """

    file_id: str
    task_type: Unset | UpdateConfluencePageTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    content: Unset | str = UNSET
    post_mortem_template_id: Unset | str = UNSET
    template: Union[Unset, "UpdateConfluencePageTaskParamsTemplate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        content = self.content

        post_mortem_template_id = self.post_mortem_template_id

        template: Unset | dict[str, Any] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

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
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_confluence_page_task_params_template import UpdateConfluencePageTaskParamsTemplate

        d = dict(src_dict)
        file_id = d.pop("file_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateConfluencePageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_confluence_page_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        _template = d.pop("template", UNSET)
        template: Unset | UpdateConfluencePageTaskParamsTemplate
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = UpdateConfluencePageTaskParamsTemplate.from_dict(_template)

        update_confluence_page_task_params = cls(
            file_id=file_id,
            task_type=task_type,
            title=title,
            content=content,
            post_mortem_template_id=post_mortem_template_id,
            template=template,
        )

        update_confluence_page_task_params.additional_properties = d
        return update_confluence_page_task_params

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
