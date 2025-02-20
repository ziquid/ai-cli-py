# helper_functions.py


def print_usage():
    print("""Usage: elevenlabs_tts.py <options>

Options:
[-h|--help]: Show this help message.
[-i|--input <filename>]: Get text to read from a file. Use '-' to read from stdin.
[-o|--output <filename>]: Save the audio to a file.  If not specified, audio will be saved to the file 'elevenlabs_tts.mp3'.
[-p|--play]: Play the audio after saving it.
[-P|--Play]: Play the audio without saving it.
[-t|--text <text>]: Specify the text to read.
[-x|--vox <voice>]: Select the voice to use.  Use --list-voices to see available voices.
[--list-voices]: List available voices.
""")


DEFAULT_TEXT = """
       Welcome to the Eleven Labs text-to-speech demo.
       This is a demonstration of the Eleven Labs text-to-speech API.
       The API allows you to generate high-quality speech from text.
       The API supports multiple languages and voices.
       You can customize the speech output by adjusting the voice settings.
       The API also supports text normalization for better speech quality.
       You can use the API to generate speech for various applications.
       The API is easy to use and provides fast response times.
       The API is reliable and provides high-quality speech output.
       Thank you for using the Eleven Labs text-to-speech demo.
       """
