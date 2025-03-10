from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_incident_permission_set_boolean_data_type import UpdateIncidentPermissionSetBooleanDataType

if TYPE_CHECKING:
    from ..models.update_incident_permission_set_boolean_data_attributes import (
        UpdateIncidentPermissionSetBooleanDataAttributes,
    )


T = TypeVar("T", bound="UpdateIncidentPermissionSetBooleanData")


@_attrs_define
class UpdateIncidentPermissionSetBooleanData:
    """
    Attributes:
        type_ (UpdateIncidentPermissionSetBooleanDataType):
        attributes (UpdateIncidentPermissionSetBooleanDataAttributes):
    """

    type_: UpdateIncidentPermissionSetBooleanDataType
    attributes: "UpdateIncidentPermissionSetBooleanDataAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_incident_permission_set_boolean_data_attributes import (
            UpdateIncidentPermissionSetBooleanDataAttributes,
        )

        d = src_dict.copy()
        type_ = UpdateIncidentPermissionSetBooleanDataType(d.pop("type"))

        attributes = UpdateIncidentPermissionSetBooleanDataAttributes.from_dict(d.pop("attributes"))

        update_incident_permission_set_boolean_data = cls(
            type_=type_,
            attributes=attributes,
        )

        update_incident_permission_set_boolean_data.additional_properties = d
        return update_incident_permission_set_boolean_data

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
