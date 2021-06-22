import pytube
import json
import pathlib


class Video():

    yt = None
    title = ""
    resolution = ""
    fps = None
    pathDownload = ""
    videoOrAudio = "video"

    updatedConditionsList = [None, None]


    def __init__(self, link):

        self.link = link
        self.yt = pytube.YouTube(self.link)
      
        self.title = self.yt.streams.filter(type = "video").first().default_filename
        self.resolution = self.GetFirstResolution()
        self.fps = self.GetFirstFps()
        self.pathDownload = self.GetDownloadPath()
        self.videoOrAudio = "video"
      
        self.updatedConditionsList = [self.resolution, None] # Primer elemento: Resolucion || Segundo elemento: Fps



    def GetDownloadPath(self):
        self.__parentPath = pathlib.Path(__file__).parent.absolute()
        self.__finalPathJson = str(self.__parentPath) + "\Download Path.json"
        self.__path = json.loads(open(self.__finalPathJson, "r").read())
        return self.__path

    def GetFirstResolution(self):
        self.getRes = self.yt.streams.filter(type = "video").first().resolution
        return self.getRes

    def GetFirstFps(self):
        self.getFps = self.yt.streams.filter(type = "video").first().fps
        return self.getFps



    def GetAllAvailableResolutions(self):
        self.listResolutions = []
        for self.__eachVideo in self.yt.streams.filter(type = "video", res = None, fps = self.updatedConditionsList[1]):
            if self.videoOrAudio == "video":
                if self.__eachVideo.video_codec == None or self.__eachVideo.audio_codec == None:
                    continue
            elif self.videoOrAudio == "audio":
                if self.__eachVideo.audio_codec == None:
                    continue

            self.__resolutionOfEachStream = self.__eachVideo.resolution
            if not self.__resolutionOfEachStream in self.listResolutions:
                self.listResolutions.append(self.__resolutionOfEachStream)

        self.__h = 0
        for self.__eachResolution in self.listResolutions:
            self.__eachResolution = self.__eachResolution[0:-1]
            self.listResolutions[self.__h] = int(self.__eachResolution)
            self.__h += 1

        self.listResolutions.sort(reverse = True)
        
        self.__h = 0
        for self.__eachResolution in self.listResolutions:
            self.__eachResolution = str(self.__eachResolution) + "p"
            self.listResolutions[self.__h] = self.__eachResolution
            self.__h += 1


        return self.listResolutions


    def GetAllAvailableFps(self):
        self.listFps = []
        for self.__eachVideo in self.yt.streams.filter(type = "video", res = self.updatedConditionsList[0], fps = None):
            if self.videoOrAudio == "video":
                if self.__eachVideo.video_codec == None or self.__eachVideo.audio_codec == None:
                    continue
            elif self.videoOrAudio == "audio":
                if self.__eachVideo.audio_codec == None:
                    continue

            self.__fpsOfEachStream = self.__eachVideo.fps
            if not self.__fpsOfEachStream in self.listFps:
                self.listFps.append(self.__fpsOfEachStream)

        self.listFps.sort(reverse = True)

        return self.listFps



    def ChangeTitle(self, newTitle):
        self.title = newTitle

    def ChangeResolution(self, newResolution):
        self.resolution = newResolution
        self.updatedConditionsList[0] = self.resolution

    def ChangeFps(self, newFps):
        self.fps = newFps
        self.updatedConditionsList[1] = self.fps

    def ChangePathDownloadForThisVideo(self, newPath):
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
            self.ChangeResolution(self.GetFirstResolution())
            self.ChangeFps(self.GetFirstFps())

    def RestartFeatures(self):
        self.title = self.yt.streams.filter(type = "video").first().default_filename
        self.resolution = self.GetResolution()
        self.fps = self.GetFps()
        self.pathDownload = self.GetDownloadPath()
        self.videoOrAudio = "video"

        self.updatedConditionsList = [None, None] # Primer elemento: Resolucion || Segundo elemento: Fps


    def ShowFeatures(self):
        if self.videoOrAudio == "video":
            self.__onlyAudio = "No"
        elif self.videoOrAudio == "audio":
            self.__onlyAudio = "Si"

        if self.__onlyAudio == "No":
            print("   TITULO: " + self.title)
            print("   RESOLUCION: " + self.resolution)
            print("   FPS: " + str(self.fps))
            print("   RUTA DE DESCARGA: " + self.pathDownload)
            print("   SOLO AUDIO: " + self.__onlyAudio)
        elif self.__onlyAudio == "Si":
            print("   TITULO: " + self.title)
            print("   RUTA DE DESCARGA: " + self.pathDownload)
            print("   SOLO AUDIO: " + self.__onlyAudio)



    def ShowInfo(self):
        print("   TITULO: se refiere al nombre con el cual va a aparecer el video descargado en tus archivos.")
        print()
        print("   RESOLUCION: se refiere a la calidad de imagen con la cual se va a descargar el video en tus archivos.")
        print("   ( Mientras mas alto sea el numero, habra mayor cantidad de pixeles, por lo tanto, es mas alta la calidad del video )")
        print()
        print("   FPS: se refiere a la cantidad de fotogramas por segundo con la cual se va a descargar el video en tus archivos.")
        print("   ( Mientras mas alto sea el numero, mas fluido ira el video, por lo tanto, mas alta es la calidad )")
        print()
        print("   RUTA DE DESCARGA: se refiere a la ruta (el lugar) en el que se va a descargar el video en tus archivos.")
        print()
        print("   SOLO AUDIO: se refiere a si preferis que se descargue el video con la imagen o solamente el audio del video.")