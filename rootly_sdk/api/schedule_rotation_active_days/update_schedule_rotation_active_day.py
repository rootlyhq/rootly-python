from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.schedule_rotation_active_day_response import ScheduleRotationActiveDayResponse
from ...models.update_schedule_rotation_active_day import UpdateScheduleRotationActiveDay
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateScheduleRotationActiveDay,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/schedule_rotation_active_days/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | ScheduleRotationActiveDayResponse | None:
    if response.status_code == 200:
        response_200 = ScheduleRotationActiveDayResponse.from_dict(response.json())

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
) -> Response[ErrorsList | ScheduleRotationActiveDayResponse]:
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
    body: UpdateScheduleRotationActiveDay,
) -> Response[ErrorsList | ScheduleRotationActiveDayResponse]:
    """Update a schedule rotation active day

     Update a specific schedule rotation active day by id

    Args:
        id (str):
        body (UpdateScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ScheduleRotationActiveDayResponse]]
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
    body: UpdateScheduleRotationActiveDay,
) -> ErrorsList | ScheduleRotationActiveDayResponse | None:
    """Update a schedule rotation active day

     Update a specific schedule rotation active day by id

    Args:
        id (str):
        body (UpdateScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ScheduleRotationActiveDayResponse]
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
    body: UpdateScheduleRotationActiveDay,
) -> Response[ErrorsList | ScheduleRotationActiveDayResponse]:
    """Update a schedule rotation active day

     Update a specific schedule rotation active day by id

    Args:
        id (str):
        body (UpdateScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ScheduleRotationActiveDayResponse]]
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
    body: UpdateScheduleRotationActiveDay,
) -> ErrorsList | ScheduleRotationActiveDayResponse | None:
    """Update a schedule rotation active day

     Update a specific schedule rotation active day by id

    Args:
        id (str):
        body (UpdateScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ScheduleRotationActiveDayResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
