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
    from ..models.update_confluence_page_task_params_integration import UpdateConfluencePageTaskParamsIntegration
    from ..models.update_confluence_page_task_params_template import UpdateConfluencePageTaskParamsTemplate


T = TypeVar("T", bound="UpdateConfluencePageTaskParams")


@_attrs_define
class UpdateConfluencePageTaskParams:
    """
    Attributes:
        file_id (str): The Confluence page ID
        task_type (Union[Unset, UpdateConfluencePageTaskParamsTaskType]):
        integration (Union[Unset, UpdateConfluencePageTaskParamsIntegration]): Specify integration id if you have more
            than one Confluence instance
        title (Union[Unset, str]): The Confluence page title
        content (Union[Unset, str]): The Confluence page content
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when updating page, if desired
        template (Union[Unset, UpdateConfluencePageTaskParamsTemplate]): The Confluence template to use
        include_overview (Union[Unset, bool]):  Default: True.
        include_timeline (Union[Unset, bool]):  Default: True.
        include_follow_ups (Union[Unset, bool]):  Default: True.
    """

    file_id: str
    task_type: Union[Unset, UpdateConfluencePageTaskParamsTaskType] = UNSET
    integration: Union[Unset, "UpdateConfluencePageTaskParamsIntegration"] = UNSET
    title: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    post_mortem_template_id: Union[Unset, str] = UNSET
    template: Union[Unset, "UpdateConfluencePageTaskParamsTemplate"] = UNSET
    include_overview: Union[Unset, bool] = True
    include_timeline: Union[Unset, bool] = True
    include_follow_ups: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        integration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        title = self.title

        content = self.content

        post_mortem_template_id = self.post_mortem_template_id

        template: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        include_overview = self.include_overview

        include_timeline = self.include_timeline

        include_follow_ups = self.include_follow_ups

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
        if include_follow_ups is not UNSET:
            field_dict["include_follow_ups"] = include_follow_ups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_confluence_page_task_params_integration import UpdateConfluencePageTaskParamsIntegration
        from ..models.update_confluence_page_task_params_template import UpdateConfluencePageTaskParamsTemplate

        d = dict(src_dict)
        file_id = d.pop("file_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, UpdateConfluencePageTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_confluence_page_task_params_task_type(_task_type)

        _integration = d.pop("integration", UNSET)
        integration: Union[Unset, UpdateConfluencePageTaskParamsIntegration]
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = UpdateConfluencePageTaskParamsIntegration.from_dict(_integration)

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        _template = d.pop("template", UNSET)
        template: Union[Unset, UpdateConfluencePageTaskParamsTemplate]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = UpdateConfluencePageTaskParamsTemplate.from_dict(_template)

        include_overview = d.pop("include_overview", UNSET)

        include_timeline = d.pop("include_timeline", UNSET)

        include_follow_ups = d.pop("include_follow_ups", UNSET)

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
            include_follow_ups=include_follow_ups,
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
