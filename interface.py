from nicegui import ui
from Map import init_map
from State import State
import time
from PathFinder import *

numRow = 50
numColumn = 50

while True:
    try:
        maze = init_map(numRow, numColumn)
        break
    except:
        pass

path = PathFinder(maze)

@ui.refreshable
#Grid visualization
def visualization():

    #Sizing of pixels
    if(numRow < 30 and numColumn < 30):
        pixelSize = "25px "
    else:
        pixelSize = "20px "

    #Display and color the grid based on cell state
    with ui.grid(columns=pixelSize*numColumn, rows=pixelSize*numRow).classes('gap-0 w-full fixed-center justify-center'):
        for i in range(numRow):
            for j in range(numColumn):
                match(maze[i][j].property):
                    case State.Water:
                        ui.label(" ").classes('border p-1 aspect-square bg-blue') 
                    case State.NorthBorder:
                        ui.label(" ").classes('border p-1 aspect-square bg-green') 
                    case State.SouthBorder:
                        ui.label(" ").classes('border p-1 aspect-square bg-lime') 
                    case State.Bridge:
                        ui.label(" ").classes('border p-1 aspect-square bg-brown') 
                    case _:
                        ui.label(" ").classes('border p-1 aspect-square bg-yellow') 

def setRow(e):
    global numRow
    numRow = int(e.value)

def setColumn(e):
    global numColumn
    numColumn = int(e.value)
    
def generateMaze(e):
    global maze
    while True:
        try:
            maze = init_map(numRow, numColumn)
            break
        except:
            pass
    visualization.refresh()
    
def solveMaze(e):
    global maze
    path = PathFinder(maze)
    for i in range(len(path)):
        maze[path[i][0]][path[i][1]].property = State.NorthBorder
    
    visualization.refresh()
        
visualization()

#Interaction 
with ui.column().classes('items-start'):
    ui.markdown("**Number of rows**")
    sliderRow = ui.slider(min=5, max=50, value=50, on_change=setRow).props('label-always').on('update:model-value',throttle=1.0)
    ui.markdown("**Number of columns**")
    sliderColumn = ui.slider(min=5, max=50, value=50, on_change=setColumn).props('label-always').on('update:model-value',throttle=1.0)
    ui.button("Generate maze", on_click=generateMaze)
    ui.button("Solve maze", on_click=solveMaze)
ui.run(title = "Bridge Maze")
