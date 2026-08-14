from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_workflow_custom_field_selection import NewWorkflowCustomFieldSelection
from ...models.workflow_custom_field_selection_response import WorkflowCustomFieldSelectionResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: NewWorkflowCustomFieldSelection,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/workflows/{workflow_id}/custom_field_selections",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | WorkflowCustomFieldSelectionResponse | None:
    if response.status_code == 201:
        response_201 = WorkflowCustomFieldSelectionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | WorkflowCustomFieldSelectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowCustomFieldSelection,
) -> Response[ErrorsList | WorkflowCustomFieldSelectionResponse]:
    """[DEPRECATED] Creates a workflow custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new workflow custom field selection from
    provided data

    Args:
        workflow_id (str):
        body (NewWorkflowCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowCustomFieldSelectionResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowCustomFieldSelection,
) -> ErrorsList | WorkflowCustomFieldSelectionResponse | None:
    """[DEPRECATED] Creates a workflow custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new workflow custom field selection from
    provided data

    Args:
        workflow_id (str):
        body (NewWorkflowCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowCustomFieldSelectionResponse]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowCustomFieldSelection,
) -> Response[ErrorsList | WorkflowCustomFieldSelectionResponse]:
    """[DEPRECATED] Creates a workflow custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new workflow custom field selection from
    provided data

    Args:
        workflow_id (str):
        body (NewWorkflowCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WorkflowCustomFieldSelectionResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: NewWorkflowCustomFieldSelection,
) -> ErrorsList | WorkflowCustomFieldSelectionResponse | None:
    """[DEPRECATED] Creates a workflow custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new workflow custom field selection from
    provided data

    Args:
        workflow_id (str):
        body (NewWorkflowCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WorkflowCustomFieldSelectionResponse]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
