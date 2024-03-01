# import pyttsx3
import speech_recognition as sr
import openai

# SINTETIZADOR DE VOZ ================================================
# def speak_chatbot(audio):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 200) # número de palavras por minuto
#     engine.setProperty('volume', 1) # min: 0, max: 1
    
#     print("Chatbot Falando:", audio)
#     engine.say(audio)
#     engine.runAndWait()

# RECONHECIMENTO DE FALA ================================================
def listen_microphone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        audio = microfone.listen(source)
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    except sr.RequestError as e:
        print("Erro ao se comunicar com o serviço de reconhecimento de fala; {0}".format(e))
    return frase

# API OPENAI ================================================
def retorna_resposta_modelo(mensagens,
                            openai_key,
                            modelo='gpt-3.5-turbo',
                            temperatura=0):
    openai.api_key = openai_key
    completion = openai.chat.completions.create(
        model=modelo,
        messages=mensagens,
        temperature=temperatura,
    )

    return completion.choices[0].message.content