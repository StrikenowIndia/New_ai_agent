from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(voice_file, headline):
    duration = AudioFileClip(voice_file).duration
    image_clip = ImageClip("templates/thumbnail.jpg", duration=duration)
    image_clip = image_clip.set_audio(AudioFileClip(voice_file))
    image_clip = image_clip.set_duration(duration).resize(height=720).set_position("center")
    final_clip = concatenate_videoclips([image_clip])
    final_clip.write_videofile("final_video.mp4", fps=24)
