import subprocess
import os
import time
import pyautogui
import pygetwindow as gw

# escribir texto
def escribir(texto):
    pyautogui.write(texto, interval=0.05)

# simulacion de tabs con intervalos
def pulsar_tab(veces, pausa=0.1):
    for _ in range(veces):
        pyautogui.press('tab')
        time.sleep(pausa)

# simulacion de enter con intervalos
def pulsar_enter(veces, pausa=0.1):
    for _ in range(veces):
        pyautogui.press('enter')
        time.sleep(pausa)

# abrir chrome
os.system('start chrome')

# esperar a que arranque entero (mejor que esperar 10 segundos fijos)
while True:
    windows = gw.getWindowsWithTitle("Nueva pestaña - Chromium")
    if windows:
        windows[0].activate()  # poner la ventana en primer plano
        break
    time.sleep(0.5)

# dar a chrome cuartelillo para que cargue
time.sleep(1)

# ir a los ajustes del motor
escribir('chrome://settings/searchEngines')
pulsar_enter(1)
time.sleep(0.25)

# tabear
pulsar_tab(1)

# escribir du (q coño es du)
escribir('du')
time.sleep(0.2)

# tabear 4 veces
pulsar_tab(4)

# pulsar enter 2 veces esperando 0.1
pulsar_enter(2)

# pulsar tab 3 veces
pulsar_tab(3)

# ir a configuración general
escribir('chrome://settings')
pulsar_enter(1)
time.sleep(0.25)

# pulsar tab 3 veces
pulsar_tab(3)

# pulsar enter 1 vez
pulsar_enter(1)

# pulsar tab 2 veces
pulsar_tab(2)

# pulsar enter 1 vez
pulsar_enter(1)

# pulsar tab 2 veces
pulsar_tab(2)

# pulsar enter
pulsar_enter(1)

# matar chrome
subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'])
