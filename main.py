import subprocess
import os
from openai import OpenAI

import subprocess
import os
from openai import OpenAI

def download_audio(url, output_filename="audio.mp3"):
    ffmpeg_location = "C:\\ffmpeg\\bin" # -> need install ffmpeg
    comand = [
        "yt-dlp",
        "-x",  
        "--audio-format", "mp3",  
        "--ffmpeg-location", ffmpeg_location, 
        "-o", output_filename,
        url
    ]
    subprocess.run(comand, check=True)
    return output_filename

def transcribe_audio(api_key, audio_file_path, language="en"):
    client = OpenAI(api_key=api_key)
    audio_file = open(audio_file_path, "rb")

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text",
        language=language 
    )

    return transcription 

def main():  
    api_openai = input("Your OpenAI API Key: ").strip()
    url = input("Write the video URL: ").strip()
    language = input("Write the language code (ex: 'en' or 'pt'): ").strip().lower()

    try:
        audio_path = download_audio(url)
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return

    try:
        transcribed_text = transcribe_audio(api_openai, audio_path, language)
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return

    print("\n=== Transcription Result ===\n")
    print(transcribed_text)

    if os.path.exists(audio_path):
        os.remove(audio_path)

if __name__ == "__main__":
    main()
