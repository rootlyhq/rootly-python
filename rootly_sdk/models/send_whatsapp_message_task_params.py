from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_whatsapp_message_task_params_task_type import (
    SendWhatsappMessageTaskParamsTaskType,
    check_send_whatsapp_message_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendWhatsappMessageTaskParams")


@_attrs_define
class SendWhatsappMessageTaskParams:
    """
    Attributes:
        phone_numbers (list[str]):
        name (str): The name
        content (str): The WhatsApp message
        task_type (Union[Unset, SendWhatsappMessageTaskParamsTaskType]):
    """

    phone_numbers: list[str]
    name: str
    content: str
    task_type: Unset | SendWhatsappMessageTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_numbers = self.phone_numbers

        name = self.name

        content = self.content

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_numbers": phone_numbers,
                "name": name,
                "content": content,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone_numbers = cast(list[str], d.pop("phone_numbers"))

        name = d.pop("name")

        content = d.pop("content")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | SendWhatsappMessageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_send_whatsapp_message_task_params_task_type(_task_type)

        send_whatsapp_message_task_params = cls(
            phone_numbers=phone_numbers,
            name=name,
            content=content,
            task_type=task_type,
        )

        send_whatsapp_message_task_params.additional_properties = d
        return send_whatsapp_message_task_params

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
