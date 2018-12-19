from pygame import*
from pygame import mixer
import datetime
import time
def gettime():
	print(datetime.datetime.now())
def watr():
    time.sleep(1800)
    file = 'water.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    water = input('Please widte drank to stop the reminder ')
    if water=='Drank' or 'drank':
        mixer.music.pause()
        with open('water.txt') as f:
            f.write(f'{gettime()} Water')
def eydone():
    time.sleep(2700)
    eyes = input('Please wite eydone to stop the reminder ')
    file = 'eyes.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    if eyes=='Eydone' or eyes=='eydone':
        mixer.music.pause()
        with open('eyes.txt') as f:
            f.write(f'{gettime()} Eyes Exersice')
def physical():
    time.sleep(3000)
    exercise = input('Please wite exdone to stop the reminder ')
    file = 'physical.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    if exercise=='Exdone' or exercise=='exdone':
        mixer.music.pause()
        with open('eyes.txt') as f:
            f.write(f'{gettime()} Physical Exersice')
while True:
    watr()
    eydone()
    physical()
