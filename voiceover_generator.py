from gtts import gTTS
from pydub import AudioSegment
import os
import time

def generate_voiceover(script_text, retries=3, delay=10):
    parts = script_text.split(". ")
    audio_segments = []

    for idx, part in enumerate(parts):
        output_path = f"part_{idx}.mp3"

        for attempt in range(retries):
            try:
                tts = gTTS(text=part, lang='hi')
                tts.save(output_path)
                audio_segments.append(AudioSegment.from_mp3(output_path))
                break
            except Exception as e:
                if "429" in str(e):
                    print(f"⚠️ Rate limit hit. Waiting {delay} sec before retry... ({attempt+1}/{retries})")
                    time.sleep(delay)
                else:
                    raise e
        else:
            raise Exception("❌ Failed after multiple attempts due to rate limit.")

    # Merge all parts
    final_audio = sum(audio_segments)
    final_path = "output_audio.mp3"
    final_audio.export(final_path, format="mp3")

    # Clean up temp files
    for idx in range(len(parts)):
        os.remove(f"part_{idx}.mp3")

    return final_path
