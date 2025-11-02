import subprocess
import os
import time
import pyautogui

#escribir texto
def escribir(texto):
    pyautogui.write(texto, interval=0.05)

#simulacion de tabs con intervalos
def pulsar_tab(veces, pausa=0.1):
    for _ in range(veces):
        pyautogui.press('tab')
        time.sleep(pausa)

#simulacion de enter con intervalos
def pulsar_enter(veces, pausa=0.1):
    for _ in range(veces):
        pyautogui.press('enter')
        time.sleep(pausa)

#abrir chrome y esperar 10 segundo a que abra
os.system('chrome')
time.sleep(10)

#ir a los ajustes de el motor 
escribir('chrome://settings/searchEngines')
time.sleep(0.25)

#tabear
pulsar_tab(1)
time.sleep(0.1)

#escribir du (q coño es du)
escribir('du')
time.sleep(0.2)

#tabear 4 veces 
pulsar_tab(4, 0.1)
time.sleep(0.1)

#pulsar enter 2 veces esperando 0.1
pulsar_enter(2, 0.1)
time.sleep(0.1)

#pulsar tab 3 veces
pulsar_tab(3,0,1)
time.sleep(0.1)

#pulsar enter 1 vez
pulsar_enter(1, 0.1)
time.sleep(0.1)

#pulsar tab 2 veces 
pulsar_tab(2, 0.1)
time.sleep(0.1)

#pulsar enter 1 vez 
pulsar_enter(1, 0.1)
time.sleep(0.1)

#pulsar tab 2 veces 
pulsar_tab(2, 0,1)
time.sleep(0.1)

#pulsar enter 
pulsar_enter(1, 0.1)
time.sleep(0.1)

#matar chrome 
subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'])