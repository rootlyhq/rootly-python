from typing import Literal, cast

CreateGoToMeetingTaskParamsConferenceCallInfo = Literal["free", "hyrid", "ptsn", "voip"]

CREATE_GO_TO_MEETING_TASK_PARAMS_CONFERENCE_CALL_INFO_VALUES: set[CreateGoToMeetingTaskParamsConferenceCallInfo] = {
    "free",
    "hyrid",
    "ptsn",
    "voip",
}


def check_create_go_to_meeting_task_params_conference_call_info(
    value: str | None,
) -> CreateGoToMeetingTaskParamsConferenceCallInfo | None:
    if value is None:
        return None
    if value in CREATE_GO_TO_MEETING_TASK_PARAMS_CONFERENCE_CALL_INFO_VALUES:
        return cast(CreateGoToMeetingTaskParamsConferenceCallInfo, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GO_TO_MEETING_TASK_PARAMS_CONFERENCE_CALL_INFO_VALUES!r}"
    )
