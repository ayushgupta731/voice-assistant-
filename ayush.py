import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 

print(voices[1].id)    # to know , which voice is there boy or girl ;1-- girl , 0 -boy
engine.setProperty('voice',voices[1].id)   #set voice 

def speak(audio): # speak
    #pass
    engine.say(audio)
    engine.runAndWait()

def wishme(): #c
 global samay             #we have to define hour globally , otherwise we will get erro
samay=int(datetime.datetime.now( ).hour)
if samay>=0 and samay<12:
 speak ("Good morning!")
elif samay>=12 and samay<16:
     speak ("Good afternoon")
else:
     speak ("Good evening")
    
speak("Ayush sir , I am jarvis , how can I help you ")

#speak ("Mai zira hu , mai aapkii kaisee madad kar sakati hoon")

def takecommand(): 
 global r
 r = sr.Recognizer()
 with sr.Microphone() as source:
    global audio
    global query
    print("Listening .....") 
    r.pause_threshold = 1
    audio = r.listen(source)
   
 try:
  print("Recognizing...") 
  query = r.recognize_google(audio)
  query = query.lower()
  print(f"User said: {query}\n")
  return query
 except Exception as e:
        # print(e)
      print("Say that again please...")
 return "None"
  
def sendemail(to,content): 
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.ehlo()
 server.starttls()
 server.login('youremail@gmail.com','your-passsword')   #insert email id and password 
 server.sendmail('youremail@gmail.com',to,content)      #insert mail id
 server.close()


if __name__== "__main__":
    wishme() 
while True:
 query = takecommand()
    #logic for executing tasks based on query
  

 if 'wikipedia' in query:
  speak ('Searching wikipedia....')
  query = query.replace("wikipedia","")
  results = wikipedia.summary(query,sentences = 2)         # 2 means number of sentences that is to be read from wikipedia 
  speak("According to wikipedia ")
  print(results)
  speak (results)

 if 'shivam' in query:
        query = 'saurabh mishra and shivam sourav'
        speak('searching about %s' %query) 
        results = 'are two friends of ayush gupta'
        print('%s %s' %(query ,results ))
        speak('%s %s' %(query,results) )

 elif 'open youtube' in query:
    webbrowser.open("youtube.com")
 elif 'open google' in query:
    webbrowser.open("google.com")
 elif 'geeks' in query:
    webbrowser.open("https://www.geeksforgeeks.org/")

#  elif  'play music' or 'spotify' or 'gana' in  query: 
#     webbrowser.open("spotify.com")

# { from desktop -- play music}
# elif 'play music' inquery:
#  music_dir = 'D:\\Folder_name\\foldername ....'
#  songs = os.listdir(music_dir)
#  print(songs)
#  os.startfile(os.path.join(music_dir,songs[0]))     it plays from the first song which is in list ; we can also play randomly , by using random module of python
#   os.startfile(os.path.join(music_dir,songs[k]))  --- k is a random number , which is picked from random module and it lies in between 0 to n-1 i.e. number of songs 
# ############################
# 
# 

 elif 'time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir ,the time is {strTime}")
    
 elif'movies folder' in query:
    codePath = "D:\\Movies"     #note while opening folder convert all the single slash to double slash 
    os.startfile(codePath)

 elif 'email' in query:   # we can make dictonary and give name and email id as key value pair respectively  #############
       try:
        speak("What should I say ?")
        content = takecommand()
        to = "Your email@gmail.com"
        sendemail(to,content)
        speak("Email has been sent")
       except Exception as e:
         print(e)
         speak("sorry sir , I was not able to sends eamil  ")

 elif any(x in query for x in ['band karo', 'exit']):                   #multiple condition checking by use of any function 
   speak("Ok sir , have a good day")
   exit()  


 elif 'date' in query:
    strDate = datetime.datetime.now().date()
    speak(f"Sir ,today's date is {strDate}")
 elif 'abhinay' in query:
    speak("Saumya ka pati")
  
   
