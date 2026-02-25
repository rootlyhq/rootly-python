from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_role_task_response import IncidentRoleTaskResponse
from ...models.new_incident_role_task import NewIncidentRoleTask
from ...types import Response


def _get_kwargs(
    incident_role_id: str,
    *,
    body: NewIncidentRoleTask,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/incident_roles/{incident_role_id}/incident_role_tasks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | IncidentRoleTaskResponse | None:
    if response.status_code == 201:
        response_201 = IncidentRoleTaskResponse.from_dict(response.json())

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
) -> Response[ErrorsList | IncidentRoleTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_role_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentRoleTask,
) -> Response[ErrorsList | IncidentRoleTaskResponse]:
    """Creates an incident role task

     Creates a new task from provided data

    Args:
        incident_role_id (str):
        body (NewIncidentRoleTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentRoleTaskResponse]]
    """

    kwargs = _get_kwargs(
        incident_role_id=incident_role_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_role_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentRoleTask,
) -> ErrorsList | IncidentRoleTaskResponse | None:
    """Creates an incident role task

     Creates a new task from provided data

    Args:
        incident_role_id (str):
        body (NewIncidentRoleTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentRoleTaskResponse]
    """

    return sync_detailed(
        incident_role_id=incident_role_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    incident_role_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentRoleTask,
) -> Response[ErrorsList | IncidentRoleTaskResponse]:
    """Creates an incident role task

     Creates a new task from provided data

    Args:
        incident_role_id (str):
        body (NewIncidentRoleTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentRoleTaskResponse]]
    """

    kwargs = _get_kwargs(
        incident_role_id=incident_role_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_role_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentRoleTask,
) -> ErrorsList | IncidentRoleTaskResponse | None:
    """Creates an incident role task

     Creates a new task from provided data

    Args:
        incident_role_id (str):
        body (NewIncidentRoleTask):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentRoleTaskResponse]
    """

    return (
        await asyncio_detailed(
            incident_role_id=incident_role_id,
            client=client,
            body=body,
        )
    ).parsed
