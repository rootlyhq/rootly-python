from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alert_data_type import UpdateAlertDataType, check_update_alert_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_data_attributes import UpdateAlertDataAttributes


T = TypeVar("T", bound="UpdateAlertData")


@_attrs_define
class UpdateAlertData:
    """
    Attributes:
        attributes (UpdateAlertDataAttributes):
        type_ (Union[Unset, UpdateAlertDataType]):
    """

    attributes: "UpdateAlertDataAttributes"
    type_: Unset | UpdateAlertDataType = UNSET
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
        from ..models.update_alert_data_attributes import UpdateAlertDataAttributes

        d = dict(src_dict)
        attributes = UpdateAlertDataAttributes.from_dict(d.pop("attributes"))

        _type_ = d.pop("type", UNSET)
        type_: Unset | UpdateAlertDataType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_update_alert_data_type(_type_)

        update_alert_data = cls(
            attributes=attributes,
            type_=type_,
        )

        update_alert_data.additional_properties = d
        return update_alert_data

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
