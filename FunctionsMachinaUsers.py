import socket
from datetime import date
from datetime import datetime
def GenerateEvent(lEvents,NombreEvento,sType):
    '''Genera el evento de log in o log out de cada usuario en una maquina
    Pre: La funcion recive como parametro la lista de eventos sucedidos, el tipo de evento (log in o log out) y el nombre que el evento recibe, ademas
    dentro de la funcion se solicita ingresar el nombre de usuario
    Pos: No se retorna nada, solamente se agrega a la lista de eventos, el nuevo evento
    '''
    sMachine=socket.gethostname()
    sUser=input("Ingrese el nombre de usuario por favor:")
    #sType=0
    #while sType!="login" or sType!="logout":
    #    sType=lower(input("Ingrese login o logout segun corresponda:"))
        
    NombreEvento=Events(sMachine,sUser,sType)
    lEvents.append(NombreEvento)  
    
def GetEventDate(cEvent):
    return cEvent.sDate
    
def CurrentUsers(lEvents):
    '''
    Esta funcion itera sobre todos los eventos de las maquinas, ordenandolos por fecha con la funcion sort, para luego armar con el apoyo de cada evento, un diccionario que muestre
    el estado actual de cada maquina con respecto a sus usuarios.
    Pre: Recibe una lista de eventos
    Pos: Retorna el diccionario con los usuarios conectados en cada maquina
    '''
    lEvents.sort(key=GetEventDate)
    dMachines={}
    for sEvent in lEvents:
        if sEvent.sMachine not in dMachines:
            dMachines[sEvent.sMachine]=set()
        if sEvent.sType=="login":
            dMachines[sEvent.sMachine].add(sEvent.sUser)
        else:
            dMachines[sEvent.sMachine].remove(sEvent.sUser)
    return dMachines

def PrintCurrentUsers(dMachines): #GenerateReport
    '''
    Esta funcion se encarga de generar un reporte de cada uno de los equipos que se encuentran en el diccionario
    Pre: Se ingresa como parametro el diccionario con las maquinas y sus usuarios
    Pos: Se hace un prin de cada maquina y sus usuarios
    '''
    for sMachine,setUsers in dMachines.items():
        if len(setUsers)>0:
            #sUserList=", ".join(setUsers)
            #print("{}: {}".format(sMachine+sUserList))
            print(sMachine+":")
            for sUser in setUsers:
                print("-> "+sUser)
                
class Events:
    def __init__(self,sMachine,sUser,sType):
        self.sDate=datetime.now()
        self.sMachine=sMachine
        self.sUser=sUser
        self.sType=sType
        
    def __str__(self):
        if sType.lower()=="login":
            sState="in"
        else:
            sState="off"
        return "The user {} is {} the machine {}.".format(sUser,sState,sMachine)

            
