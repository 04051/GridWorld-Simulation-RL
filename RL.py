from State import State
from grid import Grid
class Agent:
    def __init__(self, discount, Size):
        self.grid = []
        self.discount = discount
        self.actions = ['up', 'down', 'left', 'right']
        self.dim = Size
    
    #generate grid with -1
    def generateGrid(self):
    
        n = self.dim
        grid = [[State(i, j, -1, 'H') for j in range(n)] for i in range(n)]
        self.grid = grid
        
        #return grid
    
    #set win and lose state
    def setStates(self,win, penalty):
        for i in win:
            self.grid[i[0]][i[1]].reward = +100
            self.grid[i[0]][i[1]].isObstacle = True
            self.grid[i[0]][i[1]].value = +100
        for i in penalty: 
            self.grid[i[0]][i[1]].reward = -100
            self.grid[i[0]][i[1]].isObstacle = True
            self.grid[i[0]][i[1]].value = -100
    
    
    def evaluate(self, state):
        updatedVal = state.value
        updatedDirection = state.direction
        
        for i in self.actions:
            if i == 'up':
                nextState = [state.x-1 , state.y]
            elif i == 'down':
                nextState = [state.x+1, state.y]
            elif i == "right":
                nextState = [state.x, state.y-1]
            elif i == "left":   
                nextState = [state.x, state.y+1]

                
            if nextState[0] >= 0 and nextState[0] <= self.dim-1:
                if nextState[1] >= 0 and nextState[1] <= self.dim-1:
               
                    newValue = state.reward + (self.discount*(self.grid[nextState[0]][nextState[1]].value))
             
                    if updatedVal < newValue:
                
                        updatedVal = newValue
                        updatedDirection = i

        return [updatedVal, updatedDirection]
    
