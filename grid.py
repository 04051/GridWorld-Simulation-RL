from arrow import arrow

class Grid(object):
    
    def __init__(self, grid):
        print("Grid Object Generated.....")
        self.grid = grid
        self.Width = (width-100)//len(self.grid)
        self.Height = (height-100)//len(self.grid[0])
        self.arrow = arrow(self.Width, self.Height)
        
    def generateGridMap(self):
        
        print("Displaying Grid....")
        
        x = self.Width
        y = self.Height
   
        b= 50
        for i in self.grid:
            a = 50
            for state in i:
            
                if state.reward == 100:
                    fill(18, 84, 24)
                elif state.reward == -100:
                    fill(137, 130, 130)
                    fill(158, 0 , 11)
                else:
                    fill(0)
                
                rect(a, b ,x, y)
                state.Width = x
                state.Height = y
                state.dimY = b
                state.dimX = a
                a+=x
           
            b+=y
        
    
    def generateDirections(self, state):
    
        direction = state.direction 
        
        #if u want to see values instead of directions uncomment the commented part
        
        '''fill(0)
        stroke(18, 84, 24)
        rect(state.dimX, state.dimY, self.Width, self.Height)
        fill(200)
        font = createFont("Georgia", self.Height*0.2)
        textFont(font)
        text(state.value , (state.dimX+self.Width//2)-15, state.dimY+self.Height//2)
        '''
        
        #displays directions on the grid(comment out this part if u want to see values)
        
        if direction == 'up':
            self.arrow.arrowUp(state.dimX, state.dimY)
        elif direction == 'down':
            self.arrow.arrowDown(state.dimX, state.dimY)
        elif direction == 'right':
            self.arrow.arrowLeft(state.dimX, state.dimY)
        elif direction == 'left':
            self.arrow.arrowRight(state.dimX, state.dimY)
    
        print(direction)
        
