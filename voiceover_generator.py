from gtts import gTTS
import time

def generate_voiceover(script_text, retries=3, delay=10):
    output_path = "output_audio.mp3"

    for attempt in range(retries):
        try:
            tts = gTTS(text=script_text, lang='hi')
            tts.save(output_path)
            return output_path  # Success
        except Exception as e:
            if "429" in str(e) or "Too Many Requests" in str(e):
                print(f"⚠️ Rate limit hit. Waiting {delay} sec before retry... ({attempt+1}/{retries})")
                time.sleep(delay)
            else:
                raise e

    raise Exception("❌ Failed to generate voiceover after multiple attempts due to rate limit.")
