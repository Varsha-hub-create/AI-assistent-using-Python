import speech_recognition as sr

def Speech_to_text():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source)
            voice_data = r.recognize_google(audio)
            print("Recognized:", voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
            return "Unknown"
        except sr.RequestError:
            print("Error connecting to the speech recognition service.")
            return "Error"


Speech_to_text()
   