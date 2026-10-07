from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_problem_data_attributes_expected_status import (
    UpdateProblemDataAttributesExpectedStatus,
    check_update_problem_data_attributes_expected_status,
)
from ..models.update_problem_data_attributes_priority import (
    UpdateProblemDataAttributesPriority,
    check_update_problem_data_attributes_priority,
)
from ..models.update_problem_data_attributes_status import (
    UpdateProblemDataAttributesStatus,
    check_update_problem_data_attributes_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_problem_data_attributes_form_field_selections_item import (
        UpdateProblemDataAttributesFormFieldSelectionsItem,
    )


T = TypeVar("T", bound="UpdateProblemDataAttributes")


@_attrs_define
class UpdateProblemDataAttributes:
    """
    Attributes:
        title (str | Unset): The title of the problem
        description (None | str | Unset): The description of the problem
        owner_user_id (int | None | Unset): ID of the user who owns the problem
        owner_group_id (None | str | Unset): ID of the group (team) that owns the problem
        priority (UpdateProblemDataAttributesPriority | Unset): The priority of the problem
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
        form_field_selections (list[UpdateProblemDataAttributesFormFieldSelectionsItem] | Unset): Custom (form) field
            selections for the problem
        status (UpdateProblemDataAttributesStatus | Unset): Target status. Transitions run through the problem status
            workflow: gate fields required by the target status must be supplied in the same request. Other updatable
            attributes may accompany a status change and are applied atomically with it.
        expected_status (UpdateProblemDataAttributesExpectedStatus | Unset): Optional optimistic-concurrency guard: the
            transition is rejected unless the problem is currently in this status.
    """

    title: str | Unset = UNSET
    description: None | str | Unset = UNSET
    owner_user_id: int | None | Unset = UNSET
    owner_group_id: None | str | Unset = UNSET
    priority: UpdateProblemDataAttributesPriority | Unset = UNSET
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
    form_field_selections: list[UpdateProblemDataAttributesFormFieldSelectionsItem] | Unset = UNSET
    status: UpdateProblemDataAttributesStatus | Unset = UNSET
    expected_status: UpdateProblemDataAttributesExpectedStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

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

        form_field_selections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.form_field_selections, Unset):
            form_field_selections = []
            for form_field_selections_item_data in self.form_field_selections:
                form_field_selections_item = form_field_selections_item_data.to_dict()
                form_field_selections.append(form_field_selections_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        expected_status: str | Unset = UNSET
        if not isinstance(self.expected_status, Unset):
            expected_status = self.expected_status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
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
        if form_field_selections is not UNSET:
            field_dict["form_field_selections"] = form_field_selections
        if status is not UNSET:
            field_dict["status"] = status
        if expected_status is not UNSET:
            field_dict["expected_status"] = expected_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_problem_data_attributes_form_field_selections_item import (
            UpdateProblemDataAttributesFormFieldSelectionsItem,
        )

        d = dict(src_dict)
        title = d.pop("title", UNSET)

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
        priority: UpdateProblemDataAttributesPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_update_problem_data_attributes_priority(_priority)

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

        _form_field_selections = d.pop("form_field_selections", UNSET)
        form_field_selections: list[UpdateProblemDataAttributesFormFieldSelectionsItem] | Unset = UNSET
        if _form_field_selections is not UNSET:
            form_field_selections = []
            for form_field_selections_item_data in _form_field_selections:
                form_field_selections_item = UpdateProblemDataAttributesFormFieldSelectionsItem.from_dict(
                    form_field_selections_item_data
                )

                form_field_selections.append(form_field_selections_item)

        _status = d.pop("status", UNSET)
        status: UpdateProblemDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_problem_data_attributes_status(_status)

        _expected_status = d.pop("expected_status", UNSET)
        expected_status: UpdateProblemDataAttributesExpectedStatus | Unset
        if isinstance(_expected_status, Unset):
            expected_status = UNSET
        else:
            expected_status = check_update_problem_data_attributes_expected_status(_expected_status)

        update_problem_data_attributes = cls(
            title=title,
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
            form_field_selections=form_field_selections,
            status=status,
            expected_status=expected_status,
        )

        return update_problem_data_attributes
