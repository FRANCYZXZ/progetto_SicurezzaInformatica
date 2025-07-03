# Audio-Based Cryptographic Seeding and Encryption

Questo progetto permette di generare una chiave crittografica casuale a partire da una registrazione audio, cifrare password con diverse modalità e misurare le performance di cifratura.

## Funzionalità principali

- Registrazione audio: acquisisce campioni audio dal microfono.
- Estrazione entropia: estrae il bit meno significativo di ogni campione audio per generare dati casuali.
- Generazione seed: applica un algoritmo di hash (SHA256 o MD5) per creare un seed crittografico.
- Cifratura password: cifra password in input con diverse modalità (CBC, CFB, OFB, CTR, GCM, CHACHA20).
- Benchmark: confronta i tempi medi di cifratura per le modalità supportate.
 
## Requisiti

- Python 3.8+
- Librerie Python:
  
```
sounddevice
numpy
cryptography
```

- (Opzionale) si consiglia l'uso di un ambiente virtuale Python.

### Installazione dipendenze

```
pip install -r requirements.txt
```

## Configurazione

Imposta i parametri principali nel file config.py, ad esempio:

```
DURATION = 5              # durata registrazione in secondi
SAMPLERATE = 44100        # frequenza di campionamento
CHANNELS = 1              # numero di canali audio (mono)
SEED_HASH_ALGORITHM = "sha256"   # algoritmo hash per il seed ("sha256" o "md5")
CIPHER_MODE = "CTR"       # modalità di cifratura
```

## Uso

1. Eseguire il programma principale

```
python main.py
```

Verrà richiesto di inserire una password da cifrare; il programma registrerà audio, estrarrà il seed, e salverà password cifrata, seed e audio.

2. Eseguire i benchmark

```
python main.py test
```

I risultati vengono salvati automaticamente in un file JSON nella cartella `benchmarks/`.


## Struttura del progetto

- audio.py: gestione registrazione e salvataggio audio.
- seed.py: estrazione entropia e salvataggio seed.
- algorithm.py: funzioni di hashing e cifratura.
- cipher.py: cifratura password e salvataggio.
- benchmark.py: funzioni di benchmark.
- config.py: configurazioni e parametri globali.
- main.py: script principale e entrypoint.
