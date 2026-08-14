from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.shift_coverage_request_list import ShiftCoverageRequestList
from ...types import Response


def _get_kwargs(
    schedule_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/schedules/{schedule_id}/shift_coverage_requests",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ShiftCoverageRequestList]:
    if response.status_code == 200:
        response_200 = ShiftCoverageRequestList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ShiftCoverageRequestList]:
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
) -> Response[ShiftCoverageRequestList]:
    """list shift coverage requests

     List active shift coverage requests for a schedule.

    Args:
        schedule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShiftCoverageRequestList]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ShiftCoverageRequestList]:
    """list shift coverage requests

     List active shift coverage requests for a schedule.

    Args:
        schedule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShiftCoverageRequestList
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ShiftCoverageRequestList]:
    """list shift coverage requests

     List active shift coverage requests for a schedule.

    Args:
        schedule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShiftCoverageRequestList]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ShiftCoverageRequestList]:
    """list shift coverage requests

     List active shift coverage requests for a schedule.

    Args:
        schedule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShiftCoverageRequestList
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
        )
    ).parsed
