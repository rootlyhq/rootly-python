from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.form_set_condition_response import FormSetConditionResponse
from ...models.new_form_set_condition import NewFormSetCondition
from ...types import Response


def _get_kwargs(
    form_set_id: str,
    *,
    body: NewFormSetCondition,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/form_sets/{form_set_id}/conditions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | FormSetConditionResponse | None:
    if response.status_code == 201:
        response_201 = FormSetConditionResponse.from_dict(response.json())

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
) -> Response[ErrorsList | FormSetConditionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    form_set_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormSetCondition,
) -> Response[ErrorsList | FormSetConditionResponse]:
    """Creates a Form Set Condition

     Creates a new form_set_condition from provided data

    Args:
        form_set_id (str):
        body (NewFormSetCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, FormSetConditionResponse]]
    """

    kwargs = _get_kwargs(
        form_set_id=form_set_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    form_set_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormSetCondition,
) -> ErrorsList | FormSetConditionResponse | None:
    """Creates a Form Set Condition

     Creates a new form_set_condition from provided data

    Args:
        form_set_id (str):
        body (NewFormSetCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, FormSetConditionResponse]
    """

    return sync_detailed(
        form_set_id=form_set_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    form_set_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormSetCondition,
) -> Response[ErrorsList | FormSetConditionResponse]:
    """Creates a Form Set Condition

     Creates a new form_set_condition from provided data

    Args:
        form_set_id (str):
        body (NewFormSetCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, FormSetConditionResponse]]
    """

    kwargs = _get_kwargs(
        form_set_id=form_set_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    form_set_id: str,
    *,
    client: AuthenticatedClient,
    body: NewFormSetCondition,
) -> ErrorsList | FormSetConditionResponse | None:
    """Creates a Form Set Condition

     Creates a new form_set_condition from provided data

    Args:
        form_set_id (str):
        body (NewFormSetCondition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, FormSetConditionResponse]
    """

    return (
        await asyncio_detailed(
            form_set_id=form_set_id,
            client=client,
            body=body,
        )
    ).parsed
