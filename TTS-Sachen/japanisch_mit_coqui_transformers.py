import transformers
from TTS.api import TTS

# Documentation und Modelle auf der HP: https://docs.coqui.ai/en/latest/


def main() -> None:
    print(f"Laden des chinesischen Modells...")
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    print(f"TTS to File ... Stimme1 normal")
    tts.tts_to_file(text="部屋に家具が少ない。窓際に机が2つ並んでいる。各テーブルの前に椅子がある。",
                    speaker_wav="Stimme1.wav",
                    language="ja",
                    file_path="japanisch_mit_coqui_transformers_output_mit_stimme1.wav")
    print(f"TTS to File ... Stimme1 angry")
    tts.tts_to_file(text="部屋に家具が少ない。窓際に机が2つ並んでいる。各テーブルの前に椅子がある。",
                    speaker_wav="Stimme1.wav",
                    language="ja",
                    file_path="japanisch_mit_coqui_transformers_output_mit_stimme1_angry.wav",
                    emotion="angry")
    print(f"TTS to File ... Stimme2 normal")
    tts.tts_to_file(text="部屋に家具が少ない。窓際に机が2つ並んでいる。各テーブルの前に椅子がある。",
                    speaker_wav="Stimme2.wav",
                    language="ja",
                    file_path="japanisch_mit_coqui_transformers_output_mit_stimme2.wav")
    print(f"TTS to File ... Stimme2 angry")
    tts.tts_to_file(text="部屋に家具が少ない。窓際に机が2つ並んでいる。各テーブルの前に椅子がある。",
                    speaker_wav="Stimme2.wav",
                    language="ja",
                    file_path="japanisch_mit_coqui_transformers_output_mit_stimme2_angry.wav",
                    emotion="angry")


if __name__ == '__main__':
    main()
