from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sla_condition_match_type import SlaConditionMatchType, check_sla_condition_match_type
from ..models.sla_entity_type import SlaEntityType, check_sla_entity_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sla_conditions_item import SlaConditionsItem
    from ..models.sla_notification_configurations_item import SlaNotificationConfigurationsItem


T = TypeVar("T", bound="Sla")


@_attrs_define
class Sla:
    """
    Attributes:
        name (str): The name of the SLA
        condition_match_type (SlaConditionMatchType): Whether all or any conditions must match
        assignment_deadline_days (int): Number of days for the assignment deadline
        assignment_deadline_parent_status (str): The incident parent status that triggers the assignment deadline
        completion_deadline_days (int): Number of days for the completion deadline
        completion_deadline_parent_status (str): The incident parent status that triggers the completion deadline
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the SLA
        description (Union[None, Unset, str]): A description of the SLA
        position (Union[Unset, int]): Position of the SLA for ordering
        entity_type (Union[Unset, SlaEntityType]): The entity type this SLA applies to
        manager_role_id (Union[None, UUID, Unset]): The ID of the manager incident role. Exactly one of
            `manager_role_id` or `manager_user_id` must be provided.
        manager_user_id (Union[None, Unset, int]): The ID of the manager user. Exactly one of `manager_role_id` or
            `manager_user_id` must be provided.
        assignment_deadline_sub_status_id (Union[None, UUID, Unset]): Sub-status for the assignment deadline. Required
            when custom lifecycle statuses are enabled on the team.
        assignment_skip_weekends (Union[Unset, bool]): Whether to skip weekends when calculating the assignment deadline
        completion_deadline_sub_status_id (Union[None, UUID, Unset]): Sub-status for the completion deadline. Required
            when custom lifecycle statuses are enabled on the team.
        completion_skip_weekends (Union[Unset, bool]): Whether to skip weekends when calculating the completion deadline
        conditions (Union[Unset, list['SlaConditionsItem']]): Conditions that determine which incidents this SLA applies
            to
        notification_configurations (Union[Unset, list['SlaNotificationConfigurationsItem']]): Notification timing
            configurations
    """

    name: str
    condition_match_type: SlaConditionMatchType
    assignment_deadline_days: int
    assignment_deadline_parent_status: str
    completion_deadline_days: int
    completion_deadline_parent_status: str
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    description: None | Unset | str = UNSET
    position: Unset | int = UNSET
    entity_type: Unset | SlaEntityType = UNSET
    manager_role_id: None | UUID | Unset = UNSET
    manager_user_id: None | Unset | int = UNSET
    assignment_deadline_sub_status_id: None | UUID | Unset = UNSET
    assignment_skip_weekends: Unset | bool = UNSET
    completion_deadline_sub_status_id: None | UUID | Unset = UNSET
    completion_skip_weekends: Unset | bool = UNSET
    conditions: Unset | list["SlaConditionsItem"] = UNSET
    notification_configurations: Unset | list["SlaNotificationConfigurationsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        condition_match_type: str = self.condition_match_type

        assignment_deadline_days = self.assignment_deadline_days

        assignment_deadline_parent_status = self.assignment_deadline_parent_status

        completion_deadline_days = self.completion_deadline_days

        completion_deadline_parent_status = self.completion_deadline_parent_status

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position = self.position

        entity_type: Unset | str = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type

        manager_role_id: None | Unset | str
        if isinstance(self.manager_role_id, Unset):
            manager_role_id = UNSET
        elif isinstance(self.manager_role_id, UUID):
            manager_role_id = str(self.manager_role_id)
        else:
            manager_role_id = self.manager_role_id

        manager_user_id: None | Unset | int
        if isinstance(self.manager_user_id, Unset):
            manager_user_id = UNSET
        else:
            manager_user_id = self.manager_user_id

        assignment_deadline_sub_status_id: None | Unset | str
        if isinstance(self.assignment_deadline_sub_status_id, Unset):
            assignment_deadline_sub_status_id = UNSET
        elif isinstance(self.assignment_deadline_sub_status_id, UUID):
            assignment_deadline_sub_status_id = str(self.assignment_deadline_sub_status_id)
        else:
            assignment_deadline_sub_status_id = self.assignment_deadline_sub_status_id

        assignment_skip_weekends = self.assignment_skip_weekends

        completion_deadline_sub_status_id: None | Unset | str
        if isinstance(self.completion_deadline_sub_status_id, Unset):
            completion_deadline_sub_status_id = UNSET
        elif isinstance(self.completion_deadline_sub_status_id, UUID):
            completion_deadline_sub_status_id = str(self.completion_deadline_sub_status_id)
        else:
            completion_deadline_sub_status_id = self.completion_deadline_sub_status_id

        completion_skip_weekends = self.completion_skip_weekends

        conditions: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        notification_configurations: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.notification_configurations, Unset):
            notification_configurations = []
            for notification_configurations_item_data in self.notification_configurations:
                notification_configurations_item = notification_configurations_item_data.to_dict()
                notification_configurations.append(notification_configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "condition_match_type": condition_match_type,
                "assignment_deadline_days": assignment_deadline_days,
                "assignment_deadline_parent_status": assignment_deadline_parent_status,
                "completion_deadline_days": completion_deadline_days,
                "completion_deadline_parent_status": completion_deadline_parent_status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if manager_role_id is not UNSET:
            field_dict["manager_role_id"] = manager_role_id
        if manager_user_id is not UNSET:
            field_dict["manager_user_id"] = manager_user_id
        if assignment_deadline_sub_status_id is not UNSET:
            field_dict["assignment_deadline_sub_status_id"] = assignment_deadline_sub_status_id
        if assignment_skip_weekends is not UNSET:
            field_dict["assignment_skip_weekends"] = assignment_skip_weekends
        if completion_deadline_sub_status_id is not UNSET:
            field_dict["completion_deadline_sub_status_id"] = completion_deadline_sub_status_id
        if completion_skip_weekends is not UNSET:
            field_dict["completion_skip_weekends"] = completion_skip_weekends
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if notification_configurations is not UNSET:
            field_dict["notification_configurations"] = notification_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sla_conditions_item import SlaConditionsItem
        from ..models.sla_notification_configurations_item import SlaNotificationConfigurationsItem

        d = dict(src_dict)
        name = d.pop("name")

        condition_match_type = check_sla_condition_match_type(d.pop("condition_match_type"))

        assignment_deadline_days = d.pop("assignment_deadline_days")

        assignment_deadline_parent_status = d.pop("assignment_deadline_parent_status")

        completion_deadline_days = d.pop("completion_deadline_days")

        completion_deadline_parent_status = d.pop("completion_deadline_parent_status")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        position = d.pop("position", UNSET)

        _entity_type = d.pop("entity_type", UNSET)
        entity_type: Unset | SlaEntityType
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = check_sla_entity_type(_entity_type)

        def _parse_manager_role_id(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manager_role_id_type_0 = UUID(data)

                return manager_role_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        manager_role_id = _parse_manager_role_id(d.pop("manager_role_id", UNSET))

        def _parse_manager_user_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        manager_user_id = _parse_manager_user_id(d.pop("manager_user_id", UNSET))

        def _parse_assignment_deadline_sub_status_id(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignment_deadline_sub_status_id_type_0 = UUID(data)

                return assignment_deadline_sub_status_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        assignment_deadline_sub_status_id = _parse_assignment_deadline_sub_status_id(
            d.pop("assignment_deadline_sub_status_id", UNSET)
        )

        assignment_skip_weekends = d.pop("assignment_skip_weekends", UNSET)

        def _parse_completion_deadline_sub_status_id(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completion_deadline_sub_status_id_type_0 = UUID(data)

                return completion_deadline_sub_status_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        completion_deadline_sub_status_id = _parse_completion_deadline_sub_status_id(
            d.pop("completion_deadline_sub_status_id", UNSET)
        )

        completion_skip_weekends = d.pop("completion_skip_weekends", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = SlaConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        notification_configurations = []
        _notification_configurations = d.pop("notification_configurations", UNSET)
        for notification_configurations_item_data in _notification_configurations or []:
            notification_configurations_item = SlaNotificationConfigurationsItem.from_dict(
                notification_configurations_item_data
            )

            notification_configurations.append(notification_configurations_item)

        sla = cls(
            name=name,
            condition_match_type=condition_match_type,
            assignment_deadline_days=assignment_deadline_days,
            assignment_deadline_parent_status=assignment_deadline_parent_status,
            completion_deadline_days=completion_deadline_days,
            completion_deadline_parent_status=completion_deadline_parent_status,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            position=position,
            entity_type=entity_type,
            manager_role_id=manager_role_id,
            manager_user_id=manager_user_id,
            assignment_deadline_sub_status_id=assignment_deadline_sub_status_id,
            assignment_skip_weekends=assignment_skip_weekends,
            completion_deadline_sub_status_id=completion_deadline_sub_status_id,
            completion_skip_weekends=completion_skip_weekends,
            conditions=conditions,
            notification_configurations=notification_configurations,
        )

        sla.additional_properties = d
        return sla

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
