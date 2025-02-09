import yt_dlp


def main() -> None:
    # Optionen für yt-dlp
    ydl_opts = {
        'listsubtitles': True,  # Listet alle verfügbaren Untertitel auf
        'skip_download': True,  # Überspringt den Download des Videos
    }

    # URL des YouTube-Videos
    url = 'https://www.youtube.com/watch?v=7d4mdxC7joA'

    # yt-dlp initialisieren und die Untertitel auflisten
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        print(f"{list(info_dict.keys()) = }")
        """info_dict enthaelt neben den Untertiteln noch eine Vielazahl anderer Informationen.
            - Laenge des Videos
            - tags
        """

        # Überprüfen, ob Untertitel verfügbar sind
        if 'subtitles' in info_dict or 'automatic_captions' in info_dict:
            print("Verfügbare Untertitel:")

            # Manuelle Untertitel
            if 'subtitles' in info_dict:
                print("\nManuelle Untertitel:")
                for lang, sub_info in info_dict['subtitles'].items():
                    print(f"Sprache: {lang}, Formate: {[sub['ext'] for sub in sub_info]}")

            # Automatisch generierte Untertitel
            # if 'automatic_captions' in info_dict:
            #     print("\nAutomatisch generierte Untertitel:")
            #     for lang, sub_info in info_dict['automatic_captions'].items():
            #         print(f"Sprache: {lang}, Formate: {[sub['ext'] for sub in sub_info]}")
        else:
            print("Keine Untertitel verfügbar.")


if __name__ == '__main__':
    main()