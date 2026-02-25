from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_pulse_data_type import UpdatePulseDataType, check_update_pulse_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_pulse_data_attributes import UpdatePulseDataAttributes


T = TypeVar("T", bound="UpdatePulseData")


@_attrs_define
class UpdatePulseData:
    """
    Attributes:
        attributes (UpdatePulseDataAttributes):
        type_ (Union[Unset, UpdatePulseDataType]):
    """

    attributes: "UpdatePulseDataAttributes"
    type_: Unset | UpdatePulseDataType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_pulse_data_attributes import UpdatePulseDataAttributes

        d = dict(src_dict)
        attributes = UpdatePulseDataAttributes.from_dict(d.pop("attributes"))

        _type_ = d.pop("type", UNSET)
        type_: Unset | UpdatePulseDataType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_update_pulse_data_type(_type_)

        update_pulse_data = cls(
            attributes=attributes,
            type_=type_,
        )

        update_pulse_data.additional_properties = d
        return update_pulse_data

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
