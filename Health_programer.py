from pygame import mixer
import datetime
import time
def gettime():
    datetime.datetime.now()
def water():
    time.sleep(1800)
    water = input('Please wite drank to stop the reminder ')
    while water == 'Drank' or water == 'drank':
        file = 'water.mp3'
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        if water=='Drank' or water=='drank':
            mixer.music.pause()
            with open('water_intack.txt') as f:
                f.write(f'{gettime()} water')
                break
        else:
            print('Wrong input')
            mixer.music.play()
def eydone():
    time.sleep(2700)
    eyes = input('Please wite eydone to stop the reminder ')
    while eyes == 'Eydone' or eyes == 'eydone':
        file = 'eyes.mp3'
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        if eyes=='Eydone' or eyes=='eydone':
            mixer.music.pause()
            with open('eyes.txt') as f:
                f.write(f'{gettime()} Eyes Exersice')
                break
        else:
            print('Wrong input')
            mixer.music.play()
def physical():
    time.sleep(3000)
    exercise = input('Please wite exdone to stop the reminder ')
    while exercise == 'Exdone' or exercise == 'exdone':
        file = 'physical.mp3'
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        if exercise=='Exdone' or exercise=='exdone':
            mixer.music.pause()
            with open('eyes.txt') as f:
                f.write(f'{gettime()} Physical Exersice')
                break
        else:
            print('Wrong input')
            mixer.music.play()

while True:
    water()
    eydone()
    physical()