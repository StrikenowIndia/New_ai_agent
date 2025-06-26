import subprocess

def upload_video(video_path, title, description):
    try:
        command = [
            "youtube-upload",
            "--title", title,
            "--description", description,
            "--privacy", "public",
            video_path
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Upload failed: {result.stderr}")
    except Exception as e:
        import logging
        logging.error(f"❌ Upload error: {str(e)}")
