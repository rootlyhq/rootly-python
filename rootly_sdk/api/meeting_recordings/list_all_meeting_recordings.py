from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.meeting_recording_list import MeetingRecordingList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    created_by: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["platform"] = platform

    params["created_by"] = created_by


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/meeting_recordings",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MeetingRecordingList | None:
    if response.status_code == 200:
        response_200 = MeetingRecordingList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MeetingRecordingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    created_by: str | Unset = UNSET,

) -> Response[MeetingRecordingList]:
    """ List all meeting recordings

     List meeting recordings across the organization. Returns the current user's standalone recordings
    plus incident-backed recordings the user can access. Supports filtering by status, platform, and
    created_by.

    Args:
        status (str | Unset):
        platform (str | Unset):
        created_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeetingRecordingList]
     """


    kwargs = _get_kwargs(
        status=status,
platform=platform,
created_by=created_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    created_by: str | Unset = UNSET,

) -> MeetingRecordingList | None:
    """ List all meeting recordings

     List meeting recordings across the organization. Returns the current user's standalone recordings
    plus incident-backed recordings the user can access. Supports filtering by status, platform, and
    created_by.

    Args:
        status (str | Unset):
        platform (str | Unset):
        created_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeetingRecordingList
     """


    return sync_detailed(
        client=client,
status=status,
platform=platform,
created_by=created_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    created_by: str | Unset = UNSET,

) -> Response[MeetingRecordingList]:
    """ List all meeting recordings

     List meeting recordings across the organization. Returns the current user's standalone recordings
    plus incident-backed recordings the user can access. Supports filtering by status, platform, and
    created_by.

    Args:
        status (str | Unset):
        platform (str | Unset):
        created_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeetingRecordingList]
     """


    kwargs = _get_kwargs(
        status=status,
platform=platform,
created_by=created_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    status: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    created_by: str | Unset = UNSET,

) -> MeetingRecordingList | None:
    """ List all meeting recordings

     List meeting recordings across the organization. Returns the current user's standalone recordings
    plus incident-backed recordings the user can access. Supports filtering by status, platform, and
    created_by.

    Args:
        status (str | Unset):
        platform (str | Unset):
        created_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeetingRecordingList
     """


    return (await asyncio_detailed(
        client=client,
status=status,
platform=platform,
created_by=created_by,

    )).parsed
