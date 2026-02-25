from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_workflow_form_field_condition import NewWorkflowFormFieldCondition
from ...models.workflow_form_field_condition_response import WorkflowFormFieldConditionResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: NewWorkflowFormFieldCondition,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/workflows/{workflow_id}/form_field_conditions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | WorkflowFormFieldConditionResponse | None:
    if response.status_code == 201:
        response_201 = WorkflowFormFieldConditionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | WorkflowFormFieldConditionResponse]:
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
    body: NewWorkflowFormFieldCondition,
) -> Response[ErrorsList | WorkflowFormFieldConditionResponse]:
    """Creates a workflow form field condition

     Creates a new workflow form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowFormFieldConditionResponse]]
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
    body: NewWorkflowFormFieldCondition,
) -> ErrorsList | WorkflowFormFieldConditionResponse | None:
    """Creates a workflow form field condition

     Creates a new workflow form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowFormFieldConditionResponse]
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
    body: NewWorkflowFormFieldCondition,
) -> Response[ErrorsList | WorkflowFormFieldConditionResponse]:
    """Creates a workflow form field condition

     Creates a new workflow form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowFormFieldConditionResponse]]
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
    body: NewWorkflowFormFieldCondition,
) -> ErrorsList | WorkflowFormFieldConditionResponse | None:
    """Creates a workflow form field condition

     Creates a new workflow form field condition from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowFormFieldConditionResponse]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
