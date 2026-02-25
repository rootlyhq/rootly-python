from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_trigger_params_alert_condition import (
    AlertTriggerParamsAlertCondition,
    check_alert_trigger_params_alert_condition,
)
from ..models.alert_trigger_params_alert_condition_label import (
    AlertTriggerParamsAlertConditionLabel,
    check_alert_trigger_params_alert_condition_label,
)
from ..models.alert_trigger_params_alert_condition_payload import (
    AlertTriggerParamsAlertConditionPayload,
    check_alert_trigger_params_alert_condition_payload,
)
from ..models.alert_trigger_params_alert_condition_source import (
    AlertTriggerParamsAlertConditionSource,
    check_alert_trigger_params_alert_condition_source,
)
from ..models.alert_trigger_params_alert_condition_status import (
    AlertTriggerParamsAlertConditionStatus,
    check_alert_trigger_params_alert_condition_status,
)
from ..models.alert_trigger_params_trigger_type import (
    AlertTriggerParamsTriggerType,
    check_alert_trigger_params_trigger_type,
)
from ..models.alert_trigger_params_triggers_item import (
    AlertTriggerParamsTriggersItem,
    check_alert_trigger_params_triggers_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_trigger_params_alert_field_conditions_item import AlertTriggerParamsAlertFieldConditionsItem
    from ..models.alert_trigger_params_alert_payload_conditions import AlertTriggerParamsAlertPayloadConditions


T = TypeVar("T", bound="AlertTriggerParams")


@_attrs_define
class AlertTriggerParams:
    """
    Attributes:
        trigger_type (AlertTriggerParamsTriggerType):
        triggers (Union[Unset, list[AlertTriggerParamsTriggersItem]]):
        alert_condition (Union[Unset, AlertTriggerParamsAlertCondition]):
        alert_condition_source (Union[Unset, AlertTriggerParamsAlertConditionSource]):  Default: 'ANY'.
        alert_condition_source_use_regexp (Union[Unset, bool]):  Default: False.
        alert_sources (Union[Unset, list[str]]):
        alert_condition_label (Union[Unset, AlertTriggerParamsAlertConditionLabel]):  Default: 'ANY'.
        alert_condition_label_use_regexp (Union[Unset, bool]):  Default: False.
        alert_condition_status (Union[Unset, AlertTriggerParamsAlertConditionStatus]):  Default: 'ANY'.
        alert_condition_status_use_regexp (Union[Unset, bool]):  Default: False.
        alert_statuses (Union[Unset, list[str]]):
        alert_labels (Union[Unset, list[str]]):
        alert_condition_payload (Union[Unset, AlertTriggerParamsAlertConditionPayload]):  Default: 'ANY'.
        alert_condition_payload_use_regexp (Union[Unset, bool]):  Default: False.
        alert_payload (Union[Unset, list[str]]):
        alert_query_payload (Union[None, Unset, str]): You can use jsonpath syntax. eg: $.incident.teams[*]
        alert_field_conditions (Union[Unset, list['AlertTriggerParamsAlertFieldConditionsItem']]):
        alert_payload_conditions (Union[Unset, AlertTriggerParamsAlertPayloadConditions]):
    """

    trigger_type: AlertTriggerParamsTriggerType
    triggers: Unset | list[AlertTriggerParamsTriggersItem] = UNSET
    alert_condition: Unset | AlertTriggerParamsAlertCondition = UNSET
    alert_condition_source: Unset | AlertTriggerParamsAlertConditionSource = "ANY"
    alert_condition_source_use_regexp: Unset | bool = False
    alert_sources: Unset | list[str] = UNSET
    alert_condition_label: Unset | AlertTriggerParamsAlertConditionLabel = "ANY"
    alert_condition_label_use_regexp: Unset | bool = False
    alert_condition_status: Unset | AlertTriggerParamsAlertConditionStatus = "ANY"
    alert_condition_status_use_regexp: Unset | bool = False
    alert_statuses: Unset | list[str] = UNSET
    alert_labels: Unset | list[str] = UNSET
    alert_condition_payload: Unset | AlertTriggerParamsAlertConditionPayload = "ANY"
    alert_condition_payload_use_regexp: Unset | bool = False
    alert_payload: Unset | list[str] = UNSET
    alert_query_payload: None | Unset | str = UNSET
    alert_field_conditions: Unset | list["AlertTriggerParamsAlertFieldConditionsItem"] = UNSET
    alert_payload_conditions: Union[Unset, "AlertTriggerParamsAlertPayloadConditions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_type: str = self.trigger_type

        triggers: Unset | list[str] = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item: str = triggers_item_data
                triggers.append(triggers_item)

        alert_condition: Unset | str = UNSET
        if not isinstance(self.alert_condition, Unset):
            alert_condition = self.alert_condition

        alert_condition_source: Unset | str = UNSET
        if not isinstance(self.alert_condition_source, Unset):
            alert_condition_source = self.alert_condition_source

        alert_condition_source_use_regexp = self.alert_condition_source_use_regexp

        alert_sources: Unset | list[str] = UNSET
        if not isinstance(self.alert_sources, Unset):
            alert_sources = self.alert_sources

        alert_condition_label: Unset | str = UNSET
        if not isinstance(self.alert_condition_label, Unset):
            alert_condition_label = self.alert_condition_label

        alert_condition_label_use_regexp = self.alert_condition_label_use_regexp

        alert_condition_status: Unset | str = UNSET
        if not isinstance(self.alert_condition_status, Unset):
            alert_condition_status = self.alert_condition_status

        alert_condition_status_use_regexp = self.alert_condition_status_use_regexp

        alert_statuses: Unset | list[str] = UNSET
        if not isinstance(self.alert_statuses, Unset):
            alert_statuses = self.alert_statuses

        alert_labels: Unset | list[str] = UNSET
        if not isinstance(self.alert_labels, Unset):
            alert_labels = self.alert_labels

        alert_condition_payload: Unset | str = UNSET
        if not isinstance(self.alert_condition_payload, Unset):
            alert_condition_payload = self.alert_condition_payload

        alert_condition_payload_use_regexp = self.alert_condition_payload_use_regexp

        alert_payload: Unset | list[str] = UNSET
        if not isinstance(self.alert_payload, Unset):
            alert_payload = self.alert_payload

        alert_query_payload: None | Unset | str
        if isinstance(self.alert_query_payload, Unset):
            alert_query_payload = UNSET
        else:
            alert_query_payload = self.alert_query_payload

        alert_field_conditions: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.alert_field_conditions, Unset):
            alert_field_conditions = []
            for alert_field_conditions_item_data in self.alert_field_conditions:
                alert_field_conditions_item = alert_field_conditions_item_data.to_dict()
                alert_field_conditions.append(alert_field_conditions_item)

        alert_payload_conditions: Unset | dict[str, Any] = UNSET
        if not isinstance(self.alert_payload_conditions, Unset):
            alert_payload_conditions = self.alert_payload_conditions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_type": trigger_type,
            }
        )
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if alert_condition is not UNSET:
            field_dict["alert_condition"] = alert_condition
        if alert_condition_source is not UNSET:
            field_dict["alert_condition_source"] = alert_condition_source
        if alert_condition_source_use_regexp is not UNSET:
            field_dict["alert_condition_source_use_regexp"] = alert_condition_source_use_regexp
        if alert_sources is not UNSET:
            field_dict["alert_sources"] = alert_sources
        if alert_condition_label is not UNSET:
            field_dict["alert_condition_label"] = alert_condition_label
        if alert_condition_label_use_regexp is not UNSET:
            field_dict["alert_condition_label_use_regexp"] = alert_condition_label_use_regexp
        if alert_condition_status is not UNSET:
            field_dict["alert_condition_status"] = alert_condition_status
        if alert_condition_status_use_regexp is not UNSET:
            field_dict["alert_condition_status_use_regexp"] = alert_condition_status_use_regexp
        if alert_statuses is not UNSET:
            field_dict["alert_statuses"] = alert_statuses
        if alert_labels is not UNSET:
            field_dict["alert_labels"] = alert_labels
        if alert_condition_payload is not UNSET:
            field_dict["alert_condition_payload"] = alert_condition_payload
        if alert_condition_payload_use_regexp is not UNSET:
            field_dict["alert_condition_payload_use_regexp"] = alert_condition_payload_use_regexp
        if alert_payload is not UNSET:
            field_dict["alert_payload"] = alert_payload
        if alert_query_payload is not UNSET:
            field_dict["alert_query_payload"] = alert_query_payload
        if alert_field_conditions is not UNSET:
            field_dict["alert_field_conditions"] = alert_field_conditions
        if alert_payload_conditions is not UNSET:
            field_dict["alert_payload_conditions"] = alert_payload_conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_trigger_params_alert_field_conditions_item import AlertTriggerParamsAlertFieldConditionsItem
        from ..models.alert_trigger_params_alert_payload_conditions import AlertTriggerParamsAlertPayloadConditions

        d = dict(src_dict)
        trigger_type = check_alert_trigger_params_trigger_type(d.pop("trigger_type"))

        triggers = []
        _triggers = d.pop("triggers", UNSET)
        for triggers_item_data in _triggers or []:
            triggers_item = check_alert_trigger_params_triggers_item(triggers_item_data)

            triggers.append(triggers_item)

        _alert_condition = d.pop("alert_condition", UNSET)
        alert_condition: Unset | AlertTriggerParamsAlertCondition
        if isinstance(_alert_condition, Unset):
            alert_condition = UNSET
        else:
            alert_condition = check_alert_trigger_params_alert_condition(_alert_condition)

        _alert_condition_source = d.pop("alert_condition_source", UNSET)
        alert_condition_source: Unset | AlertTriggerParamsAlertConditionSource
        if isinstance(_alert_condition_source, Unset):
            alert_condition_source = UNSET
        else:
            alert_condition_source = check_alert_trigger_params_alert_condition_source(_alert_condition_source)

        alert_condition_source_use_regexp = d.pop("alert_condition_source_use_regexp", UNSET)

        alert_sources = cast(list[str], d.pop("alert_sources", UNSET))

        _alert_condition_label = d.pop("alert_condition_label", UNSET)
        alert_condition_label: Unset | AlertTriggerParamsAlertConditionLabel
        if isinstance(_alert_condition_label, Unset):
            alert_condition_label = UNSET
        else:
            alert_condition_label = check_alert_trigger_params_alert_condition_label(_alert_condition_label)

        alert_condition_label_use_regexp = d.pop("alert_condition_label_use_regexp", UNSET)

        _alert_condition_status = d.pop("alert_condition_status", UNSET)
        alert_condition_status: Unset | AlertTriggerParamsAlertConditionStatus
        if isinstance(_alert_condition_status, Unset):
            alert_condition_status = UNSET
        else:
            alert_condition_status = check_alert_trigger_params_alert_condition_status(_alert_condition_status)

        alert_condition_status_use_regexp = d.pop("alert_condition_status_use_regexp", UNSET)

        alert_statuses = cast(list[str], d.pop("alert_statuses", UNSET))

        alert_labels = cast(list[str], d.pop("alert_labels", UNSET))

        _alert_condition_payload = d.pop("alert_condition_payload", UNSET)
        alert_condition_payload: Unset | AlertTriggerParamsAlertConditionPayload
        if isinstance(_alert_condition_payload, Unset):
            alert_condition_payload = UNSET
        else:
            alert_condition_payload = check_alert_trigger_params_alert_condition_payload(_alert_condition_payload)

        alert_condition_payload_use_regexp = d.pop("alert_condition_payload_use_regexp", UNSET)

        alert_payload = cast(list[str], d.pop("alert_payload", UNSET))

        def _parse_alert_query_payload(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        alert_query_payload = _parse_alert_query_payload(d.pop("alert_query_payload", UNSET))

        alert_field_conditions = []
        _alert_field_conditions = d.pop("alert_field_conditions", UNSET)
        for alert_field_conditions_item_data in _alert_field_conditions or []:
            alert_field_conditions_item = AlertTriggerParamsAlertFieldConditionsItem.from_dict(
                alert_field_conditions_item_data
            )

            alert_field_conditions.append(alert_field_conditions_item)

        _alert_payload_conditions = d.pop("alert_payload_conditions", UNSET)
        alert_payload_conditions: Unset | AlertTriggerParamsAlertPayloadConditions
        if isinstance(_alert_payload_conditions, Unset):
            alert_payload_conditions = UNSET
        else:
            alert_payload_conditions = AlertTriggerParamsAlertPayloadConditions.from_dict(_alert_payload_conditions)

        alert_trigger_params = cls(
            trigger_type=trigger_type,
            triggers=triggers,
            alert_condition=alert_condition,
            alert_condition_source=alert_condition_source,
            alert_condition_source_use_regexp=alert_condition_source_use_regexp,
            alert_sources=alert_sources,
            alert_condition_label=alert_condition_label,
            alert_condition_label_use_regexp=alert_condition_label_use_regexp,
            alert_condition_status=alert_condition_status,
            alert_condition_status_use_regexp=alert_condition_status_use_regexp,
            alert_statuses=alert_statuses,
            alert_labels=alert_labels,
            alert_condition_payload=alert_condition_payload,
            alert_condition_payload_use_regexp=alert_condition_payload_use_regexp,
            alert_payload=alert_payload,
            alert_query_payload=alert_query_payload,
            alert_field_conditions=alert_field_conditions,
            alert_payload_conditions=alert_payload_conditions,
        )

        alert_trigger_params.additional_properties = d
        return alert_trigger_params

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
