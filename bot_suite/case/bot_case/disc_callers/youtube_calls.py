import youtube_dl
import ffmpeg

save_path = "D:/Cthings/prog/Bot-Python/audio"

def create_command(command_name : str, duration : float, link : str):
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = link,download=False
        )
        filename = f"D:/Cthings/prog/Bot-Python/audio/{command_name}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        downloaded_audio = ffmpeg.input(f"D:/Cthings/prog/Bot-Python/audio/{command_name}.mp3")
        audio = (
            downloaded_audio.audio
            .trim(start = 0, end = duration)
            .filter_('asetpts', 'PTS-STARTPTS')
        )
        trimmed_audio = ffmpeg.concat(audio, v= 0, a=1)
        audio_output = ffmpeg.output(trimmed_audio, f"D:/Cthings/prog/Bot-Python/audio/{command_name}.mp3")
        print("Download complete... {}".format(filename))

    except Exception as e:
        print(e)