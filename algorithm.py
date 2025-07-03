import hashlib
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from config import SEED_HASH_ALGORITHM, CIPHER_MODE

def select_seed_algorithm(entropy):
    """
    Applica un algoritmo di hash crittografico per generare un seed a partire da un buffer di entropia

    Args:
        entropy: dati casuali da cui derivare il seed

    Returns:
        bytes: digest hash del seed calcolato

    Raises:
        ValueError: se l'algoritmo di hash specificato in configurazione non è supportato
    """

    if SEED_HASH_ALGORITHM.lower() == "sha256":
        return hashlib.sha256(entropy).digest()
    elif SEED_HASH_ALGORITHM.lower() == "md5":
        return hashlib.md5(entropy).digest()
    else:
        raise ValueError(f"Algoritmo '{SEED_HASH_ALGORITHM}' non supportato. Scegli tra sha256 o md5")
    
def get_cipher(key, password, mode=None):
    """
    Cifra una password utilizzando la chiave fornita e la modalità di cifratura specificata

    Args:
        key: chiave simmetrica per la cifratura
        password: testo in chiaro da cifrare
        mode: modalità di cifratura da utilizzare. Se None, usa la modalità di default definita in config

    Returns:
        tuple(ciphertext, iv, mode): (ciphertext esadecimale, iv o nonce esadecimale, mode modalità usata)

    Raises:
        ValueError: se la modalità di cifratura non è supportata
    """

    if mode is None:
        mode = CIPHER_MODE.upper()
    else:
        mode = mode.upper()
    data = password.encode()

    if mode in ["CBC", "CFB", "OFB", "CTR"]:
        iv = secrets.token_bytes(16)

        if mode == "CBC":
            cipher_mode = modes.CBC(iv)
            padder = padding.PKCS7(128).padder()
            data = padder.update(data) + padder.finalize()
        elif mode == "CFB":
            cipher_mode = modes.CFB(iv)
        elif mode == "OFB":
            cipher_mode = modes.OFB(iv)
        elif mode == "CTR":
            cipher_mode = modes.CTR(iv)                      # Usato nonce non iv

        cipher = Cipher(algorithms.AES(key), cipher_mode, backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()

        return ciphertext.hex(), iv.hex(), mode

    elif mode == "GCM":
        nonce = secrets.token_bytes(12)
        cipher = AESGCM(key)
        ciphertext = cipher.encrypt(nonce, data, None)
        return ciphertext.hex(), nonce.hex(), mode

    elif mode == "CHACHA20":
        nonce = secrets.token_bytes(12)
        cipher = ChaCha20Poly1305(key)
        ciphertext = cipher.encrypt(nonce, data, None)
        return ciphertext.hex(), nonce.hex(), mode

    else:
        raise ValueError(f"Modalità '{mode}' non supportata")
