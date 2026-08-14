from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_watsonx_chat_completion_task_params_task_type import (
    CreateWatsonxChatCompletionTaskParamsTaskType,
    check_create_watsonx_chat_completion_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_watsonx_chat_completion_task_params_model import CreateWatsonxChatCompletionTaskParamsModel


T = TypeVar("T", bound="CreateWatsonxChatCompletionTaskParams")


@_attrs_define
class CreateWatsonxChatCompletionTaskParams:
    """
    Attributes:
        model (CreateWatsonxChatCompletionTaskParamsModel): The WatsonX model. eg: ibm/granite-3-b8b-instruct
        prompt (str): The prompt to send to WatsonX
        project_id (str):
        task_type (Union[Unset, CreateWatsonxChatCompletionTaskParamsTaskType]):
        system_prompt (Union[Unset, str]): The system prompt to send to WatsonX (optional)
    """

    model: "CreateWatsonxChatCompletionTaskParamsModel"
    prompt: str
    project_id: str
    task_type: Unset | CreateWatsonxChatCompletionTaskParamsTaskType = UNSET
    system_prompt: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model.to_dict()

        prompt = self.prompt

        project_id = self.project_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        system_prompt = self.system_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "prompt": prompt,
                "project_id": project_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_watsonx_chat_completion_task_params_model import CreateWatsonxChatCompletionTaskParamsModel

        d = dict(src_dict)
        model = CreateWatsonxChatCompletionTaskParamsModel.from_dict(d.pop("model"))

        prompt = d.pop("prompt")

        project_id = d.pop("project_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateWatsonxChatCompletionTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_watsonx_chat_completion_task_params_task_type(_task_type)

        system_prompt = d.pop("system_prompt", UNSET)

        create_watsonx_chat_completion_task_params = cls(
            model=model,
            prompt=prompt,
            project_id=project_id,
            task_type=task_type,
            system_prompt=system_prompt,
        )

        create_watsonx_chat_completion_task_params.additional_properties = d
        return create_watsonx_chat_completion_task_params

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
