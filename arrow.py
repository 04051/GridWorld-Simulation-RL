class arrow:
    def __init__(self, Width, Height):
        self.Width = Width
        self.Height = Height
        stroke(122, 202, 128)
    
        strokeWeight(2)
        
    #UP
    def arrowUp(self, x, y):

        a = x
        a1 = y
        b = x+self.Width
        b1 = y
        c = b
        c1 = y+self.Height
        d = x
        d1 = c1
        
        midab = (a + b) // 2
        midab1 = a1+(self.Height)*0.25
  
        midbc1 = y+(self.Height)*0.75
        midbc = x+(self.Width)*0.75
        
        midad = x+self.Width*0.25
        midad1 = midbc1
        
        middc = midab
        middc1 = y+self.Height*0.6
    
        fill(18, 185, 30)
        quad(midab, midab1, midbc, midbc1, middc, middc1, midad, midad1)
   
   #DOWN
    def arrowDown(self, x, y):
    
        a = x
        a1 = y
        b = x+self.Width
        b1 = y
        c = b
        c1 = y+self.Height
        d = x
        d1 = c1
        
        midab = (c + d) // 2
        midab1 = y + (self.Height)*0.75
        
        midbc1 = y+ (self.Height)*0.25
        midbc = x + (self.Width)*0.75
        
        midad = x+ (self.Width)*0.25
        midad1 = midbc1
        
        middc = midab
        middc1 = y+(self.Height)*0.4
        fill(18, 185, 30)
        quad(midab, midab1, midbc, midbc1, middc, middc1, midad, midad1)
        
    #RIGHT
    def arrowRight(self, x, y):
    
        a = x
        a1 = y
        b = x+self.Width
        b1 = y
        c = b
        c1 = y+self.Height
        d = x
        d1 = c1
        
        middc = x+(self.Width)*0.25
        middc1 = y+(self.Height)*0.75
        
        midab = middc
        midab1 = y+(self.Height)*0.25
        
        midbc1 = (b1+ c1)//2
        midbc = x+ (self.Width)*0.75
        
        midad = x+ (self.Width)*0.4
        midad1 = y+(self.Height)*0.5
        
 
        fill(18, 185, 30)
        quad(midab, midab1, midbc, midbc1, middc, middc1, midad, midad1)
    #LEFT
    def arrowLeft(self, x, y):
    
        a = x
        a1 = y
        b = x+self.Width
        b1 = y
        c = x+self.Width
        c1 = y+self.Height
        d = x
        d1 = y+self.Height
        
        middc = x+(self.Width)*0.75
        middc1 = y+(self.Height)*0.75
        
        midab = middc
        midab1 = y+(self.Height)*0.25
        
        midbc1 = (b1+ c1)//2
        midbc = x+(self.Width)*0.6
        
        midad = x +(self.Width)*0.25
        midad1 = y+(self.Height)*0.5
        fill(18, 185, 30)
        quad(midab, midab1, midbc, midbc1, middc, middc1, midad, midad1)
