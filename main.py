from gtts import gTTS
import os

# Sample text to be converted to speech
text = "Hello, this is a sample text-to-speech conversion using gTTS."

# Language in which you want to convert
language = 'en'

# Creating the gTTS object
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file
speech.save("sample.mp3")

# Playing the converted file
os.system("start sample.mp3")