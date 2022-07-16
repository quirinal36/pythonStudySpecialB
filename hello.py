from gtts import gTTS
from playsound import playsound
import os
# import time

text = '나는 재미있어. 딸기잼이 있어.'
tts = gTTS(text = text , lang='ko')

fileName = "tovoice3"
fileExtension = "mp3"

fullPath:str = fr"{os.getcwd()}/{fileName}.{fileExtension}".replace("\\", "/")

tts.save(fullPath)

playsound(fullPath)