import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set Mark voice
voices = engine.getProperty('voices')
engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM")  # Set to Mark voice

def speak(text, customSpeed: int = 195):
    engine.setProperty('rate', customSpeed)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def stop_speaking():
    engine.stop()
    engine.endLoop()

def validate():
   try:
        speak("Hello there! This is Ren doing a System Check...")
        return True, None
   except Exception as e:
        return False, e

