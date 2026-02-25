from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.update_workflow_form_field_condition import UpdateWorkflowFormFieldCondition
from ...models.workflow_form_field_condition_response import WorkflowFormFieldConditionResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateWorkflowFormFieldCondition,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/workflow_form_field_conditions/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | WorkflowFormFieldConditionResponse | None:
    if response.status_code == 200:
        response_200 = WorkflowFormFieldConditionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

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
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkflowFormFieldCondition,
) -> Response[ErrorsList | WorkflowFormFieldConditionResponse]:
    """Update a workflow form field condition

     Update a specific workflow form field condition by id

    Args:
        id (str):
        body (UpdateWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowFormFieldConditionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkflowFormFieldCondition,
) -> ErrorsList | WorkflowFormFieldConditionResponse | None:
    """Update a workflow form field condition

     Update a specific workflow form field condition by id

    Args:
        id (str):
        body (UpdateWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowFormFieldConditionResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkflowFormFieldCondition,
) -> Response[ErrorsList | WorkflowFormFieldConditionResponse]:
    """Update a workflow form field condition

     Update a specific workflow form field condition by id

    Args:
        id (str):
        body (UpdateWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowFormFieldConditionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkflowFormFieldCondition,
) -> ErrorsList | WorkflowFormFieldConditionResponse | None:
    """Update a workflow form field condition

     Update a specific workflow form field condition by id

    Args:
        id (str):
        body (UpdateWorkflowFormFieldCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowFormFieldConditionResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
