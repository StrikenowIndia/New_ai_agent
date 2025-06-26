from gtts import gTTS

def generate_voiceover(script_text):
    output_path = "output_audio.mp3"
    tts = gTTS(text=script_text, lang='hi')
    tts.save(output_path)
    return output_path  # ✅ Return the actual audio file path
