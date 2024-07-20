import os
from PIL import Image

# Pfad zu deinem Hauptordner
main_folder = 'assets'

def convert_png_to_jpg(folder):
    # Durchlaufe alle Dateien und Unterordner im angegebenen Ordner
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Prüfe, ob die Datei eine PNG-Datei ist
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                try:
                    # Öffne das Bild
                    with Image.open(file_path) as img:
                        # Konvertiere das Bild zu RGB (PNG kann Transparenzen haben, JPG nicht)
                        img = img.convert('RGB')
                        # Definiere den neuen Dateipfad
                        new_file_path = os.path.splitext(file_path)[0] + '.jpg'
                        # Speichere das Bild als JPG
                        img.save(new_file_path, 'JPEG')
                        print(f"Bild {file_path} wurde zu {new_file_path} konvertiert.")
                except Exception as e:
                    print(f"Fehler beim Verarbeiten von {file_path}: {e}")

# Starte die Konvertierung
convert_png_to_jpg(main_folder)