from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_action_item_list import ProblemActionItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    problem_id: str,
    *,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
    filterassigned_to_user_ideq: str | Unset = UNSET,
    filterassigned_to_user_idnot_eq: str | Unset = UNSET,
    filterassigned_to_user_idin: str | Unset = UNSET,
    filterassigned_to_user_idnot_in: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["sort"] = sort

    params["filter[search]"] = filtersearch

    params["filter[due_date][gt]"] = filterdue_dategt

    params["filter[due_date][gte]"] = filterdue_dategte

    params["filter[due_date][lt]"] = filterdue_datelt

    params["filter[due_date][lte]"] = filterdue_datelte

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[status][eq]"] = filterstatuseq

    params["filter[status][not_eq]"] = filterstatusnot_eq

    params["filter[status][in]"] = filterstatusin

    params["filter[status][not_in]"] = filterstatusnot_in

    params["filter[priority][eq]"] = filterpriorityeq

    params["filter[priority][not_eq]"] = filterprioritynot_eq

    params["filter[priority][in]"] = filterpriorityin

    params["filter[priority][not_in]"] = filterprioritynot_in

    params["filter[assigned_to_user_id][eq]"] = filterassigned_to_user_ideq

    params["filter[assigned_to_user_id][not_eq]"] = filterassigned_to_user_idnot_eq

    params["filter[assigned_to_user_id][in]"] = filterassigned_to_user_idin

    params["filter[assigned_to_user_id][not_in]"] = filterassigned_to_user_idnot_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/problems/{problem_id}/action_items".format(
            problem_id=quote(str(problem_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemActionItemList | None:
    if response.status_code == 200:
        response_200 = ProblemActionItemList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemActionItemList]:
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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
    filterassigned_to_user_ideq: str | Unset = UNSET,
    filterassigned_to_user_idnot_eq: str | Unset = UNSET,
    filterassigned_to_user_idin: str | Unset = UNSET,
    filterassigned_to_user_idnot_in: str | Unset = UNSET,
) -> Response[ProblemActionItemList]:
    """List a problem's action items

     List action items belonging to a problem, with filter, sort and pagination support

    Args:
        problem_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):
        filterassigned_to_user_ideq (str | Unset):
        filterassigned_to_user_idnot_eq (str | Unset):
        filterassigned_to_user_idin (str | Unset):
        filterassigned_to_user_idnot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemActionItemList]
    """

    kwargs = _get_kwargs(
        problem_id=problem_id,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
        filtersearch=filtersearch,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
        filterassigned_to_user_ideq=filterassigned_to_user_ideq,
        filterassigned_to_user_idnot_eq=filterassigned_to_user_idnot_eq,
        filterassigned_to_user_idin=filterassigned_to_user_idin,
        filterassigned_to_user_idnot_in=filterassigned_to_user_idnot_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    problem_id: str,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
    filterassigned_to_user_ideq: str | Unset = UNSET,
    filterassigned_to_user_idnot_eq: str | Unset = UNSET,
    filterassigned_to_user_idin: str | Unset = UNSET,
    filterassigned_to_user_idnot_in: str | Unset = UNSET,
) -> ProblemActionItemList | None:
    """List a problem's action items

     List action items belonging to a problem, with filter, sort and pagination support

    Args:
        problem_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):
        filterassigned_to_user_ideq (str | Unset):
        filterassigned_to_user_idnot_eq (str | Unset):
        filterassigned_to_user_idin (str | Unset):
        filterassigned_to_user_idnot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemActionItemList
    """

    return sync_detailed(
        problem_id=problem_id,
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
        filtersearch=filtersearch,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
        filterassigned_to_user_ideq=filterassigned_to_user_ideq,
        filterassigned_to_user_idnot_eq=filterassigned_to_user_idnot_eq,
        filterassigned_to_user_idin=filterassigned_to_user_idin,
        filterassigned_to_user_idnot_in=filterassigned_to_user_idnot_in,
    ).parsed


async def asyncio_detailed(
    problem_id: str,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
    filterassigned_to_user_ideq: str | Unset = UNSET,
    filterassigned_to_user_idnot_eq: str | Unset = UNSET,
    filterassigned_to_user_idin: str | Unset = UNSET,
    filterassigned_to_user_idnot_in: str | Unset = UNSET,
) -> Response[ProblemActionItemList]:
    """List a problem's action items

     List action items belonging to a problem, with filter, sort and pagination support

    Args:
        problem_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):
        filterassigned_to_user_ideq (str | Unset):
        filterassigned_to_user_idnot_eq (str | Unset):
        filterassigned_to_user_idin (str | Unset):
        filterassigned_to_user_idnot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemActionItemList]
    """

    kwargs = _get_kwargs(
        problem_id=problem_id,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
        filtersearch=filtersearch,
        filterdue_dategt=filterdue_dategt,
        filterdue_dategte=filterdue_dategte,
        filterdue_datelt=filterdue_datelt,
        filterdue_datelte=filterdue_datelte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filterpriorityeq=filterpriorityeq,
        filterprioritynot_eq=filterprioritynot_eq,
        filterpriorityin=filterpriorityin,
        filterprioritynot_in=filterprioritynot_in,
        filterassigned_to_user_ideq=filterassigned_to_user_ideq,
        filterassigned_to_user_idnot_eq=filterassigned_to_user_idnot_eq,
        filterassigned_to_user_idin=filterassigned_to_user_idin,
        filterassigned_to_user_idnot_in=filterassigned_to_user_idnot_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    problem_id: str,
    *,
    client: AuthenticatedClient,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterdue_dategt: str | Unset = UNSET,
    filterdue_dategte: str | Unset = UNSET,
    filterdue_datelt: str | Unset = UNSET,
    filterdue_datelte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filterpriorityeq: str | Unset = UNSET,
    filterprioritynot_eq: str | Unset = UNSET,
    filterpriorityin: str | Unset = UNSET,
    filterprioritynot_in: str | Unset = UNSET,
    filterassigned_to_user_ideq: str | Unset = UNSET,
    filterassigned_to_user_idnot_eq: str | Unset = UNSET,
    filterassigned_to_user_idin: str | Unset = UNSET,
    filterassigned_to_user_idnot_in: str | Unset = UNSET,
) -> ProblemActionItemList | None:
    """List a problem's action items

     List action items belonging to a problem, with filter, sort and pagination support

    Args:
        problem_id (str):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):
        filtersearch (str | Unset):
        filterdue_dategt (str | Unset):
        filterdue_dategte (str | Unset):
        filterdue_datelt (str | Unset):
        filterdue_datelte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filterpriorityeq (str | Unset):
        filterprioritynot_eq (str | Unset):
        filterpriorityin (str | Unset):
        filterprioritynot_in (str | Unset):
        filterassigned_to_user_ideq (str | Unset):
        filterassigned_to_user_idnot_eq (str | Unset):
        filterassigned_to_user_idin (str | Unset):
        filterassigned_to_user_idnot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemActionItemList
    """

    return (
        await asyncio_detailed(
            problem_id=problem_id,
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
            sort=sort,
            filtersearch=filtersearch,
            filterdue_dategt=filterdue_dategt,
            filterdue_dategte=filterdue_dategte,
            filterdue_datelt=filterdue_datelt,
            filterdue_datelte=filterdue_datelte,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterstatuseq=filterstatuseq,
            filterstatusnot_eq=filterstatusnot_eq,
            filterstatusin=filterstatusin,
            filterstatusnot_in=filterstatusnot_in,
            filterpriorityeq=filterpriorityeq,
            filterprioritynot_eq=filterprioritynot_eq,
            filterpriorityin=filterpriorityin,
            filterprioritynot_in=filterprioritynot_in,
            filterassigned_to_user_ideq=filterassigned_to_user_ideq,
            filterassigned_to_user_idnot_eq=filterassigned_to_user_idnot_eq,
            filterassigned_to_user_idin=filterassigned_to_user_idin,
            filterassigned_to_user_idnot_in=filterassigned_to_user_idnot_in,
        )
    ).parsed
