from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_confluence_page_task_params_task_type import (
    UpdateConfluencePageTaskParamsTaskType,
    check_update_confluence_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_confluence_page_task_params_integration import UpdateConfluencePageTaskParamsIntegration
    from ..models.update_confluence_page_task_params_template import UpdateConfluencePageTaskParamsTemplate


T = TypeVar("T", bound="UpdateConfluencePageTaskParams")


@_attrs_define
class UpdateConfluencePageTaskParams:
    """
    Attributes:
        file_id (str): The Confluence page ID
        task_type (UpdateConfluencePageTaskParamsTaskType | Unset):
        integration (UpdateConfluencePageTaskParamsIntegration | Unset): Specify integration id if you have more than
            one Confluence instance
        title (str | Unset): The Confluence page title
        content (str | Unset): The Confluence page content
        post_mortem_template_id (str | Unset): Retrospective template to use when updating page, if desired
        template (UpdateConfluencePageTaskParamsTemplate | Unset): The Confluence template to use
        include_overview (bool | Unset):  Default: True.
        include_timeline (bool | Unset):  Default: True.
    """

    file_id: str
    task_type: UpdateConfluencePageTaskParamsTaskType | Unset = UNSET
    integration: UpdateConfluencePageTaskParamsIntegration | Unset = UNSET
    title: str | Unset = UNSET
    content: str | Unset = UNSET
    post_mortem_template_id: str | Unset = UNSET
    template: UpdateConfluencePageTaskParamsTemplate | Unset = UNSET
    include_overview: bool | Unset = True
    include_timeline: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        file_id = self.file_id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        integration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        title = self.title

        content = self.content

        post_mortem_template_id = self.post_mortem_template_id

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        include_overview = self.include_overview

        include_timeline = self.include_timeline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if integration is not UNSET:
            field_dict["integration"] = integration
        if title is not UNSET:
            field_dict["title"] = title
        if content is not UNSET:
            field_dict["content"] = content
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if template is not UNSET:
            field_dict["template"] = template
        if include_overview is not UNSET:
            field_dict["include_overview"] = include_overview
        if include_timeline is not UNSET:
            field_dict["include_timeline"] = include_timeline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_confluence_page_task_params_integration import UpdateConfluencePageTaskParamsIntegration
        from ..models.update_confluence_page_task_params_template import UpdateConfluencePageTaskParamsTemplate

        d = dict(src_dict)
        file_id = d.pop("file_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: UpdateConfluencePageTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_confluence_page_task_params_task_type(_task_type)

        _integration = d.pop("integration", UNSET)
        integration: UpdateConfluencePageTaskParamsIntegration | Unset
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = UpdateConfluencePageTaskParamsIntegration.from_dict(_integration)

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        _template = d.pop("template", UNSET)
        template: UpdateConfluencePageTaskParamsTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = UpdateConfluencePageTaskParamsTemplate.from_dict(_template)

        include_overview = d.pop("include_overview", UNSET)

        include_timeline = d.pop("include_timeline", UNSET)

        update_confluence_page_task_params = cls(
            file_id=file_id,
            task_type=task_type,
            integration=integration,
            title=title,
            content=content,
            post_mortem_template_id=post_mortem_template_id,
            template=template,
            include_overview=include_overview,
            include_timeline=include_timeline,
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
