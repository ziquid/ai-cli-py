# voice_config.py

import os, sys
from dotenv import load_dotenv
from speechify import Speechify
from var_dump import var_dump

voice_config = {
    'dj-brian': {
        'audio_format': "wav",
        'language': "en-US",
        'model': "simba-english",
        'options': {
            'loudness_normalization': True,
            'text_normalization': True,
        },
        'voice_id': "oliver",
    },
    'spc-betty': {
        'audio_format': "wav",
        'language': "en-US",
        'model': "simba-english",
        'options': {
            'loudness_normalization': True,
            'text_normalization': True,
        },
        'voice_id': "betty",
    },
}


def list_voice_config(desired_locale="en-US"):
    for voice, config in voice_config.items():
        print(f"{voice}: {config['voice_id']}")

    load_dotenv()
    api_key = os.getenv("SPEECHIFY_API_KEY")

    client = Speechify(token=api_key)

    try:
        voices = client.tts.voices.list()
    except ApiError as e:
        print(f"Error: {e}")
        print(e.status_code)
        print(e.body)
        sys.exit(1)

    voices.sort(key=lambda x: f"{x.locale}, {x.gender}")

    locale = ""
    gender = ""
    for voice in voices:
        if voice.locale != desired_locale:
            continue
        if locale != voice.locale:
            print(f"\n{voice.locale}")
            locale = voice.locale
        if gender != voice.gender:
            print(f"-- {voice.gender}")
            gender = voice.gender
        print(f"{voice.display_name} ({voice.id}) {voice.tags} {voice.preview_audio}")
        # print(f"{voice}")
