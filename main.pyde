from RL import Agent
from grid import Grid

'''Limitations of the visualization
---- The following visualization only generates square grids
---- You can set the grid dimension in the setup 
---- You can set the discount factor in the setup
---- If you want a random grid then comment out the reaasignment of winner and obstacles on line 31 and 32.
---- You can set obstacles and winner states of your choice on line 27 and 28. This will overwrite the random configuration
---- The code will return an error if invalid winner or obstacle states are entered i.e. if states lie outside the grid'''

def setup():
    size(600, 600)
    global agent, gridObject;
    frameRate(5)
    
    #YOU CAN SPECIFY THE GRID DIMENSION AND DISCOUNT FACTOR HERE.
    #A DIMENSION VALUE GREATER THAN 25 OR LESS THAN 3 WILL RUIN THE VISUALS. YOU CAN STILL VIEW THE UPDATED VALUES IN THE CONSOLE. 
    dimension = 10
    discountFactor = 0.9
    agent = Agent(discountFactor, dimension) 
    agent.generateGrid()
    
    #RANDOMLY GENERATED WIN AND LOSE STATES
    #winner = [(int(random(0,agent.dim)),int(random(0,agent.dim))) for i in range(int(agent.dim*0.55))]
    #obstacles = [(int(random(0,agent.dim)),int(random(0,agent.dim))) for i in range(int(agent.dim*0.55))]
    
    #YOU CAN REASSIGN WIN AND LOSE STATES HERE
    winner = [(9,9)]
    obstacles = [(2,4),(2,5),(2,6),(2,7),(2,9),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(8,2),(7,2),(6,2),(7,3),(7,6),(7,7),(7,8)]

    agent.setStates(winner, obstacles) 
    gridObject = Grid(agent.grid)

    
def setBackground(framecount):
    background(39, 74, 45)
    fill(230)
    font = createFont("Georgia", height*0.028)
    textFont(font)
    textAlign(LEFT)
    text("REINFORCEMENT LEARNING - GRID WORLD", height*0.1, width*0.04)
    
    text("Frame Count =  "+ str(framecount), height*0.1, width*0.07)
        
def draw():
    
    setBackground(frameCount)
    global agent, gridObject;
    gridObject.generateGridMap()

    for i in range(agent.dim):
        for j in range(agent.dim):
            if (agent.grid[i][j].isObstacle == False):
                updatedValue = agent.evaluate(agent.grid[i][j])
                agent.grid[i][j].value = updatedValue[0]
                agent.grid[i][j].direction = updatedValue[1]
                gridObject.generateDirections(agent.grid[i][j])
        
    
    
    
