"""
This script downloads the transcript of a YouTube video and saves it to a specified file.
It is particularly useful for extracting transcripts of long podcast videos to provide them to a language model (LLM) for key insights.
Usage:
    python download_transcript.py <video_url> [output_path]
Arguments:
    video_url: The URL of the YouTube video.
    output_path: (Optional) The path where the transcript will be saved. If not provided, the transcript will be saved in the user's Downloads folder with a timestamp.
"""

import argparse
import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable
from datetime import datetime

def download_transcript(video_url, output_path=None):
    try:
        if output_path is None:
            user_downloads = os.path.expanduser('~') + '/Downloads/'
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            output_path = os.path.join(user_downloads, f"Transcripts-{timestamp}.txt")
        
        video_id = video_url.split('v=')[1]
        print('video_id is ', video_id)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        with open(output_path, 'w', encoding='utf-8') as file:
            for entry in transcript:
                file.write(f"{entry['start']}: {entry['text']}\n")
        
        print(f"Transcript saved to {output_path}")
    
    except IndexError as e:
        print("Invalid YouTube URL format.")
        print(e)
    except VideoUnavailable:
        print("The video is unavailable.")
    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download YouTube video transcript.')
    parser.add_argument('video_url', help='URL of the YouTube video')
    parser.add_argument('output_path', nargs='?', default=None, help='Path to save the transcript')

    args = parser.parse_args()
    download_transcript(args.video_url, args.output_path)
