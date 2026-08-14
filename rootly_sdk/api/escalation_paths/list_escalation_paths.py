from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.escalation_policy_path_list import EscalationPolicyPathList
from ...models.list_escalation_paths_filterpath_type import (
    ListEscalationPathsFilterpathType,
)
from ...models.list_escalation_paths_include import ListEscalationPathsInclude
from ...types import UNSET, Response, Unset


def _get_kwargs(
    escalation_policy_id: str,
    *,
    include: Union[Unset, ListEscalationPathsInclude] = UNSET,
    filterpath_type: Union[Unset, ListEscalationPathsFilterpathType] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Union[Unset, str] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_filterpath_type: Union[Unset, str] = UNSET
    if not isinstance(filterpath_type, Unset):
        json_filterpath_type = filterpath_type

    params["filter[path_type]"] = json_filterpath_type

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/escalation_policies/{escalation_policy_id}/escalation_paths",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EscalationPolicyPathList]:
    if response.status_code == 200:
        response_200 = EscalationPolicyPathList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EscalationPolicyPathList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    escalation_policy_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListEscalationPathsInclude] = UNSET,
    filterpath_type: Union[Unset, ListEscalationPathsFilterpathType] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[EscalationPolicyPathList]:
    """List escalation paths

     List escalation paths

    Args:
        escalation_policy_id (str):
        include (Union[Unset, ListEscalationPathsInclude]):
        filterpath_type (Union[Unset, ListEscalationPathsFilterpathType]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EscalationPolicyPathList]
    """

    kwargs = _get_kwargs(
        escalation_policy_id=escalation_policy_id,
        include=include,
        filterpath_type=filterpath_type,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    escalation_policy_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListEscalationPathsInclude] = UNSET,
    filterpath_type: Union[Unset, ListEscalationPathsFilterpathType] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[EscalationPolicyPathList]:
    """List escalation paths

     List escalation paths

    Args:
        escalation_policy_id (str):
        include (Union[Unset, ListEscalationPathsInclude]):
        filterpath_type (Union[Unset, ListEscalationPathsFilterpathType]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EscalationPolicyPathList
    """

    return sync_detailed(
        escalation_policy_id=escalation_policy_id,
        client=client,
        include=include,
        filterpath_type=filterpath_type,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    escalation_policy_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListEscalationPathsInclude] = UNSET,
    filterpath_type: Union[Unset, ListEscalationPathsFilterpathType] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[EscalationPolicyPathList]:
    """List escalation paths

     List escalation paths

    Args:
        escalation_policy_id (str):
        include (Union[Unset, ListEscalationPathsInclude]):
        filterpath_type (Union[Unset, ListEscalationPathsFilterpathType]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EscalationPolicyPathList]
    """

    kwargs = _get_kwargs(
        escalation_policy_id=escalation_policy_id,
        include=include,
        filterpath_type=filterpath_type,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    escalation_policy_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListEscalationPathsInclude] = UNSET,
    filterpath_type: Union[Unset, ListEscalationPathsFilterpathType] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[EscalationPolicyPathList]:
    """List escalation paths

     List escalation paths

    Args:
        escalation_policy_id (str):
        include (Union[Unset, ListEscalationPathsInclude]):
        filterpath_type (Union[Unset, ListEscalationPathsFilterpathType]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EscalationPolicyPathList
    """

    return (
        await asyncio_detailed(
            escalation_policy_id=escalation_policy_id,
            client=client,
            include=include,
            filterpath_type=filterpath_type,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
