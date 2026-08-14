from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_alert_route_data_attributes_rules_item import PatchAlertRouteDataAttributesRulesItem


T = TypeVar("T", bound="PatchAlertRouteDataAttributes")


@_attrs_define
class PatchAlertRouteDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the alert route
        enabled (Union[Unset, bool]): Whether the alert route is enabled
        alerts_source_ids (Union[Unset, list[UUID]]):
        owning_team_ids (Union[Unset, list[UUID]]):
        rules (Union[Unset, list['PatchAlertRouteDataAttributesRulesItem']]):
    """

    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    alerts_source_ids: Union[Unset, list[UUID]] = UNSET
    owning_team_ids: Union[Unset, list[UUID]] = UNSET
    rules: Union[Unset, list["PatchAlertRouteDataAttributesRulesItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        alerts_source_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alerts_source_ids, Unset):
            alerts_source_ids = []
            for alerts_source_ids_item_data in self.alerts_source_ids:
                alerts_source_ids_item = str(alerts_source_ids_item_data)
                alerts_source_ids.append(alerts_source_ids_item)

        owning_team_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.owning_team_ids, Unset):
            owning_team_ids = []
            for owning_team_ids_item_data in self.owning_team_ids:
                owning_team_ids_item = str(owning_team_ids_item_data)
                owning_team_ids.append(owning_team_ids_item)

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if alerts_source_ids is not UNSET:
            field_dict["alerts_source_ids"] = alerts_source_ids
        if owning_team_ids is not UNSET:
            field_dict["owning_team_ids"] = owning_team_ids
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_alert_route_data_attributes_rules_item import PatchAlertRouteDataAttributesRulesItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        alerts_source_ids = []
        _alerts_source_ids = d.pop("alerts_source_ids", UNSET)
        for alerts_source_ids_item_data in _alerts_source_ids or []:
            alerts_source_ids_item = UUID(alerts_source_ids_item_data)

            alerts_source_ids.append(alerts_source_ids_item)

        owning_team_ids = []
        _owning_team_ids = d.pop("owning_team_ids", UNSET)
        for owning_team_ids_item_data in _owning_team_ids or []:
            owning_team_ids_item = UUID(owning_team_ids_item_data)

            owning_team_ids.append(owning_team_ids_item)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = PatchAlertRouteDataAttributesRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        patch_alert_route_data_attributes = cls(
            name=name,
            enabled=enabled,
            alerts_source_ids=alerts_source_ids,
            owning_team_ids=owning_team_ids,
            rules=rules,
        )

        return patch_alert_route_data_attributes
