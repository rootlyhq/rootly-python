from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_sub_status_response import IncidentSubStatusResponse
from ...models.new_incident_sub_status import NewIncidentSubStatus
from ...types import Response


def _get_kwargs(
    incident_id: str,
    *,
    body: NewIncidentSubStatus,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/incidents/{incident_id}/sub_statuses",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | IncidentSubStatusResponse | None:
    if response.status_code == 201:
        response_201 = IncidentSubStatusResponse.from_dict(response.json())

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
) -> Response[ErrorsList | IncidentSubStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentSubStatus,
) -> Response[ErrorsList | IncidentSubStatusResponse]:
    """Creates a sub-status assignment

     Creates a new sub-status assignment from provided data

    Args:
        incident_id (str):
        body (NewIncidentSubStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentSubStatusResponse]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentSubStatus,
) -> ErrorsList | IncidentSubStatusResponse | None:
    """Creates a sub-status assignment

     Creates a new sub-status assignment from provided data

    Args:
        incident_id (str):
        body (NewIncidentSubStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentSubStatusResponse]
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentSubStatus,
) -> Response[ErrorsList | IncidentSubStatusResponse]:
    """Creates a sub-status assignment

     Creates a new sub-status assignment from provided data

    Args:
        incident_id (str):
        body (NewIncidentSubStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentSubStatusResponse]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentSubStatus,
) -> ErrorsList | IncidentSubStatusResponse | None:
    """Creates a sub-status assignment

     Creates a new sub-status assignment from provided data

    Args:
        incident_id (str):
        body (NewIncidentSubStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentSubStatusResponse]
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            body=body,
        )
    ).parsed
