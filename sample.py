from gtts import gTTS
from playsound import playsound

def textToAudio(str):
    audio =gTTS(str)
    audio.save('example.mp3')

textToAudio('this audio is generated using gtts module of python')   
playsound('example.mp3') 
