# voiceover_generator.py

from gtts import gTTS
import os
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO)

def generate_voiceover(script_text, lang='hi'):
    try:
        if not script_text.strip():
            raise ValueError("⚠️ Voiceover के लिए स्क्रिप्ट खाली है।")

        tts = gTTS(text=script_text, lang=lang)
        audio_path = "voiceover.mp3"
        tts.save(audio_path)
        logging.info("✅ Voiceover generated successfully.")
        return audio_path

    except Exception as e:
        logging.error(f"❌ Error in generate_voiceover: {str(e)}")
        return None

# Optional test
if __name__ == "__main__":
    sample_script = "नमस्कार दोस्तों, आज की मुख्य खबरें इस प्रकार हैं।"
    path = generate_voiceover(sample_script)
    print("Voiceover saved at:", path)
