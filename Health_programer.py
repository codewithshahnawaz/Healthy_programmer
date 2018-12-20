from pygame import*
from pygame import mixer
import datetime
import time
def gettime():
	return (datetime.datetime.now())
def watr():
    time.sleep(1800)
    file = 'water.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
    water = input('Please widte drank to stop the reminder ')
    if water=='Drank' or 'drank':
        mixer.music.pause()
        with open('water.txt','a') as f:
            f.write(f'{gettime()} Water')
def eydone():
    time.sleep(4600)
    eyes = input('Please wite eydone to stop the reminder ')
    file = 'eyes.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
    if eyes=='Eydone' or eyes=='eydone':
        mixer.music.pause()
        with open('eyes.txt','a') as f:
            f.write(f'{gettime()} Eyes Exersice')
def physical():
    time.sleep(6600)
    exercise = input('Please wite exdone to stop the reminder ')
    file = 'physical.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
    if exercise=='Exdone' or exercise=='exdone':
        mixer.music.pause()
        with open('eyes.txt','a') as f:
            f.write(f'{gettime()} Physical Exersice')
while True:
    watr()
    eydone()
    physical()
