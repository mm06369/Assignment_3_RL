from state import State
import random
# from visual import TkinterGrid
from vis import DisplayGrid
import math

class RL:

    def __init__(self, size, gamma = 0.8, alpha = 0.8, k = 0.6):
        self.gamma = gamma
        self.alpha = alpha
        self.k = k
        self.size = size
        self.grid = [[State() for j in range(self.size)] for i in range(self.size)]
        self.currentState = self.getStartPos()
        self.setupTerminal()


    def accessGridState(self,i,j):
        return self.grid[i][j].isTerminal

    def setupTerminal(self):
        #setup red terminals
        self.coord = [(2, 4), (2, 5), (2, 6), (2, 7), (2, 9),
                          (6, 2), (7, 2), (8, 2), (9, 2), (7, 3),
                          (7, 6), (7, 6), (7, 8),(7,7),
                          (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)] 

        # self.coord = [(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7)]
        for i in self.coord:
            self.grid[i[0]][i[1]].isTerminal = True
            self.grid[i[0]][i[1]].value = -100
            self.grid[i[0]][i[1]].reward = -100
        # self.coord = []
        # for i in range(13):
        #     i = random.randint(0,self.size - 1)
        #     j = random.randint(0,self.size - 1)
        #     while self.accessGridState(i, j) == True:
        #         i = random.randint(0,self.size - 1)
        #         j = random.randint(0,self.size - 1)
        #     self.grid[i][j].isTerminal = True
        #     self.grid[i][j].value = -1
        #     self.grid[i][j].reward = -100
        #     self.coord.append((i,j))
            
            
        #setup green terminals 
        # self.greenCoord = []
        # i = random.randint(0,self.size - 1)
        # j = random.randint(0,self.size - 1)
        # while self.accessGridState(i, j) == True:
        #     i = random.randint(0,self.size - 1)
        #     j = random.randint(0,self.size - 1)
        # self.grid[i][j].isTerminal = True
        # self.grid[i][j].reward = 100
        # self.grid[i][j].value = 100
        # self.finalState = (i,j)
        self.grid[9][9].isTerminal = True
        self.grid[9][9].reward = 100
        self.grid[9][9].value = 100
        
    
    def drawGrid(self):
        for i in self.grid:
            for j in i:
                print(round(j.value,2), end = "  ")
            print()
        
    def getStartPos(self):
        i = random.randint(0,self.size - 1)
        j = random.randint(0,self.size - 1)
        while self.accessGridState(i, j) == True:
            i = random.randint(0,self.size - 1)
            j = random.randint(0,self.size - 1)
        return (i,j)


    def getAction(self) -> str:
        i, j = self.currentState
        actions = {}
        if i == 0:
            if j == self.size - 1:
                actions['up'] = 0
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k))
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k))
                actions['right'] = 0
            elif j == 0:
                actions['up'] = 0
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) /  (math.exp(self.grid[i][j+1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k))
                actions['left'] = 0
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / (math.exp(self.grid[i][j+1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k))
            else:
                actions['up'] = 0
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k))
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k))
                actions['right']= math.exp(self.grid[i][j+1].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k))

        elif i == self.size - 1:
            if j == self.size - 1:
                actions['up'] =   math.exp(self.grid[i-1][j].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k))
                actions['down'] =  0
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k))
                actions['right'] = 0

            elif j == 0:
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k)    / (math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k))
                actions['down'] = 0
                actions['left'] = 0
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / (math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k))
            else:
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) /   (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k))
                actions['down'] = 0
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k))
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) /(math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k))
        else:
            if j == self.size - 1:
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) /   (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['right'] = 0
            elif j == 0:
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) /    (math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) /  (math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['left'] = 0
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / (math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
            else:
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) /    (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) /  (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) /  (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / (math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k))

        # actions = dict(sorted(actions.items(), key=lambda x: x[1], reverse=True))
        # first = next(iter(actions))
        # print(actions)
        # print()
        ranges = []
        start = 1
        for i in actions:
            end = start + actions[i]
            ranges.append((start, end))
            start = end
        # print(ranges)

        low = ranges[0][0]
        high = ranges[len(ranges)-1][1]
        randomNum = random.uniform(low,high)
        # print(randomNum)
        for i in range(len(ranges)):
            # print(ranges[i][0],ranges[i][1])
            if randomNum > ranges[i][0] and randomNum <= ranges[i][1]:
                if i == 0:
                    return 'up'
                elif i == 1:
                    return 'down'
                elif i == 2:
                    return 'left'
                else:
                    return 'right'
        

    def runEpisode(self):
        
        green = False

        for i in range(100):
            
            print("Episode: ", i)
            self.currentState = self.getStartPos()
            x,y = self.currentState

            while not self.grid[self.currentState[0]][self.currentState[1]].isTerminal:
                action = self.getAction()
                if action == 'left':
                    i = self.currentState[0]
                    j = self.currentState[1] - 1

                elif action == 'right':
                    i = self.currentState[0]
                    j = self.currentState[1] + 1

                elif action == 'up':
                    i = self.currentState[0] - 1
                    j = self.currentState[1]

                elif action == 'down':
                    i = self.currentState[0] + 1
                    j = self.currentState[1] 

                
                self.grid[self.currentState[0]][self.currentState[1]].value = self.grid[self.currentState[0]][self.currentState[1]].value + (self.alpha)*(self.grid[i][j].reward + (self.gamma)*(self.grid[i][j].value) - self.grid[self.currentState[0]][self.currentState[1]].value)
                self.currentState = (i,j)
                
                # if self.currentState == self.finalState:
                #     green = True
                #     break

                # if self.currentState in self.coord:
                #     print("Red Terminal Reached!")
                #     break

                print('Action Selected: ', action)
                print(self.currentState)
                # self.drawGrid()

            # if green == True:
            #     print("Green Terminal Reached!")
            #     break
            
    def visualizeGrid(self):
        arrowDic = {}
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j].isTerminal:
                    pass
                action = ''
                currentVal = self.grid[i][j].value
                possValues = {}
                if i == 0:
                    if j == 0:
                        possValues['right'] = self.grid[i][j+1].value
                        possValues['down'] = self.grid[i+1][j].value
                if i == 0:
                    if j == self.size - 1:
                        possValues['left'] = self.grid[i][j-1].value
                        possValues['down'] = self.grid[i+1][j].value
                    elif j == 0:
                        possValues['right'] = self.grid[i][j+1].value
                        possValues['down'] =  self.grid[i+1][j].value
                    else:
                        possValues['left'] =  self.grid[i][j-1].value
                        possValues['down'] =  self.grid[i+1][j].value
                        possValues['right'] = self.grid[i][j+1].value
                elif i == self.size - 1:
                    if j == self.size - 1:
                        possValues['left'] = self.grid[i][j-1].value
                        possValues['up'] =   self.grid[i-1][j].value
                    elif j == 0:
                        possValues['right'] = self.grid[i][j+1].value
                        possValues['up'] =    self.grid[i-1][j].value
                    else:
                        possValues['left'] =  self.grid[i][j-1].value
                        possValues['up'] =    self.grid[i-1][j].value
                        possValues['right'] = self.grid[i][j+1].value
                else:
                    if j == self.size - 1:
                        possValues['left'] = self.grid[i][j-1].value
                        possValues['up'] =   self.grid[i-1][j].value
                        possValues['down'] = self.grid[i+1][j].value
                    elif j == 0:
                        possValues['down'] =  self.grid[i+1][j].value
                        possValues['right'] = self.grid[i][j+1].value
                        possValues['up'] =    self.grid[i-1][j].value
                    else:
                        possValues['left'] =  self.grid[i][j-1].value
                        possValues['up'] =    self.grid[i-1][j].value
                        possValues['right'] = self.grid[i][j+1].value
                        possValues['down'] =  self.grid[i+1][j].value
                    possValues = dict(sorted(possValues.items(), key=lambda x: x[1], reverse=True))
                    first = next(iter(possValues))
                    arrowDic[(i,j)] = first

        # grid = TkinterGrid(self.size, self.coord, (9,9), arrowDic)
        # grid.create_grid()
        # grid.create()
        # print(arrowDic)
        grid = DisplayGrid(self.size, self.coord, (9,9) , arrowDic)
        grid.createWindow()


                            



bruh = RL(10)
# print("Initial Grid: ")
# bruh.drawGrid()
bruh.runEpisode()
# bruh.drawGrid()
bruh.visualizeGrid()