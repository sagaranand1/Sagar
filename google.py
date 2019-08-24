from gtts import gTTS 
  
import os 

def run(str):
    mytext = 'this is a'+str+' rupee note'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("final.mp3") 
    os.system("final.mp3") 


