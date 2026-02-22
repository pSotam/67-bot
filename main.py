from time import sleep
import pygame

while True:
    sleep(367)
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()
    print("67")