from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_alert_group_data_attributes_condition_type import (
    UpdateAlertGroupDataAttributesConditionType,
    check_update_alert_group_data_attributes_condition_type,
)
from ..models.update_alert_group_data_attributes_group_by_alert_title import (
    UpdateAlertGroupDataAttributesGroupByAlertTitle,
    check_update_alert_group_data_attributes_group_by_alert_title,
)
from ..models.update_alert_group_data_attributes_group_by_alert_urgency import (
    UpdateAlertGroupDataAttributesGroupByAlertUrgency,
    check_update_alert_group_data_attributes_group_by_alert_urgency,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_group_data_attributes_attributes_item import UpdateAlertGroupDataAttributesAttributesItem
    from ..models.update_alert_group_data_attributes_conditions_item import UpdateAlertGroupDataAttributesConditionsItem
    from ..models.update_alert_group_data_attributes_targets_item import UpdateAlertGroupDataAttributesTargetsItem


T = TypeVar("T", bound="UpdateAlertGroupDataAttributes")


@_attrs_define
class UpdateAlertGroupDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the alert group
        description (None | str | Unset): The description of the alert group
        time_window (int | Unset): The length of time an Alert Group should stay open and accept new alerts
        targets (list[UpdateAlertGroupDataAttributesTargetsItem] | Unset):
        attributes (list[UpdateAlertGroupDataAttributesAttributesItem] | Unset): This field is deprecated. Please use
            the `conditions` field instead, `attributes` will be removed in the future.
        group_by_alert_title (UpdateAlertGroupDataAttributesGroupByAlertTitle | Unset): [DEPRECATED] Whether the alerts
            should be grouped by titles. This field is deprecated. Please use the `conditions` field with advanced alert
            grouping instead.
        group_by_alert_urgency (UpdateAlertGroupDataAttributesGroupByAlertUrgency | Unset): [DEPRECATED] Whether the
            alerts should be grouped by urgencies. This field is deprecated. Please use the `conditions` field with advanced
            alert grouping instead.
        condition_type (UpdateAlertGroupDataAttributesConditionType | Unset): Group alerts when ANY or ALL of the fields
            are matching.
        conditions (list[UpdateAlertGroupDataAttributesConditionsItem] | Unset):
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    time_window: int | Unset = UNSET
    targets: list[UpdateAlertGroupDataAttributesTargetsItem] | Unset = UNSET
    attributes: list[UpdateAlertGroupDataAttributesAttributesItem] | Unset = UNSET
    group_by_alert_title: UpdateAlertGroupDataAttributesGroupByAlertTitle | Unset = UNSET
    group_by_alert_urgency: UpdateAlertGroupDataAttributesGroupByAlertUrgency | Unset = UNSET
    condition_type: UpdateAlertGroupDataAttributesConditionType | Unset = UNSET
    conditions: list[UpdateAlertGroupDataAttributesConditionsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        time_window = self.time_window

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        group_by_alert_title: int | Unset = UNSET
        if not isinstance(self.group_by_alert_title, Unset):
            group_by_alert_title = self.group_by_alert_title

        group_by_alert_urgency: int | Unset = UNSET
        if not isinstance(self.group_by_alert_urgency, Unset):
            group_by_alert_urgency = self.group_by_alert_urgency

        condition_type: str | Unset = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if time_window is not UNSET:
            field_dict["time_window"] = time_window
        if targets is not UNSET:
            field_dict["targets"] = targets
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if group_by_alert_title is not UNSET:
            field_dict["group_by_alert_title"] = group_by_alert_title
        if group_by_alert_urgency is not UNSET:
            field_dict["group_by_alert_urgency"] = group_by_alert_urgency
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_alert_group_data_attributes_attributes_item import (
            UpdateAlertGroupDataAttributesAttributesItem,
        )
        from ..models.update_alert_group_data_attributes_conditions_item import (
            UpdateAlertGroupDataAttributesConditionsItem,
        )
        from ..models.update_alert_group_data_attributes_targets_item import UpdateAlertGroupDataAttributesTargetsItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        time_window = d.pop("time_window", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[UpdateAlertGroupDataAttributesTargetsItem] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = UpdateAlertGroupDataAttributesTargetsItem.from_dict(targets_item_data)

                targets.append(targets_item)

        _attributes = d.pop("attributes", UNSET)
        attributes: list[UpdateAlertGroupDataAttributesAttributesItem] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = UpdateAlertGroupDataAttributesAttributesItem.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        _group_by_alert_title = d.pop("group_by_alert_title", UNSET)
        group_by_alert_title: UpdateAlertGroupDataAttributesGroupByAlertTitle | Unset
        if isinstance(_group_by_alert_title, Unset):
            group_by_alert_title = UNSET
        else:
            group_by_alert_title = check_update_alert_group_data_attributes_group_by_alert_title(_group_by_alert_title)

        _group_by_alert_urgency = d.pop("group_by_alert_urgency", UNSET)
        group_by_alert_urgency: UpdateAlertGroupDataAttributesGroupByAlertUrgency | Unset
        if isinstance(_group_by_alert_urgency, Unset):
            group_by_alert_urgency = UNSET
        else:
            group_by_alert_urgency = check_update_alert_group_data_attributes_group_by_alert_urgency(
                _group_by_alert_urgency
            )

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: UpdateAlertGroupDataAttributesConditionType | Unset
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = check_update_alert_group_data_attributes_condition_type(_condition_type)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[UpdateAlertGroupDataAttributesConditionsItem] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = UpdateAlertGroupDataAttributesConditionsItem.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        update_alert_group_data_attributes = cls(
            name=name,
            description=description,
            time_window=time_window,
            targets=targets,
            attributes=attributes,
            group_by_alert_title=group_by_alert_title,
            group_by_alert_urgency=group_by_alert_urgency,
            condition_type=condition_type,
            conditions=conditions,
        )

        return update_alert_group_data_attributes
