from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_workflow_task import NewWorkflowTask
from ...models.workflow_task_response import WorkflowTaskResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: NewWorkflowTask,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/workflows/{workflow_id}/workflow_tasks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, WorkflowTaskResponse]]:
    if response.status_code == 201:
        response_201 = WorkflowTaskResponse.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, WorkflowTaskResponse]]:
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
    body: NewWorkflowTask,
) -> Response[Union[ErrorsList, WorkflowTaskResponse]]:
    """Creates a workflow task

     Creates a new workflow task from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowTaskResponse]]
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
    body: NewWorkflowTask,
) -> Optional[Union[ErrorsList, WorkflowTaskResponse]]:
    """Creates a workflow task

     Creates a new workflow task from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowTaskResponse]
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
    body: NewWorkflowTask,
) -> Response[Union[ErrorsList, WorkflowTaskResponse]]:
    """Creates a workflow task

     Creates a new workflow task from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowTaskResponse]]
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
    body: NewWorkflowTask,
) -> Optional[Union[ErrorsList, WorkflowTaskResponse]]:
    """Creates a workflow task

     Creates a new workflow task from provided data

    Args:
        workflow_id (str):
        body (NewWorkflowTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowTaskResponse]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
