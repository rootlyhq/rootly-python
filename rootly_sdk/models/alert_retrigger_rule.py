import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.alert_retrigger_rule_match_mode import AlertRetriggerRuleMatchMode, check_alert_retrigger_rule_match_mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_retrigger_rule_conditions_item import AlertRetriggerRuleConditionsItem


T = TypeVar("T", bound="AlertRetriggerRule")


@_attrs_define
class AlertRetriggerRule:
    """
    Attributes:
        name (Union[Unset, str]): A human-readable name for the rule
        match_mode (Union[Unset, AlertRetriggerRuleMatchMode]): Whether all or any of the conditions must match
        timeout_minutes (Union[None, Unset, int]): Minutes after acknowledgment to re-trigger. Null means never re-
            trigger.
        position (Union[Unset, int]): The position of the rule for ordering evaluation
        conditions (Union[Unset, list['AlertRetriggerRuleConditionsItem']]): The conditions for the rule
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    name: Union[Unset, str] = UNSET
    match_mode: Union[Unset, AlertRetriggerRuleMatchMode] = UNSET
    timeout_minutes: Union[None, Unset, int] = UNSET
    position: Union[Unset, int] = UNSET
    conditions: Union[Unset, list["AlertRetriggerRuleConditionsItem"]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        match_mode: Union[Unset, str] = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        timeout_minutes: Union[None, Unset, int]
        if isinstance(self.timeout_minutes, Unset):
            timeout_minutes = UNSET
        else:
            timeout_minutes = self.timeout_minutes

        position = self.position

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if match_mode is not UNSET:
            field_dict["match_mode"] = match_mode
        if timeout_minutes is not UNSET:
            field_dict["timeout_minutes"] = timeout_minutes
        if position is not UNSET:
            field_dict["position"] = position
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_retrigger_rule_conditions_item import AlertRetriggerRuleConditionsItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: Union[Unset, AlertRetriggerRuleMatchMode]
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_alert_retrigger_rule_match_mode(_match_mode)

        def _parse_timeout_minutes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timeout_minutes = _parse_timeout_minutes(d.pop("timeout_minutes", UNSET))

        position = d.pop("position", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = AlertRetriggerRuleConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        alert_retrigger_rule = cls(
            name=name,
            match_mode=match_mode,
            timeout_minutes=timeout_minutes,
            position=position,
            conditions=conditions,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_retrigger_rule.additional_properties = d
        return alert_retrigger_rule

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
