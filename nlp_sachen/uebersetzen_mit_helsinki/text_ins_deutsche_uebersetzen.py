from transformers import MarianMTModel, MarianTokenizer


def jap_deutsch():
    # Modell und Tokenizer laden
    # model_name = "Helsinki-NLP/opus-mt-ja-de"
    model_name = "Nextcloud-AI/opus-mt-ja-de"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Text übersetzen
    japanese_text = "昨日、朝から夜までずっと雨が降りましたから、全然出かけませんでした。"
    inputs = tokenizer(japanese_text, return_tensors="pt")
    translated = model.generate(**inputs)
    german_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    print(f"{japanese_text} = {german_text}")


def chin_deutsch():
    # Modell und Tokenizer laden
    # model_name = "Helsinki-NLP/opus-mt-zh-de"
    model_name = "Nextcloud-AI/opus-mt-zh-de"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Text übersetzen
    chinese_text = "房间里家具不多，靠窗户摆着两张书桌，每张桌子的前边有一把椅子。"
    inputs = tokenizer(chinese_text, return_tensors="pt")
    translated = model.generate(**inputs)
    german_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    print(f"{chinese_text} = {german_text}")


if __name__ == '__main__':
    # Zumindest fuer Japanisch und Chinesisch sind die Uebersetzungen nicht so doll v_v
    jap_deutsch()  # Ist falsch
    chin_deutsch()  # Hmm, nicht falsch.
