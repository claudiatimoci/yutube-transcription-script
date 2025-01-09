from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# ID of the YouTube video
video_id = "dxkk56oLpTk"

try:
    # Get the French transcription
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr'])

    # Format the transcript as plain text
    formatter = TextFormatter()
    transcript_text = formatter.format_transcript(transcript)

    # Save to a file
    with open("transcription.txt", "w", encoding="utf-8") as file:
        file.write(transcript_text)

    print("Transcription downloaded and saved to 'transcription.txt'.")

except Exception as e:
    print(f"Error: {e}")
