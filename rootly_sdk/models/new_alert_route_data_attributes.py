from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_route_data_attributes_rules_item import NewAlertRouteDataAttributesRulesItem


T = TypeVar("T", bound="NewAlertRouteDataAttributes")


@_attrs_define
class NewAlertRouteDataAttributes:
    """
    Attributes:
        name (str): The name of the alert route
        alerts_source_ids (list[UUID]):
        enabled (bool | Unset): Whether the alert route is enabled
        owning_team_ids (list[UUID] | Unset):
        rules (list[NewAlertRouteDataAttributesRulesItem] | Unset):
    """

    name: str
    alerts_source_ids: list[UUID]
    enabled: bool | Unset = UNSET
    owning_team_ids: list[UUID] | Unset = UNSET
    rules: list[NewAlertRouteDataAttributesRulesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alerts_source_ids = []
        for alerts_source_ids_item_data in self.alerts_source_ids:
            alerts_source_ids_item = str(alerts_source_ids_item_data)
            alerts_source_ids.append(alerts_source_ids_item)

        enabled = self.enabled

        owning_team_ids: list[str] | Unset = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = []
            for owning_team_ids_item_data in self.owning_team_ids:
                owning_team_ids_item = str(owning_team_ids_item_data)
                owning_team_ids.append(owning_team_ids_item)

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "alerts_source_ids": alerts_source_ids,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_route_data_attributes_rules_item import NewAlertRouteDataAttributesRulesItem

        d = dict(src_dict)
        name = d.pop("name")

        alerts_source_ids = []
        _alerts_source_ids = d.pop("alerts_source_ids")
        for alerts_source_ids_item_data in _alerts_source_ids:
            alerts_source_ids_item = UUID(alerts_source_ids_item_data)

            alerts_source_ids.append(alerts_source_ids_item)

        enabled = d.pop("enabled", UNSET)

        _owning_team_ids = d.pop("owning_team_ids", UNSET)
        owning_team_ids: list[UUID] | Unset = UNSET
        if _owning_team_ids is not UNSET:
            owning_team_ids = []
            for owning_team_ids_item_data in _owning_team_ids:
                owning_team_ids_item = UUID(owning_team_ids_item_data)

                owning_team_ids.append(owning_team_ids_item)

        _rules = d.pop("rules", UNSET)
        rules: list[NewAlertRouteDataAttributesRulesItem] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = NewAlertRouteDataAttributesRulesItem.from_dict(rules_item_data)

                rules.append(rules_item)

        new_alert_route_data_attributes = cls(
            name=name,
            alerts_source_ids=alerts_source_ids,
            enabled=enabled,
            owning_team_ids=owning_team_ids,
            rules=rules,
        )

        return new_alert_route_data_attributes
