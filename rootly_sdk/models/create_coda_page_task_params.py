from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_coda_page_task_params_task_type import (
    CreateCodaPageTaskParamsTaskType,
    check_create_coda_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_coda_page_task_params_doc import CreateCodaPageTaskParamsDoc
    from ..models.create_coda_page_task_params_template import CreateCodaPageTaskParamsTemplate


T = TypeVar("T", bound="CreateCodaPageTaskParams")


@_attrs_define
class CreateCodaPageTaskParams:
    """
    Attributes:
        title (str): The Coda page title
        task_type (CreateCodaPageTaskParamsTaskType | Unset):
        post_mortem_template_id (str | Unset): Retrospective template to use when creating page, if desired
        mark_post_mortem_as_published (bool | Unset):  Default: True.
        subtitle (str | Unset): The Coda page subtitle
        content (str | Unset): The Coda page content
        template (CreateCodaPageTaskParamsTemplate | Unset):
        folder_id (str | Unset): The Coda folder id
        doc (CreateCodaPageTaskParamsDoc | Unset): The Coda doc object with id and name
    """

    title: str
    task_type: CreateCodaPageTaskParamsTaskType | Unset = UNSET
    post_mortem_template_id: str | Unset = UNSET
    mark_post_mortem_as_published: bool | Unset = True
    subtitle: str | Unset = UNSET
    content: str | Unset = UNSET
    template: CreateCodaPageTaskParamsTemplate | Unset = UNSET
    folder_id: str | Unset = UNSET
    doc: CreateCodaPageTaskParamsDoc | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        post_mortem_template_id = self.post_mortem_template_id

        mark_post_mortem_as_published = self.mark_post_mortem_as_published

        subtitle = self.subtitle

        content = self.content

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        folder_id = self.folder_id

        doc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doc, Unset):
            doc = self.doc.to_dict()

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
        if mark_post_mortem_as_published is not UNSET:
            field_dict["mark_post_mortem_as_published"] = mark_post_mortem_as_published
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if content is not UNSET:
            field_dict["content"] = content
        if template is not UNSET:
            field_dict["template"] = template
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if doc is not UNSET:
            field_dict["doc"] = doc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_coda_page_task_params_doc import CreateCodaPageTaskParamsDoc
        from ..models.create_coda_page_task_params_template import CreateCodaPageTaskParamsTemplate

        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateCodaPageTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_coda_page_task_params_task_type(_task_type)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        mark_post_mortem_as_published = d.pop("mark_post_mortem_as_published", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        content = d.pop("content", UNSET)

        _template = d.pop("template", UNSET)
        template: CreateCodaPageTaskParamsTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = CreateCodaPageTaskParamsTemplate.from_dict(_template)

        folder_id = d.pop("folder_id", UNSET)

        _doc = d.pop("doc", UNSET)
        doc: CreateCodaPageTaskParamsDoc | Unset
        if isinstance(_doc, Unset):
            doc = UNSET
        else:
            doc = CreateCodaPageTaskParamsDoc.from_dict(_doc)

        create_coda_page_task_params = cls(
            title=title,
            task_type=task_type,
            post_mortem_template_id=post_mortem_template_id,
            mark_post_mortem_as_published=mark_post_mortem_as_published,
            subtitle=subtitle,
            content=content,
            template=template,
            folder_id=folder_id,
            doc=doc,
        )

        create_coda_page_task_params.additional_properties = d
        return create_coda_page_task_params

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
