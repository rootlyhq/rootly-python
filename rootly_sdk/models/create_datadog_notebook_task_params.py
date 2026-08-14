from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_datadog_notebook_task_params_kind import (
    CreateDatadogNotebookTaskParamsKind,
    check_create_datadog_notebook_task_params_kind,
)
from ..models.create_datadog_notebook_task_params_task_type import (
    CreateDatadogNotebookTaskParamsTaskType,
    check_create_datadog_notebook_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_datadog_notebook_task_params_template import CreateDatadogNotebookTaskParamsTemplate


T = TypeVar("T", bound="CreateDatadogNotebookTaskParams")


@_attrs_define
class CreateDatadogNotebookTaskParams:
    """
    Attributes:
        title (str): The notebook title
        kind (CreateDatadogNotebookTaskParamsKind): The notebook kind
        task_type (Union[Unset, CreateDatadogNotebookTaskParamsTaskType]):
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when creating notebook, if desired
        mark_post_mortem_as_published (Union[Unset, bool]):  Default: True.
        template (Union[Unset, CreateDatadogNotebookTaskParamsTemplate]):
        content (Union[Unset, str]): The notebook content
    """

    title: str
    kind: CreateDatadogNotebookTaskParamsKind
    task_type: Unset | CreateDatadogNotebookTaskParamsTaskType = UNSET
    post_mortem_template_id: Unset | str = UNSET
    mark_post_mortem_as_published: Unset | bool = True
    template: Union[Unset, "CreateDatadogNotebookTaskParamsTemplate"] = UNSET
    content: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        kind: str = self.kind

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        post_mortem_template_id = self.post_mortem_template_id

        mark_post_mortem_as_published = self.mark_post_mortem_as_published

        template: Unset | dict[str, Any] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "kind": kind,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if mark_post_mortem_as_published is not UNSET:
            field_dict["mark_post_mortem_as_published"] = mark_post_mortem_as_published
        if template is not UNSET:
            field_dict["template"] = template
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_datadog_notebook_task_params_template import CreateDatadogNotebookTaskParamsTemplate

        d = dict(src_dict)
        title = d.pop("title")

        kind = check_create_datadog_notebook_task_params_kind(d.pop("kind"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateDatadogNotebookTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_datadog_notebook_task_params_task_type(_task_type)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        mark_post_mortem_as_published = d.pop("mark_post_mortem_as_published", UNSET)

        _template = d.pop("template", UNSET)
        template: Unset | CreateDatadogNotebookTaskParamsTemplate
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = CreateDatadogNotebookTaskParamsTemplate.from_dict(_template)

        content = d.pop("content", UNSET)

        create_datadog_notebook_task_params = cls(
            title=title,
            kind=kind,
            task_type=task_type,
            post_mortem_template_id=post_mortem_template_id,
            mark_post_mortem_as_published=mark_post_mortem_as_published,
            template=template,
            content=content,
        )

        create_datadog_notebook_task_params.additional_properties = d
        return create_datadog_notebook_task_params

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
