from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.restart_incident_data_type import RestartIncidentDataType, check_restart_incident_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.restart_incident_data_attributes import RestartIncidentDataAttributes


T = TypeVar("T", bound="RestartIncidentData")


@_attrs_define
class RestartIncidentData:
    """
    Attributes:
        type_ (RestartIncidentDataType):
        attributes (Union[Unset, RestartIncidentDataAttributes]):
    """

    type_: RestartIncidentDataType
    attributes: Union[Unset, "RestartIncidentDataAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restart_incident_data_attributes import RestartIncidentDataAttributes

        d = dict(src_dict)
        type_ = check_restart_incident_data_type(d.pop("type"))

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | RestartIncidentDataAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RestartIncidentDataAttributes.from_dict(_attributes)

        restart_incident_data = cls(
            type_=type_,
            attributes=attributes,
        )

        restart_incident_data.additional_properties = d
        return restart_incident_data

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
