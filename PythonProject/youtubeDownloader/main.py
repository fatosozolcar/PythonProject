import shutil
import yt_dlp

url = "https://www.youtube.com/watch?v=BboMpayJomw"

has_ffmpeg = shutil.which("ffmpeg") is not None

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    # FFmpeg varsa en iyi video+ses (ayrı akışları indirip birleştirir)
    # yoksa progressive mp4'e düş (birleştirme yok, kalite biraz düşebilir)
    'format': 'bestvideo+bestaudio/best' if has_ffmpeg else 'best[ext=mp4]/best',
    # FFmpeg yoksa birleştirmeye zorlamayalım:
    'merge_output_format': 'mp4' if has_ffmpeg else None,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("✅ Bitti")

