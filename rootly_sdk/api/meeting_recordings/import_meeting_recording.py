from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.import_meeting_recording import ImportMeetingRecording
from ...models.meeting_recording_response import MeetingRecordingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_id: str,
    *,
    body: ImportMeetingRecording | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/incidents/{incident_id}/meeting_recordings/import".format(
            incident_id=quote(str(incident_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MeetingRecordingResponse | None:
    if response.status_code == 201:
        response_201 = MeetingRecordingResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MeetingRecordingResponse]:
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
    body: ImportMeetingRecording | Unset = UNSET,
) -> Response[Any | MeetingRecordingResponse]:
    """Import a meeting recording

     Import an externally captured meeting recording and attach it to an incident. Video and transcript
    are fetched asynchronously. The existing POST /v1/incidents/{incident_id}/meeting_recordings
    endpoint invites a bot — this endpoint handles recordings that were captured outside of the bot
    flow.

    Args:
        incident_id (str):
        body (ImportMeetingRecording | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MeetingRecordingResponse]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: ImportMeetingRecording | Unset = UNSET,
) -> Any | MeetingRecordingResponse | None:
    """Import a meeting recording

     Import an externally captured meeting recording and attach it to an incident. Video and transcript
    are fetched asynchronously. The existing POST /v1/incidents/{incident_id}/meeting_recordings
    endpoint invites a bot — this endpoint handles recordings that were captured outside of the bot
    flow.

    Args:
        incident_id (str):
        body (ImportMeetingRecording | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MeetingRecordingResponse
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: ImportMeetingRecording | Unset = UNSET,
) -> Response[Any | MeetingRecordingResponse]:
    """Import a meeting recording

     Import an externally captured meeting recording and attach it to an incident. Video and transcript
    are fetched asynchronously. The existing POST /v1/incidents/{incident_id}/meeting_recordings
    endpoint invites a bot — this endpoint handles recordings that were captured outside of the bot
    flow.

    Args:
        incident_id (str):
        body (ImportMeetingRecording | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MeetingRecordingResponse]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: ImportMeetingRecording | Unset = UNSET,
) -> Any | MeetingRecordingResponse | None:
    """Import a meeting recording

     Import an externally captured meeting recording and attach it to an incident. Video and transcript
    are fetched asynchronously. The existing POST /v1/incidents/{incident_id}/meeting_recordings
    endpoint invites a bot — this endpoint handles recordings that were captured outside of the bot
    flow.

    Args:
        incident_id (str):
        body (ImportMeetingRecording | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MeetingRecordingResponse
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            body=body,
        )
    ).parsed
