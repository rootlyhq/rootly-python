from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_permission_set_resource_response import IncidentPermissionSetResourceResponse
from ...models.update_incident_permission_set_resource import UpdateIncidentPermissionSetResource
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateIncidentPermissionSetResource,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/incident_permission_set_resources/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, IncidentPermissionSetResourceResponse]]:
    if response.status_code == 200:
        response_200 = IncidentPermissionSetResourceResponse.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, IncidentPermissionSetResourceResponse]]:
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
    body: UpdateIncidentPermissionSetResource,
) -> Response[Union[ErrorsList, IncidentPermissionSetResourceResponse]]:
    """Update an incident_permission_set_resource

     Update a specific incident_permission_set_resource by id

    Args:
        id (str):
        body (UpdateIncidentPermissionSetResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentPermissionSetResourceResponse]]
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
    body: UpdateIncidentPermissionSetResource,
) -> Optional[Union[ErrorsList, IncidentPermissionSetResourceResponse]]:
    """Update an incident_permission_set_resource

     Update a specific incident_permission_set_resource by id

    Args:
        id (str):
        body (UpdateIncidentPermissionSetResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentPermissionSetResourceResponse]
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
    body: UpdateIncidentPermissionSetResource,
) -> Response[Union[ErrorsList, IncidentPermissionSetResourceResponse]]:
    """Update an incident_permission_set_resource

     Update a specific incident_permission_set_resource by id

    Args:
        id (str):
        body (UpdateIncidentPermissionSetResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentPermissionSetResourceResponse]]
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
    body: UpdateIncidentPermissionSetResource,
) -> Optional[Union[ErrorsList, IncidentPermissionSetResourceResponse]]:
    """Update an incident_permission_set_resource

     Update a specific incident_permission_set_resource by id

    Args:
        id (str):
        body (UpdateIncidentPermissionSetResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentPermissionSetResourceResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
