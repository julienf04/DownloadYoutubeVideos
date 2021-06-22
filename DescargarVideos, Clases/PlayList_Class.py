import pytube
import json
import pathlib


class PlayList():

    yt = None
    title = ""
    amountOfVideos = None
    baseResolution = ""
    baseFps = None
    pathDownload = ""
    videoOrAudio = "video"

    listIndexOfDeleteUrl = []


    def __init__(self, link):

        self.link = link
        self.yt = pytube.Playlist(self.link)

        self.title = self.yt.title
        self.amountOfVideos = self.GetAmountOfAvailableVideos()
        self.baseResolution = self.GetAvailableResolutions()[0]
        self.baseFps = self.GetAvailableFps()[0]
        self.pathDownload = self.GetDownloadPath()
        self.videoOrAudio = "video"



    def GetDownloadPath(self):
        self.__parentPath = pathlib.Path(__file__).parent.absolute()
        self.__finalPathJson = str(self.__parentPath) + "\Download Path.json"
        self.__path = json.loads(open(self.__finalPathJson, "r").read())
        return self.__path

    def GetAllVideos(self):
        self.__listAllVideos = []
        for self.url in self.yt.video_urls:
            self.video = pytube.YouTube(self.url)
            self.__listAllVideos.append(self.video.streams)

        return self.__listAllVideos


    def GetAvailableResolutions(self):
        self.superFinalAvailableResolutions = []
        self.__listAllResolutions = []
        self.__listOneStreamResolutions = []
        self.__getAllVideos = self.GetAllVideos()

        for self.__listAllStreamsVideo in self.__getAllVideos:

            for self.__eachStream in self.__listAllStreamsVideo:
                if self.videoOrAudio == "video":
                    if self.__eachStream.video_codec == None or self.__eachStream.audio_codec == None:
                        continue
                elif self.videoOrAudio == "audio":
                    if self.__eachStream.audio_codec == None:
                        continue

                self.__listOneStreamResolutions.append(self.__eachStream.resolution)

            self.__listAllResolutions.append(self.__listOneStreamResolutions)
            self.__listOneStreamResolutions = []

        self.__p = 0
        for self.__i in self.__listAllResolutions:
            self.__g = 0
            for self.__h in self.__i:
                self.__h = self.__h[0:-1]
                self.__listAllResolutions[self.__p][self.__g] = int(self.__h)
                self.__g += 1
            self.__p += 1

        self.__p = 0
        for self.__sorting in self.__listAllResolutions:
            self.__sorting.sort(reverse = True)
            self.__listAllResolutions[self.__p] = self.__sorting
            self.__p += 1
        
        self.__r = 0
        self.__k = 0
        self.__kk = 0
        for self.__q in self.__listAllResolutions:
            if len(self.__q) > self.__r:
                self.__r = len(self.__q)
                self.__k = self.__kk
            self.__kk += 1

        self.__listBoolResolutionsFirst = []
        self.__listBoolResolutionsFinal = []
        for self.__v in self.__listAllResolutions[self.__k]:
            for self.__w in self.__listAllResolutions:
                if self.__v in self.__w:
                    self.__listBoolResolutionsFirst.append(True)
                else:
                    self.__listBoolResolutionsFirst.append(False)

            if not False in self.__listBoolResolutionsFirst:
                self.__listBoolResolutionsFinal.append(True)
            else:
                self.__listBoolResolutionsFinal.append(False)


        self.__j = 0
        for self.__d in self.__listAllResolutions[self.__k]:
            if self.__listBoolResolutionsFinal[self.__j] == False:
                self.__listAllResolutions[self.__k].pop(self.__j)
            
            self.__j += 1

        self.__b = 0
        for self.__t in self.__listAllResolutions[self.__k]:
            self.__t = str(self.__t) + "p"
            self.__listAllResolutions[self.__k][self.__b] = self.__t
            self.__b += 1
        
        for i in self.__listAllResolutions[self.__k]:
            if not i in self.superFinalAvailableResolutions:
                self.superFinalAvailableResolutions.append(i)

        return self.superFinalAvailableResolutions

    def GetAvailableFps(self):
        self.superFinalAvailableFps = []
        self.__listAllFps = []
        self.__listOneStreamFps = []

        for self.__listAllStreamsVideo in self.GetAllVideos():

            for self.__eachStream in self.__listAllStreamsVideo:
                if self.videoOrAudio == "video":
                    if self.__eachStream.video_codec == None or self.__eachStream.audio_codec == None:
                        continue
                elif self.videoOrAudio == "audio":
                    if self.__eachStream.audio_codec == None:
                        continue

                self.__listOneStreamFps.append(self.__eachStream.fps)

            self.__listAllFps.append(self.__listOneStreamFps)
            self.__listOneStreamFps = []

        self.__r = 0
        self.__k = 0
        self.__kk = 0
        for self.__q in self.__listAllFps:
            if len(self.__q) > self.__r:
                self.__r = len(self.__q)
                self.__k = self.__kk
            self.__kk += 1

        self.__listBoolFpsFirst = []
        self.__listBoolFpsFinal = []
        for self.__v in self.__listAllFps[self.__k]:
            for self.__w in self.__listAllFps:
                if self.__v in self.__w:
                    self.__listBoolFpsFirst.append(True)
                else:
                    self.__listBoolFpsFirst.append(False)
            
            if not False in self.__listBoolFpsFirst:
                self.__listBoolFpsFinal.append(True)
            else:
                self.__listBoolFpsFinal.append(False)

            self.__listBoolFpsFirst = []


        self.__j = 0
        for self.__d in self.__listAllFps[self.__k]:
            if self.__listBoolFpsFinal[self.__j] == False:
                self.__listAllFps[self.__k].pop(self.__j)
            
            self.__j += 1


        for i in self.__listAllFps[self.__k]:
            if i not in self.superFinalAvailableFps:
                self.superFinalAvailableFps.append(i)

        return self.superFinalAvailableFps


    def GetAmountOfAvailableVideos(self):
        self.lenOfAvailableVideosList = len(self.GetAllVideos())
        return self.lenOfAvailableVideosList


    def ChangeTitle(self, newTitle):
        self.title = newTitle

    def ChangeAmountOfVideo(self, indexOfVideoInPlaylist):
        if not indexOfVideoInPlaylist in self.listIndexOfDeleteUrl:
            self.listIndexOfDeleteUrl.append(indexOfVideoInPlaylist)
            self.amountOfVideos -= 1

    def ChangeResolution(self, newResolution):
        self.baseResolution = newResolution

    def ChangeFps(self, newFps):
        self.baseFps = newFps

    def ChangePathDonwload(self, newPath):
        self.pathDownload = newPath

    def ChangePathDownloadConfiguration(self):
        open(self.__finalPathJson, "w").write(json.dumps(self.pathDownload))

    def OnlyAudio(self):
        if self.videoOrAudio == "video":
            self.videoOrAudio = "audio"
            self.ChangeResolution(None)
            self.ChangeFps(None)

        elif self.videoOrAudio == "audio":
            self.videoOrAudio = "video"
            self.ChangeResolution(self.GetAvailableResolutions()[0])
            self.ChangeFps(self.GetAvailableFps()[0])


    def RestartFeatures(self):
        self.title = self.yt.title
        self.amountOfVideos = self.GetAmountOfAvailableVideos()
        self.baseResolution = self.GetAvailableResolutions()[0]
        self.baseFps = self.GetAvailableFps()[0]
        self.pathDownload = self.GetDownloadPath()
        self.videoOrAudio = "video"

        self.listIndexOfDeleteUrl = []



    def ShowFeatures(self):
        if self.videoOrAudio == "video":
            self.__onlyAudio = "No"
        elif self.videoOrAudio == "audio":
            self.__onlyAudio = "Si"


        if self.__onlyAudio == "No":
            print("   TITULO: " + self.title)
            print("   CANTIDAD DE VIDEOS DE LA PLAYLIST: " + str(self.amountOfVideos))
            print("   RESOLUCION BASE: " + self.baseResolution)
            print("   FPS BASE: " + str(self.baseFps))
            print("   RUTA DE DESCARGA: " + self.pathDownload)
            print("   SOLO AUDIO: " + self.__onlyAudio)
        elif self.__onlyAudio == "Si":
            print("   TITULO: " + self.title)
            print("   CANTIDAD DE AUDIOS DE LA PLAYLIST: " + str(self.amountOfVideos))
            print("   RUTA DE DESCARGA: " + self.pathDownload)
            print("   SOLO AUDIO: " + self.__onlyAudio)


        def ShowInfo(self):
            print("   El titulo se refiere al nombre con el cual va a aparecer la Playlist descargada en tus archivos.")
            print()
            print("   La cantidad de videos de la Playlist se refiere a la cantidad de videos que se encuentran en la Playlist y que se descargaran")
            print()
            print("   La resolucion base se refiere a la calidad de imagen promedio con la cual se van a descargar los videos de la Playlist.")
            print("   ( Mientras mas alto sea el numero, habra mayor cantidad de pixeles, por lo tanto, es mas alta la calidad del video )")
            print()
            print("   Los FPS base se refieren a la cantidad de fotogramas por segundo con la cual se van a descargar los videos en la Playlist.")
            print("   ( Mientras mas alto sea el numero, mas fluido ira el video, por lo tanto, mas alta es la calidad )")
            print()
            print("   La ruta de descarga se refiere a la ruta (el lugar) en el que se van a descargar los videos de la Playlist en tus archivos.")
            print()
            print("   Este parametro se refiere a si preferis que se descargue solamente el audio de todos los videos de la Playlist.")