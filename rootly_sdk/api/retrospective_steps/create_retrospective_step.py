from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_retrospective_step import NewRetrospectiveStep
from ...models.retrospective_step_response import RetrospectiveStepResponse
from ...types import Response


def _get_kwargs(
    retrospective_process_id: str,
    *,
    body: NewRetrospectiveStep,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/retrospective_processes/{retrospective_process_id}/retrospective_steps",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, RetrospectiveStepResponse]]:
    if response.status_code == 201:
        response_201 = RetrospectiveStepResponse.from_dict(response.json())

        return response_201
    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422
    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, RetrospectiveStepResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveStep,
) -> Response[Union[ErrorsList, RetrospectiveStepResponse]]:
    """Creates a retrospective step

     Creates a new retrospective step from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, RetrospectiveStepResponse]]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveStep,
) -> Optional[Union[ErrorsList, RetrospectiveStepResponse]]:
    """Creates a retrospective step

     Creates a new retrospective step from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, RetrospectiveStepResponse]
    """

    return sync_detailed(
        retrospective_process_id=retrospective_process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveStep,
) -> Response[Union[ErrorsList, RetrospectiveStepResponse]]:
    """Creates a retrospective step

     Creates a new retrospective step from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, RetrospectiveStepResponse]]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    body: NewRetrospectiveStep,
) -> Optional[Union[ErrorsList, RetrospectiveStepResponse]]:
    """Creates a retrospective step

     Creates a new retrospective step from provided data

    Args:
        retrospective_process_id (str):
        body (NewRetrospectiveStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, RetrospectiveStepResponse]
    """

    return (
        await asyncio_detailed(
            retrospective_process_id=retrospective_process_id,
            client=client,
            body=body,
        )
    ).parsed
