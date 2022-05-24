#Instrucciones
#Ingrese las locaciones del Radar de velocidad: A - B - C
#Ingrese el estado del Radar de velocidad: Apagado = 0 | Encendido = 1

def radarVelocidad():
    #Inicializar el estado del objeto
    #Apagado = 0 | Encendido = 1
    print('------------------------------------------------------------------')
    objetivo_radar ={'A': '0', 'B': '0', 'C': '0'}
    costo = 0
    
    ubicacionRadar = input("Ingrese la ubicación del Radar de Velocidad: A - B - C: ") #ubicaciòn del Radar de velocidad
    print('------------------------------------------------------------------')

    estadoRadarA = input('Ingrese el estado del Radar de Velocidad de ' + ubicacionRadar + ': ') #estado del Radar de velocidad apagado y encendido 
    estadoRadar_complementoB = input('Ingrese el estado del Radar de Velocidad de la ubicación: ') #estado del Radar de velocidad apagado y encendido 
    estadoRadar_complementoC = input('Ingrese el estado del Radar de Velocidad de la ubicación: ') #estado del Radar de velocidad apagado y encendido 
    print('------------------------------------------------------------------')
    print('------------------------------------------------------------------')
    print('-> Objetivo de Radar de velocidad: ' + str(objetivo_radar))
    print('------------------------------------------------------------------')
    print('------------------------------------------------------------------')
    if ubicacionRadar == 'A':
        print("-> Radar de Velocidad ubicación A: ")
        print('------------------------------------------------------------------')
        if estadoRadarA == '1':
            print("-> Ubicación A está capturando Foto Vehicular.")
            print('------------------------------------------------------------------')
            # encendido y marcar como foto obtenida
            objetivo_radar['A'] = '0'
            costo += 1#incremento de costo A
            print("-> Identifica Vehiculo: CAPTURANDO..")
            print('------------------------------------------------------------------')
            print("-> Costo actual: " + str(costo))
            objetivo_radar['A'] = '0'
            costo += 1 #incremento de costo por capturar
            print('------------------------------------------------------------------')
            print("-> Foto Vehicular Obtenida")
            print("-> Costo Actual: " + str(costo))

            if estadoRadar_complementoB == '1':
                # Si B está encendido
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                print("-> Radar de Velocidad ubicación B: ")
                print('------------------------------------------------------------------')
                print("-> Ubicación B está capturando Foto Vehicular.")
                print('------------------------------------------------------------------')
                print("-> Identifica Vehiculo: CAPTURANDO.. ")
                print('------------------------------------------------------------------')
                costo += 1 #Incrementa el costo al obtener foto vehicular
                print("-> Costo Actual: " + str(costo))
                # encendido y marcar como foto obtenida
                objetivo_radar['B'] = '0'
                costo += 1 #incremento de costo por capturar
                print('------------------------------------------------------------------')
                print("-> Foto Vehicular Obtenida")
                print("-> Costo Actual: " + str(costo))
            else:
                # captura y se apaga el radar
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                print("-> Locación B del Radar Vehicular no ha capturado foto")
                print('------------------------------------------------------------------')
                print("-> Foto no capturada, Costo actual: " + str(costo))

            if estadoRadar_complementoC == '1':
                # Si C está encendido
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                print("-> Radar de Velocidad ubicación B: ")
                print('------------------------------------------------------------------')
                print("-> Ubicación C está capturando Foto Vehicular.")
                print('------------------------------------------------------------------')
                print("-> Identifica Vehiculo: CAPTURANDO.. ")
                costo += 1 #Incrementa el costo al obtener foto vehicular
                print('------------------------------------------------------------------')
                print("-> Costo Actual: " + str(costo))
                # encendido y marcar como foto obtenida
                objetivo_radar['C'] = '0'
                costo += 1 #incremento de costo por capturar
                print('------------------------------------------------------------------')
                print("-> Foto Vehicular Obtenida")
                print("-> Costo Actual: " + str(costo))
            else:
                # captura y se apaga el radar
                print('------------------------------------------------------------------')
                print("-> Radar de Velocidad ubicación C: ")
                print('------------------------------------------------------------------')
                print("-> Locación C del Radar Vehicular no ha capturado foto")
                print('------------------------------------------------------------------')
                print("-> Foto no capturada, Costo actual: " + str(costo))
            
        if estadoRadarA == '0':
            print("-> Locación A del Radar Vehicular está apagado")
            if estadoRadar_complementoB == '1':# Si B está encendido
                print('------------------------------------------------------------------')
                print("-> Radar de Velocidad ubicación B: ")
                print('------------------------------------------------------------------')
                print("-> Ubicación B está capturando Foto Vehicular.")
                print('------------------------------------------------------------------')
                print("-> Identifica Vehiculo: CAPTURANDO..")
                print('------------------------------------------------------------------')
                costo += 1 #Incrementa el costo al obtener foto vehicular
                print("-> Costo Actual: " + str(costo))
                # encendido y marcar como foto obtenida
                objetivo_radar['B'] = '0'
                costo += 1   
                print('------------------------------------------------------------------')
                print("-> Foto Vehicular Obtenida")  
                print("-> Costo Actual: "+str(costo)) #Costo incrementa
            else:
                print('------------------------------------------------------------------')
                print("-> Sin acción: " + str(costo))
                # captura y se apaga el radar
                print('------------------------------------------------------------------')
                print("-> Radar de Velocidad ubicación B: ")
                print('------------------------------------------------------------------')
                print("-> Locación B del Radar Vehicular está apagado")
                print('------------------------------------------------------------------')
                print("-> Sin acción: " + str(costo))

            if estadoRadar_complementoC == '1':# Si B está encendido
                print('------------------------------------------------------------------')
                print("-> Radar de Velocidad ubicación C: ")
                print('------------------------------------------------------------------')
                print("-> Ubicación C está capturando Foto Vehicular.")
                print('------------------------------------------------------------------')
                print("-> Identifica Vehiculo: CAPTURANDO..")
                costo += 1 #Incrementa el costo al obtener foto vehicular
                print('------------------------------------------------------------------')
                print("-> Costo Actual: " + str(costo))
                # encendido y marcar como foto obtenida
                objetivo_radar['C'] = '0'
                costo += 1   
                print('------------------------------------------------------------------')
                print("-> Foto Vehicular Obtenida") #Costo incrementa
                print("-> Costo Actual: "+str(costo))
            else:
                print('------------------------------------------------------------------')
                print("-> Radar de Velocidad ubicación C: ")
                print('------------------------------------------------------------------')
                print("-> Locación C del Radar Vehicular está apagado")
                print('------------------------------------------------------------------')
                print("-> Sin acción: " + str(costo))
                # captura y se apaga el radar
                

    else:
        print('------------------------------------------------------------------')
        print("-> Radar Vehicular se encuentra en la locación A")
        # Locación A está encendido
        if estadoRadarA == '1':
            print('------------------------------------------------------------------')
            print("-> Radar Vehicular se enciende en locación A.")
            # encendido y marcar como foto obtenida
            objetivo_radar['A'] = '0'
            costo += 1  # incremento de costo A
            print('------------------------------------------------------------------')
            print("-> Foto Vehicular A " + str(costo))
            print('------------------------------------------------------------------')
            print("-> Radar Vehicular locación ha capturado")

            if estadoRadar_complementoB == '1':
                # Locación B está encendido
                print('------------------------------------------------------------------')
                print("-> Radar Vehicular se encuentra en la locación B.")
                print('------------------------------------------------------------------')
                print("-> Radar Vehicular se enciende en locación B.")
                costo += 1  # incremento de costo por capturar
                print('------------------------------------------------------------------')
                print("-> Costo por acción: " + str(costo))
                # suck the dirt and mark it as clean
                objetivo_radar['B'] = '0'
                costo += 1  # incremento de costo por capturar
                print('------------------------------------------------------------------')
                print("-> Foto Vehicular B" + str(costo))
                print('------------------------------------------------------------------')
                print("-> Radar Vehicular locación ha capturado")
            else:
                # encendido y marcar como foto obtenida
                print('------------------------------------------------------------------')
                print("-> Locación B del Radar Vehicular está apagado")
            
            if estadoRadar_complementoC == '1':
                # Locación C está encendido
                print('------------------------------------------------------------------')
                print("-> Radar Vehicular se encuentra en la locación C.")
                print('------------------------------------------------------------------')
                print("-> Radar Vehicular se enciende en locación C.")
                print('------------------------------------------------------------------')
                costo += 1  # incremento de costo por capturar
                print("-> Costo por acción: " + str(costo))
                # encendido y marcar como foto obtenida
                objetivo_radar['C'] = '0'
                costo += 1  # incremento de costo por capturar
                print('------------------------------------------------------------------')
                print("-> Foto Vehicular C" + str(costo))
                print('------------------------------------------------------------------')
                print("-> Radar Vehicular locación ha capturado")
            else:
                # encendido y marcar como foto obtenida
                print('------------------------------------------------------------------')
                print("-> Locación C del Radar Vehicular está apagado")

                if estadoRadar_complementoB == '1':  # Locación A está encendido
                    print('------------------------------------------------------------------')
                    print("-> Radar Vehicular se encuentra en la locación A")
                    print('------------------------------------------------------------------')
                    print("-> Radar Vehicular se enciende en locación A.")
                    costo += 1  # incremento de costo A
                    print("-> Costo por acción: " + str(costo))
                    # encendido y marcar como foto obtenida
                    objetivo_radar['A'] = '0'
                    costo += 1  # incremento de costo A
                    print('------------------------------------------------------------------')
                    print("-> Foto Vehicular A: " + str(costo))
                    print("-> Radar Vehicular locación ha capturado ")
                else:
                    print('------------------------------------------------------------------')
                    print("-> Sin acción: " + str(costo))
                    # encendido y marcar como foto obtenida
                    print('------------------------------------------------------------------')
                    print("-> Locación A del Radar Vehicular está apagado")
    
    # captura de foto realizada
    print('------------------------------------------------------------------')
    print('------------------------------------------------------------------')
    print("OBJETIVO DEL RADAR VEHICULAR: ")
    print(objetivo_radar)
    print("Desempeño del Radar Vehicular: " + str(costo))
    print('------------------------------------------------------------------')
    print('------------------------------------------------------------------')

                
radarVelocidad()