# voice_config.py

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
}


def list_voice_config():
    for voice, config in voice_config.items():
        print(f"{voice}: {config['voice_id']}")
