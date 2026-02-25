from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.update_alert_routing_rule_data_attributes_condition_type import (
    UpdateAlertRoutingRuleDataAttributesConditionType,
    check_update_alert_routing_rule_data_attributes_condition_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_routing_rule_data_attributes_conditions_item import (
        UpdateAlertRoutingRuleDataAttributesConditionsItem,
    )
    from ..models.update_alert_routing_rule_data_attributes_destination import (
        UpdateAlertRoutingRuleDataAttributesDestination,
    )


T = TypeVar("T", bound="UpdateAlertRoutingRuleDataAttributes")


@_attrs_define
class UpdateAlertRoutingRuleDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the alert routing rule
        enabled (Union[Unset, bool]): Whether the alert routing rule is enabled
        alerts_source_id (Union[Unset, UUID]): The ID of the alerts source
        position (Union[Unset, int]): The position of the alert routing rule for ordering evaluation
        owning_team_ids (Union[Unset, list[UUID]]): The IDs of the teams that own the alert routing rule
        condition_type (Union[Unset, UpdateAlertRoutingRuleDataAttributesConditionType]): The type of condition for the
            alert routing rule
        conditions (Union[Unset, list['UpdateAlertRoutingRuleDataAttributesConditionsItem']]):
        destination (Union[Unset, UpdateAlertRoutingRuleDataAttributesDestination]):
    """

    name: Unset | str = UNSET
    enabled: Unset | bool = UNSET
    alerts_source_id: Unset | UUID = UNSET
    position: Unset | int = UNSET
    owning_team_ids: Unset | list[UUID] = UNSET
    condition_type: Unset | UpdateAlertRoutingRuleDataAttributesConditionType = UNSET
    conditions: Unset | list["UpdateAlertRoutingRuleDataAttributesConditionsItem"] = UNSET
    destination: Union[Unset, "UpdateAlertRoutingRuleDataAttributesDestination"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        alerts_source_id: Unset | str = UNSET
        if not isinstance(self.alerts_source_id, Unset):
            alerts_source_id = str(self.alerts_source_id)

        position = self.position

        owning_team_ids: Unset | list[str] = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = []
            for owning_team_ids_item_data in self.owning_team_ids:
                owning_team_ids_item = str(owning_team_ids_item_data)
                owning_team_ids.append(owning_team_ids_item)

        condition_type: Unset | str = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type

        conditions: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        destination: Unset | dict[str, Any] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if alerts_source_id is not UNSET:
            field_dict["alerts_source_id"] = alerts_source_id
        if position is not UNSET:
            field_dict["position"] = position
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_alert_routing_rule_data_attributes_conditions_item import (
            UpdateAlertRoutingRuleDataAttributesConditionsItem,
        )
        from ..models.update_alert_routing_rule_data_attributes_destination import (
            UpdateAlertRoutingRuleDataAttributesDestination,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _alerts_source_id = d.pop("alerts_source_id", UNSET)
        alerts_source_id: Unset | UUID
        if isinstance(_alerts_source_id, Unset):
            alerts_source_id = UNSET
        else:
            alerts_source_id = UUID(_alerts_source_id)

        position = d.pop("position", UNSET)

        owning_team_ids = []
        _owning_team_ids = d.pop("owning_team_ids", UNSET)
        for owning_team_ids_item_data in _owning_team_ids or []:
            owning_team_ids_item = UUID(owning_team_ids_item_data)

            owning_team_ids.append(owning_team_ids_item)

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: Unset | UpdateAlertRoutingRuleDataAttributesConditionType
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = check_update_alert_routing_rule_data_attributes_condition_type(_condition_type)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = UpdateAlertRoutingRuleDataAttributesConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        _destination = d.pop("destination", UNSET)
        destination: Unset | UpdateAlertRoutingRuleDataAttributesDestination
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = UpdateAlertRoutingRuleDataAttributesDestination.from_dict(_destination)

        update_alert_routing_rule_data_attributes = cls(
            name=name,
            enabled=enabled,
            alerts_source_id=alerts_source_id,
            position=position,
            owning_team_ids=owning_team_ids,
            condition_type=condition_type,
            conditions=conditions,
            destination=destination,
        )

        return update_alert_routing_rule_data_attributes
