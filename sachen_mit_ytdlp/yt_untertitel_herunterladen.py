import yt_dlp


def main() -> None:
    # Optionen als Dictionary
    opts = {
        'writesubtitles': True,      # Untertitel herunterladen
        'subtitlesformat': 'srt',    # Untertitelformat (z. B. 'srt', 'vtt')
        'subtitleslangs': ['zh', 'en'],   # Sprachen der Untertitel als list[str]
        'skip_download': True  # Video nicht herunterladen
    }

    # YouTube-URL
    url = 'https://www.youtube.com/watch?v=v6FqTLIcub8'

    # yt-dlp initialisieren und den Download durchführen
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])  # Die URL muss als Liste übergeben werden


if __name__ == '__main__':
    main()
