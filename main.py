import speech_recognition as sr
# Remember, we import as SpeechRecognition and we need pyaudio as well for it to work
import pyautogui
import time
from openai import OpenAI
from pathlib import Path
import os
import requests
import pyperclip
import warnings
from datetime import datetime
import ollama
import subprocess
import whisper

'''
# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
# Text to speech to a file
tts.tts_to_file(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
'''
# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

city = "indianapolis"
youtuber_list = [["Micheal Reeves", "https://www.youtube.com/watch?v=mvz3LRK263E&list=UULPtHaxi4GTYDpJgMSGy7AeSw"],
                 ["PewDiePie", "https://www.youtube.com/watch?v=QRALuk2kq0I&list=UULF-lHJZR3Gqxm24_Vd_AJ5Yw"],
                 ["Hacksmith", "https://www.youtube.com/watch?v=Li1t6jPn3Yo&list=UULPjgpFI5dU-D1-kh9H1muoxQ"],
                 ["Mumbo Jumbo", "https://www.youtube.com/watch?v=pxlIpmKQ-XE&list=UULFhFur_NwVSbUozOcF_F2kMg"],
                 ["", ""]]
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=indianapolis&appid=25c3301dc7b7a72a13b83eb4a39cef51"
api_key = "sk-proj-HohQBzV1jzM5C3hfgZYTT3BlbkFJFwa6kJ8jQNoxGmGNDu1N"
client = OpenAI(api_key=api_key)

conversation = []


def updateMessages():
    global conversation
    conversation = []
    f = open('convo.txt', 'r')
    for line in f:
        if line[:5] == "Syst ":
            conversation.append({'role': 'system', 'content': '' + str(line).replace("Syst ", "").replace("\n", "") + ''})
        elif line[:5] == "User ":
            conversation.append({'role': 'user', 'content': '' + str(line).replace("User ", "").replace("\n", "") + ''})
        elif line[:5] == "Asst ":
            conversation.append({'role': 'assistant', 'content': '' + str(line).replace("Asst ", "").replace("\n", "") + ''})
    f.close()


def asstWrite(command):
    f = open('convo.txt', 'a')
    command = command.replace("\n", "")
    f.write("Asst " + str(command) + "\n")
    f.close()
    updateMessages()


call_minsec = 0
minsec = 0
standby = 120


def openAicall(call):
    global conversation
    updateMessages()
    response = ollama.chat(model='llama3.1:8b',
                           messages=conversation,
                           options={'temperature': 0})
    print(response['message']['content'])
    return str(response['message']['content'])

def sandbox(call):
    response = ollama.generate(model='deepseek-coder-v2',
                               prompt=call)
    return str(response['response'])
def codeLlama(call):
    response = ollama.generate(model='codellama',
                               prompt=call + ". No extra comments or words, only code. Respond only with code. "
                                             "Anything besides code requires a comment symbol to be made infront of it."
                                             "Do not add any explanations of the code")
    print(response['response'])
    return str(response['response'])

def openAicallV1(call):
    global conversation

    # Things to do. Try and make the Ai understand emotions by making functions with conversations to use as a baseline
    # Use this function to call the AI with a prompt instead of adding it in every time it needs to be used
    # Have the Ai respond to every sentance said unless its unnecassary
    # Possibly use c.ai to make a more natural conversation

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation + [{"role": "user", "content": call}],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    response = completion.choices[0].message.content
    conversation = conversation + [{"role": "user", "content": call}]
    conversation = conversation + [{"role": "assistant", "content": response}]
    #print(conversation)


    return response

def speech(text):
    speech_file_path = Path(__file__).parent / "speech.mp3"

    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text
    )

    response.stream_to_file(speech_file_path)

def findIndex(stringArr, keyString):
    #  Initialising result array to -1
    #  in case keyString is not found
    result = []
    #  Iteration over all the elements
    #  of the 2-D array
    #  Rows
    for i in range(len(stringArr)):
        #  Columns
        for j in range(len(stringArr[i])):
            #  If keyString is found
            if stringArr[i][j] == keyString:
                result.append(i)
                result.append(j)
                return result
    result.append(-1)
    result.append(-1)
    #  If keyString is not found
    #  then -1 is returned
    return result


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_whisper(audio, language="english")
    except sr.UnknownValueError:
        return ""

def changeStandby(sec):
    global standby
    standby = sec

def recentSpeak(talk):

    global call_minsec, minsec, standby
    if talk:
        now = datetime.now()
        # str(%H,%M,%S)
        curr_min = now.strftime("%M")
        curr_sec = now.strftime("%S")
        minsec = int(curr_min)*60 + int(curr_sec)
    else:
        now = datetime.now()
        call_min = now.strftime("%M")
        call_sec = now.strftime("%S")
        call_minsec = (int(call_min)*60) + int(call_sec)

    time_since_wake = call_minsec - minsec
    '''
    print("Time since wake: " + str(time_since_wake))
    print("Current Standby: " + str(standby))
    print("call_minsec: " + str(call_minsec))
    print("minsec: " + str(minsec))
    '''
    if time_since_wake < standby:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        print("ready")
        print(standby)
        command = listen().lower()
        print(command)
        if "jarvis" in command:
            recentSpeak(True)
            curtime = datetime.now()
            curtime = curtime.strftime("%d/%m/%y %H-%M-%S")
            f = open('convo.txt', 'a')
            f.write("User " + command + ". TIMESTAMP: " + curtime +  "\n")
            f.close()
            updateMessages()
        if recentSpeak(False) and "jarvis" not in command:
            if command != "":
                command = "jarvis " + command
                f = open('convo.txt', 'a')
                f.write("User " + command + "\n")
                f.close()
                updateMessages()
        if "jarvis start up" in command:
            subprocess.call(['open', "/System/Applications/Safari.app"])
            subprocess.call(['open', "/System/Applications/PyCharm.app"])
            subprocess.call(['open', "/System/Applications/Music.app"])
            pyautogui.press('enter')
            recentSpeak(True)
            asstWrite("Starting up now")
        elif "jarvis" in command and "process and understand the screen" in command:
            pyautogui.keyDown('command')
            pyautogui.press('a')
            pyautogui.press('c')
            pyautogui.keyUp('command')
            pyautogui.press('escape')
            # Copy the contents of the clipboard to a variable
            clipboard_contents = pyperclip.paste()
            f = open('convo.txt', 'a')
            curtime = datetime.now()
            curtime = curtime.strftime("%d/%m/%y %H-%M-%S")
            f.write("User " + str(clipboard_contents).replace("\n","") + ". TIMESTAMP: " + curtime + "\n")
            f.close()
            response = openAicall(clipboard_contents)
            speech(response)
            os.system("afplay speech.mp3")
            asstWrite(response)
        elif "jarvis" in command and "change standby" in command:
            command = command[(command.index("to")+2):]
            command = command[:(command.index("second")-1)]
            changeStandby(int(command))
            asstWrite("Changing standby to " + str(standby) + " seconds")
        elif "jarvis" in command and "enter sandbox mode" in command:
            print("Entering Sandbox Mode")
            f = open('convo.txt', 'a')
            f.write("User You have now entered sandbox mode. Here, anything you respond is put into deepseek-coder-v2"
                    "and should output a code-like response. Use that to learn more about how code works."
                    "Once you want be done, simply respond with: EXIT_SANDBOX and it will take you out of the mode \n")
            f.close()
            asstWrite(openAicall(command).replace("\n",""))
            breaker = False
            f = open('convo.txt', 'a')
            f.write("User You are now in sandbox mode. Start the code prompt \n")
            f.close()
            while not breaker:
                response = openAicall("")
                asstWrite(response)
                f = open('convo.txt', 'a')
                f.write("User " + sandbox(response).replace("\n","")+ "\n")
                f.close()
            f = open('convo.txt', 'a')
            f.write("User You are out of sandbox mode \n")
            f.close()
        elif "jarvis" in command and "summarize" in command:
            pyautogui.keyDown('command')
            pyautogui.press('a')
            pyautogui.press('c')
            pyautogui.keyUp('command')
            pyautogui.press('escape')
            # Copy the contents of the clipboard to a variable
            clipboard_contents = pyperclip.paste()
            prompt = ("Summarize the contents of this file in a sentence " + clipboard_contents)
            tokenized_prompt = len(clipboard_contents)/5
            while tokenized_prompt > 1024:
                speech("Prompt too long, cutting down the length of the prompt")
                os.system("afplay speech.mp3")
                reduction_rate = (tokenized_prompt/1024) * 2
                index = int(len(clipboard_contents) / reduction_rate - 1)
                prompt = clipboard_contents[:index]
            # Use slicing to remove everything after the last occurrence of the delimiter
            summary = openAicall(prompt)
            print(summary)
            speech(summary)
            os.system("afplay speech.mp3")
            print("here2")
        elif "jarvis" in command and "mail" in command:
            if command.index("about") != -1:
                i = command.index("about")
                p = i+4
                command = "Compose and email about " + command[p:]
            else:
                asstWrite("What would you like the email topic to be about")
                speech("What would you like the email topic to be about?")
                os.system("afplay speech.mp3")
                command = listen().lower()
                while command == "":
                    command = listen().lower()
            subprocess.call(['open', "/System/Applications/Mail.app"])
            pyautogui.keyDown('command')
            pyautogui.press('n')
            pyautogui.keyUp('command')
            emailBody = openAicall(command)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.PAUSE = 0
            pyautogui.typewrite(emailBody)
            speech("Email body has been written")
            asstWrite("Email Body has been written")
            os.system("afplay speech.mp3")
        elif "jarvis search" in command:
            command = command.replace("jarvis search", "Searching")
            speech(command)
            asstWrite(command)
            os.system("afplay speech.mp3")
            subprocess.call(['open', "/System/Applications/Safari.app"])
            pyautogui.keyDown('command')
            pyautogui.press('t')
            pyautogui.keyUp('command')
            command = command.replace("Searching", "")
            pyautogui.typewrite(command)
            pyautogui.press('enter')
        elif "jarvis" in command and "initiate protocol 1" in command:
            speech("Initiating Protocol 1")
            asstWrite("Initiating Protocol 1")
            os.system("afplay speech.mp3")
        elif "jarvis volume down" in command:
            speech("turning volume down")
            asstWrite("Turning volume down")
            # play speech audi
            os.system("afplay speech.mp3")
            pyautogui.keyDown('alt')
            pyautogui.press('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite("voldown")
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite("voldown")
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite("voldown")
            pyautogui.press('enter')
        elif "jarvis volume up" in command:
            speech("turning up the volume")
            asstWrite("turning up the volume")
            os.system("afplay speech.mp3")
            pyautogui.keyDown('alt')
            pyautogui.press('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite("volup")
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite("volup")
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite("volup")
            pyautogui.press('enter')
        elif "jarvis quit all" in command:
            speech("Are you sure?")
            asstWrite("Are you sure?")
            os.system("afplay speech.mp3")
            command = listen().lower()
            while command == "":
                command = listen().lower()
            if "yes" in command:
                pyautogui.keyDown('alt')
                pyautogui.keyDown('space')
                pyautogui.keyUp('space')
                pyautogui.keyUp('alt')
                pyautogui.typewrite("quitall")
                pyautogui.press('enter')
            asstWrite("Okay")
            speech("Okay")
            os.system("afplay speech.mp3")

        elif "jarvis play" in command and "youtube" in command:
            asstWrite("Who would you like to play?")
            speech("Who would you like to play?")
            os.system("afplay speech.mp3")
            command = listen().lower()
            while command == "":
                command = listen().lower()
            '''
            try:
                pywhatkit.playonyt(command, use_api=True)

                speech("Playing " + command + " on youtube")
                # play speech audi
                tts.save("speak.mp3")
                time.sleep(.5)
                os.system("afplay speak.mp3")

            except:

                # printing the error message
                print("Network Error Occurred")
            '''
            result = findIndex(youtuber_list, command)
            subprocess.call(['open', "/System/Applications/Safari.app"])
            pyautogui.keyDown('command')
            pyautogui.press('t')
            pyautogui.keyUp('command')
            pyautogui.typewrite(youtuber_list[result[1] + 1][result[0]])
            pyautogui.press('enter')

        elif "jarvis play" in command or "jarvis pause" in command:
            asstWrite("Toggling")
            pyautogui.hotkey('play/pause')
        elif "jarvis show me" in command:
            subprocess.call(['open', "/System/Applications/Safari.app"])
            pyautogui.keyDown('command')
            pyautogui.press('t')
            pyautogui.keyUp('command')
            pyautogui.typewrite("chatgpt.com")
            pyautogui.press('enter')
            time.sleep(2)
            command = command.replace("jarvis show me", "")
            pyautogui.typewrite(command)
            pyautogui.press('enter')
            asstWrite("Bringing it up now")
        elif "jarvis play" in command:
            command = command.replace("jarvis play", "")
            asstWrite("playing" + command)
            speech("playing " + command)
            os.system("afplay speech.mp3")
        elif "jarvis open" in command:
            command = command.replace("jarvis open ", "")
            pyautogui.keyDown('alt')
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite(command)
            pyautogui.press('enter')
            asstWrite("Opening" + command)
        elif "jarvis what" in command and "weather" in command:
            response = requests.get(weather_url)
            if response.status_code == 200:
                weather_data = response.json()
                asstWrite(f"The weather in {city} is {weather_data['weather'][0]['description']}.")
                speech(f"The weather in {city} is {weather_data['weather'][0]['description']}.")
                os.system("afplay speech.mp3")
            else:
                asstWrite("Sorry, I couldn't retrieve the weather data")
                speech("Sorry, I couldn't retrieve the weather data")
                os.system("afplay speech.mp3")
        elif "jarvis what" in command and "temperature" in command:
            response = requests.get(weather_url)
            if response.status_code == 200:
                weather_data = response.json()
                data = response.json()

                temperature = data["main"]["temp"]
                temp_f = (temperature - 273.15) * 9 / 5 + 32
                temp_f = int(temp_f)
                asstWrite(f"The temperature in {city} is {temp_f} Fahrenheit.")
                speech(f"The temperature in {city} is {temp_f} Fahrenheit.")
                os.system("afplay speech.mp3")
            else:
                asstWrite("Sorry, I couldn't retrive the weather data")
                speech("Sorry, I couldn't retrieve the weather data")
                os.system("afplay speech.mp3")
        elif "jarvis" in command and "remind" in command:
            speech("What would you like to set a reminder for?")
            asstWrite("What would you like to set a reminde for?")
            os.system("afplay speech.mp3")
            command = listen().lower()
            while command == "":
                command = listen().lower()
            reminderName = command
            speech("When would you like this reminder set for?")
            asstWrite("When would you like this reminder set for?")
            os.system("afplay speech.mp3")
            command = listen().lower()
            while command == "":
                command = listen().lower()
            subprocess.call(['open', "/System/Applications/Reminders.app"])
            pyautogui.keyDown('command')
            pyautogui.press('n')
            pyautogui.keyUp('command')
            time.sleep(1)
            pyautogui.typewrite(reminderName)
            if "today" in command:
                pyautogui.keyDown('command')
                pyautogui.press('t')
                pyautogui.keyUp('command')
                speech("Set a reminder to " + reminderName + " for " + command)
                os.system("afplay speech.mp3")
            elif "tomorrow" in command:
                pyautogui.keyDown('command')
                pyautogui.keyDown('option')
                pyautogui.press('t')
                pyautogui.keyUp('option')
                pyautogui.keyUp('command')
                speech("Set a reminder to " + reminderName + " for " + command)
                os.system("afplay speech.mp3")
            elif "weekend" in command:
                pyautogui.keyDown('command')
                pyautogui.press('k')
                pyautogui.keyUp('command')
                speech("Set a reminder to " + reminderName + " for " + command)
                os.system("afplay speech.mp3")
            elif ("next" in command or "coming" in command) and "week" in command:
                pyautogui.keyDown('command')
                pyautogui.keyDown('option')
                pyautogui.press('k')
                pyautogui.keyUp('option')
                pyautogui.keyUp('command')
                speech("Set a reminder to " + reminderName + " for " + command)
                os.system("afplay speech.mp3")
            pyautogui.press('enter')
            asstWrite("Set a reminder to" + reminderName + " for " + command)
        elif "jarvis" in command and ("write" in command or "build" in command) and "a" in command and ("program" in command or "file" in command or "function" in command):
            command = command.replace("jarvis", "")
            response = codeLlama(command)
            asstWrite(response)
            f = open('convo.txt', 'a')
            f.write("User Respond with filetype of this program and only the filetype of this program. Ex .py, .java, .cpp\n" + response + "\n")
            f.close()
            filetype = openAicall("Respond with filetype of this program and only the filetype of this program. Ex .py, .java, .cpp\n" + response)
            programTime = datetime.now()
            programTime = programTime.strftime("%H,%M,%S")
            filename = str(programTime) + filetype
            f = open(filename, "x")
            f.write(response)
            f.close()
            response = "Summarize this program in 2 sentances or less: " + response
            f = open('convo.txt', 'a')
            f.write("User Summarize this program in 2 sentances or less: " + response + "\n")
            f.close()
            answer = openAicall(response)
            speech(answer)
            subprocess.call(['open', filename])
            '''
            time.sleep(1)
            pyautogui.keyDown('alt')
            pyautogui.press('space')
            pyautogui.keyUp('alt')
            pyautogui.typewrite(filename)
            pyautogui.press('enter')
            '''
            os.system("afplay speech.mp3")
        elif "jarvis, shut down confirm" in command:
            speech("Shutting Down Now")
            asstWrite("Shutting Down Now")
            os.system("afplay speech.mp3")
            break
        elif "jarvis" in command:
            command = command.replace("jarvis", "")
            response = openAicall(command)
            speech(response)
            os.system("afplay speech.mp3")
            asstWrite(response)
