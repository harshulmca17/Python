class Square:
    '''
    This class describes the shape Square
    '''
    count = 0
    
    #Constructor
    def __init__(self,side):
        '''
        Objective : To initialize a the Square object
        Input Variables :
            self:
            side: The length of side 
        '''
        self.side = side
        Square.count+=1

    def getSide(self):
        return self.side
    
    def getArea(self):
        return self.side*self.side
    
    def getPerimeter(self):
        return self.side*4
    
    def setSide(self,side):
        self.side = side
        
    
