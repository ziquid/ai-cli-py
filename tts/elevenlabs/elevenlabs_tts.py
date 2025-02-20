#!/usr/bin/env python3

import os
import sys
import getopt
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save, play
from voice_config import voice_config, list_voice_config
from helper_functions import print_usage, DEFAULT_TEXT


def generate_tts(voice, text):
    load_dotenv()
    api_key = os.getenv("ELEVENLABS_API_KEY")

    client = ElevenLabs(api_key=api_key)

    text = text.replace("%%name%%", voice)

    audio = client.text_to_speech.convert(
        text=text,
        **voice_config[voice]
    )

    return audio


def main(argv):
    output_file = "elevenlabs_tts.mp3"
    voice = "dallin-turbo"
    play_audio = False
    play_only = False
    text = DEFAULT_TEXT

    try:
        opts, args = getopt.getopt(argv, "ho:x:i:pPt:",
                                   ["help", "output=", "vox=", "input=", "list-voices", "play", "Play", "text="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit(0)
        if opt in ("--list-voices"):
            list_voice_config()
            sys.exit(0)
        if opt in ("-o", "--output"):
            output_file = arg
        if opt in ("-x", "--vox"):
            voice = arg
        if opt in ("-i", "--input"):
            if arg == "-":
                text = sys.stdin.read()
            else:
                with open(arg, 'r') as file:
                    text = file.read()
        if opt in ("-t", "--text"):
            text = arg
        if opt in ("-p", "--play"):
            play_audio = True
        if opt in ("-P", "--Play"):
            play_only = True

    audio = generate_tts(voice, text=text)

    if play_only:
        play(audio)
    else:
        save(audio, output_file)
        print(f"audio saved as {output_file}")

        if play_audio:
            play(audio)


if __name__ == "__main__":
    main(sys.argv[1:])
