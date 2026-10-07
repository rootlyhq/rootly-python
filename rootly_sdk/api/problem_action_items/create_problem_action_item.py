from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_problem_action_item import NewProblemActionItem
from ...models.problem_action_item_response import ProblemActionItemResponse
from ...types import Response


def _get_kwargs(
    problem_id: str,
    *,
    body: NewProblemActionItem,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/problems/{problem_id}/action_items".format(
            problem_id=quote(str(problem_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | ProblemActionItemResponse | None:
    if response.status_code == 201:
        response_201 = ProblemActionItemResponse.from_dict(response.json())

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
) -> Response[ErrorsList | ProblemActionItemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    problem_id: str,
    *,
    client: AuthenticatedClient,
    body: NewProblemActionItem,
) -> Response[ErrorsList | ProblemActionItemResponse]:
    """Creates a problem action item

     Creates a new action item on a problem from provided data

    Args:
        problem_id (str):
        body (NewProblemActionItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | ProblemActionItemResponse]
    """

    kwargs = _get_kwargs(
        problem_id=problem_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    problem_id: str,
    *,
    client: AuthenticatedClient,
    body: NewProblemActionItem,
) -> ErrorsList | ProblemActionItemResponse | None:
    """Creates a problem action item

     Creates a new action item on a problem from provided data

    Args:
        problem_id (str):
        body (NewProblemActionItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | ProblemActionItemResponse
    """

    return sync_detailed(
        problem_id=problem_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    problem_id: str,
    *,
    client: AuthenticatedClient,
    body: NewProblemActionItem,
) -> Response[ErrorsList | ProblemActionItemResponse]:
    """Creates a problem action item

     Creates a new action item on a problem from provided data

    Args:
        problem_id (str):
        body (NewProblemActionItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | ProblemActionItemResponse]
    """

    kwargs = _get_kwargs(
        problem_id=problem_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    problem_id: str,
    *,
    client: AuthenticatedClient,
    body: NewProblemActionItem,
) -> ErrorsList | ProblemActionItemResponse | None:
    """Creates a problem action item

     Creates a new action item on a problem from provided data

    Args:
        problem_id (str):
        body (NewProblemActionItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | ProblemActionItemResponse
    """

    return (
        await asyncio_detailed(
            problem_id=problem_id,
            client=client,
            body=body,
        )
    ).parsed
