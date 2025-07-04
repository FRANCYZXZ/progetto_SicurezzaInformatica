from config import FOLDER_CIPHERS
from benchmark import run_benchmarks
from algorithm import get_cipher
import os

def encrypt_password(key, password, timestamp, do_benchmark=False):
    """
    Cifra la password usando la chiave fornita, salva il risultato nella cartella ciphers e (opzionalmente) esegue un benchmark delle modalità di cifratura.

    Args:
        key: chiave di cifratura simmetrica
        password: password in chiaro da cifrare
        timestamp: identificatore usato per nominare il file di output
        do_benchmark: se True, esegue benchmark comparativo delle modalità di cifratura

    Azioni:
        - Crea la cartella di destinazione se non esiste
        - Esegue la cifratura chiamando get_cipher
        - Salva su file testo la modalità usata, IV o nonce, e il ciphertext esadecimale
        - Se richiesto, esegue il benchmark e salva i risultati in formato JSON
        - Stampa messaggio di conferma con percorso del file salvato
    """
    os.makedirs(FOLDER_CIPHERS, exist_ok=True)

    ciphertext_hex, iv_hex, mode = get_cipher(key, password, mode=None)

    if do_benchmark:
        run_benchmarks(key, password)

    filename = os.path.join(FOLDER_CIPHERS, f"cifrato_{timestamp}.txt")
    with open(filename, "w") as f:
        f.write(f"MODE: {mode}\n")
        f.write(f"IV/NONCE: {iv_hex}\n")
        f.write(f"CIPHERTEXT: {ciphertext_hex}\n")

    print(f"Password cifrata salvata in: ciphers/cifrato_{timestamp}.txt")
