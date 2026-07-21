from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_meeting_recording_include import check_get_meeting_recording_include
from ...models.get_meeting_recording_include import GetMeetingRecordingInclude
from ...models.meeting_recording_response import MeetingRecordingResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    include: GetMeetingRecordingInclude | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/meeting_recordings/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | MeetingRecordingResponse | None:
    if response.status_code == 200:
        response_200 = MeetingRecordingResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | MeetingRecordingResponse]:
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
    include: GetMeetingRecordingInclude | Unset = UNSET,

) -> Response[Any | MeetingRecordingResponse]:
    """ Get a meeting recording

     Retrieve a single meeting recording session including its status, duration, speaker count, word
    count, and transcript summary.

    Args:
        id (str):
        include (GetMeetingRecordingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MeetingRecordingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
include=include,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    include: GetMeetingRecordingInclude | Unset = UNSET,

) -> Any | MeetingRecordingResponse | None:
    """ Get a meeting recording

     Retrieve a single meeting recording session including its status, duration, speaker count, word
    count, and transcript summary.

    Args:
        id (str):
        include (GetMeetingRecordingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MeetingRecordingResponse
     """


    return sync_detailed(
        id=id,
client=client,
include=include,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: GetMeetingRecordingInclude | Unset = UNSET,

) -> Response[Any | MeetingRecordingResponse]:
    """ Get a meeting recording

     Retrieve a single meeting recording session including its status, duration, speaker count, word
    count, and transcript summary.

    Args:
        id (str):
        include (GetMeetingRecordingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MeetingRecordingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
include=include,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include: GetMeetingRecordingInclude | Unset = UNSET,

) -> Any | MeetingRecordingResponse | None:
    """ Get a meeting recording

     Retrieve a single meeting recording session including its status, duration, speaker count, word
    count, and transcript summary.

    Args:
        id (str):
        include (GetMeetingRecordingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MeetingRecordingResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
include=include,

    )).parsed
