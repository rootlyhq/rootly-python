from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_coda_page_task_params_task_type import (
    UpdateCodaPageTaskParamsTaskType,
    check_update_coda_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_coda_page_task_params_template import UpdateCodaPageTaskParamsTemplate


T = TypeVar("T", bound="UpdateCodaPageTaskParams")


@_attrs_define
class UpdateCodaPageTaskParams:
    """
    Attributes:
        page_id (str): The Coda page id
        task_type (Union[Unset, UpdateCodaPageTaskParamsTaskType]):
        doc_id (Union[Unset, str]): The Coda doc id
        title (Union[Unset, str]): The Coda page title
        subtitle (Union[Unset, str]): The Coda page subtitle
        content (Union[Unset, str]): The Coda page content
        template (Union[Unset, UpdateCodaPageTaskParamsTemplate]):
    """

    page_id: str
    task_type: Unset | UpdateCodaPageTaskParamsTaskType = UNSET
    doc_id: Unset | str = UNSET
    title: Unset | str = UNSET
    subtitle: Unset | str = UNSET
    content: Unset | str = UNSET
    template: Union[Unset, "UpdateCodaPageTaskParamsTemplate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_id = self.page_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        doc_id = self.doc_id

        title = self.title

        subtitle = self.subtitle

        content = self.content

        template: Unset | dict[str, Any] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_id": page_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if doc_id is not UNSET:
            field_dict["doc_id"] = doc_id
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if content is not UNSET:
            field_dict["content"] = content
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_coda_page_task_params_template import UpdateCodaPageTaskParamsTemplate

        d = dict(src_dict)
        page_id = d.pop("page_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateCodaPageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_coda_page_task_params_task_type(_task_type)

        doc_id = d.pop("doc_id", UNSET)

        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        content = d.pop("content", UNSET)

        _template = d.pop("template", UNSET)
        template: Unset | UpdateCodaPageTaskParamsTemplate
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = UpdateCodaPageTaskParamsTemplate.from_dict(_template)

        update_coda_page_task_params = cls(
            page_id=page_id,
            task_type=task_type,
            doc_id=doc_id,
            title=title,
            subtitle=subtitle,
            content=content,
            template=template,
        )

        update_coda_page_task_params.additional_properties = d
        return update_coda_page_task_params

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
