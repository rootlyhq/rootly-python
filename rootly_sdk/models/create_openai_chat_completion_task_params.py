from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_openai_chat_completion_task_params_reasoning_effort import (
    CreateOpenaiChatCompletionTaskParamsReasoningEffort,
    check_create_openai_chat_completion_task_params_reasoning_effort,
)
from ..models.create_openai_chat_completion_task_params_reasoning_summary import (
    CreateOpenaiChatCompletionTaskParamsReasoningSummary,
    check_create_openai_chat_completion_task_params_reasoning_summary,
)
from ..models.create_openai_chat_completion_task_params_task_type import (
    CreateOpenaiChatCompletionTaskParamsTaskType,
    check_create_openai_chat_completion_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_openai_chat_completion_task_params_model import CreateOpenaiChatCompletionTaskParamsModel


T = TypeVar("T", bound="CreateOpenaiChatCompletionTaskParams")


@_attrs_define
class CreateOpenaiChatCompletionTaskParams:
    """
    Attributes:
        model (CreateOpenaiChatCompletionTaskParamsModel): The OpenAI model. eg: gpt-5-nano
        prompt (str): The prompt to send to OpenAI
        task_type (Union[Unset, CreateOpenaiChatCompletionTaskParamsTaskType]):
        system_prompt (Union[Unset, str]): The system prompt to send to OpenAI (optional)
        temperature (Union[Unset, float]): Controls randomness in the response. Higher values make output more random
        max_tokens (Union[Unset, int]): Maximum number of tokens to generate in the response
        top_p (Union[Unset, float]): Controls diversity via nucleus sampling. Lower values make output more focused
        reasoning_effort (Union[Unset, CreateOpenaiChatCompletionTaskParamsReasoningEffort]): Constrains effort on
            reasoning for GPT-5 and o-series models
        reasoning_summary (Union[Unset, CreateOpenaiChatCompletionTaskParamsReasoningSummary]): Summary of the reasoning
            performed by the model for GPT-5 and o-series models
    """

    model: "CreateOpenaiChatCompletionTaskParamsModel"
    prompt: str
    task_type: Union[Unset, CreateOpenaiChatCompletionTaskParamsTaskType] = UNSET
    system_prompt: Union[Unset, str] = UNSET
    temperature: Union[Unset, float] = UNSET
    max_tokens: Union[Unset, int] = UNSET
    top_p: Union[Unset, float] = UNSET
    reasoning_effort: Union[Unset, CreateOpenaiChatCompletionTaskParamsReasoningEffort] = UNSET
    reasoning_summary: Union[Unset, CreateOpenaiChatCompletionTaskParamsReasoningSummary] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model.to_dict()

        prompt = self.prompt

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        system_prompt = self.system_prompt

        temperature = self.temperature

        max_tokens = self.max_tokens

        top_p = self.top_p

        reasoning_effort: Union[Unset, str] = UNSET
        if not isinstance(self.reasoning_effort, Unset):
            reasoning_effort = self.reasoning_effort

        reasoning_summary: Union[Unset, str] = UNSET
        if not isinstance(self.reasoning_summary, Unset):
            reasoning_summary = self.reasoning_summary

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
        if reasoning_effort is not UNSET:
            field_dict["reasoning_effort"] = reasoning_effort
        if reasoning_summary is not UNSET:
            field_dict["reasoning_summary"] = reasoning_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_openai_chat_completion_task_params_model import CreateOpenaiChatCompletionTaskParamsModel

        d = dict(src_dict)
        model = CreateOpenaiChatCompletionTaskParamsModel.from_dict(d.pop("model"))

        prompt = d.pop("prompt")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, CreateOpenaiChatCompletionTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_openai_chat_completion_task_params_task_type(_task_type)

        system_prompt = d.pop("system_prompt", UNSET)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        top_p = d.pop("top_p", UNSET)

        _reasoning_effort = d.pop("reasoning_effort", UNSET)
        reasoning_effort: Union[Unset, CreateOpenaiChatCompletionTaskParamsReasoningEffort]
        if isinstance(_reasoning_effort, Unset):
            reasoning_effort = UNSET
        else:
            reasoning_effort = check_create_openai_chat_completion_task_params_reasoning_effort(_reasoning_effort)

        _reasoning_summary = d.pop("reasoning_summary", UNSET)
        reasoning_summary: Union[Unset, CreateOpenaiChatCompletionTaskParamsReasoningSummary]
        if isinstance(_reasoning_summary, Unset):
            reasoning_summary = UNSET
        else:
            reasoning_summary = check_create_openai_chat_completion_task_params_reasoning_summary(_reasoning_summary)

        create_openai_chat_completion_task_params = cls(
            model=model,
            prompt=prompt,
            task_type=task_type,
            system_prompt=system_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            reasoning_effort=reasoning_effort,
            reasoning_summary=reasoning_summary,
        )

        create_openai_chat_completion_task_params.additional_properties = d
        return create_openai_chat_completion_task_params

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
