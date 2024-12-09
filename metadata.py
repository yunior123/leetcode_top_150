import subprocess
import json

def get_video_metadata(file_path):
    """
    Reads the metadata of a video file using ffprobe.

    Args:
        file_path (str): The path to the video file.

    Returns:
        dict: A dictionary containing metadata of the video.
    """
    try:
        # Run ffprobe command to get metadata
        command = [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format:stream_tags",
            "-print_format", "json",
            file_path
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Parse the JSON output
        metadata = json.loads(result.stdout)
        return metadata
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return None

# Example usage
if __name__ == "__main__":
    video_file_path = "Retry.mp4"  # Update with your video file path
    metadata = get_video_metadata(video_file_path)

    if metadata:
        print("Metadata retrieved successfully:")
        print(json.dumps(metadata, indent=4))
    else:
        print("Failed to retrieve metadata.")
