from config import FOLDER_CIPHERS
from algorithm import get_cipher
import os

def encrypt_password(key, password, timestamp):
    """
    Cifra una password usando la chiave fornita, salva il risultato su file.

    Args:
        key: chiave di cifratura simmetrica.
        password: password in chiaro da cifrare.
        timestamp: identificatore usato per nominare il file di output.

    Azioni:
        - Crea la cartella di destinazione se non esiste.
        - Esegue la cifratura chiamando get_cipher.
        - Salva su file testo la modalità usata, IV o nonce, e il ciphertext esadecimale.
        - Stampa messaggio di conferma con percorso del file salvato.
    """
    os.makedirs(FOLDER_CIPHERS, exist_ok=True)

    ciphertext_hex, iv_hex, mode = get_cipher(key, password, mode=None)

    filename = os.path.join(FOLDER_CIPHERS, f"cifrato_{timestamp}.txt")
    with open(filename, "w") as f:
        f.write(f"MODE: {mode}\n")
        f.write(f"IV/NONCE: {iv_hex}\n")
        f.write(f"CIPHERTEXT: {ciphertext_hex}\n")

    print(f"Password cifrata salvata in: ciphers/cifrato_{timestamp}.txt")
