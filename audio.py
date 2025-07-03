import sounddevice as sd
import wave
import os
import datetime
from config import FOLDER_RECORDINGS, DURATION, SAMPLERATE, CHANNELS

def record_audio():
    """
    Registra audio dal microfono

    Returns:
        numpy.ndarray: array monodimensionale dei campioni audio (int16)
    """
    print("Registrazione in corso...")
    audio = sd.rec(int(DURATION * SAMPLERATE), SAMPLERATE, CHANNELS, dtype='int16')
    sd.wait()
    print("Registrazione terminata")
    return audio.flatten()

def save_audio(audio_samples):
    """
    Salva i campioni audio in formato WAV nella cartella registrazioni

    Args:
        audio_samples: campioni audio da salvare
        
    Returns:
        timestamp
    """
    os.makedirs(FOLDER_RECORDINGS, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(FOLDER_RECORDINGS, f"registrazione_{timestamp}.wav")
    
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLERATE)
        wf.writeframes(audio_samples.tobytes())

    print(f"Audio salvato in: {filename}")
    return timestamp
