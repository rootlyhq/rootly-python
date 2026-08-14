from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_incident_feedback_data_attributes_rating import (
    NewIncidentFeedbackDataAttributesRating,
    check_new_incident_feedback_data_attributes_rating,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentFeedbackDataAttributes")


@_attrs_define
class NewIncidentFeedbackDataAttributes:
    """
    Attributes:
        feedback (str): The feedback of the incident feedback
        rating (NewIncidentFeedbackDataAttributesRating): The rating of the incident feedback
        anonymous (Union[Unset, bool]): Is the feedback anonymous?
    """

    feedback: str
    rating: NewIncidentFeedbackDataAttributesRating
    anonymous: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        feedback = self.feedback

        rating: int = self.rating

        anonymous = self.anonymous

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "feedback": feedback,
                "rating": rating,
            }
        )
        if anonymous is not UNSET:
            field_dict["anonymous"] = anonymous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feedback = d.pop("feedback")

        rating = check_new_incident_feedback_data_attributes_rating(d.pop("rating"))

        anonymous = d.pop("anonymous", UNSET)

        new_incident_feedback_data_attributes = cls(
            feedback=feedback,
            rating=rating,
            anonymous=anonymous,
        )

        return new_incident_feedback_data_attributes
