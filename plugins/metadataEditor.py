#
# (c) Yash Oswal | yashoswal18@gmail.com

from pyrogram import Client
from pyrogram.types import Message
from bot import mergeApp, LOGGER
from config import Config

async def metaEditor(c:Client, m: Message):
    1
    import

def extract_video_metadata(video_path):
    """
    Extracts metadata from a video file.

    Args:
    video_path (str): Path to the video file.

    Returns:
    dict: Dictionary containing video metadata.
    """
    video_capture = cv2.VideoCapture(video_path)
    metadata = {
        'width': int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'fps': video_capture.get(cv2.CAP_PROP_FPS),
        'total_frames': int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT)),
        'duration_sec': int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT)) / video_capture.get(cv2.CAP_PROP_FPS)
    }
    video_capture.release()
    return metadata

# Example usage
video_path = 'path_to_video_file.mp4'
metadata = extract_video_metadata(video_path)
print(metadata)
