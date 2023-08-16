# PDF to Audio Converter
import os
from gtts import gTTS
import PyPDF2

# path to pdf file
PATH = '/Users/ashleywu/Downloads/RichardIII Synopsis.pdf'

reader = PyPDF2.PdfReader(open(PATH, 'rb'))
final_text = ''

# extract the text
for page_num in range(len(reader.pages)):
    text = reader.pages[page_num].extract_text()
    final_text += text.strip().replace('\n', ' ')

# test:
# print(final_text)

# audio file name
AUDIO = 'audio.mp3'

# initialize gTTS + play temporary saved audio file
def speak_text(text):
    speech = gTTS(text)
    speech.save(AUDIO)
    os.system('afplay ' + AUDIO)

speak_text(final_text)
