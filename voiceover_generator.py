import pyttsx3

def generate_voiceover(script_text):
    output_path = "output_audio.mp3"
    engine = pyttsx3.init()

    # Optional: Try setting Hindi voice if available
    for voice in engine.getProperty('voices'):
        if "hi" in voice.id or "hindi" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.save_to_file(script_text, output_path)
    engine.runAndWait()
    return output_path
