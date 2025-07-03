import time
import secrets
import json
import os
from algorithm import get_cipher
from config import CIPHER_MODE, BENCHMARKS_DIR, TIMESTAMP

def run_benchmarks():
    key = secrets.token_bytes(32)
    password = "test_password_to_encrypt"
    results = benchmark_ciphers(key, password, iterations=1000)
    for mode, avg_time in results.items():
        print(f"Modalità {mode}: tempo medio cifratura = {avg_time*1000:.5f} ms")

    os.makedirs(BENCHMARKS_DIR, exist_ok=True)

    # Converti i tempi in ms e arrotonda a 5 decimali
    results_ms = {mode: round(avg_time * 1000, 5) for mode, avg_time in results.items()}

    with open(os.path.join(BENCHMARKS_DIR, f"benchmark_results_{TIMESTAMP}.json"), "w") as f:
        json.dump(results_ms, f, indent=4)

    print(f"Risultati salvati in 'benchmark_results_{TIMESTAMP}.json'")


def benchmark_ciphers(key, password, modes_to_test=None, iterations=1000):
    """
    Esegue il benchmark della cifratura per le modalità specificate

    Args:
        key: la chiave di cifratura (deve avere lunghezza corretta per AES/ChaCha20)
        password: il testo da cifrare
        modes_to_test: lista delle modalità da testare, es. ["CBC", "GCM", ...]. Se None, usa tutte le modalità supportate
        iterations: numero di ripetizioni per mediare il tempo

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
        for _ in range(iterations):
            _, _, _ = get_cipher(key, password)
        end = time.perf_counter()

        avg_time = (end - start) / iterations
        results[mode] = avg_time

    return results
