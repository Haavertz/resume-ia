import yt_dlp
import whisper
import os

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio', 
        'verbose': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return 'audio.mp3'

def transcribe_audio(audio_file):
    model = whisper.load_model('base')
    
    result = model.transcribe(audio_file)
    
    with open('transcribe_audio.txt', 'w', encoding='utf-8') as f:
        f.write(result['text'])
    
    return result['text']

def main():
    video_url = input("Past URL to video: ")
    
    print("Download áudio...")
    audio_file = download_audio(video_url)
    
    print("Transcribe áudio...")
    transcription = transcribe_audio(audio_file)
    
    print("\nTranscribe:")
    print(transcription)
    
    # os.remove(audio_file)

if __name__ == "__main__":
    main()