from typing import Literal, cast

NewLiveCallRouterDataAttributesWaitingMusicUrl = Literal[
    "https://storage.rootly.com/twilio/voicemail/BusyStrings.mp3",
    "https://storage.rootly.com/twilio/voicemail/ClockworkWaltz.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_brahms-116-4.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_chopin-15-2.mp3",
    "https://storage.rootly.com/twilio/voicemail/MARKOVICHAMP-Borghestral.mp3",
    "https://storage.rootly.com/twilio/voicemail/Mellotroniac_-_Flight_Of_Young_Hearts_Flute.mp3",
    "https://storage.rootly.com/twilio/voicemail/oldDog_-_endless_goodbye_%28instr.%29.mp3",
]

NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_WAITING_MUSIC_URL_VALUES: set[NewLiveCallRouterDataAttributesWaitingMusicUrl] = {
    "https://storage.rootly.com/twilio/voicemail/BusyStrings.mp3",
    "https://storage.rootly.com/twilio/voicemail/ClockworkWaltz.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_brahms-116-4.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_chopin-15-2.mp3",
    "https://storage.rootly.com/twilio/voicemail/MARKOVICHAMP-Borghestral.mp3",
    "https://storage.rootly.com/twilio/voicemail/Mellotroniac_-_Flight_Of_Young_Hearts_Flute.mp3",
    "https://storage.rootly.com/twilio/voicemail/oldDog_-_endless_goodbye_%28instr.%29.mp3",
}


def check_new_live_call_router_data_attributes_waiting_music_url(
    value: str | None,
) -> NewLiveCallRouterDataAttributesWaitingMusicUrl | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_WAITING_MUSIC_URL_VALUES:
        return cast(NewLiveCallRouterDataAttributesWaitingMusicUrl, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_WAITING_MUSIC_URL_VALUES!r}"
    )
