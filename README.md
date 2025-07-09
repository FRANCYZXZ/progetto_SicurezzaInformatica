# Audio-Based Cryptographic Seeding and Encryption

Questo progetto permette di generare una chiave crittografica casuale a partire da una registrazione audio, cifrare password con diverse modalità e (opzionalmente) misurare le performance di cifratura.

## Funzionalità principali

- **Registrazione audio**: acquisisce campioni audio dal microfono.
- **Estrazione entropia**: estrae il bit meno significativo di ogni campione audio per generare dati casuali.
- **Derivazione della chiave**: utilizza HKDF (basato su SHA256) per derivare una chiave crittografica dal seed.
- **Cifratura password**: cifra una password in input con una modalità selezionabile tra:
  - AES (CBC, CFB, OFB, CTR, GCM)
  - ChaCha20
- **Benchmark (opzionale)**: confronta i tempi medi di cifratura per tutte le modalità supportate.

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
CIPHER_MODE = "CTR"       # modalità di cifratura
```

## Uso

Eseguire il programma principale

```
python main.py
```

Verrà richiesto di inserire una password da cifrare; il programma registrerà audio, estrarrà il seed, e salverà password cifrata, seed e audio.

## Struttura del progetto

- audio.py: gestione registrazione e salvataggio audio.
- seed.py: estrazione entropia e salvataggio seed.
- algorithm.py: derivazione della chiave (HKDF) e funzioni di cifratura.
- cipher.py: cifratura password e salvataggio.
- benchmark.py: funzioni di benchmark.
- config.py: configurazioni e parametri globali.
- main.py: script principale.
