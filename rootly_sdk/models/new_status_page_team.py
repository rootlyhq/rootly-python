from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_status_page_team_data import NewStatusPageTeamData


T = TypeVar("T", bound="NewStatusPageTeam")


@_attrs_define
class NewStatusPageTeam:
    """
    Attributes:
        data (NewStatusPageTeamData):
    """

    data: NewStatusPageTeamData

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
        from ..models.new_status_page_team_data import NewStatusPageTeamData

        d = dict(src_dict)
        data = NewStatusPageTeamData.from_dict(d.pop("data"))

        new_status_page_team = cls(
            data=data,
        )

        return new_status_page_team
