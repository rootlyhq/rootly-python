from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_event_response import AlertEventResponse
from ...models.errors_list import ErrorsList
from ...models.update_alert_event import UpdateAlertEvent
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateAlertEvent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/alert_events/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlertEventResponse, ErrorsList]]:
    if response.status_code == 200:
        response_200 = AlertEventResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AlertEventResponse, ErrorsList]]:
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
    body: UpdateAlertEvent,
) -> Response[Union[AlertEventResponse, ErrorsList]]:
    """Update alert event

     Updates a specific alert event. Only alert events with kind 'note' (user-created notes) can be
    updated. System-generated events are immutable to maintain audit trail integrity.

    Args:
        id (str):
        body (UpdateAlertEvent): Update an alert event. Note: Only alert events with kind='note'
            can be updated. You cannot change the kind field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertEventResponse, ErrorsList]]
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
    body: UpdateAlertEvent,
) -> Optional[Union[AlertEventResponse, ErrorsList]]:
    """Update alert event

     Updates a specific alert event. Only alert events with kind 'note' (user-created notes) can be
    updated. System-generated events are immutable to maintain audit trail integrity.

    Args:
        id (str):
        body (UpdateAlertEvent): Update an alert event. Note: Only alert events with kind='note'
            can be updated. You cannot change the kind field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertEventResponse, ErrorsList]
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
    body: UpdateAlertEvent,
) -> Response[Union[AlertEventResponse, ErrorsList]]:
    """Update alert event

     Updates a specific alert event. Only alert events with kind 'note' (user-created notes) can be
    updated. System-generated events are immutable to maintain audit trail integrity.

    Args:
        id (str):
        body (UpdateAlertEvent): Update an alert event. Note: Only alert events with kind='note'
            can be updated. You cannot change the kind field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertEventResponse, ErrorsList]]
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
    body: UpdateAlertEvent,
) -> Optional[Union[AlertEventResponse, ErrorsList]]:
    """Update alert event

     Updates a specific alert event. Only alert events with kind 'note' (user-created notes) can be
    updated. System-generated events are immutable to maintain audit trail integrity.

    Args:
        id (str):
        body (UpdateAlertEvent): Update an alert event. Note: Only alert events with kind='note'
            can be updated. You cannot change the kind field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertEventResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
