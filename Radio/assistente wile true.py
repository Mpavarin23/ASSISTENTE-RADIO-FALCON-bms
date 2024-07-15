import speech_recognition as sr

def riconoscimento_vocale_continuo():
    # Crea un'istanza del riconoscitore
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("In ascolto...")

        # Regola automaticamente il livello di riconoscimento del rumore
        r.adjust_for_ambient_noise(source)

        while True:
            try:
               
                audio = r.listen(source)

                # Specifica le lingue da riconoscere (italiano e inglese)
                testo = r.recognize_google(audio, language="it-IT,en-US")
                print(testo)
            except sr.UnknownValueError:
                print("Non sono riuscito a capire l'audio")
            except sr.RequestError as e:
                print(f"Errore nella richiesta a Google: {e}")
            except KeyboardInterrupt:
                print("Interruzione da tastiera rilevata. Uscita dal programma.")
                break
            except Exception as e:
                print(f"Si è verificato un errore: {e}")
            
            if 'chiudere radio' in testo.lower():
                print('____HOLA MAURO_____\n;)')
                break




# Esegui la funzione di riconoscimento vocale continuo
if __name__ == "__main__":
    riconoscimento_vocale_continuo()