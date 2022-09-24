import FunctionsMachinaUsers
'''
Este programa se trata de un programa encargado de registrar usuarios en ciertas maquinas a traves de eventos, para luego imprimir un reporte de que usuarios se encuentran activos en
cada maquina.
pre: Eventos(Maquina,Usuario,Fecha y hora, Login o logout)
pos: Reporte con los usuarios conectados en cada maquina
'''


def main():
    print("Hola! Bienvenidos a un nuevo dia!")
    lEvents=[]
    while True:
        sContinue=input("Si desea iniciar sesion con un usuario en esta maquina, presione 1.\nSi desea cerrar una sesion, presione 2\nSi desea terminar el dia, presione 3:")
        if sContinue=="1" or sContinue=="2":
            AuxNum=len(lEvents)
            if sContinue=="1":
                sType="login"
            else:
                sType="logout"
            FuncionesMachinayUsers.GenerateEvent(lEvents,"Evento"+str(AuxNum),sType)
        elif sContinue=="3":
            dMachines=FuncionesMachinayUsers.CurrentUsers(lEvents)
            FuncionesMachinayUsers.PrintCurrentUsers(dMachines)
            break
        else:
            print("Ingreso un valor invalido, intentelo nuevamente.")

if __name__=="__main__":
    main()