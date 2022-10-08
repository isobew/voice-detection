import speech_recognition as sr

import os


#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:

        #chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        #frase para o usuário dizer algo
        print("Fala alguma coisa ae meu consagrado")
        
        #armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:

        #passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio,language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")

        elif "Excel" in frase:
            os.system("start Excel.exe")

        elif "Quem é Lolly?" in frase:
            print("É a dona dessa casa toda")

        #Retorna a frase pronunciada
        print("Você disse: " + frase)
    
    #Se não reconheceu o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi o quê que tu disse ae, repete")

    return frase

ouvir_microfone()