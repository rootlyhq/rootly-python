from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_shift_coverage_request import NewShiftCoverageRequest
from ...models.shift_coverage_request_list import ShiftCoverageRequestList
from ...types import Response


def _get_kwargs(
    schedule_id: str,
    *,
    body: NewShiftCoverageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/schedules/{schedule_id}/shift_coverage_requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | ShiftCoverageRequestList | None:
    if response.status_code == 201:
        response_201 = ShiftCoverageRequestList.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | ShiftCoverageRequestList]:
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
    body: NewShiftCoverageRequest,
) -> Response[ErrorsList | ShiftCoverageRequestList]:
    """creates shift coverage requests

     Creates coverage requests for the shifts overlapping the requested time range. A range can span
    multiple consecutive shifts (e.g. across a handoff), so one or more coverage requests may be
    created; the response is always a list. A coverage request broadcasts to schedule members so someone
    can volunteer to cover the shift.

    Args:
        schedule_id (str):
        body (NewShiftCoverageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ShiftCoverageRequestList]]
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
    body: NewShiftCoverageRequest,
) -> ErrorsList | ShiftCoverageRequestList | None:
    """creates shift coverage requests

     Creates coverage requests for the shifts overlapping the requested time range. A range can span
    multiple consecutive shifts (e.g. across a handoff), so one or more coverage requests may be
    created; the response is always a list. A coverage request broadcasts to schedule members so someone
    can volunteer to cover the shift.

    Args:
        schedule_id (str):
        body (NewShiftCoverageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ShiftCoverageRequestList]
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
    body: NewShiftCoverageRequest,
) -> Response[ErrorsList | ShiftCoverageRequestList]:
    """creates shift coverage requests

     Creates coverage requests for the shifts overlapping the requested time range. A range can span
    multiple consecutive shifts (e.g. across a handoff), so one or more coverage requests may be
    created; the response is always a list. A coverage request broadcasts to schedule members so someone
    can volunteer to cover the shift.

    Args:
        schedule_id (str):
        body (NewShiftCoverageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, ShiftCoverageRequestList]]
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
    body: NewShiftCoverageRequest,
) -> ErrorsList | ShiftCoverageRequestList | None:
    """creates shift coverage requests

     Creates coverage requests for the shifts overlapping the requested time range. A range can span
    multiple consecutive shifts (e.g. across a handoff), so one or more coverage requests may be
    created; the response is always a list. A coverage request broadcasts to schedule members so someone
    can volunteer to cover the shift.

    Args:
        schedule_id (str):
        body (NewShiftCoverageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, ShiftCoverageRequestList]
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            body=body,
        )
    ).parsed
