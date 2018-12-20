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
    water = input('Please write drank to stop the reminder ')
    if water=='Drank' or 'drank':
        mixer.music.pause()
def eydone():
    time.sleep(600)
    file = 'eyes.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
	eyes = input('Please write eydone to stop the reminder ')
    if eyes=='Eydone' or eyes=='eydone':
        mixer.music.pause()
        with open('eyes.txt','a') as f:
            f.write(f'{gettime()} Eyes Exersice\n')
def physical():
    time.sleep(300)
    file = 'physical.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10000,0.0)
	exercise = input('Please write exdone to stop the reminder ')
    if exercise=='Exdone' or exercise=='exdone':
        mixer.music.pause()
        with open('Exercise.txt','a') as f:
            f.write(f'{gettime()} Physical Exersice\n')
water_level = 0
while water_level != 3500:
    watr()
    level = int(input('How much water did you drink '))
    with open('water.txt','a') as f:
        f.write(f'{gettime()} Water {level} ml\n')
    water_level += level
    print(f'{3500-water_level} ml remainig')
    eydone()
    physical()
