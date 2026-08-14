from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.receipt_reason import ReceiptReason, check_receipt_reason
from ..models.receipt_state import ReceiptState, check_receipt_state
from ..types import UNSET, Unset

T = TypeVar("T", bound="Receipt")


@_attrs_define
class Receipt:
    """
    Attributes:
        state (ReceiptState): Delivery state of the receipt.
        reason (Union[Unset, ReceiptReason]): Reason a receipt failed. Present when state is failed.
        resource_type (Union[Unset, str]): Type of the referenced resource (present when set).
        resource_id (Union[Unset, str]): ID of the referenced resource (present when set).
    """

    state: ReceiptState
    reason: Union[Unset, ReceiptReason] = UNSET
    resource_type: Union[Unset, str] = UNSET
    resource_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str = self.state

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        resource_type = self.resource_type

        resource_id = self.resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = check_receipt_state(d.pop("state"))

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ReceiptReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_receipt_reason(_reason)

        resource_type = d.pop("resource_type", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        receipt = cls(
            state=state,
            reason=reason,
            resource_type=resource_type,
            resource_id=resource_id,
        )

        receipt.additional_properties = d
        return receipt

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
