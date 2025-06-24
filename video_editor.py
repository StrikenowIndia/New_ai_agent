from moviepy.editor import *

def create_video(voice_file, headline):
    background = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=180)
    audio = AudioFileClip(voice_file)
    text_clip = TextClip(headline, fontsize=50, color='white', size=(1200, None)).set_duration(audio.duration).set_position('center')

    video = CompositeVideoClip([background, text_clip.set_audio(audio)])
    output_path = "final_video.mp4"
    video.write_videofile(output_path, fps=24)
    return output_path
