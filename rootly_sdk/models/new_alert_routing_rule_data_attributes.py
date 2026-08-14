from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.new_alert_routing_rule_data_attributes_condition_type import (
    NewAlertRoutingRuleDataAttributesConditionType,
    check_new_alert_routing_rule_data_attributes_condition_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_routing_rule_data_attributes_conditions_item import (
        NewAlertRoutingRuleDataAttributesConditionsItem,
    )
    from ..models.new_alert_routing_rule_data_attributes_destination import NewAlertRoutingRuleDataAttributesDestination


T = TypeVar("T", bound="NewAlertRoutingRuleDataAttributes")


@_attrs_define
class NewAlertRoutingRuleDataAttributes:
    """
    Attributes:
        name (str): The name of the alert routing rule
        alerts_source_id (UUID): The ID of the alerts source
        destination (NewAlertRoutingRuleDataAttributesDestination):
        enabled (Union[Unset, bool]): Whether the alert routing rule is enabled
        owning_team_ids (Union[Unset, list[UUID]]): The IDs of the teams which own the alert routing rule. If the user
            doesn't have Alert Routing Create Permission in On-Call Roles, then this field is required and can contain Team
            IDs the user is an admin of.
        position (Union[Unset, int]): The position of the alert routing rule for ordering evaluation
        condition_type (Union[Unset, NewAlertRoutingRuleDataAttributesConditionType]): The type of condition for the
            alert routing rule
        conditions (Union[Unset, list['NewAlertRoutingRuleDataAttributesConditionsItem']]):
    """

    name: str
    alerts_source_id: UUID
    destination: "NewAlertRoutingRuleDataAttributesDestination"
    enabled: Unset | bool = UNSET
    owning_team_ids: Unset | list[UUID] = UNSET
    position: Unset | int = UNSET
    condition_type: Unset | NewAlertRoutingRuleDataAttributesConditionType = UNSET
    conditions: Unset | list["NewAlertRoutingRuleDataAttributesConditionsItem"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alerts_source_id = str(self.alerts_source_id)

        destination = self.destination.to_dict()

        enabled = self.enabled

        owning_team_ids: Unset | list[str] = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = []
            for owning_team_ids_item_data in self.owning_team_ids:
                owning_team_ids_item = str(owning_team_ids_item_data)
                owning_team_ids.append(owning_team_ids_item)

        position = self.position

        condition_type: Unset | str = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type

        conditions: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "alerts_source_id": alerts_source_id,
                "destination": destination,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if position is not UNSET:
            field_dict["position"] = position
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_routing_rule_data_attributes_conditions_item import (
            NewAlertRoutingRuleDataAttributesConditionsItem,
        )
        from ..models.new_alert_routing_rule_data_attributes_destination import (
            NewAlertRoutingRuleDataAttributesDestination,
        )

        d = dict(src_dict)
        name = d.pop("name")

        alerts_source_id = UUID(d.pop("alerts_source_id"))

        destination = NewAlertRoutingRuleDataAttributesDestination.from_dict(d.pop("destination"))

        enabled = d.pop("enabled", UNSET)

        owning_team_ids = []
        _owning_team_ids = d.pop("owning_team_ids", UNSET)
        for owning_team_ids_item_data in _owning_team_ids or []:
            owning_team_ids_item = UUID(owning_team_ids_item_data)

            owning_team_ids.append(owning_team_ids_item)

        position = d.pop("position", UNSET)

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: Unset | NewAlertRoutingRuleDataAttributesConditionType
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = check_new_alert_routing_rule_data_attributes_condition_type(_condition_type)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = NewAlertRoutingRuleDataAttributesConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        new_alert_routing_rule_data_attributes = cls(
            name=name,
            alerts_source_id=alerts_source_id,
            destination=destination,
            enabled=enabled,
            owning_team_ids=owning_team_ids,
            position=position,
            condition_type=condition_type,
            conditions=conditions,
        )

        return new_alert_routing_rule_data_attributes
