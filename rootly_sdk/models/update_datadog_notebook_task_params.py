from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_datadog_notebook_task_params_kind import (
    UpdateDatadogNotebookTaskParamsKind,
    check_update_datadog_notebook_task_params_kind,
)
from ..models.update_datadog_notebook_task_params_task_type import (
    UpdateDatadogNotebookTaskParamsTaskType,
    check_update_datadog_notebook_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_datadog_notebook_task_params_template import UpdateDatadogNotebookTaskParamsTemplate


T = TypeVar("T", bound="UpdateDatadogNotebookTaskParams")


@_attrs_define
class UpdateDatadogNotebookTaskParams:
    """
    Attributes:
        file_id (str): The Datadog notebook ID
        task_type (Union[Unset, UpdateDatadogNotebookTaskParamsTaskType]):
        title (Union[Unset, str]): The Datadog notebook title
        content (Union[Unset, str]): The Datadog notebook content
        kind (Union[Unset, UpdateDatadogNotebookTaskParamsKind]): The notebook type
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when updating notebook, if desired
        template (Union[Unset, UpdateDatadogNotebookTaskParamsTemplate]): The Datadog notebook template to use
    """

    file_id: str
    task_type: Unset | UpdateDatadogNotebookTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    content: Unset | str = UNSET
    kind: Unset | UpdateDatadogNotebookTaskParamsKind = UNSET
    post_mortem_template_id: Unset | str = UNSET
    template: Union[Unset, "UpdateDatadogNotebookTaskParamsTemplate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        content = self.content

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_datadog_notebook_task_params_template import UpdateDatadogNotebookTaskParamsTemplate

        d = dict(src_dict)
        file_id = d.pop("file_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateDatadogNotebookTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_datadog_notebook_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Unset | UpdateDatadogNotebookTaskParamsKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_datadog_notebook_task_params_kind(_kind)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        _template = d.pop("template", UNSET)
        template: Unset | UpdateDatadogNotebookTaskParamsTemplate
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = UpdateDatadogNotebookTaskParamsTemplate.from_dict(_template)

        update_datadog_notebook_task_params = cls(
            file_id=file_id,
            task_type=task_type,
            title=title,
            content=content,
            kind=kind,
            post_mortem_template_id=post_mortem_template_id,
            template=template,
        )

        update_datadog_notebook_task_params.additional_properties = d
        return update_datadog_notebook_task_params

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
