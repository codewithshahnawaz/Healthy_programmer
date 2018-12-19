from pygame import mixer
import datetime
import time
def gettime():
    datetime.datetime.now()
def water(u):
    time.sleep(1800)
    while u == 'Drank' or u == 'drank':
        file = 'water.mp3'
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        if u=='Drank' or u=='drank':
            mixer.music.pause()
            with open('water_intack.txt') as f:
                f.write(f'{gettime()} water')
                break
        else:
            print('Wrong input')
            mixer.music.play()
def eydone(u):
    time.sleep(2700)
    while u == 'Eydone' or u == 'eydone':
        file = 'eyes.mp3'
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        if u=='Eydone' or u=='eydone':
            mixer.music.pause()
            with open('eyes.txt') as f:
                f.write(f'{gettime()} Eyes Exersice')
                break
        else:
            print('Wrong input')
            mixer.music.play()
def physical(u):
    time.sleep(3000)
    while u == 'Exdone' or u == 'exdone':
        file = 'physical.mp3'
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        if u=='Exdone' or u=='exdone':
            mixer.music.pause()
            with open('eyes.txt') as f:
                f.write(f'{gettime()} Physical Exersice')
                break
        else:
            print('Wrong input')
            mixer.music.play()

while True:
    water = input('Please wite drank to stop the reminder ')
    water(water)
    eyes = input('Please wite eydone to stop the reminder ')
    eydone(eyes)
    exercise = input('Please wite exdone to stop the reminder ')
    physical(exercise)