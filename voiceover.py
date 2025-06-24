from gtts import gTTS
import os

def generate_voiceover(text, filename="voiceover.mp3"):
    tts = gTTS(text=text, lang='hi')
    tts.save(filename)
    return filename
