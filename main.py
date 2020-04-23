from datetime import datetime
from selenium import webdriver
import sys
from time import sleep
from pytube import YouTube
import googletrans
from googletrans import Translator


def tradutor():
    translator = Translator()
    language_list = print('As linguas que sei falar no momento são:\n')
    sleep(2)
    print(googletrans.LANGUAGES)
    sleep(2)
    lg = input('Para qual idioma deseja traduzir?')
    if lg in (googletrans.LANGUAGES):
        texto = input('O que deseja traduzir:\n-->')
        traduzido = translator.translate(texto, dest=lg)
        print(traduzido.text)
        again = input('Deseja traduzir mais alguma coisa?')
        if again == 'sim':
            tradutor()
        else:
            pass
    else:
        print('Eu não conheço este idioma, por favor insira outro idioma')
        tradutor()
    sleep(5)    
def pesquisar_Google():#PESQUISA DO GOOGLE
    pesquisar = input('O que você quer pesquisar?\n:')
    url = 'https://google.com/search?q=' + pesquisar
    print("Só um momento por favor")
    sleep(5)
    driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    driver.get(url)
    print('Aqui está oque eu achei!!!')
    sleep(5)

def localizar_Maps():#PESQUISA GOOGLE MAPS
    location = input('Qual o lugar deseja localizar?\n:')
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    print("Só um momento por favor")
    sleep(5)
    driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    driver.get(url)
    print('Aqui está a localização de' + location)
    sleep(5)

def youtube_Video():#ABRE VIDEOS DO YOUTUBE/BAIXA TAMBÉM
    download = ['download','baixar','baixar video', 'baixe esse video']
    video = input('Qual video deseja assistir?\n:')
    print('Irei procurar imediatamente')
    sleep(5)
    driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    url = "https://www.youtube.com/results?search_query=" + video
    sleep(10)
    driver.get(url)
    sleep(15)      
    vd = driver.find_element_by_id('video-title')
    vd.click()
    sleep(10)
    print('Deseja baixar esse video?')
    dld = input(':')
    if dld == 'sim':
        video_url = driver.current_url
        yt = YouTube(video_url)
        title = yt.title
        x = print(title + '\nIrei baixar este video..')       
        stream = yt.streams.first()
        stream.download()
        print('Dowload completo!!!')            
    else:
        print('Poderia me ajudar me informando o link do video por favor?')
        url = input(':')
        yt = YouTube(url)
        stream = yt.streams.first()
        print('Baixando o video!!')
        stream.download()
        print("Download Completo")
    sleep(5)

def downtube():#BAIXA VIDEOS DO YOUTUBE PELO LINK FORNECIDO
    url = input('Me informe o link do video por favor..\n:')
    youtube = YouTube(url)
    stram = youtube.streams.first()
    print('Estou baixando o video')
    stram.download()
    print('Download completo!!!')
    sleep(5)
    again = input('Deseja baixar mais algum video?')
    if again == 'sim':
        downtube()
    else:
        sleep(5)
        pass





def respond(voce):#AQUI REALIZA AS FUNÇÕES QUE SÃO REQUISITADAS PELO USUARIO, AS FUNÇÕES INCLUEM(SE APRESENTAR,ABRIR VIDEO NO YOUTUBE, PESQUISAR NO GOOGLE, PESQUISAR UM LUGAR)
    nome = ['seu', 'nome', 'Qual seu nome?']
    pesquisas = ['pesquisar', 'Google', 'Pesquisar no google']
    maps = ['localizar', 'google maps', 'procure no google maps']
    video = ['video', 'abrir youtube', 'eu quero assistir um video']
    download = ['download','baixar','baixar video', 'baixe esse video']
    traduzir = ['traduza', 'eu quero traduzir', 'traduzir', 'tradutor']
    

    if voce in nome:
        print('Meu nome é Hanna, prazer em te conhecer!!') 
        hanna_quest()   
    elif voce in pesquisas:#FAZ PESQUISAS NO GOOGLE
        pesquisar_Google()
        hanna_quest()
    elif voce in maps:#FAZ PESQUISAS NO GOOGLE MAPS
        localizar_Maps()
        hanna_quest()
    elif voce in video:#ABRE VIDEOS NO YOUTUBE
        youtube_Video()
        hanna_quest()
    elif voce in download:#DOWNLOAD DE VIDEOS DO YOUTUBE
        qst = input('Voce tem o link do video?')
        if qst == 'sim':
            downtube()
        else:
            youtube_Video()
    elif voce in traduzir:
        tradutor()
    elif voce in ['sair']:#SAIR DO PROGRAMA
        print('Até mais!')
        sys.exit()

sleep(1)
while 1:
    print(' Olá meu nome é Hanna, sua assistente virtual!!\n No momento estou realizando as seguintes tarefas:\n Pesquisas no google, Pesquisas e Download do Youtube, Pesquisas no GoogleMaps e Tradução de textos.\n Por favor me diga como posso ajudar??')
    voce = input(' :')
    respond(voce)

