from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.meeting_recording_list import MeetingRecordingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_id: str,
    *,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/incidents/{incident_id}/meeting_recordings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MeetingRecordingList]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, MeetingRecordingList]]:
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
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[Union[Any, MeetingRecordingList]]:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MeetingRecordingList]]
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
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, MeetingRecordingList]]:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MeetingRecordingList]
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
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[Union[Any, MeetingRecordingList]]:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MeetingRecordingList]]
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
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, MeetingRecordingList]]:
    """List meeting recordings

     List all meeting recording sessions for an incident. Returns recordings sorted by session number.
    Each recording represents one bot session with its own transcript, status, and metadata.

    Args:
        incident_id (str):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MeetingRecordingList]
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
