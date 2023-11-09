import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import weather as wt
import urllib.request as urec
import tasks as ts
import time
#Checking For is User Connected To Internet Or Not
def check_conn():
      host="https://www.google.com/"
      try:
            urec.urlopen(host)   
            return True
            
      except:
            return False
      

# it will Convert text to speech
def speak(content):
    engine=pyttsx3.init()
    engine.setProperty('voice','en-us')
    engine.setProperty('rate', 150)
    engine.say(content)
    engine.runAndWait()
    engine.stop()

# It will convert speech To text OR Taking input from Our Microphone
def take():
      
      r=sr.Recognizer()
      with sr.Microphone() as source:
            print("Listening...........")
            speak("listening...........")
            
            r.adjust_for_ambient_noise(source, duration=0.1)      #Adjust For noice Cancellation
            r.pause_threshold=1
            r.energy_threshold=250
            r.phrase_threshold=0.1
            audio=r.listen(source)
            try:
                print("Recognizing......")
                speak("Recognizing......")  #it analyze recorded voice through our microphone
                  
                query=r.recognize_google(audio,language='en-in')
                print(f"User Said {query}")
                return query
            except Exception as e:
                  print(f"Error Occured {e}")

# It will wish According To System Time
def wish(name):
       current_time = datetime.datetime.now().time()
    
       if current_time >= datetime.time(6, 0) and current_time <= datetime.time(12, 0):
            msg=f"Good Moring {name}"
            print(f"Good Morning {name}")
            speak(msg)
    
       elif current_time > datetime.time(12, 0) and current_time <= datetime.time(18, 0):
            msg=f"Good Afternoon {name}"
            print(f"Good Afternoon {name}")
            speak(msg)
    
       else:
            msg=f"Good Evening {name}"
            print(f"Good Evening {name}")
            speak(msg)

var=check_conn()
# It Will Get Input Of Name If name.txt file does not exist and save it to it for future refrence
if var==True:
      file_exists=os.path.exists('name.txt')
      if file_exists:
            with open('name.txt','r') as f:
                    name=f.read()
                    wish(name)

      else:
            with open('name.txt','w') as f:
                      names=input("What is Your Good Name?")
                      
                      f.write(names)
                      wish(names)

try:
      
      while True:
      
            
              text=take()
              
              
              if "open youtube".lower() in text.lower():
                    speak("Opening Youtube..")
                    webbrowser.open("https://www.youtube.com/")
                    
              elif "open google".lower() in text.lower():
                    speak("Opening Google...")
                    webbrowser.open("https://www.google.com/")
             
              elif "search".lower() in text.lower():
                    speak("Opening Browser...")
                    que=text.split('search')

                    webbrowser.open(f"https://www.google.com/search?q={que[1]}")

              elif "wikipedia ".lower() in text.lower():
                    speak("Opening Wikipedia....")
                    search="wikipedia "
                    startindex=text.lower().find(search)
                    res=text[startindex+len(search):].strip()
                    
                    webbrowser.open(f"https://en.wikipedia.org/wiki/{res}")
                    
              elif "hello".lower() in text.lower():
                    speak("Hello! How Are You?")

              

              elif "What is weather in ".lower() in text.lower():
                    search="what is weather in "
                    startindex=text.lower().find(search)
                    location=text[startindex+len(search):].strip()
                    print(location)
                    op=wt.weather(location)
                  
                 
                    speak(f"Location : {op[0]}")
                    speak(f"Condition : {op[1]}")
                    speak(f"Temprature : {op[2]} degree Celsius")

             #   elif "open Calculator".lower() in text.lower():
             #         speak("Opening Calculator.......")
             #         os.system('cmd /k "calc"')

              elif "Create new task".lower() in text.lower():
                    speak("Creating New Task")
                    speak("Enter Task Name")
                    task_nm=take()
                    speak("Enter Task Date")
                    date=take()
                    ts.createtask(task_nm,date)
                    speak(f"Task Created.... Title : {task_nm} and date : {date}")

              elif "Print Task".lower() in text.lower():
                    
                    speak("List Of Tasks")
                    with open("task.csv", mode='r') as file:
                        tasks = file.read()
                        print(tasks)

                    file.close()
              elif "mark done task".lower() in text.lower():
                    speak("Marking Done Tasks")
                    speak("Enter Task Name To Mark Done")
                    tasknm=take()
                    speak("Enter Task Date To Mark Done")
                    date=take()
                    ts.markdone(tasknm,date)
                    
                          

              elif "exit".lower() in text.lower():
                    speak(f"Thanks {name} for visiting Our Desktop Assistant.....")
                    break
      else:
            print("Internet Connection Required")             

except ValueError:
        speak("Enter Valid Input")
       
except IndexError:
        speak("Nothing To print.....")

except NameError:
        speak("Invalid Input")
except TypeError:
        speak("Invalid Input")

except FileNotFoundError:
        speak("file not found")

except KeyboardInterrupt:
      speak("\nKeyboard interrupted. Exiting...")
      
except SystemExit:
      speak("Error Occured")
     
except Exception as e:
      
      print(f"Error Occured {e}")
      exit
