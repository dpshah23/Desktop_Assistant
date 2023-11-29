import speech_recognition as sr
import subprocess

def take():
      
      r=sr.Recognizer()
      with sr.Microphone() as source:
            
            
            r.adjust_for_ambient_noise(source, duration=0.1)      #Adjust For noice Cancellation
            r.pause_threshold=1
            r.energy_threshold=250
            r.phrase_threshold=0.01
            audio=r.listen(source)
            try:
                
                  
                query=r.recognize_google(audio,language='en-in')
                print(f"User Said {query}")
                return query
            except sr.UnknownValueError:
                  print("Sorry, I could not understand what you said.")
                  

            except sr.RequestError as e:
                  print(f"Could not request results from Google Speech Recognition service; {e}")
                  
            except Exception as e:
                  print(f"Error Occured {e}")


def main():
      while True:
            key=take()
            print(key)
            if key and "hello assistant" in key:
                  print("Running Another script")
                  subprocess.run(['python','C:/Users/dpsha/OneDrive/Desktop/DEEP/Desktop_Assistant/main.py '])
                  break
        

if __name__=="__main__":
      main()
