from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.meeting_recording_list import MeetingRecordingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_id: str,
    *,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/incidents/{incident_id}/meeting_recordings".format(
            incident_id=quote(str(incident_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MeetingRecordingList | None:
    if response.status_code == 200:
        response_200 = MeetingRecordingList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MeetingRecordingList]:
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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Any | MeetingRecordingList]:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MeetingRecordingList]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Any | MeetingRecordingList | None:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MeetingRecordingList
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Any | MeetingRecordingList]:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MeetingRecordingList]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Any | MeetingRecordingList | None:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MeetingRecordingList
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
