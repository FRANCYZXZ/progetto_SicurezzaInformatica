from audio import record_audio, save_audio
from seed import extract_entropy, save_seed
from cipher import encrypt_password
from algorithm import derive_key_from_seed

def main():
    """
    Script principale che coordina la registrazione audio, l'estrazione del seed, la generazione della chiave di cifratura,
    la cifratura della password e il salvataggio dei relativi file
    """
    samples = record_audio()
    timestamp = save_audio(samples)

    seed = extract_entropy(samples)
    save_seed(seed, timestamp)

    key = derive_key_from_seed(seed)

    password = input("Inserisci la password da cifrare: ")

    encrypt_password(key, password, timestamp)

if __name__ == "__main__":
    main()
