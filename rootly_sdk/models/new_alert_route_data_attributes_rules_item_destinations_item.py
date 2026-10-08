from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.new_alert_route_data_attributes_rules_item_destinations_item_target_type import (
    NewAlertRouteDataAttributesRulesItemDestinationsItemTargetType,
    check_new_alert_route_data_attributes_rules_item_destinations_item_target_type,
)

T = TypeVar("T", bound="NewAlertRouteDataAttributesRulesItemDestinationsItem")


@_attrs_define
class NewAlertRouteDataAttributesRulesItemDestinationsItem:
    """
    Attributes:
        target_type (NewAlertRouteDataAttributesRulesItemDestinationsItemTargetType): The type of the target. Please
            contact support if you encounter issues using `Functionality` as a target type.
        target_id (UUID): The ID of the target
    """

    target_type: NewAlertRouteDataAttributesRulesItemDestinationsItemTargetType
    target_id: UUID

    def to_dict(self) -> dict[str, Any]:
        target_type: str = self.target_type

        target_id = str(self.target_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_type": target_type,
                "target_id": target_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = check_new_alert_route_data_attributes_rules_item_destinations_item_target_type(
            d.pop("target_type")
        )

        target_id = UUID(d.pop("target_id"))

        new_alert_route_data_attributes_rules_item_destinations_item = cls(
            target_type=target_type,
            target_id=target_id,
        )

        return new_alert_route_data_attributes_rules_item_destinations_item
