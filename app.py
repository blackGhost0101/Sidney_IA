import os
import openai
import docx
import speech_recognition as sr
import pyttsx3
openai.apy_key = os.get_env("Open_ai_key")
engine = pyttsx3.init()

##
##  THIS CODE DON'T WORK IT'S JUST AN IDEA 
##

sidney_commands = ['create','break']


def ask_chat_gpt(question):
     prompt = f"Q: {question}\nA:"
     response = openai.Completion.create(
         engine = "davinci",
         prompt = prompt,
         temperature=0.7,
         max_tokens=1024,
         n=1,
         stop=None,
         timeout=15,
     )
     answer = response.choice[0].text.strip()
     return answer
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()



# def do_task_for_command(command):
#     if command in sidney_commands:
#         print('comando reconhecido')
#         if command == 'create':
#             create_work()
#         elif command == 'verify':
#             lint_work()
#         elif command == 'break':
#             quit()
#     else:
#         print('comando desconhecido')



# def create_work():
#     def listen():
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             speak('Im hearing...')
#             audio = r.listen(source,phrase_time_limit=60000,timeout=500)
#             print('...')
#         try:
#             command = r.recognize_sphinx(audio)
#             return command        
#         except	sr.UnknownValueError:
#             print('Occurred an error!')
#         except sr.RequestError as err:
#             print(f"Could not access voice recognizing service \n {err}")

#     speak('Give me details about the work!')
#     work_details = listen()
#


# def lint_work():
#     pass


# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak('Im hearing...')
#         audio = r.listen(source)
#         print('...')
#     try:
#         command = r.recognize_sphinx(audio)
#         do_task_for_command(command)
#         listen()
        
#     except	sr.UnknownValueError:
#         print('Occurred an error!')
#     except sr.RequestError as err:
#         print(f"Could not access voice recognizing service \n {err}")
    




