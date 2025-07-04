from audio import record_audio, save_audio
from seed import extract_entropy, save_seed
from cipher import encrypt_password
from algorithm import select_seed_algorithm

def main():
    """
    Script principale che coordina la registrazione audio, l'estrazione del seed,
    la cifratura della password e il salvataggio dei relativi file
    """
    
    samples = record_audio()
    timestamp = save_audio(samples)

    entropy = extract_entropy(samples)
    seed = select_seed_algorithm(entropy)

    save_seed(seed, timestamp)

    password = input("Inserisci la password da cifrare: ")

    encrypt_password(seed, password, timestamp)

if __name__ == "__main__":
    main()
