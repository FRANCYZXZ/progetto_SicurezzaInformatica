import hashlib
import secrets
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from config import CIPHER_MODE

def derive_key_from_seed(seed):
    """
    Deriva una chiave crittografica da un seed usando HKDF con SHA256

    Args:
        seed: dati sorgente (entropia da audio)

    Returns:
        bytes: chiave a 32 byte derivata dal seed
    """
    hkdf = HKDF(
        algorithm = hashes.SHA256(),
        length = 32,             
        salt = None,             # Si può specificare un salt opzionale per aumentare la sicurezza
        info = b'encryption',    # Informazioni opzionali per contestualizzare la chiave
        backend = default_backend()
    )
    return hkdf.derive(seed)

def get_cipher(key, password, mode=None):
    """
    Cifra una password utilizzando la chiave fornita e la modalità di cifratura specificata

    Args:
        key: chiave simmetrica per la cifratura
        password: testo in chiaro da cifrare
        mode: modalità di cifratura da utilizzare. Se None, usa la modalità di default definita nel file config.py

    Returns:
        tuple(ciphertext, iv, mode): ciphertext esadecimale, iv o nonce esadecimale, mode modalità usata

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
