from datetime import datetime
from selenium import webdriver
import sys
from time import sleep
from pytube import YouTube




def pesquisar_Google():#PESQUISA DO GOOGLE
    pesquisar = input('O que você quer pesquisar?\n:')
    url = 'https://google.com/search?q=' + pesquisar
    print("Só um momento por favor")
    sleep(5)
    driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    driver.get(url)
    print('Aqui está oque eu achei!!!')

def localizar_Maps():#PESQUISA GOOGLE MAPS
    location = input('Qual o lugar deseja localizar?\n:')
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    print("Só um momento por favor")
    sleep(5)
    driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    driver.get(url)
    print('Aqui está a localização de' + location)

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

def downtube():#BAIXA VIDEOS DO YOUTUBE PELO LINK FORNECIDO
    url = input('Me informe o link do video por favor..\n:')
    youtube = YouTube(url)
    stram = youtube.streams.first()
    print('Estou baixando o video')
    stram.download()
    print('Download completo!!!')





def respond(voce):#AQUI REALIZA AS FUNÇÕES QUE SÃO REQUISITADAS PELO USUARIO, AS FUNÇÕES INCLUEM(SE APRESENTAR,ABRIR VIDEO NO YOUTUBE, PESQUISAR NO GOOGLE, PESQUISAR UM LUGAR)
    nome = ['seu', 'nome', 'Qual seu nome?']
    pesquisas = ['pesquisar', 'Google', 'Pesquisar no google']
    maps = ['localizar', 'google maps', 'procure no google maps']
    video = ['video', 'abrir youtube', 'eu quero assistir um video']
    download = ['download','baixar','baixar video', 'baixe esse video']
    

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
    elif voce in ['sair']:#SAIR DO PROGRAMA
        print('Até mais!')
        sys.exit()

def hanna_quest():
    print(' Olá meu nome é Hanna, sua assistente virtual!!\n No momento estou realizando as seguintes tarefas:\n Pesquisas no google, Pesquisas no Youtube, Pesquisas no GoogleMaps.\n Por favor me diga como posso ajudar??')
    voce = input(' :')
    respond(voce)

hanna_quest()