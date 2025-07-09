import os
from datetime import datetime

FOLDER_BASE = os.path.dirname(os.path.abspath(__file__))

FOLDER_RECORDINGS = os.path.join(FOLDER_BASE, "recordings")
FOLDER_SEEDS = os.path.join(FOLDER_BASE, "seeds")
FOLDER_CIPHERS = os.path.join(FOLDER_BASE, "ciphers")
FOLDER_BENCHMARKS = os.path.join(FOLDER_BASE, "benchmarks")

ITERATIONS = 1000            # Numero di iterazioni per il benchmark

DURATION = 1                 # Durata registrazione in secondi
SAMPLERATE = 44100           # Frequenza di campionamento in Hz    
CHANNELS = 1                 # numero di canali audio (mono)

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

CIPHER_MODE = "CTR"          # Modalità di cifratura, possibili valori: "CBC", "CFB", "OFB", "CTR", "GCM", "CHACHA20"