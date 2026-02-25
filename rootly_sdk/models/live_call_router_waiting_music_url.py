from typing import Literal, cast

LiveCallRouterWaitingMusicUrl = Literal[
    "https://storage.rootly.com/twilio/voicemail/BusyStrings.mp3",
    "https://storage.rootly.com/twilio/voicemail/ClockworkWaltz.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_brahms-116-4.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_chopin-15-2.mp3",
    "https://storage.rootly.com/twilio/voicemail/MARKOVICHAMP-Borghestral.mp3",
    "https://storage.rootly.com/twilio/voicemail/Mellotroniac_-_Flight_Of_Young_Hearts_Flute.mp3",
    "https://storage.rootly.com/twilio/voicemail/oldDog_-_endless_goodbye_%28instr.%29.mp3",
]

LIVE_CALL_ROUTER_WAITING_MUSIC_URL_VALUES: set[LiveCallRouterWaitingMusicUrl] = {
    "https://storage.rootly.com/twilio/voicemail/BusyStrings.mp3",
    "https://storage.rootly.com/twilio/voicemail/ClockworkWaltz.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_brahms-116-4.mp3",
    "https://storage.rootly.com/twilio/voicemail/ith_chopin-15-2.mp3",
    "https://storage.rootly.com/twilio/voicemail/MARKOVICHAMP-Borghestral.mp3",
    "https://storage.rootly.com/twilio/voicemail/Mellotroniac_-_Flight_Of_Young_Hearts_Flute.mp3",
    "https://storage.rootly.com/twilio/voicemail/oldDog_-_endless_goodbye_%28instr.%29.mp3",
}


def check_live_call_router_waiting_music_url(value: str | None) -> LiveCallRouterWaitingMusicUrl | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_WAITING_MUSIC_URL_VALUES:
        return cast(LiveCallRouterWaitingMusicUrl, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_WAITING_MUSIC_URL_VALUES!r}")
