from moviepy.editor import concatenate_videoclips

def create_video(script, audio_path):
    try:
        import moviepy.editor as mp
        from moviepy.editor import TextClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips

        if not os.path.exists(audio_path):
            logging.error(f"❌ Audio file not found at: {audio_path}")
            return None

        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration

        # Split script into lines and make multiple TextClips
        lines = script.split('. ')
        clips = []

        per_clip_duration = duration / max(1, len(lines))

        for line in lines:
            txt = TextClip(line.strip(), fontsize=32, color='white', size=(1280, 720), bg_color='black')
            txt = txt.set_duration(per_clip_duration)
            txt = txt.set_position('center')
            clips.append(txt)

        video = concatenate_videoclips(clips)
        final_video = video.set_audio(audio_clip)

        output_path = "output_video.mp4"
        final_video.write_videofile(output_path, fps=24)

        logging.info("✅ Video created successfully.")
        return output_path

    except Exception as e:
        logging.error(f"❌ Error in create_video: {e}")
        return None
