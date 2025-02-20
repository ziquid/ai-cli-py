# voice_config.py

voice_config = {
    'dallin-turbo': {
        "voice_id": "alFofuDn3cOwyoz1i44T",
        "model_id": "eleven_flash_v2",
        "output_format": "mp3_44100_128",
        "voice_settings": {
            "stability": 0.38,
            "similarity_boost": 0.85,
            "style": 0.4,
            "use_speaker_boost": True
        },
        "apply_text_normalization": "on"
    },
    'dallin': {
        "voice_id": "alFofuDn3cOwyoz1i44T",
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_128",
        "voice_settings": {
            "stability": 0.38,
            "similarity_boost": 0.85,
            "style": 0.4,
            "use_speaker_boost": True
        },
        "apply_text_normalization": "on"
    },
    'natasha': {
        "voice_id": "j05EIz3iI3JmBTWC3CsA",
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_128",
        "voice_settings": {
            "stability": 0.38,
            "similarity_boost": 0.85,
            "style": 0.4,
            "use_speaker_boost": True
        },
        "apply_text_normalization": "on"
    },
    'drew': {
        "voice_id": "wgHvco1wiREKN0BdyVx5",
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_128",
        "voice_settings": {
            "stability": 0.38,
            "similarity_boost": 0.85,
            "style": 0.4,
            "use_speaker_boost": True
        },
        "apply_text_normalization": "on"
    },
    'gentle-american-male': {
        "voice_id": "TYUYa0yb237TBkUqLxZR",
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_128",
        "voice_settings": {
            "stability": 0.38,
            "similarity_boost": 0.85,
            "style": 0.4,
            "use_speaker_boost": True
        },
        "apply_text_normalization": "on"
    },
}


def list_voice_config():
    for voice, config in voice_config.items():
        print(f"{voice}: {config['voice_id']}")
