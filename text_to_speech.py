# import pyttsx3

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     rate = engine.getProperty('rate')  # Get current speech rate
#     engine.setProperty('rate', rate - 70)  # Decrease rate by 70
#     engine.say(text)
#     engine.runAndWait()

# text_to_speech("Hello")

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    
    # Set the speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)
    
    # Set the voice to female
    voices = engine.getProperty('voices')  # Get the list of available voices
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():  # Look for a female voice
            engine.setProperty('voice', voice.id)
            break
    else:
        print("No female voice found. Using default voice.")
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Test the function
text_to_speech("Hello, this is a female voice.")

