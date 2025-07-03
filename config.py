import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FOLDER_RECORDINGS = os.path.join(BASE_DIR, "recordings")
FOLDER_SEEDS = os.path.join(BASE_DIR, "seeds")
FOLDER_CIPHERS = os.path.join(BASE_DIR, "ciphers")

DURATION = 5                 # Durata registrazione in secondi
SAMPLERATE = 44100           # Frequenza di campionamento in Hz    
CHANNELS = 1                 # numero di canali audio (mono)

SEED_HASH_ALGORITHM = "md5"  # Algoritmo hash per il seed. Possibili valori: "sha256", "md5"
CIPHER_MODE = "CTR"          # Modalità di cifratura