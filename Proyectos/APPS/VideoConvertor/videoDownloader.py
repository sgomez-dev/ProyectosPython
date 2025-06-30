import yt_dlp

def download_video_with_audio(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': r'C:\Users\santiago.gomez\Desktop\%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': False,
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Pega el enlace de YouTube: ")
    download_video_with_audio(url)
