from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_incident_feedback_data import NewIncidentFeedbackData


T = TypeVar("T", bound="NewIncidentFeedback")


@_attrs_define
class NewIncidentFeedback:
    """
    Attributes:
        data (NewIncidentFeedbackData):
    """

    data: NewIncidentFeedbackData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_incident_feedback_data import NewIncidentFeedbackData

        d = dict(src_dict)
        data = NewIncidentFeedbackData.from_dict(d.pop("data"))

        new_incident_feedback = cls(
            data=data,
        )

        return new_incident_feedback
