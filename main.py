import yt_dlp as youtube_dl

def download_channel_videos(channel_url):
    # ダウンロードオプションを定義
    ydl_opts = {
        'format': 'best',  # 動画の最適なフォーマットをダウンロード
        'outtmpl': '%(title)s.%(ext)s',  # 保存するファイル名のフォーマット
        'ignoreerrors': True  # エラーがあっても処理を継続する
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

# チャンネルのURLを指定
channel_url = 'https://www.youtube.com/@/チャンネルのID/videos'
download_channel_videos(channel_url)

