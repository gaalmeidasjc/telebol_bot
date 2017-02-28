import json, requests

time={}


def getTagAPI(h): #Faz toda a manipulação da string(h) baixada da API
	tam=0
	ult=0

	fim=h.find(':')

	tag=h[tam+1:fim-1]
	tam=fim
	
	fim=h.find(',')
	if fim==-1:
		fim=-3
		ult=1
	key=h[tam+1:fim]#tam+2 fim-1
	key=key.replace('"',"")

	if key=="ul":
		key="-"
	
	if fim!=-3:
		h=h[fim+1:]

		tam=0
		fim=0
	return [tag, key, h, ult]
	

def getTeam(nomeTime):#Função inicial para setar o time
	global time

	response = requests.get('http://thesportsdb.com/api/v1/json/1/searchteams.php?t='+nomeTime)		

	text=response.content
	textAPI=text.decode('utf-8')

	if textAPI=='{"teams":null}':
		return -1
		
	textAPI=(textAPI[11:])#retira caracteres desnecessários

	while True:
		temp=getTagAPI(textAPI)

		time[temp[0]]=temp[1]
		textAPI=temp[2]

		if temp[3]==1:
			break
	return time

def ultAdver():#Pega os ultimos 5 adversários
	global time
	final=""
	
	response = requests.get('http://thesportsdb.com/api/v1/json/1/eventslast.php?id='+time['idTeam'])		

	text=response.content
	textAPI=text.decode('utf-8')

			
	textAPI=(textAPI[13:])

	while True:
		temp=getTagAPI(textAPI)

		tag = temp[0]
		key = temp[1]
		textAPI = temp[2]

		if tag=="strFilename":
			final+=key
		if tag=="intHomeScore":
			final+=" ("+key+' x '
		if tag=="intAwayScore":
			final+=key+")\n"
		if tag=="strHomeGoalDetails":
			if key!="":
				final+="\tCasa: "+key+" "
			else:
				final+="\t"
		if tag=="strAwayGoalDetails":
			if key!="":
				final+="Visitante: "+key+"\n"
			else:
				final+='\n'
			
		
		if temp[3]==1:
			break
	return final

def adver():#Pega todos os adversários
	global time
	final=""

	response = requests.get('http://thesportsdb.com/api/v1/json/1/searchevents.php?e='+time['strTeam'])		

	text=response.content
	textAPI=text.decode('utf-8')

			
	textAPI=(textAPI[13:])

	while True:
		temp=getTagAPI(textAPI)

		tag = temp[0]
		key = temp[1]
		textAPI = temp[2]

		if tag=="strFilename":
			final+=key
		if tag=="intHomeScore":
			final+=" ("+key+' x '
		if tag=="intAwayScore":
			final+=key+")\n"
		if tag=="strHomeGoalDetails":
			if key!="":
				final+="\tCasa: "+key+" "
			else:
				final+="\t"
		if tag=="strAwayGoalDetails":
			if key!="":
				final+="Visitante: "+key+"\n"
			else:
				final+="\n"
		
		if temp[3]==1:
			break
	return final

def nextAdver():#Pega todos os proximos adversários
	global time
	final=""

	response = requests.get('http://thesportsdb.com/api/v1/json/1/eventsnext.php?id='+time['idTeam'])		

	text=response.content
	textAPI=text.decode('utf-8')

	if textAPI=='{"events":null}':
		return "Próximos jogos indisponíveis"

			
	textAPI=(textAPI[13:])

	while True:
		temp=getTagAPI(textAPI)

		tag = temp[0]
		key = temp[1]
		textAPI = temp[2]

		if tag=="strFilename":
			final += key + "\n"
		
		if temp[3]==1:
			break
	return final

def tabela():
	final=""

	response = requests.get("http://thesportsdb.com/api/v1/json/1/lookuptable.php?l=4351")		

	text=response.content
	textAPI=text.decode('utf-8')
	
	textAPI=textAPI[11:]

	textAPI = textAPI.replace("{","")
	textAPI = textAPI.replace("}","")
	
	while True:
		temp=getTagAPI(textAPI)

		tag = temp[0]
		key = temp[1]
		textAPI = temp[2]

		if len(key)==1:
			key="0"+key

		if tag=="name":
			if len(key)<8:
				key+=" "*int(8-len(key))
			final += key + '\t'
		if tag=='played':
			final += key + " "
		if tag=="goalsdifference":
			final += key + " "
		if tag=="win":
			final += key + " "
		if tag=="total":
			final += str(key) + "\n"
	
		if temp[3]==1:
			break
		
	return final



def liveScore():
	jogos={}

	response = requests.get('http://thesportsdb.com/api/v1/json/1/latestsoccer.php')		

	text=response.content
	textAPI=text.decode('utf-8')

			
	textAPI=(textAPI[13:])

	while True:
		temp=getTagAPI(textAPI)

		tag = temp[0]
		key = temp[1]
		textAPI = temp[2]

		jogos[tag]=key

		if tag=="strFilename":
			print(key, end='')
		
		if temp[3]==1:
			break
	return jogos
# Live Score http://thesportsdb.com/api/v1/json/1/latestsoccer.php
#tabela: http://thesportsdb.com/api/v1/json/1/lookuptable.php?l=4351
#adversarios antigos'http://thesportsdb.com/api/v1/json/1/searchevents.php?e='+time['strTeam']
#next http://thesportsdb.com/api/v1/json/1/eventsnext.php?id=






