import pyautogui
import time
from rich.console import Console
from rich.progress import track
rojo = "[red]"
verde = "[green]"
amarillo = "[yellow]"
azul = "[blue]"
resetColor = "[reset]"
console = Console()

def clickear(x,y):
    pyautogui.click(x,y)

def ciclo():
    coordenadas = pyautogui.position()
    #X=741, Y=209
    for i in range(0,2):
        clickear(*coordenadas)
        time.sleep(.4)
    #X=598, Y=465
    nueva_x = 500
    nueva_y = 500
    clickear(nueva_x, nueva_y)
    pyautogui.moveTo(*coordenadas, duration=0)
    pyautogui.FAILSAFE

def slow():
    time.sleep(.02)

repeticiones = int(input("¿Cuántas veces desea borrar? "))
cont=0
for _ in track(range(repeticiones), description='[green]Procesando información'):
    cont+=1
    ciclo()
    console.print(amarillo,"Tweet N°",resetColor,rojo, cont, resetColor, amarillo, resetColor, azul) 
    slow()
