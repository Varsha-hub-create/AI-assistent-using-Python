import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data=data.lower()

    if "what is your name" in user_data:
      text_to_speech.text_to_speech("My name is virtual assistant")
      return "My name is virtual assistant"

    elif "hello" in user_data or "bye" in user_data:
      text_to_speech.text_to_speech("hey,How can help you")
      return 'hey,How can help you'

    elif "good morning" in user_data:
      text_to_speech.text_to_speech("Good Morning")
      return "Good Morning"

    elif "time now" in user_data:
      current_time=datetime.datetime.now()
      Time=(str)(current_time) + "Hour:" ,(str)(current_time.minute) + "Minute"
      text_to_speech.text_to_speech(Time)
      return Time

    elif "shutdown" in user_data:
      text_to_speech.text_to_speech("Ok Sir")
      return 'Ok Sir'

    elif "play music" in user_data:
      webbrowser.open("https://gaana.com/")
      text_to_speech.text_to_speech("gaana.com is now ready for you")
      return "gaana.com is now ready for you"

    elif "youtube" in user_data:
      webbrowser.open("https://youtube.com/")
      text_to_speech.text_to_speech("youtube.com is now ready for you")
      return "youtube.com is now ready for you"

    elif "open google" in user_data:
      webbrowser.open("https://google.com/")
      text_to_speech.text_to_speech("google.com is now ready for you")
      return "google.com is now ready for you"

    elif "weather" in user_data:
      ans= weather.weather()
      text_to_speech.text_to_speech(ans)
      return ans


    else:
      text_to_speech.text_to_speech("I'm not able to understand")
      return "I'm not able to understand"



