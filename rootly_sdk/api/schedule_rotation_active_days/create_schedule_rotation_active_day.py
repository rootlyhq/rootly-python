from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_schedule_rotation_active_day import NewScheduleRotationActiveDay
from ...models.schedule_rotation_active_day_response import ScheduleRotationActiveDayResponse
from ...types import Response


def _get_kwargs(
    schedule_rotation_id: str,
    *,
    body: NewScheduleRotationActiveDay,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/schedule_rotations/{schedule_rotation_id}/schedule_rotation_active_days",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | ScheduleRotationActiveDayResponse | None:
    if response.status_code == 201:
        response_201 = ScheduleRotationActiveDayResponse.from_dict(response.json())

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
) -> Response[ErrorsList | ScheduleRotationActiveDayResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_rotation_id: str,
    *,
    client: AuthenticatedClient,
    body: NewScheduleRotationActiveDay,
) -> Response[ErrorsList | ScheduleRotationActiveDayResponse]:
    """Creates a schedule rotation active day

     Creates a new schedule rotation active day from provided data

    Args:
        schedule_rotation_id (str):
        body (NewScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ScheduleRotationActiveDayResponse]]
    """

    kwargs = _get_kwargs(
        schedule_rotation_id=schedule_rotation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_rotation_id: str,
    *,
    client: AuthenticatedClient,
    body: NewScheduleRotationActiveDay,
) -> ErrorsList | ScheduleRotationActiveDayResponse | None:
    """Creates a schedule rotation active day

     Creates a new schedule rotation active day from provided data

    Args:
        schedule_rotation_id (str):
        body (NewScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ScheduleRotationActiveDayResponse]
    """

    return sync_detailed(
        schedule_rotation_id=schedule_rotation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    schedule_rotation_id: str,
    *,
    client: AuthenticatedClient,
    body: NewScheduleRotationActiveDay,
) -> Response[ErrorsList | ScheduleRotationActiveDayResponse]:
    """Creates a schedule rotation active day

     Creates a new schedule rotation active day from provided data

    Args:
        schedule_rotation_id (str):
        body (NewScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ScheduleRotationActiveDayResponse]]
    """

    kwargs = _get_kwargs(
        schedule_rotation_id=schedule_rotation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_rotation_id: str,
    *,
    client: AuthenticatedClient,
    body: NewScheduleRotationActiveDay,
) -> ErrorsList | ScheduleRotationActiveDayResponse | None:
    """Creates a schedule rotation active day

     Creates a new schedule rotation active day from provided data

    Args:
        schedule_rotation_id (str):
        body (NewScheduleRotationActiveDay):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ScheduleRotationActiveDayResponse]
    """

    return (
        await asyncio_detailed(
            schedule_rotation_id=schedule_rotation_id,
            client=client,
            body=body,
        )
    ).parsed
