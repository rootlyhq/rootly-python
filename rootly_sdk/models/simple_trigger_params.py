from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.simple_trigger_params_trigger_type import (
    SimpleTriggerParamsTriggerType,
    check_simple_trigger_params_trigger_type,
)
from ..models.simple_trigger_params_triggers_item import (
    SimpleTriggerParamsTriggersItem,
    check_simple_trigger_params_triggers_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleTriggerParams")


@_attrs_define
class SimpleTriggerParams:
    """
    Attributes:
        trigger_type (SimpleTriggerParamsTriggerType):
        triggers (Union[Unset, list[SimpleTriggerParamsTriggersItem]]):
    """

    trigger_type: SimpleTriggerParamsTriggerType
    triggers: Unset | list[SimpleTriggerParamsTriggersItem] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_type: str = self.trigger_type

        triggers: Unset | list[str] = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item: str = triggers_item_data
                triggers.append(triggers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_type": trigger_type,
            }
        )
        if triggers is not UNSET:
            field_dict["triggers"] = triggers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_type = check_simple_trigger_params_trigger_type(d.pop("trigger_type"))

        triggers = []
        _triggers = d.pop("triggers", UNSET)
        for triggers_item_data in _triggers or []:
            triggers_item = check_simple_trigger_params_triggers_item(triggers_item_data)

            triggers.append(triggers_item)

        simple_trigger_params = cls(
            trigger_type=trigger_type,
            triggers=triggers,
        )

        simple_trigger_params.additional_properties = d
        return simple_trigger_params

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
