from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_group_attributes_item import AlertGroupAttributesItem
    from ..models.alert_group_conditions_item import AlertGroupConditionsItem
    from ..models.alert_group_targets_item import AlertGroupTargetsItem


T = TypeVar("T", bound="AlertGroup")


@_attrs_define
class AlertGroup:
    """
    Attributes:
        name (str): The name of the alert group
        description (Union[None, str]): The description of the alert group
        condition_type (str): Grouping condition for the alert group
        time_window (int): Time window for the alert grouping
        created_at (str): Date of creation
        updated_at (str): Date of last update
        deleted_at (Union[None, str]): Date or deletion
        slug (Union[Unset, str]): The slug of the alert group
        group_by_alert_title (Union[Unset, bool]): [DEPRECATED] Whether the alerts are grouped by title or not. This
            field is deprecated. Please use the `conditions` field with advanced alert grouping instead.
        group_by_alert_urgency (Union[Unset, bool]): [DEPRECATED] Whether the alerts are grouped by urgency or not. This
            field is deprecated. Please use the `conditions` field with advanced alert grouping instead.
        targets (Union[Unset, list['AlertGroupTargetsItem']]):
        attributes (Union[Unset, list['AlertGroupAttributesItem']]): This field is deprecated. Please use the
            `conditions` field instead, `attributes` will be removed in the future.
        conditions (Union[Unset, list['AlertGroupConditionsItem']]): The conditions for the alert group
    """

    name: str
    description: Union[None, str]
    condition_type: str
    time_window: int
    created_at: str
    updated_at: str
    deleted_at: Union[None, str]
    slug: Union[Unset, str] = UNSET
    group_by_alert_title: Union[Unset, bool] = UNSET
    group_by_alert_urgency: Union[Unset, bool] = UNSET
    targets: Union[Unset, list["AlertGroupTargetsItem"]] = UNSET
    attributes: Union[Unset, list["AlertGroupAttributesItem"]] = UNSET
    conditions: Union[Unset, list["AlertGroupConditionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, str]
        description = self.description

        condition_type = self.condition_type

        time_window = self.time_window

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        slug = self.slug

        group_by_alert_title = self.group_by_alert_title

        group_by_alert_urgency = self.group_by_alert_urgency

        targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "condition_type": condition_type,
                "time_window": time_window,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if group_by_alert_title is not UNSET:
            field_dict["group_by_alert_title"] = group_by_alert_title
        if group_by_alert_urgency is not UNSET:
            field_dict["group_by_alert_urgency"] = group_by_alert_urgency
        if targets is not UNSET:
            field_dict["targets"] = targets
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_group_attributes_item import AlertGroupAttributesItem
        from ..models.alert_group_conditions_item import AlertGroupConditionsItem
        from ..models.alert_group_targets_item import AlertGroupTargetsItem

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        condition_type = d.pop("condition_type")

        time_window = d.pop("time_window")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        slug = d.pop("slug", UNSET)

        group_by_alert_title = d.pop("group_by_alert_title", UNSET)

        group_by_alert_urgency = d.pop("group_by_alert_urgency", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = AlertGroupTargetsItem.from_dict(targets_item_data)

            targets.append(targets_item)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = AlertGroupAttributesItem.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = AlertGroupConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        alert_group = cls(
            name=name,
            description=description,
            condition_type=condition_type,
            time_window=time_window,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            slug=slug,
            group_by_alert_title=group_by_alert_title,
            group_by_alert_urgency=group_by_alert_urgency,
            targets=targets,
            attributes=attributes,
            conditions=conditions,
        )

        alert_group.additional_properties = d
        return alert_group

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
