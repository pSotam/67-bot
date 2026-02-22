from time import sleep
import pygame
import os

while True:
    sleep(67)
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()
    os.startfile("text.txt")