from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attach_retrospective_pdf_to_freshservice_ticket_task_params_task_type import (
    AttachRetrospectivePdfToFreshserviceTicketTaskParamsTaskType,
    check_attach_retrospective_pdf_to_freshservice_ticket_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachRetrospectivePdfToFreshserviceTicketTaskParams")


@_attrs_define
class AttachRetrospectivePdfToFreshserviceTicketTaskParams:
    """
    Attributes:
        ticket_id (str): The Freshservice ticket id
        task_type (Union[Unset, AttachRetrospectivePdfToFreshserviceTicketTaskParamsTaskType]):
        filename (Union[Unset, str]): The attachment filename
    """

    ticket_id: str
    task_type: Unset | AttachRetrospectivePdfToFreshserviceTicketTaskParamsTaskType = UNSET
    filename: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticket_id = self.ticket_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticket_id": ticket_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticket_id = d.pop("ticket_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AttachRetrospectivePdfToFreshserviceTicketTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_attach_retrospective_pdf_to_freshservice_ticket_task_params_task_type(_task_type)

        filename = d.pop("filename", UNSET)

        attach_retrospective_pdf_to_freshservice_ticket_task_params = cls(
            ticket_id=ticket_id,
            task_type=task_type,
            filename=filename,
        )

        attach_retrospective_pdf_to_freshservice_ticket_task_params.additional_properties = d
        return attach_retrospective_pdf_to_freshservice_ticket_task_params

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
