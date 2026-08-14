from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_event_service_response import IncidentEventServiceResponse
from ...models.new_incident_event_service import NewIncidentEventService
from ...types import Response


def _get_kwargs(
    incident_event_id: str,
    *,
    body: NewIncidentEventService,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/events/{incident_event_id}/services",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | IncidentEventServiceResponse | None:
    if response.status_code == 201:
        response_201 = IncidentEventServiceResponse.from_dict(response.json())

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
) -> Response[ErrorsList | IncidentEventServiceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_event_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentEventService,
) -> Response[ErrorsList | IncidentEventServiceResponse]:
    """Creates an incident event service

     Creates a new event service from provided data

    Args:
        incident_event_id (str):
        body (NewIncidentEventService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentEventServiceResponse]]
    """

    kwargs = _get_kwargs(
        incident_event_id=incident_event_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_event_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentEventService,
) -> ErrorsList | IncidentEventServiceResponse | None:
    """Creates an incident event service

     Creates a new event service from provided data

    Args:
        incident_event_id (str):
        body (NewIncidentEventService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentEventServiceResponse]
    """

    return sync_detailed(
        incident_event_id=incident_event_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    incident_event_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentEventService,
) -> Response[ErrorsList | IncidentEventServiceResponse]:
    """Creates an incident event service

     Creates a new event service from provided data

    Args:
        incident_event_id (str):
        body (NewIncidentEventService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentEventServiceResponse]]
    """

    kwargs = _get_kwargs(
        incident_event_id=incident_event_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_event_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentEventService,
) -> ErrorsList | IncidentEventServiceResponse | None:
    """Creates an incident event service

     Creates a new event service from provided data

    Args:
        incident_event_id (str):
        body (NewIncidentEventService):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentEventServiceResponse]
    """

    return (
        await asyncio_detailed(
            incident_event_id=incident_event_id,
            client=client,
            body=body,
        )
    ).parsed
