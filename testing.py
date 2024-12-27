presses = [["y",1],["x",2]]
print(presses[0][0])




'''import os
import pyttsx3
from gtts import gTTS

tts = gTTS("Hello, this is a Siri-like voice.", lang='en')
tts.save("hello.mp3")

engine = pyttsx3.init()
engine.say("Hello, this is a Siri-like voice.")
engine.runAndWait()
os.system("say Hello")
'''



'''x = 0
while x < 10:
	exec(f'y = 1')
	x+=1
print(y)



'''


'''import os
import threading
import subprocess
texts = "This is a testing sentence. This is a second testing sentence"
texts = texts.split(".")
def runScript(scriptName):
	subprocess.run("python", scriptName)

if __name__ == '__main__':
	x = 0
	arr = []
	while x < len(texts):
		arr.append(threading.Thread(target=runScript, args=(f'TTS.py {texts[x]}',)))
		x+=1
	x = 0
	while x < len(arr):
		arr[x].start()
		x+=1
	x = 0
	while x < len(arr):
		arr[x].join()
		x+=1

'''
'''import ollama

res = ollama.chat(
	model="llama3.2-vision",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image:',
			'images': ['./test.png']
		}
	]
)

print(res['message']['content'])
'''

'''# importing required module
import http.client as httplib
# function to check internet connectivity
connection = httplib.HTTPConnection("www.google.com", timeout=10)
try:
    connection.request("HEAD","/")
    connection.close()
    print("Connection on")
except:
    print("Connection failed")


import PySimpleGUI as sg
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
'''