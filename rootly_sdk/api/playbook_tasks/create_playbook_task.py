from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_playbook_task import NewPlaybookTask
from ...models.playbook_task_response import PlaybookTaskResponse
from ...types import Response


def _get_kwargs(
    playbook_id: str,
    *,
    body: NewPlaybookTask,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/playbooks/{playbook_id}/playbook_tasks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | PlaybookTaskResponse | None:
    if response.status_code == 201:
        response_201 = PlaybookTaskResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | PlaybookTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playbook_id: str,
    *,
    client: AuthenticatedClient,
    body: NewPlaybookTask,
) -> Response[ErrorsList | PlaybookTaskResponse]:
    """Creates a playbook task

     Creates a new task from provided data

    Args:
        playbook_id (str):
        body (NewPlaybookTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, PlaybookTaskResponse]]
    """

    kwargs = _get_kwargs(
        playbook_id=playbook_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playbook_id: str,
    *,
    client: AuthenticatedClient,
    body: NewPlaybookTask,
) -> ErrorsList | PlaybookTaskResponse | None:
    """Creates a playbook task

     Creates a new task from provided data

    Args:
        playbook_id (str):
        body (NewPlaybookTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, PlaybookTaskResponse]
    """

    return sync_detailed(
        playbook_id=playbook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    playbook_id: str,
    *,
    client: AuthenticatedClient,
    body: NewPlaybookTask,
) -> Response[ErrorsList | PlaybookTaskResponse]:
    """Creates a playbook task

     Creates a new task from provided data

    Args:
        playbook_id (str):
        body (NewPlaybookTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, PlaybookTaskResponse]]
    """

    kwargs = _get_kwargs(
        playbook_id=playbook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playbook_id: str,
    *,
    client: AuthenticatedClient,
    body: NewPlaybookTask,
) -> ErrorsList | PlaybookTaskResponse | None:
    """Creates a playbook task

     Creates a new task from provided data

    Args:
        playbook_id (str):
        body (NewPlaybookTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, PlaybookTaskResponse]
    """

    return (
        await asyncio_detailed(
            playbook_id=playbook_id,
            client=client,
            body=body,
        )
    ).parsed
