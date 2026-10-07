from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.acknowledge_alert_data_type import AcknowledgeAlertDataType, check_acknowledge_alert_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledge_alert_data_attributes import AcknowledgeAlertDataAttributes


T = TypeVar("T", bound="AcknowledgeAlertData")


@_attrs_define
class AcknowledgeAlertData:
    """
    Attributes:
        type_ (AcknowledgeAlertDataType | Unset):
        attributes (AcknowledgeAlertDataAttributes | Unset):
    """

    type_: AcknowledgeAlertDataType | Unset = UNSET
    attributes: AcknowledgeAlertDataAttributes | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acknowledge_alert_data_attributes import AcknowledgeAlertDataAttributes

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AcknowledgeAlertDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_acknowledge_alert_data_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: AcknowledgeAlertDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = AcknowledgeAlertDataAttributes.from_dict(_attributes)

        acknowledge_alert_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return acknowledge_alert_data
