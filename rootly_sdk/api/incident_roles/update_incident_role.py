from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_role_response import IncidentRoleResponse
from ...models.update_incident_role import UpdateIncidentRole
from ...types import Response


def _get_kwargs(
    id: UUID | str,
    *,
    body: UpdateIncidentRole,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/incident_roles/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | IncidentRoleResponse | None:
    if response.status_code == 200:
        response_200 = IncidentRoleResponse.from_dict(response.json())

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
) -> Response[ErrorsList | IncidentRoleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    body: UpdateIncidentRole,
) -> Response[ErrorsList | IncidentRoleResponse]:
    """Update an incident role

     Update a specific incident_role by id

    Args:
        id (Union[UUID, str]):
        body (UpdateIncidentRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentRoleResponse]]
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
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    body: UpdateIncidentRole,
) -> ErrorsList | IncidentRoleResponse | None:
    """Update an incident role

     Update a specific incident_role by id

    Args:
        id (Union[UUID, str]):
        body (UpdateIncidentRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentRoleResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    body: UpdateIncidentRole,
) -> Response[ErrorsList | IncidentRoleResponse]:
    """Update an incident role

     Update a specific incident_role by id

    Args:
        id (Union[UUID, str]):
        body (UpdateIncidentRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentRoleResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    body: UpdateIncidentRole,
) -> ErrorsList | IncidentRoleResponse | None:
    """Update an incident role

     Update a specific incident_role by id

    Args:
        id (Union[UUID, str]):
        body (UpdateIncidentRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentRoleResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
