from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.attach_alert_data_type import AttachAlertDataType, check_attach_alert_data_type

if TYPE_CHECKING:
    from ..models.attach_alert_data_attributes import AttachAlertDataAttributes


T = TypeVar("T", bound="AttachAlertData")


@_attrs_define
class AttachAlertData:
    """
    Attributes:
        type_ (AttachAlertDataType):
        attributes (AttachAlertDataAttributes):
    """

    type_: AttachAlertDataType
    attributes: AttachAlertDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attach_alert_data_attributes import AttachAlertDataAttributes

        d = dict(src_dict)
        type_ = check_attach_alert_data_type(d.pop("type"))

        attributes = AttachAlertDataAttributes.from_dict(d.pop("attributes"))

        attach_alert_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return attach_alert_data
