import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import weather as wt
import urllib.request as urec
import tasks as ts
import time
import pyautogui
import worldtime as wt
import jokes as jk
found=0

# List Of MicroSoft Application
mapps={'calculator':'calc','calender':'outlookcal:','clock':'ms-clock:','paint':'mspaint','notepad':  'notepad','wordpad':'wordpad','excel':'excel','powerpoint':'powerpnt','word':'winword'}

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
            r.phrase_threshold=0.01
            audio=r.listen(source)
            try:
                print("Recognizing......")
                speak("Recognizing......")  #it analyze recorded voice through our microphone
                  
                query=r.recognize_google(audio,language='en-in')
                print(f"User Said {query}")
                return query
            except sr.UnknownValueError:
                  print("Sorry, I could not understand what you said.")
                  speak("Sorry, I could not understand what you said.")

            except sr.RequestError as e:
                  print(f"Could not request results from Google Speech Recognition service; {e}")
                  speak("Could not request results from Google Speech Recognition service. Please check your internet connection.")
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

else:
      print("Internet Connection Required")   

try:
      
      while True:
      
            
              text=take()
              
              
              if "open youtube".lower() in text.lower():
                    speak("Opening Youtube..")
                    webbrowser.open("https://www.youtube.com/")
                    time.sleep(6)
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    speak("Speak Thing to search")
                    query=take()
                    pyautogui.write(query)
                    pyautogui.press('enter')


                    
              elif "open google".lower() in text.lower():
                    speak("Opening Google...")
                    webbrowser.open("https://www.google.com/")
                    time.sleep(10)

                    speak("Speak To Search.........")
                    query=take()
                    pyautogui.write(query)
                    pyautogui.press('enter')

                    
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

              elif "open Gmail".lower() in text.lower():
                    speak("Opening Gmail")
                    webbrowser.open('https://mail.google.com/')

              elif "open notes".lower() in text.lower():
                    speak("Opening Notes")
                    os.system("start onenote")

              
              elif 'open'.lower() in text.lower():
                    keys=mapps.keys()
                   #   search="open "
                   #   startindex=text.lower().find(search)
                   #   appsearch=text[startindex+len(search):].strip
                    search="open "
                    appsearch1=text.strip(search)
                    appsearch=appsearch1.lower()
                    print(appsearch)
                    for key in keys:
                       if appsearch==key:
                             os.system(f"start {mapps[key]}")
                             speak(f"Opening {key}")
                             found=1
                             if appsearch != ('calculator' or 'calender'):
                                 speak("Do You Want to create New File..")
                                 choice=input("Enter Your choice:")
                                 if "yes".lower() in choice.lower():
                                    time.sleep(2)
                                    pyautogui.hotkey('ctrl','n')
                                    break
                                 else:
                                   break
                                 
      
                                   

                             
                    else:
                        pass
                       
                    if found==0:
                          speak("App Not Found")
                             
                          

              elif 'create new folder'.lower() in text.lower():
                    speak("What is name of folder")
                    data=take()
                    os.system(f'mkdir {data}')
                    
                          

              elif "exit".lower() in text.lower():
                    speak(f"Thanks {name} for visiting Our Desktop Assistant.....")
                    break
             
              elif "Live Cricket Score".lower() in text.lower():
                    speak("Opening Browser......")
                    webbrowser.open("https://crex.live/")

              elif "what is time in ".lower() in text.lower():
                    search="what is time in "
                    startindex=text.lower().find(search)
                    city=text[startindex+len(search):].strip()
                    speak("fetching Data ")

                    wt.worldtime(city)

              elif "new tab".lower() in text.lower():
                    speak("Opening New Tab")
                    pyautogui.hotkey('ctrl','n')   

              elif "New incognito tab".lower() in text.lower():
                    speak("Opening New Incognito Tab")
                    pyautogui.hotkey('ctrl','shift','n')

              elif "Close This Tab".lower() in text.lower():
                    speak("Closing Tab")
                    pyautogui.hotkey('ctrl','w')

              elif "Create New Tab".lower() in text.lower():
                    speak("Opening New Tab")
                    pyautogui.hotkey('ctrl','t')

              elif "open new window".lower() in text.lower():
                    speak("Opening New Window")
                    pyautogui.hotkey('ctrl','shift','n')
           

              elif "Go to next Tab".lower() in text.lower():
                    pyautogui.hotkey('ctrl','tab')  


              elif "Close this app".lower() in text.lower():
                    pyautogui.hotkey('alt','f4')

              elif "right".lower() or "write".lower()  in text.lower():
                    speak("Speak To Write")
                    writetext=take()
                    pyautogui.write(writetext)

              elif "tell me a joke".lower() in text.lower():
                    jk.joke()
            
              elif "one more".lower() in text.lower():
                    jk.joke()
                    

              else:
                    print("It's Out of my knowledge")
                    speak("It's Out of my knowledge")



                

              
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
      