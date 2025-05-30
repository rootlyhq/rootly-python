from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_incident_feedback_data_attributes_rating import NewIncidentFeedbackDataAttributesRating
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
    anonymous: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        feedback = self.feedback

        rating = self.rating.value

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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        feedback = d.pop("feedback")

        rating = NewIncidentFeedbackDataAttributesRating(d.pop("rating"))

        anonymous = d.pop("anonymous", UNSET)

        new_incident_feedback_data_attributes = cls(
            feedback=feedback,
            rating=rating,
            anonymous=anonymous,
        )

        return new_incident_feedback_data_attributes
