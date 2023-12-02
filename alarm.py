import speak as sp
import datetime
import os
from pygame import mixer

def ring(time):
    timeset = str(time)
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            sp.speak("Alarm ringing,sir")
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
        elif currenttime + "00:00:30" == Alarmtime:
            exit()



extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()
ring(time)

