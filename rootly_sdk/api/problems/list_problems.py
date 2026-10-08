from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.problem_list import ProblemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterowner_user_id: int | Unset = UNSET,
    filterowner_group_id: str | Unset = UNSET,
    filtercreated_by_user_id: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["sort"] = sort

    params["filter[search]"] = filtersearch

    params["filter[owner_user_id]"] = filterowner_user_id

    params["filter[owner_group_id]"] = filterowner_group_id

    params["filter[created_by_user_id]"] = filtercreated_by_user_id

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[due_date][gt]"] = filterdue_dategt

    params["filter[due_date][gte]"] = filterdue_dategte

    params["filter[due_date][lt]"] = filterdue_datelt

    params["filter[due_date][lte]"] = filterdue_datelte

    params["filter[status][eq]"] = filterstatuseq

    params["filter[status][not_eq]"] = filterstatusnot_eq

    params["filter[status][in]"] = filterstatusin

    params["filter[status][not_in]"] = filterstatusnot_in

    params["filter[priority][eq]"] = filterpriorityeq

    params["filter[priority][not_eq]"] = filterprioritynot_eq

    params["filter[priority][in]"] = filterpriorityin

    params["filter[priority][not_in]"] = filterprioritynot_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/problems",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | ProblemList | None:
    if response.status_code == 200:
        response_200 = ProblemList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorsList.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | ProblemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterowner_user_id: int | Unset = UNSET,
    filterowner_group_id: str | Unset = UNSET,
    filtercreated_by_user_id: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
) -> Response[ErrorsList | ProblemList]:
    """List problems

     Sorting by incidents_count would let callers without incident read infer relative hidden incident
    counts, so it is rejected.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterowner_user_id (int | Unset):
        filterowner_group_id (str | Unset):
        filtercreated_by_user_id (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | ProblemList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
        filtersearch=filtersearch,
        filterowner_user_id=filterowner_user_id,
        filterowner_group_id=filterowner_group_id,
        filtercreated_by_user_id=filtercreated_by_user_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterowner_user_id: int | Unset = UNSET,
    filterowner_group_id: str | Unset = UNSET,
    filtercreated_by_user_id: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
) -> ErrorsList | ProblemList | None:
    """List problems

     Sorting by incidents_count would let callers without incident read infer relative hidden incident
    counts, so it is rejected.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterowner_user_id (int | Unset):
        filterowner_group_id (str | Unset):
        filtercreated_by_user_id (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | ProblemList
    """

    return sync_detailed(
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
        filtersearch=filtersearch,
        filterowner_user_id=filterowner_user_id,
        filterowner_group_id=filterowner_group_id,
        filtercreated_by_user_id=filtercreated_by_user_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterowner_user_id: int | Unset = UNSET,
    filterowner_group_id: str | Unset = UNSET,
    filtercreated_by_user_id: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
) -> Response[ErrorsList | ProblemList]:
    """List problems

     Sorting by incidents_count would let callers without incident read infer relative hidden incident
    counts, so it is rejected.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterowner_user_id (int | Unset):
        filterowner_group_id (str | Unset):
        filtercreated_by_user_id (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | ProblemList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
        filtersearch=filtersearch,
        filterowner_user_id=filterowner_user_id,
        filterowner_group_id=filterowner_group_id,
        filtercreated_by_user_id=filtercreated_by_user_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterowner_user_id: int | Unset = UNSET,
    filterowner_group_id: str | Unset = UNSET,
    filtercreated_by_user_id: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
) -> ErrorsList | ProblemList | None:
    """List problems

     Sorting by incidents_count would let callers without incident read infer relative hidden incident
    counts, so it is rejected.

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterowner_user_id (int | Unset):
        filterowner_group_id (str | Unset):
        filtercreated_by_user_id (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | ProblemList
    """

    return (
        await asyncio_detailed(
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
            sort=sort,
            filtersearch=filtersearch,
            filterowner_user_id=filterowner_user_id,
            filterowner_group_id=filterowner_group_id,
            filtercreated_by_user_id=filtercreated_by_user_id,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterdue_dategt=filterdue_dategt,
            filterdue_dategte=filterdue_dategte,
            filterdue_datelt=filterdue_datelt,
            filterdue_datelte=filterdue_datelte,
            filterstatuseq=filterstatuseq,
            filterstatusnot_eq=filterstatusnot_eq,
            filterstatusin=filterstatusin,
            filterstatusnot_in=filterstatusnot_in,
            filterpriorityeq=filterpriorityeq,
            filterprioritynot_eq=filterprioritynot_eq,
            filterpriorityin=filterpriorityin,
            filterprioritynot_in=filterprioritynot_in,
        )
    ).parsed
