from pynput.mouse import Controller 
import time

mouse = Controller()
mouse.position = (853, 533)
posicao = mouse.position
mouse.position = (posicao[0]+100, posicao[1])
time.sleep(1)
posicao = mouse.position
while True:
    mouse.position = (posicao[0], posicao[1]-100)
    time.sleep(1)
    posicao = mouse.position
    mouse.position = (posicao[0]-100, posicao[1])
    time.sleep(1)
    posicao = mouse.position
    mouse.position = (posicao[0]-100, posicao[1])
    time.sleep(1)
    posicao = mouse.position
    mouse.position = (posicao[0], posicao[1]+100)
    time.sleep(1)
    posicao = mouse.position
    mouse.position = (posicao[0], posicao[1]+100)
    time.sleep(1)
    posicao = mouse.position
    mouse.position = (posicao[0]+100, posicao[1])
    time.sleep(1)
    posicao = mouse.position
    mouse.position = (posicao[0]+100, posicao[1])
    time.sleep(1)
    posicao = mouse.position
    mouse.position = (posicao[0], posicao[1]-100)
    time.sleep(1)
    posicao = mouse.position