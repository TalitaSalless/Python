#Faça um programa que abra e reproduza um arquivo de audio mp3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('away.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
