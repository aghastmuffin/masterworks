#music helper DO NOT LOAD WINDOW
#
from pygame import mixer
from time import sleep
status = open("status.txt", "a")
log = open("log.txt", "w")
mixer.init()
mixer.music.load(r"C:\Users\levic\Python_files\Masterworks\Assets\intro.wav")
mixer.music.set_volume(0.7)
mixer.music.play()
sleep(51)
mixer.music.stop()
exit()
