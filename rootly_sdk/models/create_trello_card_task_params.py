from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_trello_card_task_params_task_type import (
    CreateTrelloCardTaskParamsTaskType,
    check_create_trello_card_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_trello_card_task_params_archivation import CreateTrelloCardTaskParamsArchivation
    from ..models.create_trello_card_task_params_board import CreateTrelloCardTaskParamsBoard
    from ..models.create_trello_card_task_params_labels_item import CreateTrelloCardTaskParamsLabelsItem
    from ..models.create_trello_card_task_params_list import CreateTrelloCardTaskParamsList


T = TypeVar("T", bound="CreateTrelloCardTaskParams")


@_attrs_define
class CreateTrelloCardTaskParams:
    """
    Attributes:
        title (str): The card title
        board (CreateTrelloCardTaskParamsBoard): The board id and display name
        list_ (CreateTrelloCardTaskParamsList): The list id and display name
        task_type (Union[Unset, CreateTrelloCardTaskParamsTaskType]):
        description (Union[Unset, str]): The card description
        due_date (Union[Unset, str]): The due date
        labels (Union[Unset, list['CreateTrelloCardTaskParamsLabelsItem']]):
        archivation (Union[Unset, CreateTrelloCardTaskParamsArchivation]): The archivation id and display name
    """

    title: str
    board: "CreateTrelloCardTaskParamsBoard"
    list_: "CreateTrelloCardTaskParamsList"
    task_type: Unset | CreateTrelloCardTaskParamsTaskType = UNSET
    description: Unset | str = UNSET
    due_date: Unset | str = UNSET
    labels: Unset | list["CreateTrelloCardTaskParamsLabelsItem"] = UNSET
    archivation: Union[Unset, "CreateTrelloCardTaskParamsArchivation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        board = self.board.to_dict()

        list_ = self.list_.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        due_date = self.due_date

        labels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        archivation: Unset | dict[str, Any] = UNSET
        if not isinstance(self.archivation, Unset):
            archivation = self.archivation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "board": board,
                "list": list_,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if labels is not UNSET:
            field_dict["labels"] = labels
        if archivation is not UNSET:
            field_dict["archivation"] = archivation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_trello_card_task_params_archivation import CreateTrelloCardTaskParamsArchivation
        from ..models.create_trello_card_task_params_board import CreateTrelloCardTaskParamsBoard
        from ..models.create_trello_card_task_params_labels_item import CreateTrelloCardTaskParamsLabelsItem
        from ..models.create_trello_card_task_params_list import CreateTrelloCardTaskParamsList

        d = dict(src_dict)
        title = d.pop("title")

        board = CreateTrelloCardTaskParamsBoard.from_dict(d.pop("board"))

        list_ = CreateTrelloCardTaskParamsList.from_dict(d.pop("list"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateTrelloCardTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_trello_card_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        due_date = d.pop("due_date", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = CreateTrelloCardTaskParamsLabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        _archivation = d.pop("archivation", UNSET)
        archivation: Unset | CreateTrelloCardTaskParamsArchivation
        if isinstance(_archivation, Unset):
            archivation = UNSET
        else:
            archivation = CreateTrelloCardTaskParamsArchivation.from_dict(_archivation)

        create_trello_card_task_params = cls(
            title=title,
            board=board,
            list_=list_,
            task_type=task_type,
            description=description,
            due_date=due_date,
            labels=labels,
            archivation=archivation,
        )

        create_trello_card_task_params.additional_properties = d
        return create_trello_card_task_params

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
