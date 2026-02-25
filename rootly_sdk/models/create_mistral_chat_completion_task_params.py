from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_mistral_chat_completion_task_params_task_type import (
    CreateMistralChatCompletionTaskParamsTaskType,
    check_create_mistral_chat_completion_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_mistral_chat_completion_task_params_model import CreateMistralChatCompletionTaskParamsModel


T = TypeVar("T", bound="CreateMistralChatCompletionTaskParams")


@_attrs_define
class CreateMistralChatCompletionTaskParams:
    """
    Attributes:
        model (CreateMistralChatCompletionTaskParamsModel): The Mistral model. eg: mistral-large-latest
        prompt (str): The prompt to send to Mistral
        task_type (Union[Unset, CreateMistralChatCompletionTaskParamsTaskType]):
        system_prompt (Union[Unset, str]): The system prompt to send to Mistral (optional)
        temperature (Union[Unset, float]): Sampling temperature (0.0-1.5). Higher values make output more random.
        max_tokens (Union[Unset, int]): Maximum number of tokens to generate
        top_p (Union[Unset, float]): Nucleus sampling parameter (0.0-1.0)
    """

    model: "CreateMistralChatCompletionTaskParamsModel"
    prompt: str
    task_type: Unset | CreateMistralChatCompletionTaskParamsTaskType = UNSET
    system_prompt: Unset | str = UNSET
    temperature: Unset | float = UNSET
    max_tokens: Unset | int = UNSET
    top_p: Unset | float = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model.to_dict()

        prompt = self.prompt

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        system_prompt = self.system_prompt

        temperature = self.temperature

        max_tokens = self.max_tokens

        top_p = self.top_p

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "prompt": prompt,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if top_p is not UNSET:
            field_dict["top_p"] = top_p

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_mistral_chat_completion_task_params_model import CreateMistralChatCompletionTaskParamsModel

        d = dict(src_dict)
        model = CreateMistralChatCompletionTaskParamsModel.from_dict(d.pop("model"))

        prompt = d.pop("prompt")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateMistralChatCompletionTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_mistral_chat_completion_task_params_task_type(_task_type)

        system_prompt = d.pop("system_prompt", UNSET)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        top_p = d.pop("top_p", UNSET)

        create_mistral_chat_completion_task_params = cls(
            model=model,
            prompt=prompt,
            task_type=task_type,
            system_prompt=system_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )

        create_mistral_chat_completion_task_params.additional_properties = d
        return create_mistral_chat_completion_task_params

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
