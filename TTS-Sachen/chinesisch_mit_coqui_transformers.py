import torch
import transformers
from TTS.api import TTS

# Documentation und Modelle auf der HP: https://docs.coqui.ai/en/latest/


def main() -> None:
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"Laden des chinesischen Models... mit {device.capitalize()}")
    # tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)  # cude funktioniert nicht auf i7
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    print(f"TTS to File ... Stimme1 normal")
    # Das Argument emotions hat keinen Einfluss auf die Ausgabe. Ist wohl noch von frueher uebrig.
    tts.tts_to_file(text="房间里家具不多，靠窗户摆着两张书桌，每张桌子的前边有一把椅子。",
                    speaker_wav="Stimme1.wav",
                    language="zh-cn",
                    file_path="chinesisch_mit_coqui_transformers_output_mit_stimme1.wav")
    print(f"TTS to File ... Stimme1 angry")
    tts.tts_to_file(text="房间里家具不多，靠窗户摆着两张书桌，每张桌子的前边有一把椅子。",
                    speaker_wav="Stimme1.wav",
                    language="zh-cn",
                    file_path="chinesisch_mit_coqui_transformers_output_mit_stimme1_angry.wav",
                    emotion="angry")
    print(f"TTS to File ... Stimme2 normal")
    tts.tts_to_file(text="房间里家具不多，靠窗户摆着两张书桌，每张桌子的前边有一把椅子。",
                    speaker_wav="Stimme2.wav",
                    language="zh-cn",
                    file_path="chinesisch_mit_coqui_transformers_output_mit_stimme2.wav")
    print(f"TTS to File ... Stimme2 angry")
    tts.tts_to_file(text="房间里家具不多，靠窗户摆着两张书桌，每张桌子的前边有一把椅子。",
                    speaker_wav="Stimme2.wav",
                    language="zh-cn",
                    file_path="chinesisch_mit_coqui_transformers_output_mit_stimme2_angry.wav",
                    emotion="angry")


if __name__ == '__main__':
    main()