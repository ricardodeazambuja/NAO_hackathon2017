import wikipedia
import naoqi
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559)
strstr = wikipedia.summary("priapism", sentences=1)
tts.say(str(strstr))

