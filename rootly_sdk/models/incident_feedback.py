from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_feedback_rating import IncidentFeedbackRating, check_incident_feedback_rating

T = TypeVar("T", bound="IncidentFeedback")


@_attrs_define
class IncidentFeedback:
    """
    Attributes:
        feedback (str): The feedback of the incident feedback
        rating (IncidentFeedbackRating): The rating of the incident feedback
        anonymous (bool): Is the feedback anonymous?
        created_at (str): Date of creation
        updated_at (str): Date of last update
    """

    feedback: str
    rating: IncidentFeedbackRating
    anonymous: bool
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feedback = self.feedback

        rating: int = self.rating

        anonymous = self.anonymous

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedback": feedback,
                "rating": rating,
                "anonymous": anonymous,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feedback = d.pop("feedback")

        rating = check_incident_feedback_rating(d.pop("rating"))

        anonymous = d.pop("anonymous")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        incident_feedback = cls(
            feedback=feedback,
            rating=rating,
            anonymous=anonymous,
            created_at=created_at,
            updated_at=updated_at,
        )

        incident_feedback.additional_properties = d
        return incident_feedback

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
