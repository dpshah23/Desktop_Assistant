import pyttsx3
def speak(content):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice','en-us')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(content)
    engine.runAndWait()
    engine.stop()

