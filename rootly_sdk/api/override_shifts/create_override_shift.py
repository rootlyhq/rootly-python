from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_override_shift import NewOverrideShift
from ...models.override_shift_response import OverrideShiftResponse
from ...types import Response


def _get_kwargs(
    schedule_id: str,
    *,
    body: NewOverrideShift,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/schedules/{schedule_id}/override_shifts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | OverrideShiftResponse | None:
    if response.status_code == 201:
        response_201 = OverrideShiftResponse.from_dict(response.json())

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
) -> Response[ErrorsList | OverrideShiftResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    body: NewOverrideShift,
) -> Response[ErrorsList | OverrideShiftResponse]:
    """creates an override shift

     Creates a new override shift from provided data. If any existing override shifts overlap with the
    specified time range, they will be automatically deleted and replaced by the new override.

    Args:
        schedule_id (str):
        body (NewOverrideShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, OverrideShiftResponse]]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    body: NewOverrideShift,
) -> ErrorsList | OverrideShiftResponse | None:
    """creates an override shift

     Creates a new override shift from provided data. If any existing override shifts overlap with the
    specified time range, they will be automatically deleted and replaced by the new override.

    Args:
        schedule_id (str):
        body (NewOverrideShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, OverrideShiftResponse]
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    body: NewOverrideShift,
) -> Response[ErrorsList | OverrideShiftResponse]:
    """creates an override shift

     Creates a new override shift from provided data. If any existing override shifts overlap with the
    specified time range, they will be automatically deleted and replaced by the new override.

    Args:
        schedule_id (str):
        body (NewOverrideShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, OverrideShiftResponse]]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
    body: NewOverrideShift,
) -> ErrorsList | OverrideShiftResponse | None:
    """creates an override shift

     Creates a new override shift from provided data. If any existing override shifts overlap with the
    specified time range, they will be automatically deleted and replaced by the new override.

    Args:
        schedule_id (str):
        body (NewOverrideShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, OverrideShiftResponse]
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            body=body,
        )
    ).parsed
