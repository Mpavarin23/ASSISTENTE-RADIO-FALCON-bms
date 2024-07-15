import speech_recognition as sr
import pyautogui

class Riconoscitore:
    def __init__(self):
        self.r = sr.Recognizer()
    
    def riconoscimento_vocale(self):
        with sr.Microphone() as source:
            print("In ascolto...")

            self.r.adjust_for_ambient_noise(source)

            while True:
                try:
                    audio = self.r.listen(source)
                    testo = self.r.recognize_google(audio, language="it-IT,en-US").lower()
                    print(testo)

                    if 'interrompere radio' in testo:
                        return "stop"
                    
                    return testo

                except sr.UnknownValueError:
                    print("Non sono riuscito a capire l'audio.")
                except sr.RequestError as e:
                    print(f"Errore nella richiesta a Google: {e}")
                except Exception as e:
                    print(f"Si è verificato un errore: {e}")

class Esecutore:
    def __init__(self):
        pass
    
    def reset(self):
        pyautogui.press('t')
        pyautogui.press('esc')

    def riconoscimento(self, testo):
        if 'aereoporto' in testo:
            self.reset()
            pyautogui.press('t')
        elif 'stop' in testo:
            print("Interruzione del riconoscimento vocale.")
            return False
        return True

ricevitore = Riconoscitore()
emettitore = Esecutore()

def AutoRadio():
    while True:
        testo = ricevitore.riconoscimento_vocale()
        if testo:
            if testo == "stop":
                print("Interruzione del riconoscimento vocale.")
                break
            if not emettitore.riconoscimento(testo):
                print('nessuna azione riconosciuta')

if __name__ == '__main__':
    AutoRadio()
