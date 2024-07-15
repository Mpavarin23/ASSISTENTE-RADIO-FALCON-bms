import speech_recognition as sr

def riconoscimento_vocale():
    # Crea un'istanza del riconoscitore
    r = sr.Recognizer()

    # Usa il microfono come sorgente audio
    with sr.Microphone() as source:
        print("In ascolto...")

        # Regola automaticamente il livello di riconoscimento del rumore
        r.adjust_for_ambient_noise(source)

        # Ascolta l'input audio
        audio = r.listen(source)

        try:
            # Utilizza il servizio di riconoscimento vocale di Google
            print("Riconoscimento in corso...")
            # Specifica le lingue da riconoscere (italiano e inglese)
            testo = r.recognize_google(audio, language="it-IT,en-US")
            print("Ho capito: " + testo)
        except sr.UnknownValueError:
            print("Non sono riuscito a capire l'audio")
        except sr.RequestError as e:
            print(f"Errore nella richiesta a Google: {e}")
        except Exception as e:
            print(f"Si è verificato un errore: {e}")

# Esegui la funzione di riconoscimento vocale
if __name__ == "__main__":
    riconoscimento_vocale()
