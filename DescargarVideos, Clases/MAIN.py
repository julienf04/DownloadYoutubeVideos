import pytube
import os
from timeit import time
import Video_Class
import PlayList_Class


ytVideo = None
ytPlayList = None
link = ""
respuesta = ""

listaDeVideosConModificaciones = []
listIndexDelVideoConModificaciones = []
numeroDeModificacion = None


############################################### FUNCIONES PARA TODO EL PROGRAMA ###############################################

def BuenDiaPongaLink():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   Hola, buen dia. Con este programa vas a poder descargar videos o Playlist de Youtube, o simplemente el audio")
    print("   de los mismos, si asi lo deseas")
    print()
    print("   Por favor, pone el link del video o Playlist que quieras descargar")
    print()
    link = input("   ")

    while True:
        try:
            print()
            print("   Buscando video...")
            ytVideo = Video_Class.Video(link)
            print()
            print("   Video encontrado!")
            break
        except:
            try:
                print()
                print("   Buscando Playlist...")
                ytPlayList = PlayList_Class.PlayList(link)
                print()
                print("   Playlist encontrada!")
                break
            except:
                print()
                print("   El link que colocaste no fue encontrado. Por favor, intentelo de nuevo")
                print()
                link = input("   ")
                continue


def ElVideoSeDescargaConLasSiguientesCaracteristicas(ceroOuno):
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   El video se descargara con las siguientes caracteristicas. Desea modificar alguna? Responda con SI o con NO.")
    if ceroOuno == 0:
        print("   Si su respuesta es NO (no desea modificar ninguna caracteristica), el video se descargara automaticamente.")
    print("   Si necesita mas informacion para entender cada una de las caracteristicas, solamente ponga la palabra INFO.")
    print()
    print()
    ytVideo.ShowFeatures()
    print()
    respuesta = input("   ")


def LaPlaylistSeDescargaConLasSiguientesCaracteristicas():
    global ytVideo
    global ytPlayList
    global link
    global respuesta
    
    print("   La Playlist se descargara con las siguientes caracteristicas. Desea modificar alguna? Responda con SI o con NO.")
    print("   Si su respuesta es NO (no desea modificar ninguna caracteristica), la Playlist se descargara automaticamente.")
    print("   Si necesita mas informacion para entender cada una de las caracteristicas, solamente ponga la palabra INFO.")
    print()
    print("   Extra: si deseas cambiar los parametros de un unico video, solamente coloque el numero del video que corresponde en")
    print("   la Playlist. Por ejemplo, si solamente deseas cambiar los parametros del primer video de la Playlist, escribi el numero 1")
    print("   Los demas videos que no sean ese, se descargaran con los parametros base")
    print()
    print()
    ytPlayList.ShowFeatures()
    print()
    respuesta = input("   ")


def ParaContinuarPongaSIoNOoINFOoINFORMACIONoLoDemas(ceroOuno):
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   Debe poner alguna de las siguientes palabras para continuar, dependiendo de lo que desee:")
    print()
    print("   SI: para cambiar algun parametro")
    if ceroOuno == 0:
        print("   NO: para descargar automaticamente")
    else:
        print("   NO: para guardar los parametros actuales del video")
    print("   INFO: para obtener mas informacion de cada una de las caraceristicas con las cuales se descargara el video")
    print()
    respuesta = input("   ")


def ParaContinuarPongaSIoNOoINFOoINFORMACIONoLoDemasParaPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   Debe escribir alguna de las siguientes opciones para continuar, dependiendo de lo que desee:")
    print()
    print("   SI: para cambiar algun parametro")
    print("   NO: para descargar automaticamente")
    print("   INFO: para obtener mas informacion de cada una de las caraceristicas con las cuales se descargara el video")
    print("   Numero del video en la Playlist: para cambiar los parametros de ese video solamente")
    print()
    respuesta = input("   ")


def PongaElParametroQueDeseaModificar(ceroOuno):
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    if ceroOuno == 0:
        if ytVideo.videoOrAudio == "video":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, RESOLUCION, FPS, RUTA DE DESCARGA, SOLO AUDIO)")
        elif ytVideo.videoOrAudio == "audio":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, RUTA DE DESCARGA, SOLO AUDIO)")
        print("   Si desea volver a poner las caracteristicas predeterminadas, simplemente ponga la palabra REINICIAR")
        print()
        respuesta = input("   ")
    elif ceroOuno == 1:
        if ytVideo.videoOrAudio == "video":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, RESOLUCION, FPS, RUTA DE DESCARGA, SOLO AUDIO)")
        elif ytVideo.videoOrAudio == "audio":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, RUTA DE DESCARGA, SOLO AUDIO)")
        print("   Si desea volver a poner las caracteristicas predeterminadas, simplemente ponga la palabra REINICIAR")
        print()
        respuesta = input("   ")


def PongaElParametroQueDeseaModificarPlaylist(ceroOuno):
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    if ceroOuno == 0:
        if ytPlayList.videoOrAudio == "video":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, CANTIDAD, RESOLUCION, FPS, RUTA DE DESCARGA, SOLO AUDIO)")
        elif ytPlayList.videoOrAudio == "audio":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, CANTIDAD, RUTA DE DESCARGA, SOLO AUDIO)")
        print("   Si desea volver a poner las caracteristicas predeterminadas, simplemente ponga la palabra REINICIAR")
        print()
        respuesta = input("   ")
    elif ceroOuno == 1:
        if ytPlayList.videoOrAudio == "video":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, CANTIDAD, RESOLUCION, FPS, RUTA DE DESCARGA, SOLO AUDIO)")
        elif ytPlayList.videoOrAudio == "audio":
            print("   Ponga el nombre del parametro que desea modificar (TITULO, CANTIDAD, RUTA DE DESCARGA, SOLO AUDIO)")
        print("   Si desea volver a poner las caracteristicas predeterminadas, simplemente ponga la palabra REINICIAR")
        print()
        respuesta = input("   ")


def MostraraMasInformacion():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    ytVideo.ShowInfo()
    print()
    print()
    print("-------------------------------------------")
    print()
    print("   Toque ENTER para continuar")
    print()
    input("   ")
    respuesta = ""


def MostraraMasInformacionPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    ytPlayList.ShowInfo()
    print()
    print()
    print("-------------------------------------------")
    print()
    print("   Toque ENTER para continuar")
    print()
    input("   ")
    respuesta = ""


def DescargarVideo():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   Descargando video...")
    print()
    print(ytVideo.yt.streams.filter(type = ytVideo.videoOrAudio, res = ytVideo.resolution, fps = ytVideo.fps))
    print()
    print()
    print(ytVideo.yt.streams.filter(type = ytVideo.videoOrAudio, res = ytVideo.resolution, fps = ytVideo.fps).first())
    ytVideo.yt.streams.filter(type = ytVideo.videoOrAudio, res = ytVideo.resolution, fps = ytVideo.fps).first().download(filename = ytVideo.title, output_path = ytVideo.pathDownload)
    print()
    print("   Video descargado con exito!")

def DescargarPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    rutaFinal = ytPlayList.pathDownload + "\\" + ytPlayList.title

    print("   Descargando Playlist...")

    p = 0
    for numeroParaDeletear in ytPlayList.listIndexOfDeleteUrl:
        numeroParaDeletear = numeroParaDeletear - 1
        ytPlayList.listIndexOfDeleteUrl[p] = numeroParaDeletear
        p += 1

    p = 0
    g = 1
    print(listIndexDelVideoConModificaciones)
    todosLosStreams = ytPlayList.GetAllVideos()
    for cadaUnoDeLosStreams in todosLosStreams:
        if not p in ytPlayList.listIndexOfDeleteUrl:
            if g in listIndexDelVideoConModificaciones:
                print()
                print()
                print("   ----- Descargando el video " + str(p + 1))
                print()
                listaDeVideosConModificaciones[0].yt.streams.filter(type = listaDeVideosConModificaciones[0].videoOrAudio, res = listaDeVideosConModificaciones[0].resolution, fps = listaDeVideosConModificaciones[0].fps).first().download(filename = listaDeVideosConModificaciones[0].title, output_path = listaDeVideosConModificaciones[0].pathDownload)

                del(listaDeVideosConModificaciones[0])
                listIndexDelVideoConModificaciones.remove(g)

            
            else:
                print()
                print()
                print("   ----- Descargando el video " + str(p + 1))
                print()
                cadaUnoDeLosStreams.filter(type = ytPlayList.videoOrAudio, res = ytPlayList.baseResolution, fps = ytPlayList.baseFps).first().download(output_path = rutaFinal)

        else:
            ytPlayList.listIndexOfDeleteUrl.remove(p)

        p += 1

    print()
    print("   Playlist descargada con exito!")



def CambiarElTitulo():
    global ytVideo
    global ytPlayList

    global link
    global respuesta

    print("   Ponga el titulo con el cual desea que aparezca el video descargado")
    print("   ( El titulo se refiere al nombre con el cual va a aparecer el video descargado en tus archivos )")
    print()
    respuesta = input("   ")

    ytVideo.ChangeTitle(respuesta)
    respuesta = ""


def CambiarElTituloPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   Ponga el titulo con el cual desea que aparezca la Playlist descargada")
    print("   ( El titulo se refiere al nombre con el cual va a aparecer la Playlist descargada en tus archivos )")
    print()
    respuesta = input("   ")

    ytPlayList.ChangeTitle(respuesta)
    respuesta = ""


def CambiarLaCantidadDeVideosDeLaPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta
    
    yaSeEjecutoElPrimero = False
    while True:

        print("   Ponga el numero que le corresponde al video dentro de la Playlist el cual desea que no se descargue")
        print("   (Por ejemplo, si deseas que el primer video de la Playlist no se descargue, pone el numero 1)")
        print()
        respuesta = input("   ")

        if respuesta.isnumeric() == False:
            print("   !!! Su respuesta debe ser un numero que represente el video el cual no queres que se descargue")
            print()
            continue
        elif int(respuesta) < 1 or int(respuesta) > ytPlayList.amountOfVideos:
            print("   !!! Su respuesta debe ser un numero entre el 1 y la cantidad de videos que tenga la Playlist")
            print()
            continue

        ytPlayList.ChangeAmountOfVideo(int(respuesta))
        respuesta = ""
        break



def CambiarResolucion():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    listaDeResolucionesSinLaP = []

    print("   Ponga la resolucion con la cual desea que aparezca el video descargado")
    print("   (La resolucion se refiere a la calidad de imagen con la cual se va a descargar el video en tus archivos)")

    print("   Aclaracion: las resoluciones disponibles dependen de los FPS que hayas elegido anteriormente, si es que los elegiste.")
    print("   Las resoluciones disponibles para este video son las siguientes: " + str(ytVideo.GetAllAvailableResolutions()))
    print()
    respuesta = input("   ")

    for resolution in ytVideo.GetAllAvailableResolutions():
        resolution = resolution[0:-1]
        listaDeResolucionesSinLaP.append(resolution)

    while not respuesta in ytVideo.GetAllAvailableResolutions() and not respuesta in listaDeResolucionesSinLaP:
        print()
        print("-------------------------------------------")
        print()
        print("   Por favor, la resolucion que elija para descargar el video debe estar disponible.")
        print("   Las resoluciones disponibles para este video son las siguientes: " + str(ytVideo.GetAllAvailableResolutions))
        print()
        respuesta = input("   ")

    if respuesta[-1] != "p":
        respuesta = str(respuesta) + "p"

    ytVideo.ChangeResolution(respuesta)
    respuesta = ""


def CambiarResolucionPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    listaDeResolucionesSinLaP = []

    print("   Ponga la resolucion base con la cual desea que aparezcan los videos de la Playlist descargados")
    print("   (La resolucion base se refiere a la calidad de imagen promedio con la cual se van a descargar los videos en tus archivos)")

    print("   Aclaracion: las resoluciones disponibles dependen de los FPS base que hayas elegido anteriormente, si es que los elegiste.")
    print("   Las resoluciones base disponibles para los videos de esta Playlist son las siguientes: " + str(ytPlayList.GetAvailableResolutions()))
    print()
    respuesta = input("   ")

    for resolution in ytPlayList.GetAvailableResolutions():
        resolution = resolution[0:-1]
        listaDeResolucionesSinLaP.append(resolution)

    while not respuesta in ytPlayList.GetAvailableResolutions() and not respuesta in listaDeResolucionesSinLaP:
        print()
        print("-------------------------------------------")
        print()
        print("   Por favor, la resolucion base que elija para descargar los videos debe estar disponible.")
        print("   Las resoluciones base disponibles para estos videos son las siguientes: " + str(ytPlayList.GetAvailableResolutions()))
        print()
        respuesta = input("   ")

    if respuesta[-1] != "p":
        respuesta = str(respuesta) + "p"

    ytPlayList.ChangeResolution(respuesta)
    respuesta = ""


def CambiarFPS():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   Ponga los FPS con los cuales desea que aparezca el video descargado")
    print("   (Los FPS se refieren a la cantidad de fotogramas por segundo con la cual se va a descargar el video en tus archivos.)")

    print("   Aclaracion: los FPS disponibles dependen de la resolucion que hayas elegido anteriormente, si es que la elegiste.")
    print("   La cantidad de FPS disponibles para este video son los siguientes: " + str(ytVideo.GetAllAvailableFps()))
    print()
    respuesta = input("   ")

    while respuesta.isnumeric() == False:
        print()
        print("-------------------------------------------")
        print()
        print("   Su respuesta debe ser un numero, que represente la cantidad de FPS.")
        print("   La cantidad de FPS disponibles para este video son los siguientes: " + str(ytVideo.GetAllAvailableFps()))
        print()
        respuesta = input("   ")

    while not int(respuesta) in ytVideo.GetAllAvailableFps():
        print()
        print("-------------------------------------------")
        print()
        print("   Por favor, la cantidad de FPS que elija para descargar el video deben estar disponibles")
        print("   La cantidad de FPS disponibles para este video son los siguientes: " + str(ytVideo.GetAllAvailableFps()))
        print()
        respuesta = input("   ")

        while respuesta.isnumeric() == False:
            print()
            print("-------------------------------------------")
            print()
            print("   Su respuesta debe ser un numero, que represente la cantidad de FPS.")
            print("   La cantidad de FPS disponibles para este video son los siguientes: " + str(ytVideo.GetAllAvailableFps()))
            print()
            respuesta = input("   ")


    ytVideo.ChangeFps(int(respuesta))
    respuesta = ""


def CambiarFPSPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print("   Ponga los FPS base con los cuales desea que aparezcan los videos descargados")
    print("   (Los FPS base se refieren a la cantidad de fotogramas por segundo promedio con la cual se va a descargar los videos en tus archivos.)")

    print("   Aclaracion: los FPS base disponibles dependen de la resolucion base que hayas elegido anteriormente, si es que la elegiste.")
    print("   La cantidad de FPS base disponibles para estos videos son los siguientes: " + str(ytPlayList.GetAvailableFps()))
    print()
    respuesta = input("   ")

    while respuesta.isnumeric() == False:
        print()
        print("-------------------------------------------")
        print()
        print("   Su respuesta debe ser un numero, que represente la cantidad de FPS base.")
        print("   La cantidad de FPS base disponibles para estos videos son los siguientes: " + str(ytPlayList.GetAvailableFps()))
        print()
        respuesta = input("   ")

    while not int(respuesta) in ytPlayList.GetAvailableFps():
        print()
        print("-------------------------------------------")
        print()
        print("   Por favor, la cantidad de FPS base que elija para descargar los videos deben estar disponibles")
        print("   La cantidad de FPS base disponibles para estos videos son los siguientes: " + str(ytPlayList.GetAvailableFps()))
        print()
        respuesta = input("   ")

        while respuesta.isnumeric() == False:
            print()
            print("-------------------------------------------")
            print()
            print("   Su respuesta debe ser un numero, que represente la cantidad de FPS base.")
            print("   La cantidad de FPS base disponibles para estos videos son los siguientes: " + str(ytPlayList.GetAvailableFps()))
            print()
            respuesta = input("   ")


    ytPlayList.ChangeFps(int(respuesta))
    respuesta = ""


def CambiarRutaDeDescarga():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print()
    print("-------------------------------------------")
    print()
    print("   Ponga la ruta de descarga en la cual desea que se descargue su video en los archivos")
    print("   (La ruta de descarga se refiere a la ruta (el lugar) en el que se va a descargar el video en tus archivos)")
    print("   TIP: Para poner su ruta de descarga, vaya a su explorador de archivos, toque un click en la carpeta en la que")
    print("   desee descargar el video. Luego presione 'Home', y luego 'Copy-path'. O en su defecto, lo mismo pero en español")
    print()
    respuesta = input("   ")

    while os.path.exists(respuesta) == False:
        print()
        print("-------------------------------------------")
        print()
        print("   No se pudo encontrar la ruta de descarga que puso. Por favor, vuelva a intentarlo")
        print()
        respuesta = input("   ")


    ytVideo.ChangePathDownloadForThisVideo(respuesta)
    respuesta = ""


    print()
    print("   Ruta de descarga cambiada!")
    print()
    print("-------------------------------------------")
    print()
    print("   Desea guardar esta ruta de descarga como un parametro predeterminado?")
    print("   Esto significa que en proximas veces que use el programa, se usara esta ruta de descarga como caracteristica predeterminada")
    print("   Responda con 'SI' si desea guardar la ruta de descarga, y responda con 'NO' si desea usar esta ruta solamente")
    print("   para esta descarga en particular")
    print()
    quiereGuardar = input("   ")

    while quiereGuardar.upper() != "SI" and quiereGuardar.upper() != "NO":
        print()
        print("-------------------------------------------")
        print()
        print("   La respuesta debe ser un SI o un NO")
        print("   SI: para configurar el parametro de la ruta de descarga del video, y para guardar la ruta para usarse en futuras descargas")
        print("   NO: para, solamente, configurar el parametro de la ruta de descarga del video")
        print()
        quiereGuardar = input("   ")

    if quiereGuardar.upper() == "SI":
        ytVideo.ChangePathDownloadConfiguration()

def CambiarRutaDeDescargaPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    print()
    print("-------------------------------------------")
    print()
    print("   Ponga la ruta de descarga en la cual desea que se descargue la Playlist en los archivos")
    print("   (La ruta de descarga se refiere a la ruta (el lugar) en el que se va a descargar la Playlist en tus archivos)")
    print("   TIP: Para poner su ruta de descarga, vaya a su explorador de archivos, toque un click en la carpeta en la que")
    print("   desee descargar el video. Luego presione 'Home', y luego 'Copy-path'. O en su defecto, lo mismo pero en español")
    print()
    respuesta = input("   ")

    while os.path.exists(respuesta) == False:
        print()
        print("-------------------------------------------")
        print()
        print("   No se pudo encontrar la ruta de descarga que puso. Por favor, vuelva a intentarlo")
        print()
        respuesta = input("   ")


    ytPlayList.ChangePathDonwload(respuesta)
    respuesta = ""


    print()
    print("   Ruta de descarga cambiada!")
    print()
    print("-------------------------------------------")
    print()
    print("   Desea guardar esta ruta de descarga como un parametro predeterminado?")
    print("   Esto significa que en proximas veces que use el programa, se usara esta ruta de descarga como caracteristica predeterminada")
    print("   Responda con 'SI' si desea guardar la ruta de descarga, y responda con 'NO' si desea usar esta ruta solamente")
    print("   para esta descarga en particular")
    print()
    quiereGuardar = input("   ")

    while quiereGuardar.upper() != "SI" and quiereGuardar.upper() != "NO":
        print()
        print("-------------------------------------------")
        print()
        print("   La respuesta debe ser un SI o un NO")
        print("   SI: para configurar el parametro de la ruta de descarga de la Playlist, y para guardar la ruta para usarse en futuras descargas")
        print("   NO: para, solamente, configurar el parametro de la ruta de descarga de la Playlist")
        print()
        quiereGuardar = input("   ")

    if quiereGuardar.upper() == "SI":
        ytPlayList.ChangePathDownloadConfiguration()



def CambiarSoloAudio():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    ytVideo.OnlyAudio()
    respuesta = ""


def CambiarSoloAudioPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta
    
    ytPlayList.OnlyAudio()
    respuesta = ""


def ReiniciarParametros():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    ytVideo.RestartFeatures()
    respuesta = ""

def ReiniciarParametrosPlaylist():
    global ytVideo
    global ytPlayList
    global link
    global respuesta

    ytPlayList.RestartFeatures()
    respuesta = ""




############################################### LA EJECUCION DEL PROGRAMA ###############################################


BuenDiaPongaLink()
print()
print("-------------------------------------------")
print()


while True:
    if ytVideo != None:

        while True:

            ElVideoSeDescargaConLasSiguientesCaracteristicas(0)
            print()
            print("-------------------------------------------")
            print()


            while respuesta.upper() != "SI" and respuesta.upper() != "NO" and respuesta.upper() != "INFO" and respuesta.upper() != "INFORMACION":
                
                ParaContinuarPongaSIoNOoINFOoINFORMACIONoLoDemas(0)
                print()
                print("-------------------------------------------")
                print()


            if respuesta.upper() == "SI":
                PongaElParametroQueDeseaModificar(0)
                print()
                print("-------------------------------------------")
                print()

                if ytVideo.videoOrAudio == "audio":
                    if respuesta.upper() == "RESOLUCION" or respuesta.upper() == "FPS":
                        respuesta = ""

                while respuesta.upper() != "TITULO" and respuesta.upper() != "RESOLUCION" and respuesta.upper() != "FPS" and respuesta.upper() != "RUTA DE DESCARGA" and respuesta.upper() != "RUTA" and respuesta.upper() != "SOLO AUDIO" and respuesta.upper() != "AUDIO" and respuesta.upper() != "REINICIAR":
                    
                    PongaElParametroQueDeseaModificar(1)

                    if ytVideo.videoOrAudio == "audio":
                        if respuesta.upper() == "RESOLUCION" or respuesta.upper() == "FPS":
                            respuesta = ""


                if respuesta.upper() == "TITULO":

                    CambiarElTitulo()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue

                elif respuesta.upper() == "RESOLUCION":
                    CambiarResolucion()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue



                elif respuesta.upper() == "FPS":
                    CambiarFPS()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue



                elif respuesta.upper() == "RUTA DE DESCARGA" or respuesta.upper() == "RUTA":
                    CambiarRutaDeDescarga()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue




                elif respuesta.upper() == "SOLO AUDIO" or respuesta.upper() == "AUDIO":
                    CambiarSoloAudio()
                    continue

                elif respuesta.upper() == "REINICIAR":
                    ReiniciarParametros()
                    continue




            elif respuesta.upper() == "INFO" or respuesta.upper() == "INFORMACION":

                MostraraMasInformacion()
                print()
                print("-------------------------------------------")
                print()
                continue
        


            elif respuesta.upper() == "NO":
                
                DescargarVideo()
                print()
                print("-------------------------------------------")
                print()
                break

        break





    elif ytPlayList != None:
        while True:
            LaPlaylistSeDescargaConLasSiguientesCaracteristicas()
            print()
            print("-------------------------------------------")
            print()

            while True:
                if respuesta.upper() != "SI" and respuesta.upper() != "NO" and respuesta.upper() != "INFO" and respuesta.upper() != "INFORMACION" and respuesta.isnumeric() == False:
                
                    ParaContinuarPongaSIoNOoINFOoINFORMACIONoLoDemasParaPlaylist()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue
                elif respuesta.isnumeric() == True:
                    if int(respuesta) < 1 and int(respuesta) > ytPlayList.amountOfVideos:
                        ParaContinuarPongaSIoNOoINFOoINFORMACIONoLoDemasParaPlaylist()
                        print()
                        print("-------------------------------------------")
                        print()
                        continue

                break


            if respuesta.upper() == "SI":
                PongaElParametroQueDeseaModificarPlaylist(0)
                print()
                print("-------------------------------------------")
                print()

                if ytPlayList.videoOrAudio == "audio":
                    if respuesta.upper() == "RESOLUCION" or respuesta.upper() == "FPS":
                        respuesta = ""

                while respuesta.upper() != "TITULO" and respuesta.upper() != "CANTIDAD" and respuesta.upper() != "RESOLUCION" and respuesta.upper() != "FPS" and respuesta.upper() != "RUTA DE DESCARGA" and respuesta.upper() != "RUTA" and respuesta.upper() != "SOLO AUDIO" and respuesta.upper() != "AUDIO" and respuesta.upper() != "REINICIAR":
                    
                    PongaElParametroQueDeseaModificarPlaylist(1)

                    if ytPlayList.videoOrAudio == "audio":
                        if respuesta.upper() == "RESOLUCION" or respuesta.upper() == "FPS":
                            respuesta = ""


                if respuesta.upper() == "TITULO":
                    CambiarElTituloPlaylist()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue


                elif respuesta.upper() == "CANTIDAD":
                    CambiarLaCantidadDeVideosDeLaPlaylist()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue

                elif respuesta.upper() == "RESOLUCION":
                    CambiarResolucionPlaylist()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue

                elif respuesta.upper() == "FPS":
                    CambiarFPSPlaylist()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue

                elif respuesta.upper() == "RUTA DE DESCARGA" or respuesta.upper() == "RUTA":
                    CambiarRutaDeDescargaPlaylist()
                    print()
                    print("-------------------------------------------")
                    print()
                    continue

                elif respuesta.upper() == "SOLO AUDIO" or respuesta.upper() == "AUDIO":
                    CambiarSoloAudioPlaylist()
                    continue

                elif respuesta.upper() == "REINICIAR":
                    ReiniciarParametrosPlaylist()
                    continue




            elif respuesta.isnumeric() == True:
                numeroDeModificacion = int(respuesta) - 1
                if not int(respuesta) in listIndexDelVideoConModificaciones:
                    listIndexDelVideoConModificaciones.append(int(respuesta))
                    indexRealDelVideoConModificaciones = int(respuesta) - 1

                    linkDelVideoParaModificar = ytPlayList.yt.video_urls[indexRealDelVideoConModificaciones]

                    ytVideo = Video_Class.Video(linkDelVideoParaModificar)

                    ytVideo.ChangePathDownloadForThisVideo(ytPlayList.pathDownload + "\\" + ytPlayList.title)

                else:
                    ytVideo = listaDeVideosConModificaciones[int(respuesta) - 1]
                    del (listaDeVideosConModificaciones[int(respuesta) - 1])


                while True:
                
                    ElVideoSeDescargaConLasSiguientesCaracteristicas(1)
                    print()
                    print("-------------------------------------------")
                    print()
                
                
                    while respuesta.upper() != "SI" and respuesta.upper() != "NO" and respuesta.upper() != "INFO" and respuesta.upper() != "INFORMACION":
                        
                        ParaContinuarPongaSIoNOoINFOoINFORMACIONoLoDemas(1)
                        print()
                        print("-------------------------------------------")
                        print()
                
                
                    if respuesta.upper() == "SI":
                        PongaElParametroQueDeseaModificar(0)
                        print()
                        print("-------------------------------------------")
                        print()
                
                
                        while respuesta.upper() != "TITULO" and respuesta.upper() != "RESOLUCION" and respuesta.upper() != "FPS" and respuesta.upper() != "RUTA DE DESCARGA" and respuesta.upper() != "RUTA" and respuesta.upper() != "SOLO AUDIO" and respuesta.upper() != "AUDIO" and respuesta.upper() != "REINICIAR":
                            
                            PongaElParametroQueDeseaModificar(1)
                
                
                        if respuesta.upper() == "TITULO":
                
                            CambiarElTitulo()
                            print()
                            print("-------------------------------------------")
                            print()
                            continue
                
                        elif respuesta.upper() == "RESOLUCION":
                            CambiarResolucion()
                            print()
                            print("-------------------------------------------")
                            print()
                            continue
                
                
                
                        elif respuesta.upper() == "FPS":
                            CambiarFPS()
                            print()
                            print("-------------------------------------------")
                            print()
                            continue
                
                
                
                        elif respuesta.upper() == "RUTA DE DESCARGA" or respuesta.upper() == "RUTA":
                            CambiarRutaDeDescarga()
                            print()
                            print("-------------------------------------------")
                            print()
                            continue
                
                
                
                
                        elif respuesta.upper() == "SOLO AUDIO" or respuesta.upper() == "AUDIO":
                            CambiarSoloAudio()
                            continue
                
                        elif respuesta.upper() == "REINICIAR":
                            ReiniciarParametros()
                            continue
                
                
                
                
                    elif respuesta.upper() == "INFO" or respuesta.upper() == "INFORMACION":
                
                        MostraraMasInformacion()
                        print()
                        print("-------------------------------------------")
                        print()
                        continue
                
                
                
                    elif respuesta.upper() == "NO":
                        
                        listaDeVideosConModificaciones.insert(numeroDeModificacion, ytVideo)

                        print()
                        print("-------------------------------------------")
                        print()
                        break
                
                continue




            elif respuesta.upper() == "INFO" or respuesta.upper() == "INFORMACION":
                MostraraMasInformacionPlaylist()
                print()
                print("-------------------------------------------")
                print()
                continue
            
            elif respuesta.upper() == "NO":
                DescargarPlaylist()
                print()
                print("-------------------------------------------")
                print()
                break

        break
