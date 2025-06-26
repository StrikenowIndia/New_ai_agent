def generate_voiceover(script_text):
    # Save voiceover to file
    output_path = "output_audio.mp3"

    # Generate audio using TTS engine (e.g., pyttsx3, gTTS, etc.)
    # For example:
    from gtts import gTTS
    tts = gTTS(script_text, lang="hi")
    tts.save(output_path)

    return output_path  # ✅ Return the file path, not the script itself
