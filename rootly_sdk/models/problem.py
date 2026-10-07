from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.problem_priority import ProblemPriority, check_problem_priority
from ..models.problem_status import ProblemStatus, check_problem_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="Problem")


@_attrs_define
class Problem:
    """
    Attributes:
        title (str): The title of the problem
        status (ProblemStatus): The status of the problem
        created_at (str): Date of creation
        updated_at (str): Date of last update
        sequential_id (int | Unset): Team-scoped sequential number of the problem
        display_id (str | Unset): Human-readable identifier of the problem (e.g. PROB-12)
        description (None | str | Unset): The description of the problem
        owner_user_id (int | None | Unset): ID of the user who owns the problem
        owner_group_id (None | str | Unset): ID of the group (team) that owns the problem
        priority (ProblemPriority | Unset): The priority of the problem
        due_date (datetime.date | None | Unset): The due date of the problem
        scope (None | str | Unset): The scope of the problem
        exit_criteria (None | str | Unset): The exit criteria of the problem
        impact_so_far (None | str | Unset): The impact observed so far
        root_cause (None | str | Unset): The root cause of the problem
        resolution (None | str | Unset): The resolution of the problem
        deferral_reason (None | str | Unset): The reason and accepted risk for deferring the problem
        cancellation_reason (None | str | Unset): The reason for cancelling the problem
        next_review_at (None | str | Unset): The next review date for a deferred problem
        re_review_cadence (int | None | Unset): Days between reviews for a deferred problem
        created_by_user_id (int | Unset): ID of the user who created the problem
        in_progress_by_user_id (int | None | Unset): ID of the user who moved the problem to in progress
        completed_by_user_id (int | None | Unset): ID of the user who completed the problem
        deferred_by_user_id (int | None | Unset): ID of the user who approved deferring the problem
        cancelled_by_user_id (int | None | Unset): ID of the user who cancelled the problem
        in_progress_at (None | str | Unset): When the problem moved to in progress
        completed_at (None | str | Unset): When the problem was completed
        deferred_at (None | str | Unset): When the problem was deferred
        cancelled_at (None | str | Unset): When the problem was cancelled
        incident_ids (list[str] | Unset): IDs of incidents linked to the problem
        incidents_count (int | Unset): Number of incidents linked to the problem
        action_items_count (int | Unset): Number of action items on the problem
        subscribers_count (int | Unset): Number of users following the problem
        users_assigned_count (int | Unset): Number of problem role assignees
        url (str | Unset): URL of the problem in the Rootly web app
    """

    title: str
    status: ProblemStatus
    created_at: str
    updated_at: str
    sequential_id: int | Unset = UNSET
    display_id: str | Unset = UNSET
    description: None | str | Unset = UNSET
    owner_user_id: int | None | Unset = UNSET
    owner_group_id: None | str | Unset = UNSET
    priority: ProblemPriority | Unset = UNSET
    due_date: datetime.date | None | Unset = UNSET
    scope: None | str | Unset = UNSET
    exit_criteria: None | str | Unset = UNSET
    impact_so_far: None | str | Unset = UNSET
    root_cause: None | str | Unset = UNSET
    resolution: None | str | Unset = UNSET
    deferral_reason: None | str | Unset = UNSET
    cancellation_reason: None | str | Unset = UNSET
    next_review_at: None | str | Unset = UNSET
    re_review_cadence: int | None | Unset = UNSET
    created_by_user_id: int | Unset = UNSET
    in_progress_by_user_id: int | None | Unset = UNSET
    completed_by_user_id: int | None | Unset = UNSET
    deferred_by_user_id: int | None | Unset = UNSET
    cancelled_by_user_id: int | None | Unset = UNSET
    in_progress_at: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    deferred_at: None | str | Unset = UNSET
    cancelled_at: None | str | Unset = UNSET
    incident_ids: list[str] | Unset = UNSET
    incidents_count: int | Unset = UNSET
    action_items_count: int | Unset = UNSET
    subscribers_count: int | Unset = UNSET
    users_assigned_count: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        status: str = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        sequential_id = self.sequential_id

        display_id = self.display_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        owner_user_id: int | None | Unset
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = self.owner_user_id

        owner_group_id: None | str | Unset
        if isinstance(self.owner_group_id, Unset):
            owner_group_id = UNSET
        else:
            owner_group_id = self.owner_group_id

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        exit_criteria: None | str | Unset
        if isinstance(self.exit_criteria, Unset):
            exit_criteria = UNSET
        else:
            exit_criteria = self.exit_criteria

        impact_so_far: None | str | Unset
        if isinstance(self.impact_so_far, Unset):
            impact_so_far = UNSET
        else:
            impact_so_far = self.impact_so_far

        root_cause: None | str | Unset
        if isinstance(self.root_cause, Unset):
            root_cause = UNSET
        else:
            root_cause = self.root_cause

        resolution: None | str | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        deferral_reason: None | str | Unset
        if isinstance(self.deferral_reason, Unset):
            deferral_reason = UNSET
        else:
            deferral_reason = self.deferral_reason

        cancellation_reason: None | str | Unset
        if isinstance(self.cancellation_reason, Unset):
            cancellation_reason = UNSET
        else:
            cancellation_reason = self.cancellation_reason

        next_review_at: None | str | Unset
        if isinstance(self.next_review_at, Unset):
            next_review_at = UNSET
        else:
            next_review_at = self.next_review_at

        re_review_cadence: int | None | Unset
        if isinstance(self.re_review_cadence, Unset):
            re_review_cadence = UNSET
        else:
            re_review_cadence = self.re_review_cadence

        created_by_user_id = self.created_by_user_id

        in_progress_by_user_id: int | None | Unset
        if isinstance(self.in_progress_by_user_id, Unset):
            in_progress_by_user_id = UNSET
        else:
            in_progress_by_user_id = self.in_progress_by_user_id

        completed_by_user_id: int | None | Unset
        if isinstance(self.completed_by_user_id, Unset):
            completed_by_user_id = UNSET
        else:
            completed_by_user_id = self.completed_by_user_id

        deferred_by_user_id: int | None | Unset
        if isinstance(self.deferred_by_user_id, Unset):
            deferred_by_user_id = UNSET
        else:
            deferred_by_user_id = self.deferred_by_user_id

        cancelled_by_user_id: int | None | Unset
        if isinstance(self.cancelled_by_user_id, Unset):
            cancelled_by_user_id = UNSET
        else:
            cancelled_by_user_id = self.cancelled_by_user_id

        in_progress_at: None | str | Unset
        if isinstance(self.in_progress_at, Unset):
            in_progress_at = UNSET
        else:
            in_progress_at = self.in_progress_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        deferred_at: None | str | Unset
        if isinstance(self.deferred_at, Unset):
            deferred_at = UNSET
        else:
            deferred_at = self.deferred_at

        cancelled_at: None | str | Unset
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = self.cancelled_at

        incident_ids: list[str] | Unset = UNSET
        if not isinstance(self.incident_ids, Unset):
            incident_ids = self.incident_ids

        incidents_count = self.incidents_count

        action_items_count = self.action_items_count

        subscribers_count = self.subscribers_count

        users_assigned_count = self.users_assigned_count

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if sequential_id is not UNSET:
            field_dict["sequential_id"] = sequential_id
        if display_id is not UNSET:
            field_dict["display_id"] = display_id
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if scope is not UNSET:
            field_dict["scope"] = scope
        if exit_criteria is not UNSET:
            field_dict["exit_criteria"] = exit_criteria
        if impact_so_far is not UNSET:
            field_dict["impact_so_far"] = impact_so_far
        if root_cause is not UNSET:
            field_dict["root_cause"] = root_cause
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if deferral_reason is not UNSET:
            field_dict["deferral_reason"] = deferral_reason
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if next_review_at is not UNSET:
            field_dict["next_review_at"] = next_review_at
        if re_review_cadence is not UNSET:
            field_dict["re_review_cadence"] = re_review_cadence
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if in_progress_by_user_id is not UNSET:
            field_dict["in_progress_by_user_id"] = in_progress_by_user_id
        if completed_by_user_id is not UNSET:
            field_dict["completed_by_user_id"] = completed_by_user_id
        if deferred_by_user_id is not UNSET:
            field_dict["deferred_by_user_id"] = deferred_by_user_id
        if cancelled_by_user_id is not UNSET:
            field_dict["cancelled_by_user_id"] = cancelled_by_user_id
        if in_progress_at is not UNSET:
            field_dict["in_progress_at"] = in_progress_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if deferred_at is not UNSET:
            field_dict["deferred_at"] = deferred_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if incident_ids is not UNSET:
            field_dict["incident_ids"] = incident_ids
        if incidents_count is not UNSET:
            field_dict["incidents_count"] = incidents_count
        if action_items_count is not UNSET:
            field_dict["action_items_count"] = action_items_count
        if subscribers_count is not UNSET:
            field_dict["subscribers_count"] = subscribers_count
        if users_assigned_count is not UNSET:
            field_dict["users_assigned_count"] = users_assigned_count
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        status = check_problem_status(d.pop("status"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        sequential_id = d.pop("sequential_id", UNSET)

        display_id = d.pop("display_id", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_owner_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))

        def _parse_owner_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_group_id = _parse_owner_group_id(d.pop("owner_group_id", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: ProblemPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_problem_priority(_priority)

        def _parse_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = datetime.date.fromisoformat(data)

                return due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_exit_criteria(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exit_criteria = _parse_exit_criteria(d.pop("exit_criteria", UNSET))

        def _parse_impact_so_far(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        impact_so_far = _parse_impact_so_far(d.pop("impact_so_far", UNSET))

        def _parse_root_cause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_cause = _parse_root_cause(d.pop("root_cause", UNSET))

        def _parse_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_deferral_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deferral_reason = _parse_deferral_reason(d.pop("deferral_reason", UNSET))

        def _parse_cancellation_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_reason = _parse_cancellation_reason(d.pop("cancellation_reason", UNSET))

        def _parse_next_review_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_review_at = _parse_next_review_at(d.pop("next_review_at", UNSET))

        def _parse_re_review_cadence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        re_review_cadence = _parse_re_review_cadence(d.pop("re_review_cadence", UNSET))

        created_by_user_id = d.pop("created_by_user_id", UNSET)

        def _parse_in_progress_by_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        in_progress_by_user_id = _parse_in_progress_by_user_id(d.pop("in_progress_by_user_id", UNSET))

        def _parse_completed_by_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completed_by_user_id = _parse_completed_by_user_id(d.pop("completed_by_user_id", UNSET))

        def _parse_deferred_by_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deferred_by_user_id = _parse_deferred_by_user_id(d.pop("deferred_by_user_id", UNSET))

        def _parse_cancelled_by_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cancelled_by_user_id = _parse_cancelled_by_user_id(d.pop("cancelled_by_user_id", UNSET))

        def _parse_in_progress_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        in_progress_at = _parse_in_progress_at(d.pop("in_progress_at", UNSET))

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_deferred_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deferred_at = _parse_deferred_at(d.pop("deferred_at", UNSET))

        def _parse_cancelled_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

        incident_ids = cast(list[str], d.pop("incident_ids", UNSET))

        incidents_count = d.pop("incidents_count", UNSET)

        action_items_count = d.pop("action_items_count", UNSET)

        subscribers_count = d.pop("subscribers_count", UNSET)

        users_assigned_count = d.pop("users_assigned_count", UNSET)

        url = d.pop("url", UNSET)

        problem = cls(
            title=title,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            sequential_id=sequential_id,
            display_id=display_id,
            description=description,
            owner_user_id=owner_user_id,
            owner_group_id=owner_group_id,
            priority=priority,
            due_date=due_date,
            scope=scope,
            exit_criteria=exit_criteria,
            impact_so_far=impact_so_far,
            root_cause=root_cause,
            resolution=resolution,
            deferral_reason=deferral_reason,
            cancellation_reason=cancellation_reason,
            next_review_at=next_review_at,
            re_review_cadence=re_review_cadence,
            created_by_user_id=created_by_user_id,
            in_progress_by_user_id=in_progress_by_user_id,
            completed_by_user_id=completed_by_user_id,
            deferred_by_user_id=deferred_by_user_id,
            cancelled_by_user_id=cancelled_by_user_id,
            in_progress_at=in_progress_at,
            completed_at=completed_at,
            deferred_at=deferred_at,
            cancelled_at=cancelled_at,
            incident_ids=incident_ids,
            incidents_count=incidents_count,
            action_items_count=action_items_count,
            subscribers_count=subscribers_count,
            users_assigned_count=users_assigned_count,
            url=url,
        )

        problem.additional_properties = d
        return problem

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
