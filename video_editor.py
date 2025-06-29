import os
import logging
from moviepy.editor import AudioFileClip, ColorClip

def create_video(script, audio_path):
    try:
        logging.info("🎞️ Creating video...")

        if not os.path.exists(audio_path):
            logging.error(f"❌ Audio file not found at: {audio_path}")
            return None

        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration

        # Solid black background
        video_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        video_clip = video_clip.set_audio(audio_clip)

        output_path = "output_video.mp4"
        video_clip.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

        logging.info("✅ Video created successfully.")
        return output_path

    except Exception as e:
        logging.error(f"❌ Error in create_video: {e}")
        return None
