from gtts import gTTS
import os
file = open("talk.txt", "r").read()
speech = gTTS(text = file, lang = 'en', slow = False)
speech.save("audio.mp3")
os.system("audio.mp3")
