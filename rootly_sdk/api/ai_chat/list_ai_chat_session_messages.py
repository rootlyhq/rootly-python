from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_chat_session_message_list import AiChatSessionMessageList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: UUID,
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
        "url": "/v1/ai/chat/sessions/{session_id}/messages".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AiChatSessionMessageList | Any | None:
    if response.status_code == 200:
        response_200 = AiChatSessionMessageList.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AiChatSessionMessageList | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> Response[AiChatSessionMessageList | Any]:
    """ List AI chat session messages

     Returns the user and assistant message history for a session, paginated and chronologically ordered.
    Internal tool messages are filtered out. Requires `ai.chat:read` OAuth scope or an API key.

    Args:
        session_id (UUID):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiChatSessionMessageList | Any]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
pagenumber=pagenumber,
pagesize=pagesize,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: UUID,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> AiChatSessionMessageList | Any | None:
    """ List AI chat session messages

     Returns the user and assistant message history for a session, paginated and chronologically ordered.
    Internal tool messages are filtered out. Requires `ai.chat:read` OAuth scope or an API key.

    Args:
        session_id (UUID):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiChatSessionMessageList | Any
     """


    return sync_detailed(
        session_id=session_id,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,

    ).parsed

async def asyncio_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> Response[AiChatSessionMessageList | Any]:
    """ List AI chat session messages

     Returns the user and assistant message history for a session, paginated and chronologically ordered.
    Internal tool messages are filtered out. Requires `ai.chat:read` OAuth scope or an API key.

    Args:
        session_id (UUID):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiChatSessionMessageList | Any]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
pagenumber=pagenumber,
pagesize=pagesize,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: UUID,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> AiChatSessionMessageList | Any | None:
    """ List AI chat session messages

     Returns the user and assistant message history for a session, paginated and chronologically ordered.
    Internal tool messages are filtered out. Requires `ai.chat:read` OAuth scope or an API key.

    Args:
        session_id (UUID):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiChatSessionMessageList | Any
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
pagenumber=pagenumber,
pagesize=pagesize,

    )).parsed
