from TTS.api import TTS


def main() -> None:
    print(f"Laden des chinesischen Modells")
    tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False)
    print(f"TTS to File ... (normal)")
    # Synthese der Sprache und Speichern in einer Datei
    tts.tts_to_file(text="房间里家具不多，靠窗户摆着两张书桌，每张桌子的前边有一把椅子。",
                    file_path="coquiTTS_chinesisch_modell_output_chinese.wav")
    # Argument emotion ist veraltet. Wird nicht verarbeitet.
    print(f"TTS to File ... (angry")
    # Synthese der Sprache und Speichern in einer Datei
    tts.tts_to_file(text="我很生气！房间里家具不多，靠窗户摆着两张书桌，每张桌子的前边有一把椅子。",
                    file_path="coquiTTS_chinesisch_modell_output_angry_chinses.wav", emotion="angry")


if __name__ == '__main__':
    main()
