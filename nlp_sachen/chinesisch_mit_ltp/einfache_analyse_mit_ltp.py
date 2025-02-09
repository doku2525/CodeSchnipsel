import torch  # Benötigt für LTP Pipeline
from ltp import LTP
from ltp.generic import LTPOutput


def erzeuge_output() -> LTPOutput:
    # 1. Modell laden (nur einmal!)
    ltp = LTP("LTP/small")  # Oder der Pfad zu deinen LTP-Modellen

    # text = "这是一个中文句子。这是另一个句子。第三个句子。阿里巴巴是一家知名的科技公司，总部位于杭州。马云是阿里巴巴的创始人。"
    text = "他写的书很有意思。我觉得他今天不会来滑冰，因为他不舒服。"

    # 2. Pipeline ausführen
    output = ltp.pipeline([text], tasks=["cws", "pos", "ner", "srl", "dep"])  # Wichtiger Hinweis unten!
    return output


def main() -> None:
    output = erzeuge_output()

    # 3. Ergebnisse extrahieren und ausgeben

    # a. Wortsegmentierung (cws)
    words = output.cws[0]  # [0] weil wir nur einen Text übergeben haben
    print("Wortsegmentierung:", words)

    # b. Wortartbestimmung (pos)
    postags = output.pos[0]
    print("Wortartbestimmung:", postags)

    # c. Erkennung benannter Entitäten (ner)
    netags = output.ner[0]
    print("Erkennung benannter Entitäten:", netags)

    # d. Dependenzanalyse (dep)
    arcs = output.dep[0]
    print("Dependenzanalyse:", arcs)

    # e. Semantische Rollenmarkierung (srl)
    roles = output.srl[0]
    print("Semantische Rollenmarkierung:", roles)

    # 4.  Satzsegmentierung (Manuell, da keine Pipeline dafür exitiert.)
    sentences = []
    current_sentence = []
    for word in words:  # Nutze die bereits segmentierten Wörter!
        current_sentence.append(word)
        if word in ["。", "！", "？", "……", "；"]:   # ; hinzugefügt
            sentences.append("".join(current_sentence))
            current_sentence = []
    if current_sentence:
        sentences.append("".join(current_sentence))

    print("\nSätze:")
    for sent in sentences:
        print(sent)


if __name__ == '__main__':
    main()
