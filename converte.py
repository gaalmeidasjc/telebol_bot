from getAPI import *

def converte(time):
    times = getTeam(time)
    resultado = []
    resultado.append("Time: "+times['strTeam'])
    resultado.append("Esporte: "+times['strSport'])
    resultado.append("Liga: "+times['strLeague'])
    resultado.append("Divisão: "+times['strDivision'])
    resultado.append("Estadio: "+times['strStadium'])
    resultado.append("Local: "+times['strStadiumLocation'])
    resultado.append("Site: "+times['strWebsite'])
    string = ""
    for i in resultado:
        string += i + "\n"
    print(resultado)
    return string
    
    
