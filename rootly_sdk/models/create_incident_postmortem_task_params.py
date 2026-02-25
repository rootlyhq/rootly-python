from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_incident_postmortem_task_params_task_type import (
    CreateIncidentPostmortemTaskParamsTaskType,
    check_create_incident_postmortem_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_incident_postmortem_task_params_template_type_0 import (
        CreateIncidentPostmortemTaskParamsTemplateType0,
    )


T = TypeVar("T", bound="CreateIncidentPostmortemTaskParams")


@_attrs_define
class CreateIncidentPostmortemTaskParams:
    """
    Attributes:
        incident_id (str): UUID of the incident that needs a retrospective
        title (str): The retrospective title
        task_type (Union[Unset, CreateIncidentPostmortemTaskParamsTaskType]):
        status (Union[None, Unset, str]):
        template (Union['CreateIncidentPostmortemTaskParamsTemplateType0', None, Unset]): Retrospective template to use
    """

    incident_id: str
    title: str
    task_type: Unset | CreateIncidentPostmortemTaskParamsTaskType = UNSET
    status: None | Unset | str = UNSET
    template: Union["CreateIncidentPostmortemTaskParamsTemplateType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_incident_postmortem_task_params_template_type_0 import (
            CreateIncidentPostmortemTaskParamsTemplateType0,
        )

        incident_id = self.incident_id

        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        status: None | Unset | str
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        template: None | Unset | dict[str, Any]
        if isinstance(self.template, Unset):
            template = UNSET
        elif isinstance(self.template, CreateIncidentPostmortemTaskParamsTemplateType0):
            template = self.template.to_dict()
        else:
            template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if status is not UNSET:
            field_dict["status"] = status
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_incident_postmortem_task_params_template_type_0 import (
            CreateIncidentPostmortemTaskParamsTemplateType0,
        )

        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateIncidentPostmortemTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_incident_postmortem_task_params_task_type(_task_type)

        def _parse_status(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_template(data: object) -> Union["CreateIncidentPostmortemTaskParamsTemplateType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_0 = CreateIncidentPostmortemTaskParamsTemplateType0.from_dict(data)

                return template_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CreateIncidentPostmortemTaskParamsTemplateType0", None, Unset], data)

        template = _parse_template(d.pop("template", UNSET))

        create_incident_postmortem_task_params = cls(
            incident_id=incident_id,
            title=title,
            task_type=task_type,
            status=status,
            template=template,
        )

        create_incident_postmortem_task_params.additional_properties = d
        return create_incident_postmortem_task_params

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
