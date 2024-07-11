from speech_recognition import Recognizer, Microphone
import distutils
import os
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\Users\Admin\Downloads\OCCT.config.json'


r = Recognizer()

with Microphone() as source:
    print('in ascolto...')
    audio = r.listen(source)
    testo = r.recognize_google_cloud(audio)
    print(testo)