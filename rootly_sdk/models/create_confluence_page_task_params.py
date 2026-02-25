from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_confluence_page_task_params_task_type import (
    CreateConfluencePageTaskParamsTaskType,
    check_create_confluence_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_confluence_page_task_params_ancestor import CreateConfluencePageTaskParamsAncestor
    from ..models.create_confluence_page_task_params_integration import CreateConfluencePageTaskParamsIntegration
    from ..models.create_confluence_page_task_params_space import CreateConfluencePageTaskParamsSpace
    from ..models.create_confluence_page_task_params_template import CreateConfluencePageTaskParamsTemplate


T = TypeVar("T", bound="CreateConfluencePageTaskParams")


@_attrs_define
class CreateConfluencePageTaskParams:
    """
    Attributes:
        space (CreateConfluencePageTaskParamsSpace):
        title (str): The page title
        task_type (Union[Unset, CreateConfluencePageTaskParamsTaskType]):
        integration (Union[Unset, CreateConfluencePageTaskParamsIntegration]): Specify integration id if you have more
            than one Confluence instance
        ancestor (Union[Unset, CreateConfluencePageTaskParamsAncestor]):
        template (Union[Unset, CreateConfluencePageTaskParamsTemplate]):
        content (Union[Unset, str]): The page content
        post_mortem_template_id (Union[Unset, str]): The Retrospective template to use
        mark_post_mortem_as_published (Union[Unset, bool]):  Default: True.
    """

    space: "CreateConfluencePageTaskParamsSpace"
    title: str
    task_type: Unset | CreateConfluencePageTaskParamsTaskType = UNSET
    integration: Union[Unset, "CreateConfluencePageTaskParamsIntegration"] = UNSET
    ancestor: Union[Unset, "CreateConfluencePageTaskParamsAncestor"] = UNSET
    template: Union[Unset, "CreateConfluencePageTaskParamsTemplate"] = UNSET
    content: Unset | str = UNSET
    post_mortem_template_id: Unset | str = UNSET
    mark_post_mortem_as_published: Unset | bool = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        space = self.space.to_dict()

        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        integration: Unset | dict[str, Any] = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        ancestor: Unset | dict[str, Any] = UNSET
        if not isinstance(self.ancestor, Unset):
            ancestor = self.ancestor.to_dict()

        template: Unset | dict[str, Any] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        content = self.content

        post_mortem_template_id = self.post_mortem_template_id

        mark_post_mortem_as_published = self.mark_post_mortem_as_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "space": space,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if integration is not UNSET:
            field_dict["integration"] = integration
        if ancestor is not UNSET:
            field_dict["ancestor"] = ancestor
        if template is not UNSET:
            field_dict["template"] = template
        if content is not UNSET:
            field_dict["content"] = content
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if mark_post_mortem_as_published is not UNSET:
            field_dict["mark_post_mortem_as_published"] = mark_post_mortem_as_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_confluence_page_task_params_ancestor import CreateConfluencePageTaskParamsAncestor
        from ..models.create_confluence_page_task_params_integration import CreateConfluencePageTaskParamsIntegration
        from ..models.create_confluence_page_task_params_space import CreateConfluencePageTaskParamsSpace
        from ..models.create_confluence_page_task_params_template import CreateConfluencePageTaskParamsTemplate

        d = dict(src_dict)
        space = CreateConfluencePageTaskParamsSpace.from_dict(d.pop("space"))

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateConfluencePageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_confluence_page_task_params_task_type(_task_type)

        _integration = d.pop("integration", UNSET)
        integration: Unset | CreateConfluencePageTaskParamsIntegration
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = CreateConfluencePageTaskParamsIntegration.from_dict(_integration)

        _ancestor = d.pop("ancestor", UNSET)
        ancestor: Unset | CreateConfluencePageTaskParamsAncestor
        if isinstance(_ancestor, Unset):
            ancestor = UNSET
        else:
            ancestor = CreateConfluencePageTaskParamsAncestor.from_dict(_ancestor)

        _template = d.pop("template", UNSET)
        template: Unset | CreateConfluencePageTaskParamsTemplate
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = CreateConfluencePageTaskParamsTemplate.from_dict(_template)

        content = d.pop("content", UNSET)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        mark_post_mortem_as_published = d.pop("mark_post_mortem_as_published", UNSET)

        create_confluence_page_task_params = cls(
            space=space,
            title=title,
            task_type=task_type,
            integration=integration,
            ancestor=ancestor,
            template=template,
            content=content,
            post_mortem_template_id=post_mortem_template_id,
            mark_post_mortem_as_published=mark_post_mortem_as_published,
        )

        create_confluence_page_task_params.additional_properties = d
        return create_confluence_page_task_params

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
