from pygame import*
from pygame import mixer
import datetime
import time
def gettime():
	return (datetime.datetime.now())
def watr():
    time.sleep(10)
    file = 'water.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
    water = input('Please write drank to stop the reminder ')
    if water=='Drank' or 'drank':
        mixer.music.pause()
        with open('water.txt','a') as f:
            f.write(f'{gettime()} Water\n')
def eydone():
    time.sleep(25)
    eyes = input('Please write eydone to stop the reminder ')
    file = 'eyes.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
    if eyes=='Eydone' or eyes=='eydone':
        mixer.music.pause()
        with open('eyes.txt','a') as f:
            f.write(f'{gettime()} Eyes Exersice\n')
def physical():
    time.sleep(35)
    exercise = input('Please write exdone to stop the reminder ')
    file = 'physical.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
    if exercise=='Exdone' or exercise=='exdone':
        mixer.music.pause()
        with open('Exercise.txt','a') as f:
            f.write(f'{gettime()} Physical Exersice\n')
while True:
    watr()
    eydone()
    physical()
