# voiceover_generator.py

from gtts import gTTS
import os

def generate_voiceover(script_text, lang='hi'):
    tts = gTTS(text=script_text, lang=lang)
    audio_path = "voiceover.mp3"
    tts.save(audio_path)
    return audio_path
