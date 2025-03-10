from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resolve_alert_data_type import ResolveAlertDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolve_alert_data_attributes import ResolveAlertDataAttributes


T = TypeVar("T", bound="ResolveAlertData")


@_attrs_define
class ResolveAlertData:
    """
    Attributes:
        type_ (Union[Unset, ResolveAlertDataType]):
        attributes (Union[Unset, ResolveAlertDataAttributes]):
    """

    type_: Union[Unset, ResolveAlertDataType] = UNSET
    attributes: Union[Unset, "ResolveAlertDataAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.resolve_alert_data_attributes import ResolveAlertDataAttributes

        d = src_dict.copy()
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ResolveAlertDataType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ResolveAlertDataType(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ResolveAlertDataAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ResolveAlertDataAttributes.from_dict(_attributes)

        resolve_alert_data = cls(
            type_=type_,
            attributes=attributes,
        )

        resolve_alert_data.additional_properties = d
        return resolve_alert_data

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
