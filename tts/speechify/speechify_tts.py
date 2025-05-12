#!/usr/bin/env python3

import os
import sys
import getopt
import base64
from inspect import getmembers
from pprint import pprint
from var_dump import var_dump
from dotenv import load_dotenv
from speechify import Speechify
from speechify.tts import GetSpeechOptionsRequest
from speechify.core.api_error import ApiError
from voice_config import voice_config, list_voice_config
from helper_functions import print_usage, DEFAULT_TEXT


def generate_tts(voice, text):
    load_dotenv()
    api_key = os.getenv("SPEECHIFY_API_KEY")

    client = Speechify(token=api_key)
    text = text.replace("%%name%%", voice)

    try:
        audio = client.tts.audio.speech(
            input=text,
            **voice_config[voice]
        )
    except ApiError as e:
        print(f"Error: {e}")
        print(e.status_code)
        print(e.body)
        sys.exit(1)

    #     var_dump(audio)
    #     print("audio object:", vars(audio))
    # for name, value in getmembers(audio):
    #     if not name.startswith('__'):
    #         value_repr = repr(value)
    #         value_trunc = value_repr[:60] + "..." if len(value_repr) > 60 else value_repr
    #         pprint(f"{name}: {value_trunc}")

    return audio


def save(audio, output_file):
    decoded = base64.b64decode(audio.audio_data)
    with open(output_file, "wb") as f:
        f.write(decoded)
    f.close()


def main(argv):
    output_file = "speechify_tts.wav"
    voice = "dj-brian"
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
