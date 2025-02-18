# import streamlit as st
# import time
#
#
# def main():
#     st.set_page_config(page_title="Google Sign In", page_icon="🔒")
#
#     if "step" not in st.session_state:
#         st.session_state["step"] = "email"
#
#     st.markdown("""
#         <style>
#             @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
#             * {
#                 margin: 0;
#                 padding: 0;
#                 box-sizing: border-box;
#                 font-family: 'Roboto', sans-serif;
#             }
#             body {
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 height: 100vh;
#                 background-color: #fff;
#             }
#             .container {
#                 max-width: 450px;
#                 padding: 40px;
#                 border-radius: 8px;
#                 box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#                 text-align: center;
#                 overflow: hidden;
#             }
#             .top-content img {
#                 width: 75px;
#                 margin-bottom: 10px;
#             }
#             h2 {
#                 font-weight: 500;
#                 font-size: 24px;
#                 margin-bottom: 8px;
#             }
#             .heading {
#                 color: #5f6368;
#                 font-size: 16px;
#                 margin-bottom: 20px;
#             }
#             .input {
#                 width: 100%;
#                 padding: 15px;
#                 font-size: 16px;
#                 border: 1px solid #ccc;
#                 border-radius: 4px;
#                 outline: none;
#                 margin-bottom: 10px;
#             }
#             .next-btn {
#                 background-color: #1a73e8;
#                 color: white;
#                 padding: 10px 20px;
#                 font-size: 14px;
#                 border: none;
#                 border-radius: 4px;
#                 cursor: pointer;
#                 margin-top: 10px;
#             }
#             .next-btn:hover {
#                 background-color: #1765c0;
#             }
#             .loading {
#                 width: 25px;
#                 height: 25px;
#                 border: 3px solid rgba(0, 0, 0, 0.2);
#                 border-top: 3px solid #1a73e8;
#                 border-radius: 50%;
#                 animation: spin 1s linear infinite;
#                 margin: 10px auto;
#                 display: block;
#             }
#             @keyframes spin {
#                 0% { transform: rotate(0deg); }
#                 100% { transform: rotate(360deg); }
#             }
#         </style>
#     """, unsafe_allow_html=True)
#
#     st.markdown("""
#         <div class='container'>
#             <div class='top-content'>
#                 <img src='https://i.postimg.cc/CL7CmGSx/google-logo-png-29530.png' width='100'/>
#                 <h2>Sign in</h2>
#                 <p class='heading'>Use your Google Account</p>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)
#
#     if st.session_state["step"] == "email":
#         email = st.text_input("Email or phone", key="email_input")
#         if st.button("Next", key="next_email"):
#             if email:
#                 st.session_state["email"] = email
#                 st.session_state["step"] = "loading"
#                 st.rerun()
#             else:
#                 st.error("Please enter your email.")
#
#     elif st.session_state["step"] == "loading":
#         st.markdown("<div class='loading'></div>", unsafe_allow_html=True)
#         with st.spinner("Processing..."):
#             time.sleep(1.5)
#         st.session_state["step"] = "password"
#         st.rerun()
#
#     elif st.session_state["step"] == "password":
#         password = st.text_input("Enter your password", type="password", key="password_input")
#         if st.button("Next", key="next_password"):
#             if password:
#                 st.session_state["password"] = password
#                 print(f"Email: {st.session_state['email']}, Password: {st.session_state['password']}")
#                 st.success("Redirecting...")
#                 time.sleep(1.5)
#                 st.markdown("[Continue to Google](https://www.google.com)")
#             else:
#                 st.error("Please enter your password.")
#
#
# if __name__ == "__main__":
#     main()

import pyautogui
import time
import math
start = time.time()
i = 0
while i < 50:
    x = 0
    print(i)
    while x < 20:
        #off = pow(abs(20*x), 1/3)
        pyautogui.moveRel(i,0, _pause=False)
        x+=1
    x = 0
    while x < 20:
        #off = pow(abs(20*x), 1/3)
        pyautogui.moveRel(-i,0, _pause=False)
        x+=1
    i += 5
end = time.time()

print(f"Took {end - start:,.2f} seconds")
from spacy.displacy import parse_ents

# import ollama
# import pyautogui
#
# def call(prompt, imagePath):
#     response = ollama.chat(
#         model='llama3.2-vision',
#         messages=[{
#             'role': 'user',
#             'content': prompt,
#             'images': [imagePath]
#         }],
#         format = {
#         "type": "string",
#         "enum": ["CLICK", "TYPE"]
#         },
#     )
#     return str(response['message']['content'])
#
#
# def locationCall(prompt, imagePath):
#     response = ollama.chat(
#         model='llama3.2-vision',
#         messages=[{
#             'role': 'user',
#             'content': prompt,
#             'images': [imagePath]
#         }],
#         format={
#             "type": "integer",
#         },
#     )
#     return str(response['message']['content'])
#
# def typeCall(prompt, imagePath):
#     response = ollama.chat(
#         model='llama3.2-vision',
#         messages=[{
#             'role': 'user',
#             'content': prompt,
#             'images': [imagePath]
#         }],
#
#     )
#     return str(response['message']['content'])
#
#
#
# def LLMCode():
#     #ADD YOUR CODE HERE
#     print()
#
#
# def main():
#     image = pyautogui.screenshot("testSS.png")
#     image.save("testSS.png")
#     prompt = "DO NOT DESCRIBE THE IMAGE YOU ARE SEEING. Your goal is to find the LLMCode() function, click on it and then type some code into it as well. You are tasked with interpreting a given query and determining the most appropriate action between the two options: CLICK or TYPE. Carefully analyze the context and intent of the query before making your decision. Your response must consist solely of one of these two words: CLICK or TYPE, without any additional text, explanation, or commentary. Ensure your reply is concise, precise, and adheres strictly to this format."
#     response = call(prompt, "testSS.png").replace("\"","")
#     print(response)
#     while response != "CLICK" and response != "TYPE" and response != "click" and response != "type":
#         prompt = "DO NOT DESCRIBE THE IMAGE YOU ARE SEEING. That was not a response of one word which was either CLICK or TYPE, Respond with only CLICK or TYPE, no punctuation, formatting, spaces, and in all capital letters. Now, choose an action to do in this image, CLICK or TYPE. Respond in only one word"
#         response = call(prompt, "testSS.png")
#         print(response)
#     if response == "CLICK":
#         x = int(locationCall("Respond with the x coordinate of the pixel you want to click", "testSS.png"))
#         y = int(locationCall("Respond with the y coordinate of the pixel you want to click", "testSS.png"))
#         print("Clicking at" + str(x) + ", " + str(y))
#         pyautogui.moveTo(x, y)
#         pyautogui.click()
#     elif response == "TYPE":
#         prompt = "DO NOT DESCRIBE THE IMAGE YOU ARE SEEING. Your goal is to find the LLMCode() function, click on it and then type some code into it as well. What would you like to type? Respond only with what you want to type"
#         response = typeCall(prompt, "testSS.png")
#         pyautogui.typewrite(response)
#         print("Typing " + response)
#
#
# if __name__ == '__main__':
#     while True:
#         print("running")
#         main()


# number = "64 32"
# number = number.split(" ")
# if number[0].isdigit():
#     print(number[0])
# else:
#     print("Not a digit")


# import keyboard
# keyboard.press_and_release("cmd+space")
#

# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import sounddevice as sd
# import time
#
# # Set up constants
# SAMPLE_RATE = 44100  # Sample rate (samples per second)
# CHANNELS = 1  # Mono audio
# BUFFER_SIZE = 1024  # Number of samples per update
#
#
# # Function to update the audio plot in real-time
# def plot_waveform(audio_data):
#     plt.figure(figsize=(10, 4))
#     plt.plot(audio_data, color='blue')
#     plt.title("Live Audio Waveform")
#     plt.xlabel("Samples")
#     plt.ylabel("Amplitude")
#     plt.grid(True)
#     plt.tight_layout()
#     st.pyplot(plt)
#
#
# # Function to capture microphone audio in real-time and visualize
# def record_and_visualize():
#     # Streamlit title and instructions
#     st.title("Live Microphone Audio Visualizer")
#     st.write("This app captures and visualizes live microphone audio.")
#
#     # Create a placeholder for the plot
#     audio_placeholder = st.empty()
#
#     # Start recording audio
#     with st.spinner("Recording..."):
#         try:
#             # Set up the stream for audio capture
#             audio_stream = sd.InputStream(callback=audio_callback, channels=CHANNELS, samplerate=SAMPLE_RATE,
#                                           blocksize=BUFFER_SIZE)
#             audio_stream.start()
#
#             while True:
#                 # Keep the plot updated
#                 audio_data = np.array(audio_data_buffer)
#                 audio_placeholder.pyplot(plot_waveform(audio_data))
#
#                 time.sleep(0.1)  # Update every 100 ms
#         except KeyboardInterrupt:
#             st.warning("Recording stopped manually.")
#             audio_stream.stop()
#
#
# # Global buffer to store incoming audio
# audio_data_buffer = []
#
#
# # Callback function for audio data stream
# def audio_callback(indata, frames, time, status):
#     """Callback function for processing audio data."""
#     if status:
#         print(status)
#     # Append new audio data to the buffer
#     audio_data_buffer.append(indata[:, 0])  # We're using mono audio (single channel)
#
#     # Limit the buffer size to the last BUFFER_SIZE samples to visualize a moving window
#     if len(audio_data_buffer) > BUFFER_SIZE:
#         audio_data_buffer.pop(0)
#
#
# # Main function to run the Streamlit app
# if __name__ == "__main__":
#     record_and_visualize()

#THIS CODE DOESNT WORK
'''import streamlit as st
import pyaudio
import numpy as np
import time

# Parameters
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate in Hz

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

# Streamlit setup
st.title("Real-Time Audio Visualizer")
plot_placeholder = st.empty()

# Main loop
try:
    while True:
        data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
        plot_placeholder.line_chart(data)
        time.sleep(0.05)  # Small delay to prevent excessive updates
except KeyboardInterrupt:
    pass

# Clean up
stream.stop_stream()
stream.close()
p.terminate()


'''



# import pyaudio
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# # Parameters
# CHUNK = 1024  # Number of audio samples per frame
# FORMAT = pyaudio.paInt16  # Audio format
# CHANNELS = 1  # Mono audio
# RATE = 44100  # Sampling rate in Hz
#
# # Initialize PyAudio
# p = pyaudio.PyAudio()
# stream = p.open(
#     format=FORMAT,
#     channels=CHANNELS,
#     rate=RATE,
#     input=True,
#     frames_per_buffer=CHUNK
# )
#
# # Initialize Matplotlib plot
# fig, ax = plt.subplots()
# x = np.arange(0, CHUNK)
# y = np.zeros(CHUNK)
# line, = ax.plot(x, y)
# ax.set_ylim(-32768, 32767)  # 16-bit audio range
# ax.set_xlim(0, CHUNK)
# ax.set_title("Real-Time Audio Waveform")
# ax.set_xlabel("Sample")
# ax.set_ylabel("Amplitude")
#
# # Update function for the animation
# def update(frame):
#     data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
#     line.set_ydata(data)
#     return line,
#
# # Create animation
# ani = FuncAnimation(fig, update, blit=True, interval=50)
#
# try:
#     plt.show()
# except KeyboardInterrupt:
#     pass
#
# # Clean up
# stream.stop_stream()
# stream.close()
# p.terminate()
#
#


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