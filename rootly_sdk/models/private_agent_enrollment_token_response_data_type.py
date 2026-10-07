from typing import Literal

PrivateAgentEnrollmentTokenResponseDataType = Literal["private_agent_enrollment_tokens"]

PRIVATE_AGENT_ENROLLMENT_TOKEN_RESPONSE_DATA_TYPE_VALUES: set[PrivateAgentEnrollmentTokenResponseDataType] = {
    "private_agent_enrollment_tokens",
}


def check_private_agent_enrollment_token_response_data_type(
    value: str | None,
) -> PrivateAgentEnrollmentTokenResponseDataType | None:
    if value is None:
        return None
    if value in PRIVATE_AGENT_ENROLLMENT_TOKEN_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRIVATE_AGENT_ENROLLMENT_TOKEN_RESPONSE_DATA_TYPE_VALUES!r}"
    )
