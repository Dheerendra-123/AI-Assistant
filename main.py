
import os
from time import sleep
from urllib.request import urlopen
import pyttsx3
import speech_recognition as sr
import datetime
import pyautogui
import pyjokes
import wolframalpha
from keyboard import press_and_release
import keyboard
import webbrowser
import requests
import pywhatkit
from googletrans import Translator
from pywikihow import search_wikihow
import wikipedia
from win10toast import ToastNotifier
from PIL import Image 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)
def Speak(audio):   
    print("    ")   
    print(f":{audio}")    
    engine.say(audio)
    engine.runAndWait()
    print(" ")
  
    
      
ToastNotifier().show_toast("Ruby is now activated")
# os.startfile('C:\\Users\\HP\\My AI assistant\\aiGui.py')
Speak("Activated")
Speak("hello sir!")  
Speak("how can i help you?") 


def TakeCommand(audio):
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print(":listening.....")
        print("\n") 
        r.pause_threshold = 0.5
        
        audio=r.listen(source)
        
    try:
        
        print(":Recognizing...") 
        query=r.recognize_google(audio,language='en-in')
        
        print(f": Your Command:{query}\n")
    except:   
        return "none"
    return query.lower() 



def TaskExe():

    
    
    while True:
        query=TakeCommand('audio')
         
        if 'google search' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            import wikipedia as googleScrap
            query=query.replace("ruby","")
            query=query.replace("google search","")
            query=query.replace("google","")
            Speak("According to google search.")
            
            try:
                pywhatkit.search(query)
                result=googleScrap.summary(query,3)
                Speak(result)
            except:
                Speak("no speakable data available")
                
        elif 'current time' in query or 'what is the time' in query or 'kitna time hua hai' in query or 'what is time now' in query or 'kitna time hua hai' in query or 'time' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            strTime = datetime.datetime.now().strftime("%H:%S %p")
            print(f"\n\tit is {strTime}")
            Speak(f"Sir the time is: {strTime}")
                                
                      
            
        elif 'youtube search' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Searching ,sir")
            Query = query.replace("ruby","")
            query = Query.replace("youtube search","")
            from features import YouTubeSearch
            YouTubeSearch(query) 
            
        elif 'translater' in query or 'tranlater kholo' in query or 'translate' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("opening....")
            from features import Tran
            Tran()  
            
        elif 'what is' in query or 'mera name kya hai' in query or 'mera naam kya hai' in query or 'mera nam batao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("your name is Dheerendra Dixit ,Sir.")
            
        elif 'what is your' in query or 'tumhara naam kya hai' in query or 'what ise your name?' in query or 'apna naam batao' in query:   
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("My name is ruby ,Sir.")      
        
        elif 'open youtube' in query or 'youtube kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("opening....")
            Speak("opening youtube")
            webbrowser.open('https://www.youtube.com')
            sleep(3)
            from automations import YouTubeAuto
            query=query.replace('youtube','')
            YouTubeAuto(query) 
           
            
        elif 'open chrome' in query or 'chrome kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("opening....")
            Speak("opening chrome")
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            sleep(3)
            from automations import ChromeAuto
            query = query.replace('chrome', '')
            ChromeAuto(query) 
            
        elif 'open brave' in query or 'brave kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening brave")
            os.startfile('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe') 
            
        elif 'close chrome' in query or 'chrome band karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("closing chrome")
            os.system("TASKKILL /F /im chrome.exe")
             
            
        elif 'close brave' in query or 'brave band karo' in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay,sir") 
            os.system("TASKKILL /F /im brave.exe")   
            
        elif 'open file explorer' in query or 'file explorer kholo' in query:
            Speak("okay ,sir")
            press_and_release('windows + E')
            
        elif 'open settings' in query or 'settings kholo' in query:
            press_and_release('windows + I')
            Speak("okay ,sir")
        elif 'lock window' in query or 'window lock kardo' in query:  
            press_and_release('windows + L')      
            Speak("okay ,sir") 
            
        elif 'open my sql' in query or 'my sql kholo' in query or 'my sql' in query : 
            Speak("okay ,sir") 
            os.stratfile("C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe") 
            
        elif 'take screenshot' in query or 'screenshot lo' in query or 'screenshot' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            press_and_release("windows + PrtScn")    
            os.startfile('C:\\Users\HP\\Pictures\\Screenshots')
            sleep(3)
            os.close('C:\\Users\HP\\Pictures\\Screenshots')
        elif 'open microsoft excel' in query or 'microsoft excel kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening....")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')   
            
        elif 'microsoft word kholo' in query or 'open microsoft word' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening....")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007') 
            
        elif 'open this pc' in query or 'this pc kholo' in query or 'this pc' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak('okay,sir')
            press_and_release('windows+E')
            sleep(1)
            pyautogui.click(x=202, y=434)
            
        elif 'open amazon' in query or 'amazon open' in query or 'amazon' in query:
            Speak("opening amazon.com...")
            open.url=('http://www.amazon.com')
            
        elif 'open flipkart' in query or 'flipkart open' in query or 'flipkart' in query:
            Speak("opening amazon.com...")
            open.url=('http://www.flipkart.com')          
            
        elif 'open pycharm' in query or 'py charm kholo' in query:
            os.startfile('D:\\PyCharm\\PyCharm 2023.2.3\\bin\\pycharm64.exe')
            
        elif 'open command prompt' in query or 'command prompt kholo' in query:
            os.startfile('C:\\Windows\\system32\\cmd.exe')     
            
        elif 'open apache' in query or 'apache' in query:
            os.startfile('C:\\Program Files\\NetBeans-18\\netbeans\\bin\\netbeans64.exe')  
            
        elif 'open mangodb' in query or 'mangodb' in query:
            os.startfile('C:\\Users\\HP\\AppData\\Local\\MongoDBCompass\\MongoDBCompass.exe')       
                
            
        elif 'open power point' in query or 'power point kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening....")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007')    
        
             
        elif 'speed test' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("opening ,sir")
            Speak("opening speed test")
            from features import SpeedTest
            SpeedTest()
          
        elif 'temperature' in query or 'temperature kya hai' in query or 'tapman kaisa hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from features import temp
            temp(query)
            
        elif 'weather in' in query or "today's weather in" in query or "what is today's weather in" in query or 'aaj ka weather kaisa hai' in query or 'aaj mausam kaisa hai' in query or 'kaisa mausam hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            query=query.replace('weather in','')
            query=query.replace('in','')
            query=query.replace("what is today's weather in",'')
            query=query.replace("today's weather in",'')
            query=query.replace("me",'')
            query=query.replace("mein",'')
            query=query.replace("aaj ka weather kaisa hai",'')
            query=query.replace("aaj mausam kaisa hai",'')
            url='https://wttr.in/{}'.format(query)
            Speak(f"you can see the data for the weather in {query}")
            res=requests.get(url)
            print(res.text)   
          
                
        
        elif "calculate" in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()  
            app_id = "6X5GUL-WUH3JHJAR9"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            Speak("The answer is " + answer)  
             
            
            
        elif "what is" in query or 'kya hota hai' in query or 'who is' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            query=query.replace("kya hota hai",'')
            query=query.replace("kaun hai",'')
            client = wolframalpha.Client("6X5GUL-WUH3JHJAR9")
            res = client.query(query)
             
            try:
                Speak (next(res.results).text)
            except StopIteration:

                from chatbot.chatbot import Chatterbot
                reply=Chatterbot(query)
                Speak(reply)   
              
                
          
        elif 'space news' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            
            Speak("Tell me the date for news extracting process.")
            
            Date=TakeCommand('audio')
            

            
            from nasa import NasaNews
            value=input("date::-")
            NasaNews(value)
            
        elif 'mars images' in query or 'mars image' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            
            from nasa import MarsImage
            
            MarsImage()
            
        elif 'near earth' in query or 'near earth objects' in query or 'passed through earth' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            
            from nasa import Astro
            
            Speak("tell me the starting date")
            start=input("enter the starting date::")
            Speak("tell me the ending date")
            end=input("enter the ending date::")
            
            Astro(start, end)
        
        elif 'solar system' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from nasa import SolarBodies
            Speak("tell me the name of body in solar system , you want to know about.")
            bod=TakeCommand('audio')
            body=bod.replace(" ", "")
            body=body.replace(" ", "")
            Body=str(body)
            SolarBodies(body=Body)
                
        elif 'my current location' in query or 'meri location kya hai' in query or 'meri current location kya hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from features import my_location
            my_location()
          
        elif 'where is' in query or 'kaha hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from automations import google_maps
            place=query.replace("where is", "")
            place=place.replace("alex", "")
            
            google_maps(place)
           
        elif 'write a note' in query or 'note likho' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from automations import Notepad    
            Notepad()  
        
        elif 'close notepad' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("closing..")
            Speak("closing notepad")
            from automations import CloseNotepad
            
            CloseNotepad()
            
        elif 'change your voice' in query or 'apni awaj badlo' in query or 'awaj change karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay sir, i am changing my voice")
            engine.setProperty('voice', voices[1].id)
            Speak("now that is my voice ") 
            
        elif 'back to your voice' in query or 'back to your orginal voice' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay sir, i am changing my voice")
            engine.setProperty('voice', voices[0].id)
            Speak("now that is my orginal voice ")             
            
        elif 'how to' in query or 'kaise' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("getting data from internet.")
            op=query.replace("ruby","")
            max_result= 1
            how_to_func=search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
            
        elif 'website' in query :
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Ok sir,Launching...") 
            query=query.replace("ruby","")
            query=query.replace("Website", "")
            query=query.replace(" ","")
            web1=query.replace("open","")
            web2='https://wwww.'+web1+'.com'  
            webbrowser.open(web2)
            Speak("Launched!")
            
            
        elif 'wikipedia' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("searching Wikipedia....")
            query=query.replace("ruby","")
            query=query.replace("wikipidea", "")  
            wiki=wikipedia.summary(query,2)  
            Speak(f"According to Wikipedia:{wiki}")
            
    
            
        elif 'set alarm' in query or 'set the alarm' in query or 'alarm set karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Enter the time ,sir")
            time=input("Enter the time:")
            Speak(f"setting the alarm to:{time}")
            Speak("Aalarm has been set")
            
            while True:
                time_ac=datetime.datetime.now()
                now=time_ac.strftime("%H:%M")
                
                if now==time:
                    os.startfile('C:\\Users\\HP\\My AI assistant\\Database\\Sound\\1.mp3')
                    Speak("time to wake up sir")
                elif now>time:
                    Speak("Alarm Closed")
                    break
                  
            
        elif 'remember that' in query or 'yad rakho' in query or 'yad rakhna' in query or 'remember' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            remsg=query.replace("remember that","")
            remsg=query.replace("yad rakho","")
            remsg=query.replace("yad rakhna","")
            remsg=remsg.replace("ruby","")
            Speak("sir, you told me to remember this:"+remsg)
            Speak("i am storing that in my data")
            remember=open('C:\\Users\\HP\\My AI assistant\\Database\\remem.txt', 'w')
            remember.write(remsg)
            remember.close()
            
        elif 'what did i told you to remember' in query or 'kya yad rakhne ko bola tha' in query or 'tumhe kya yad hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            remember=open('C:\\Users\\HP\\My AI assistant\\Database\\remem.txt','r' )
            remsg=remember.read()
            Speak("Accoding to saved data")
            Speak(f"you tell me that:- {remsg} ")
           
        elif 'jokes' in query or 'tell me some jokes' in query or 'joke sunao' in query or 'koi joke sunao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            get=pyjokes.get_joke()
            Speak(get)
            
        elif 'repeat my words' in query or 'mere words dohrao' in query or  'mere sabd dohrao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            jj=TakeCommand('audio')  
            Speak(f" sir , you said:{jj}") 
            
        elif "will you be my gf" in query or "will you be my bf" in query:   
            Speak("I'm not sure about, may be you should give me some time")     
             
        elif 'you need a break' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("ok sir, you can call me anytime ")
            break  
        
        
        
        elif 'today news' in query or "what is today's news" in query or 'aaj ki news kya hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from features import TodayNews  
            TodayNews()  
  
            
        elif 'song please' in query or 'play some songs' in query or 'can you play some songs?' in query or 'play song' in query or 'koi gana chalao' in query or 'koi gana play karo' in query or 'koi song play karo' in query or 'bajao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay sir,what song should i play...")
            song =TakeCommand('audio')
            webbrowser.open(f'https://open.spotify.com/search/{song}')  
            sleep(10) 
            pyautogui.click(x=1214, y=386)
            sleep(5)
            pyautogui.click(x=533, y=712)
            Speak("Playing:-"+song) 
        
        elif 'stop song' in query or 'stop music' in query or 'gana band karo' in query or 'song band karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            song =TakeCommand('audio')
            pyautogui.click(x=533, y=712)
            Speak("stopped:") 
            
        elif 'add item' in query or 'add items' in query:
            Speak("give me the items name to add in youur shopping list")
            file1 = open('C:\\Users\\HP\\My AI assistant\\ExtraPro\\shop.txt', 'a')
            for i in range(1,10):
               items=TakeCommand('audio')
               if 'stop' in items or 'no items' in items:
                   items.replace('stop','')
                   Speak('ok')
                   break
               file1.writelines(items)
               file1.write("\n")
               Speak('done')
               Speak('next')      
           
           
        elif 'open shopping list' in query:
            from ExtraPro import shop 
            
            Speak('you can add or delete itrms  manually in your shopping list here')
         
        elif 'game' in query or "let's play" in query: 
            from ExtraPro import game    
            
        elif 'play' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            song =TakeCommand('audio')
            song=song.replace('play','')
            pyautogui.click(x=97, y=253)
            keyboard.write(song)
            sleep(5)
            pyautogui.click(x=1214, y=385)
            sleep(5)
            pyautogui.click(x=533, y=712)
            Speak("Playing:-"+song) 
                 
            
        elif 'generate qr' in query or 'qr generate karo' in query or 'create qr' in query or 'qr' in query:
            query=query.replace("for",'')
            query=query.replace("for this",'')
            query=query.replace("generate qr",'')   
            query=query.replace("qr generate karo",'') 
            Speak("okay sir")
            Speak("Enter the text, sir")
            s=input("Enter the text::") 
            from ExtraPro.qr import qr
            qr(s) 
            Speak('qr generated sir')
            Speak("you can check this")
            img=Image.open("C:\\Users\\HP\\My AI assistant\\Database\\qr_images\\qr.png")
            img.show()
                                
       
        elif 'aaj kitni tarikh hai' in query or 'aaj tarikh kitni hai' in query or 'what date is today' in query or 'what date ise today' in query or 'tell the date' in query or "today's date" in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            strDate=datetime.datetime.now().strftime("%m/ %d /%y")
            print(f"\n\tToday is:- {strDate}") 
            Speak(f"Today is:-{strDate}")
          
            
        elif "change name" in query or 'channge your name' in query:
            Speak("What would you like to call me, Sir.")
            assname = TakeCommand('audio')
            Speak("Thanks for naming me")
            
        elif 'show note' in query: 
            from automations import showNote
            showNote()                     
  
        
        else:
            
            from chatbot.chatbot import Chatterbot
            if query=='none':
                continue
            reply=Chatterbot(query)
            
            Speak(reply)
            
            if 'bye' in query:
                break
            
            elif 'exit' in query: 
                Speak("okay sir, it was nice to meet you")
                break
            elif 'stop' in query:
                Speak("okay sir")
                break
            
           
TaskExe()    
     
            
         