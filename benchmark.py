import time
import secrets
import json
import os
from algorithm import get_cipher
from config import CIPHER_MODE, FOLDER_BENCHMARKS, TIMESTAMP, ITERATIONS

def run_benchmarks(key, password):
    """
    Esegue il benchmark comparativo delle prestazioni dei vari algoritmi di cifratura

    - Esegue un numero prefissato di iterazioni di cifratura per ciascuna modalità specificata
    - Calcola il tempo medio di cifratura per ogni modalità in millisecondi
    - Salva i risultati in un file formato JSON all'interno della cartella 'benchmarks'
    """
    results = benchmark_ciphers(key, password, modes_to_test=None)
    os.makedirs(FOLDER_BENCHMARKS, exist_ok=True)

    # Converti i tempi in ms e arrotonda a 5 decimali
    results_ms = {mode: round(avg_time * 1000, 5) for mode, avg_time in results.items()}

    with open(os.path.join(FOLDER_BENCHMARKS, f"benchmark_results_{TIMESTAMP}.json"), "w") as f:
        json.dump(results_ms, f, indent=4)

    print(f"Risultati salvati in 'benchmark_results_{TIMESTAMP}.json'")

def benchmark_ciphers(key, password, modes_to_test=None):
    """
    Esegue il benchmark della cifratura per le modalità specificate

    Args:
        key: la chiave di cifratura (deve avere lunghezza corretta per AES/ChaCha20)
        password: il testo da cifrare
        modes_to_test: lista delle modalità da testare, es. ["CBC", "GCM", ...]. Se None, usa tutte le modalità supportate

    Returns:
        dict: {mode_name: avg_time_in_seconds}
    """
    if modes_to_test is None:
        modes_to_test = ["CBC", "CFB", "OFB", "CTR", "GCM", "CHACHA20"]

    results = {}
    global CIPHER_MODE  # Per sovrascrivere temporaneamente la modalità usata in get_cipher

    for mode in modes_to_test:
        CIPHER_MODE = mode  # Setto la modalità globale temporaneamente

        # Misuro il tempo totale di 'iterations' cifrature
        start = time.perf_counter()
        for _ in range(ITERATIONS):
            _, _, _ = get_cipher(key, password)
        end = time.perf_counter()

        avg_time = (end - start) / ITERATIONS
        results[mode] = avg_time

    return results
