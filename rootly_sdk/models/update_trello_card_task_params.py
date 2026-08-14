from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_trello_card_task_params_task_type import (
    UpdateTrelloCardTaskParamsTaskType,
    check_update_trello_card_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_trello_card_task_params_archivation import UpdateTrelloCardTaskParamsArchivation
    from ..models.update_trello_card_task_params_board import UpdateTrelloCardTaskParamsBoard
    from ..models.update_trello_card_task_params_labels_item import UpdateTrelloCardTaskParamsLabelsItem
    from ..models.update_trello_card_task_params_list import UpdateTrelloCardTaskParamsList


T = TypeVar("T", bound="UpdateTrelloCardTaskParams")


@_attrs_define
class UpdateTrelloCardTaskParams:
    """
    Attributes:
        card_id (str): The card id
        archivation (UpdateTrelloCardTaskParamsArchivation): The archivation id and display name
        task_type (Union[Unset, UpdateTrelloCardTaskParamsTaskType]):
        title (Union[Unset, str]): The card title
        description (Union[Unset, str]): The card description
        due_date (Union[Unset, str]): The due date
        board (Union[Unset, UpdateTrelloCardTaskParamsBoard]): The board id and display name
        list_ (Union[Unset, UpdateTrelloCardTaskParamsList]): The list id and display name
        labels (Union[Unset, list['UpdateTrelloCardTaskParamsLabelsItem']]):
    """

    card_id: str
    archivation: "UpdateTrelloCardTaskParamsArchivation"
    task_type: Unset | UpdateTrelloCardTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    due_date: Unset | str = UNSET
    board: Union[Unset, "UpdateTrelloCardTaskParamsBoard"] = UNSET
    list_: Union[Unset, "UpdateTrelloCardTaskParamsList"] = UNSET
    labels: Unset | list["UpdateTrelloCardTaskParamsLabelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        archivation = self.archivation.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        due_date = self.due_date

        board: Unset | dict[str, Any] = UNSET
        if not isinstance(self.board, Unset):
            board = self.board.to_dict()

        list_: Unset | dict[str, Any] = UNSET
        if not isinstance(self.list_, Unset):
            list_ = self.list_.to_dict()

        labels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card_id": card_id,
                "archivation": archivation,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if board is not UNSET:
            field_dict["board"] = board
        if list_ is not UNSET:
            field_dict["list"] = list_
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_trello_card_task_params_archivation import UpdateTrelloCardTaskParamsArchivation
        from ..models.update_trello_card_task_params_board import UpdateTrelloCardTaskParamsBoard
        from ..models.update_trello_card_task_params_labels_item import UpdateTrelloCardTaskParamsLabelsItem
        from ..models.update_trello_card_task_params_list import UpdateTrelloCardTaskParamsList

        d = dict(src_dict)
        card_id = d.pop("card_id")

        archivation = UpdateTrelloCardTaskParamsArchivation.from_dict(d.pop("archivation"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateTrelloCardTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_trello_card_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        due_date = d.pop("due_date", UNSET)

        _board = d.pop("board", UNSET)
        board: Unset | UpdateTrelloCardTaskParamsBoard
        if isinstance(_board, Unset):
            board = UNSET
        else:
            board = UpdateTrelloCardTaskParamsBoard.from_dict(_board)

        _list_ = d.pop("list", UNSET)
        list_: Unset | UpdateTrelloCardTaskParamsList
        if isinstance(_list_, Unset):
            list_ = UNSET
        else:
            list_ = UpdateTrelloCardTaskParamsList.from_dict(_list_)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = UpdateTrelloCardTaskParamsLabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        update_trello_card_task_params = cls(
            card_id=card_id,
            archivation=archivation,
            task_type=task_type,
            title=title,
            description=description,
            due_date=due_date,
            board=board,
            list_=list_,
            labels=labels,
        )

        update_trello_card_task_params.additional_properties = d
        return update_trello_card_task_params

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
