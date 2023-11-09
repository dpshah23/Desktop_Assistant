import pyttsx3
def speak(content):
    engine=pyttsx3.init()
    engine.setProperty('voice','en-us')
    engine.setProperty('rate', 150)
    engine.say(content)
    engine.runAndWait()
    engine.stop()

