from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_workflow_action_item_form_field_condition import NewWorkflowActionItemFormFieldCondition
from ...models.workflow_action_item_form_field_condition_response import WorkflowActionItemFormFieldConditionResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: NewWorkflowActionItemFormFieldCondition,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/workflows/{workflow_id}/action_item_form_field_conditions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]:
    if response.status_code == 201:
        response_201 = WorkflowActionItemFormFieldConditionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowActionItemFormFieldCondition,
) -> Response[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]:
    """Creates a workflow action item form field condition

     Creates a new workflow action item form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowActionItemFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowActionItemFormFieldCondition,
) -> Optional[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]:
    """Creates a workflow action item form field condition

     Creates a new workflow action item form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowActionItemFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowActionItemFormFieldCondition,
) -> Response[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]:
    """Creates a workflow action item form field condition

     Creates a new workflow action item form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowActionItemFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowActionItemFormFieldCondition,
) -> Optional[Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]]:
    """Creates a workflow action item form field condition

     Creates a new workflow action item form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowActionItemFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorsList, WorkflowActionItemFormFieldConditionResponse]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
