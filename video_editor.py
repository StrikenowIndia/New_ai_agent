# video_editor.py

from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO)

def create_video(voice_file, headline):
    try:
        if not os.path.exists(voice_file):
            raise FileNotFoundError(f"Voice file '{voice_file}' नहीं मिला।")
        if not os.path.exists("templates/thumbnail.jpg"):
            raise FileNotFoundError("thumbnail.jpg नहीं मिला।")

        audio_clip = AudioFileClip(voice_file)
        duration = audio_clip.duration

        image_clip = ImageClip("templates/thumbnail.jpg", duration=duration)
        image_clip = image_clip.set_audio(audio_clip)
        image_clip = image_clip.set_duration(duration).resize(height=720).set_position("center")

        final_clip = concatenate_videoclips([image_clip])
        final_clip.write_videofile("final_video.mp4", fps=24, logger=None)  # suppress moviepy logs

        logging.info("✅ Video successfully created as 'final_video.mp4'")

    except Exception as e:
        logging.error(f"❌ Error in create_video: {str(e)}")
        print(f"Error: {str(e)}")
