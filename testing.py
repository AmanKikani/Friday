# '''import torch
# import torchaudio
# import ChatTTS
# import os
# import sys
# import getopt
# import threading
#
# torch._dynamo.config.cache_size_limit = 64
# torch._dynamo.config.suppress_errors = True
# torch.set_float32_matmul_precision('high')
#
# chat = ChatTTS.Chat()
# chat.load(compile=True)  # Set to True for better performance
#
#
# def main(texts, num):
#     print(texts)
#     wavs = chat.infer(texts)
#     for i in range(len(wavs)):
#         try:
#             torchaudio.save(f"speech{num}.mp3", torch.from_numpy(wavs[i]).unsqueeze(0), 24000)
#         except:
#             torchaudio.save(f"speech{num}.mp3", torch.from_numpy(wavs[i]), 24000)
#
#
# if __name__ == "__main__":
#     texts = "This is a first sentence. This is a second sentence. This is the third sentence. This is the fourth sentence. This is the fifth sentence."
#     texts = texts.split(".")
#     x = 0
#     arr = []
#     '''
# '''    t1 = threading.Thread(target=main, args=(texts[0],))
#     t2 = threading.Thread(target=main, args=(texts[1],))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
# '''
#     '''
#     print(texts)
#     # x = 0
#     # t0 = threading.Thread(target=main, args=(texts[0],))
#     # t1 = threading.Thread(target=main, args=(texts[1],))
#     # '''
#
#
# while x < len(texts):
#     #     exec(f't{x} = threading.Thread(target=main, args=(texts[{x}],))')
#     #     x+=1'''
#     #
#     # x = 0
#     # while x < len(texts):
#     #     exec(f't{x}.start()')
#     #     x += 1
#     # x = 0
#     # while x < len(texts):
#     #     exec(f't{x}.join()')
#     #     x += 1
#
#     threads = []
#     x = 0
#     for i in range(len(texts)):
#         t = threading.Thread(target=main, args=(texts[i], x))
#         threads.append(t)
#         t.start()
#         x += 1
#     x = 0
#     print("Done")
#
#
# '''import streamlit as st
# import json
#
# def microphone_action():
#     return {"message": "Microphone activated!", "status": "success"}
#
# def main():
#     st.set_page_config(page_title="LUMIN App", layout="centered")
#
#     # Header with LUMIN branding
#     st.markdown("""<div style='display: flex; justify-content: space-between; align-items: center;'>
#     <h1 style='font-size: 2.5em; margin: 0;'>LUMIN</h1>
#     <img src='https://via.placeholder.com/50' alt='Account' style='border-radius: 50%;'>
#     </div><hr>""", unsafe_allow_html=True)
#
#     # Microphone button in the center
#     st.markdown("""<div style='display: flex; justify-content: center; margin-top: 50px;'>
#     <button style='font-size: 1.5em; padding: 10px 20px; cursor: pointer;' onclick='activateMicrophone()'>🎤 Activate Microphone</button>
#     </div>""", unsafe_allow_html=True)
#
#     # JavaScript for button functionality
#     st.markdown("""
#     <script>
#     function activateMicrophone() {
#         fetch('/microphone', {
#             method: 'POST',
#             headers: {
#                 'Content-Type': 'application/json',
#             },
#             body: JSON.stringify({}),
#         }).then(response => response.json()).then(data => {
#             alert(data.message);
#         });
#     }
#     </script>
#     """, unsafe_allow_html=True)
#
#     # Cool feature: Recent activity log
#     st.sidebar.title("Recent Activity")
#     activity_log = st.sidebar.empty()
#     if st.button("Simulate Activity"):
#         result = microphone_action()
#         activity_log.text(json.dumps(result, indent=2))
#
# if __name__ == "__main__":
#     main()
#
# '''
#
# '''presses = [["y",1],["x",2]]
#
# print(presses[0][0])
#
# '''
#
#
#
# '''import os
# import pyttsx3
# from gtts import gTTS
#
# tts = gTTS("Hello, this is a Siri-like voice.", lang='en')
# tts.save("hello.mp3")
#
# engine = pyttsx3.init()
# engine.say("Hello, this is a Siri-like voice.")
# engine.runAndWait()
# os.system("say Hello")
# '''
#
#
#
# '''x = 0
# while x < 10:
# 	exec(f'y = 1')
# 	x+=1
# print(y)
#
#
#
# '''
#
#
# '''import os
# import threading
# import subprocess
# texts = "This is a testing sentence. This is a second testing sentence"
# texts = texts.split(".")
# def runScript(scriptName):
# 	subprocess.run("python", scriptName)
#
# if __name__ == '__main__':
# 	x = 0
# 	arr = []
# 	while x < len(texts):
# 		arr.append(threading.Thread(target=runScript, args=(f'Site.py {texts[x]}',)))
# 		x+=1
# 	x = 0
# 	while x < len(arr):
# 		arr[x].start()
# 		x+=1
# 	x = 0
# 	while x < len(arr):
# 		arr[x].join()
# 		x+=1
#
# '''
# '''import ollama
#
# res = ollama.chat(
# 	model="llama3.2-vision",
# 	messages=[
# 		{
# 			'role': 'user',
# 			'content': 'Describe this image:',
# 			'images': ['./test.png']
# 		}
# 	]
# )
#
# print(res['message']['content'])
# '''
#
# '''# importing required module
# import http.client as httplib
# # function to check internet connectivity
# connection = httplib.HTTPConnection("www.google.com", timeout=10)
# try:
#     connection.request("HEAD","/")
#     connection.close()
#     print("Connection on")
# except:
#     print("Connection failed")
#
#
# import PySimpleGUI as sg
# # All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]
#
# # Create the Window
# window = sg.Window('Window Title', layout)
#
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])
#
# window.close()
# '''