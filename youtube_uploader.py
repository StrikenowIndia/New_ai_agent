import subprocess
import logging

def upload_video(video_path, title, description):
    try:
        logging.info("🚀 Uploading video to YouTube...")
        command = [
            "youtube-upload",
            "--title", title,
            "--description", description,
            "--privacy", "public",
            video_path
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Debug: Upload result logs
        logging.info(f"STDOUT:\n{result.stdout}")
        logging.info(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            raise Exception(f"Upload failed: {result.stderr}")
        
        logging.info("✅ Upload successful! Video URL should be printed above.")
        
    except Exception as e:
        logging.error(f"❌ Upload error: {str(e)}")
