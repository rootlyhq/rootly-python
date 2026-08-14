from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_incident_role_task_data_type import (
    UpdateIncidentRoleTaskDataType,
    check_update_incident_role_task_data_type,
)

if TYPE_CHECKING:
    from ..models.update_incident_role_task_data_attributes import UpdateIncidentRoleTaskDataAttributes


T = TypeVar("T", bound="UpdateIncidentRoleTaskData")


@_attrs_define
class UpdateIncidentRoleTaskData:
    """
    Attributes:
        type_ (UpdateIncidentRoleTaskDataType):
        attributes (UpdateIncidentRoleTaskDataAttributes):
    """

    type_: UpdateIncidentRoleTaskDataType
    attributes: "UpdateIncidentRoleTaskDataAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_incident_role_task_data_attributes import UpdateIncidentRoleTaskDataAttributes

        d = dict(src_dict)
        type_ = check_update_incident_role_task_data_type(d.pop("type"))

        attributes = UpdateIncidentRoleTaskDataAttributes.from_dict(d.pop("attributes"))

        update_incident_role_task_data = cls(
            type_=type_,
            attributes=attributes,
        )

        update_incident_role_task_data.additional_properties = d
        return update_incident_role_task_data

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
