from gtts import gTTS 
   
import os 
  
# The text that you want to convert to audio 
mytext = 'Hi'
  
# Language in which you want to convert 
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 
 
myobj.save("welcome.mp3") 
  
