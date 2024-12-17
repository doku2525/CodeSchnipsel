import qrcode
import tkinter as tk
from PIL import Image, ImageTk


def generate_qr_code(data: str) -> Image:
    """Generiert einen QR-Code und gibt ihn als PIL-Image zurück.

    Args:
        data (str): Die Daten, die im QR-Code codiert werden sollen.

    Returns:
        PIL.Image: Das erzeugte QR-Code-Bild.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def show_qr_code_in_tkinter(img: Image) -> None:
    """Zeigt den QR-Code in einem Tkinter-Fenster an.
    Kann mit <q>, <ESC> oder <Enter> geschlossen werden.

    Args:
        img (PIL.Image): Das QR-Code-Bild.
    """

    def close_window(event):
        window.destroy()

    window = tk.Tk()
    window.title("QR-Code")

    # Konvertiere das PIL-Image in ein PhotoImage für Tkinter
    photo = ImageTk.PhotoImage(img)  # Vereinfachte Syntax

    label = tk.Label(window, image=photo)
    label.pack()
    window.bind("<q>", close_window)
    window.bind("<Escape>", close_window)
    window.bind("<Return>", close_window)

    window.mainloop()


if __name__ == '__main__':
    # Beispielaufruf
    url = "https://www.example.com"
    qr_img = generate_qr_code(url)
    show_qr_code_in_tkinter(qr_img)
