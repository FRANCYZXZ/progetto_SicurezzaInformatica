import os
from config import FOLDER_SEEDS

def extract_entropy(audio_samples):
    """
    Estrae entropia dai campioni audio selezionando il bit meno significativo di ciascun sample

    Args:
        audio_samples: campioni audio (int16)

    Returns:
        bytearray: bytes derivati dall'entropia, pronti per l'hash
    """
    lsb_bits = [sample & 1 for sample in audio_samples]                       # sample & 1 restituisce 0 se il numero è pari, 1 se dispari
    bitstring = ''.join(str(bit) for bit in lsb_bits)                         # Converte la lista di bit in una stringa binaria
    byte_chunks = [bitstring[i:i+8] for i in range(0, len(bitstring), 8)]     # Divide la stringa binaria in gruppi di 8 bit
    byte_array = bytearray(int(b, 2) for b in byte_chunks if len(b) == 8)     # Converte ciascun gruppo di 8 bit in un intero
    return byte_array

def save_seed(seed_bytes, timestamp):
    """
    Salva il seed crittografico calcolato (hash) in un file .txt

    Args:
        seed_bytes: hash del seed
        timestamp: identificativo legato alla registrazione

    Returns:
        str: percorso del file seed generato
    """
    os.makedirs(FOLDER_SEEDS, exist_ok=True)
    filename = os.path.join(FOLDER_SEEDS, f"seed_{timestamp}.txt")
    
    with open(filename, "w") as f:
        f.write(seed_bytes.hex())

    print(f"Seed salvato in: {filename}")
    return filename
