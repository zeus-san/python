import telepot
import sys
#obter alguns dados da mensagem
def dados(id_men):
    tipochat=response[id_men]['message']['chat']['type']
    texto=response[id_men]['message']['text']
    nome=response[id_men]['message']['from']['username']
    nome=nome+'@'
    return {'nome':nome,'tip_chat':tipochat,'men_b':texto}
    
#falar para o telegram nao manda mensagens antigas  
def fim():
    lido=response[n_mensagem - 1]['update_id']
    robo.getUpdates(offset=lido)
#tamanho da lista
def t(lista):
    tamanho=len(lista)
    return tamanho
def resultado():
    pass
def help():
    ajuda="cartas sao feitas no formato nome>dano>magia>descriçao"
    exemplo="/start"
    
def obt_card(texto):
    bruto=texto.split('°')
    dano=bruto[1]
    magia=bruto[2]
    return {'dano':dano,'magia':magia}

def baixar_men():
    from pprint import pprint
    response = robo.getUpdates()
    pprint(response)
    return response

def comando(indentificaçao):
    texto=response[indentificaçao]['message']['text']
    texto=texto.split(' ')
    return texto[0]
    
    

robo = telepot.Bot('1301046600:AAGV_-F4fKNr4cIuByFVAuLVS2kEh5hFXrw')
#baixar mesagens
response=baixar_men()
#numero de mensagens
n_mensagem = t(response)
    

if comando(2) == '/julgar':
        
        if comando(0) ==  comando(1):
            #cartas contem nome,tipo de chta e texto
            carta1=dados(response[0])
            carta2=dados(response[1])
            #card possuem apenas dano magia
            card1=obt_card(carta1['men_b'])
            card2=obt_card(carta2['men_b'])

if comando(-1) == '/start@leitor_de_card_bot' and :
    print(1)
            

  
    

