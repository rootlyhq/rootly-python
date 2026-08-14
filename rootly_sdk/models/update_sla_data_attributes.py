from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.update_sla_data_attributes_assignment_deadline_days import (
    UpdateSlaDataAttributesAssignmentDeadlineDays,
    check_update_sla_data_attributes_assignment_deadline_days,
)
from ..models.update_sla_data_attributes_assignment_deadline_parent_status import (
    UpdateSlaDataAttributesAssignmentDeadlineParentStatus,
    check_update_sla_data_attributes_assignment_deadline_parent_status,
)
from ..models.update_sla_data_attributes_completion_deadline_days import (
    UpdateSlaDataAttributesCompletionDeadlineDays,
    check_update_sla_data_attributes_completion_deadline_days,
)
from ..models.update_sla_data_attributes_completion_deadline_parent_status import (
    UpdateSlaDataAttributesCompletionDeadlineParentStatus,
    check_update_sla_data_attributes_completion_deadline_parent_status,
)
from ..models.update_sla_data_attributes_condition_match_type import (
    UpdateSlaDataAttributesConditionMatchType,
    check_update_sla_data_attributes_condition_match_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_sla_data_attributes_conditions_item import UpdateSlaDataAttributesConditionsItem
    from ..models.update_sla_data_attributes_notification_configurations_item import (
        UpdateSlaDataAttributesNotificationConfigurationsItem,
    )


T = TypeVar("T", bound="UpdateSlaDataAttributes")


@_attrs_define
class UpdateSlaDataAttributes:
    """
    Attributes:
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        name (Union[Unset, str]): The name of the SLA
        description (Union[None, Unset, str]): A description of the SLA
        position (Union[None, Unset, int]): Position of the SLA for ordering
        condition_match_type (Union[Unset, UpdateSlaDataAttributesConditionMatchType]): Whether all or any conditions
            must match
        manager_role_id (Union[None, UUID, Unset]): The ID of the incident role responsible for this SLA. Exactly one of
            `manager_role_id` or `manager_user_id` must be provided.
        manager_user_id (Union[None, Unset, int]): The ID of the user responsible for this SLA. Exactly one of
            `manager_role_id` or `manager_user_id` must be provided.
        assignment_deadline_days (Union[Unset, UpdateSlaDataAttributesAssignmentDeadlineDays]): Number of days for the
            assignment deadline
        assignment_deadline_parent_status (Union[Unset, UpdateSlaDataAttributesAssignmentDeadlineParentStatus]): The
            incident parent status that triggers the assignment deadline
        assignment_deadline_sub_status_id (Union[None, UUID, Unset]): Sub-status for the assignment deadline. Required
            when custom lifecycle statuses are enabled on the team.
        assignment_skip_weekends (Union[Unset, bool]): Whether to skip weekends when calculating the assignment deadline
        completion_deadline_days (Union[Unset, UpdateSlaDataAttributesCompletionDeadlineDays]): Number of days for the
            completion deadline
        completion_deadline_parent_status (Union[Unset, UpdateSlaDataAttributesCompletionDeadlineParentStatus]): The
            incident parent status that triggers the completion deadline
        completion_deadline_sub_status_id (Union[None, UUID, Unset]): Sub-status for the completion deadline. Required
            when custom lifecycle statuses are enabled on the team.
        completion_skip_weekends (Union[Unset, bool]): Whether to skip weekends when calculating the completion deadline
        conditions (Union[Unset, list['UpdateSlaDataAttributesConditionsItem']]): Conditions that determine which
            incidents this SLA applies to. Replaces all existing conditions.
        notification_configurations (Union[Unset, list['UpdateSlaDataAttributesNotificationConfigurationsItem']]):
            Notification timing configurations. Replaces all existing configurations.
    """

    slug: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    condition_match_type: Union[Unset, UpdateSlaDataAttributesConditionMatchType] = UNSET
    manager_role_id: Union[None, UUID, Unset] = UNSET
    manager_user_id: Union[None, Unset, int] = UNSET
    assignment_deadline_days: Union[Unset, UpdateSlaDataAttributesAssignmentDeadlineDays] = UNSET
    assignment_deadline_parent_status: Union[Unset, UpdateSlaDataAttributesAssignmentDeadlineParentStatus] = UNSET
    assignment_deadline_sub_status_id: Union[None, UUID, Unset] = UNSET
    assignment_skip_weekends: Union[Unset, bool] = UNSET
    completion_deadline_days: Union[Unset, UpdateSlaDataAttributesCompletionDeadlineDays] = UNSET
    completion_deadline_parent_status: Union[Unset, UpdateSlaDataAttributesCompletionDeadlineParentStatus] = UNSET
    completion_deadline_sub_status_id: Union[None, UUID, Unset] = UNSET
    completion_skip_weekends: Union[Unset, bool] = UNSET
    conditions: Union[Unset, list["UpdateSlaDataAttributesConditionsItem"]] = UNSET
    notification_configurations: Union[Unset, list["UpdateSlaDataAttributesNotificationConfigurationsItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        condition_match_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_match_type, Unset):
            condition_match_type = self.condition_match_type

        manager_role_id: Union[None, Unset, str]
        if isinstance(self.manager_role_id, Unset):
            manager_role_id = UNSET
        elif isinstance(self.manager_role_id, UUID):
            manager_role_id = str(self.manager_role_id)
        else:
            manager_role_id = self.manager_role_id

        manager_user_id: Union[None, Unset, int]
        if isinstance(self.manager_user_id, Unset):
            manager_user_id = UNSET
        else:
            manager_user_id = self.manager_user_id

        assignment_deadline_days: Union[Unset, int] = UNSET
        if not isinstance(self.assignment_deadline_days, Unset):
            assignment_deadline_days = self.assignment_deadline_days

        assignment_deadline_parent_status: Union[Unset, str] = UNSET
        if not isinstance(self.assignment_deadline_parent_status, Unset):
            assignment_deadline_parent_status = self.assignment_deadline_parent_status

        assignment_deadline_sub_status_id: Union[None, Unset, str]
        if isinstance(self.assignment_deadline_sub_status_id, Unset):
            assignment_deadline_sub_status_id = UNSET
        elif isinstance(self.assignment_deadline_sub_status_id, UUID):
            assignment_deadline_sub_status_id = str(self.assignment_deadline_sub_status_id)
        else:
            assignment_deadline_sub_status_id = self.assignment_deadline_sub_status_id

        assignment_skip_weekends = self.assignment_skip_weekends

        completion_deadline_days: Union[Unset, int] = UNSET
        if not isinstance(self.completion_deadline_days, Unset):
            completion_deadline_days = self.completion_deadline_days

        completion_deadline_parent_status: Union[Unset, str] = UNSET
        if not isinstance(self.completion_deadline_parent_status, Unset):
            completion_deadline_parent_status = self.completion_deadline_parent_status

        completion_deadline_sub_status_id: Union[None, Unset, str]
        if isinstance(self.completion_deadline_sub_status_id, Unset):
            completion_deadline_sub_status_id = UNSET
        elif isinstance(self.completion_deadline_sub_status_id, UUID):
            completion_deadline_sub_status_id = str(self.completion_deadline_sub_status_id)
        else:
            completion_deadline_sub_status_id = self.completion_deadline_sub_status_id

        completion_skip_weekends = self.completion_skip_weekends

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        notification_configurations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_configurations, Unset):
            notification_configurations = []
            for notification_configurations_item_data in self.notification_configurations:
                notification_configurations_item = notification_configurations_item_data.to_dict()
                notification_configurations.append(notification_configurations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if condition_match_type is not UNSET:
            field_dict["condition_match_type"] = condition_match_type
        if manager_role_id is not UNSET:
            field_dict["manager_role_id"] = manager_role_id
        if manager_user_id is not UNSET:
            field_dict["manager_user_id"] = manager_user_id
        if assignment_deadline_days is not UNSET:
            field_dict["assignment_deadline_days"] = assignment_deadline_days
        if assignment_deadline_parent_status is not UNSET:
            field_dict["assignment_deadline_parent_status"] = assignment_deadline_parent_status
        if assignment_deadline_sub_status_id is not UNSET:
            field_dict["assignment_deadline_sub_status_id"] = assignment_deadline_sub_status_id
        if assignment_skip_weekends is not UNSET:
            field_dict["assignment_skip_weekends"] = assignment_skip_weekends
        if completion_deadline_days is not UNSET:
            field_dict["completion_deadline_days"] = completion_deadline_days
        if completion_deadline_parent_status is not UNSET:
            field_dict["completion_deadline_parent_status"] = completion_deadline_parent_status
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
        from ..models.update_sla_data_attributes_conditions_item import UpdateSlaDataAttributesConditionsItem
        from ..models.update_sla_data_attributes_notification_configurations_item import (
            UpdateSlaDataAttributesNotificationConfigurationsItem,
        )

        d = dict(src_dict)

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        _condition_match_type = d.pop("condition_match_type", UNSET)
        condition_match_type: Union[Unset, UpdateSlaDataAttributesConditionMatchType]
        if isinstance(_condition_match_type, Unset):
            condition_match_type = UNSET
        else:
            condition_match_type = check_update_sla_data_attributes_condition_match_type(_condition_match_type)

        def _parse_manager_role_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        manager_role_id = _parse_manager_role_id(d.pop("manager_role_id", UNSET))

        def _parse_manager_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        manager_user_id = _parse_manager_user_id(d.pop("manager_user_id", UNSET))

        _assignment_deadline_days = d.pop("assignment_deadline_days", UNSET)
        assignment_deadline_days: Union[Unset, UpdateSlaDataAttributesAssignmentDeadlineDays]
        if isinstance(_assignment_deadline_days, Unset):
            assignment_deadline_days = UNSET
        else:
            assignment_deadline_days = check_update_sla_data_attributes_assignment_deadline_days(
                _assignment_deadline_days
            )

        _assignment_deadline_parent_status = d.pop("assignment_deadline_parent_status", UNSET)
        assignment_deadline_parent_status: Union[Unset, UpdateSlaDataAttributesAssignmentDeadlineParentStatus]
        if isinstance(_assignment_deadline_parent_status, Unset):
            assignment_deadline_parent_status = UNSET
        else:
            assignment_deadline_parent_status = check_update_sla_data_attributes_assignment_deadline_parent_status(
                _assignment_deadline_parent_status
            )

        def _parse_assignment_deadline_sub_status_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        assignment_deadline_sub_status_id = _parse_assignment_deadline_sub_status_id(
            d.pop("assignment_deadline_sub_status_id", UNSET)
        )

        assignment_skip_weekends = d.pop("assignment_skip_weekends", UNSET)

        _completion_deadline_days = d.pop("completion_deadline_days", UNSET)
        completion_deadline_days: Union[Unset, UpdateSlaDataAttributesCompletionDeadlineDays]
        if isinstance(_completion_deadline_days, Unset):
            completion_deadline_days = UNSET
        else:
            completion_deadline_days = check_update_sla_data_attributes_completion_deadline_days(
                _completion_deadline_days
            )

        _completion_deadline_parent_status = d.pop("completion_deadline_parent_status", UNSET)
        completion_deadline_parent_status: Union[Unset, UpdateSlaDataAttributesCompletionDeadlineParentStatus]
        if isinstance(_completion_deadline_parent_status, Unset):
            completion_deadline_parent_status = UNSET
        else:
            completion_deadline_parent_status = check_update_sla_data_attributes_completion_deadline_parent_status(
                _completion_deadline_parent_status
            )

        def _parse_completion_deadline_sub_status_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        completion_deadline_sub_status_id = _parse_completion_deadline_sub_status_id(
            d.pop("completion_deadline_sub_status_id", UNSET)
        )

        completion_skip_weekends = d.pop("completion_skip_weekends", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = UpdateSlaDataAttributesConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        notification_configurations = []
        _notification_configurations = d.pop("notification_configurations", UNSET)
        for notification_configurations_item_data in _notification_configurations or []:
            notification_configurations_item = UpdateSlaDataAttributesNotificationConfigurationsItem.from_dict(
                notification_configurations_item_data
            )

            notification_configurations.append(notification_configurations_item)

        update_sla_data_attributes = cls(
            slug=slug,
            name=name,
            description=description,
            position=position,
            condition_match_type=condition_match_type,
            manager_role_id=manager_role_id,
            manager_user_id=manager_user_id,
            assignment_deadline_days=assignment_deadline_days,
            assignment_deadline_parent_status=assignment_deadline_parent_status,
            assignment_deadline_sub_status_id=assignment_deadline_sub_status_id,
            assignment_skip_weekends=assignment_skip_weekends,
            completion_deadline_days=completion_deadline_days,
            completion_deadline_parent_status=completion_deadline_parent_status,
            completion_deadline_sub_status_id=completion_deadline_sub_status_id,
            completion_skip_weekends=completion_skip_weekends,
            conditions=conditions,
            notification_configurations=notification_configurations,
        )

        return update_sla_data_attributes
