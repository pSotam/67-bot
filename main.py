from time import sleep
import pygame
import ctypes
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin:
    ctypes.windll.shell32.ShellExecuteW(None, "runas",sys.executable," ".join(sys.argv),None,1)
    sys.exit()

def say_six_seven():
    while True:
        sleep(67)
        pygame.mixer.init() # Inicia o mixer do pygame
        pygame.mixer.music.load("audio.mp3") # Carrega o áudio
        pygame.mixer.music.play() # Toca o áudio
        os.startfile("text.txt") # Mostra o bloco de notas

say_six_seven()