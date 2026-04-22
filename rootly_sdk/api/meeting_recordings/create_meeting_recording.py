from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_meeting_recording_platform import (
    CreateMeetingRecordingPlatform,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_id: str,
    *,
    platform: CreateMeetingRecordingPlatform | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform

    params["platform"] = json_platform

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/incidents/{incident_id}/meeting_recordings".format(
            incident_id=quote(str(incident_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 201:
        return None

    if response.status_code == 422:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    platform: CreateMeetingRecordingPlatform | Unset = UNSET,
) -> Response[Any]:
    """Create meeting recording

     Invite a recording bot to the incident's meeting. If no previous recordings exist for the platform,
    a new bot is invited (session 1). If previous sessions exist, a new session is created (re-invite).
    The bot joins the meeting, records audio/video, and generates a transcript when the session ends.

    Args:
        incident_id (str):
        platform (CreateMeetingRecordingPlatform | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        platform=platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    platform: CreateMeetingRecordingPlatform | Unset = UNSET,
) -> Response[Any]:
    """Create meeting recording

     Invite a recording bot to the incident's meeting. If no previous recordings exist for the platform,
    a new bot is invited (session 1). If previous sessions exist, a new session is created (re-invite).
    The bot joins the meeting, records audio/video, and generates a transcript when the session ends.

    Args:
        incident_id (str):
        platform (CreateMeetingRecordingPlatform | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        platform=platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
