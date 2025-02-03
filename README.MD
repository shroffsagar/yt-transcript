This script downloads the transcript of a YouTube video and saves it to a specified file.
It is particularly useful for extracting transcripts of long podcast videos to provide them to a language model (LLM) for key insights.

## Usage:
```
python download_transcript.py <video_url> [output_path]
```

### Arguments:
- `video_url`: The URL of the YouTube video.
- `output_path`: (Optional) The path where the transcript will be saved. If not provided, the transcript will be saved in the user's Downloads folder with a timestamp.

## Adding an Alias
To make it easier to run the script, you can add an alias to your bash_profile or rc file:
```
alias yt="python /Users/sagar/Code/tools/yt-transcript/download_transcript.py"
```
After adding the alias, you can use the script with:
```
yt <video_url> [output_path]
```