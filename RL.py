from state import State
import random
import math

class RL:

    def __init__(self, size, gamma = 0.8, alpha = 0.8, k = 1):
        self.gamma = gamma
        self.alpha = alpha
        self.k = k
        self.size = size
        self.grid = [[State() for j in range(self.size)] for i in range(self.size)]
        # self.currentState = self.getStartPos()
        self.currentState = (0,0)
        self.setupTerminal()
        # self.drawGrid()
        # self.getAction()

    def accessGridState(self,i,j):
        return self.grid[i][j].isTerminal

    def setupTerminal(self):
        #setup red terminals
        coord = [(0,1),(1,1),(2,1),(3,1)]
        for i in coord:
            self.grid[i[0]][i[1]].isTerminal = True
            self.grid[i[0]][i[1]].value = -1
            self.grid[i[0]][i[1]].reward = -100
        # for i in range(self.size):
        #     i = random.randint(0,self.size - 1)
        #     j = random.randint(0,self.size - 1)
        #     while self.accessGridState(i, j) == True:
        #         i = random.randint(0,self.size - 1)
        #         j = random.randint(0,self.size - 1)
        #     self.grid[i][j].isTerminal = True
        #     self.grid[i][j].value = -1
        #     self.grid[i][j].reward = -100
            
        #setup green terminals 
        # i = random.randint(0,self.size - 1)
        # j = random.randint(0,self.size - 1)
        # while self.accessGridState(i, j) == True:
        #     i = random.randint(0,self.size - 1)
        #     j = random.randint(0,self.size - 1)
        # self.grid[i][j].isTerminal = True
        # self.grid[i][j].reward = 100
        # self.grid[i][j].value = 1
        self.grid[1][2].isTerminal = True
        self.grid[1][2].reward = 100
        self.grid[1][2].value = 1
        
        

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
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)
                actions['up'] = 0
                actions['right'] = 0
            elif j == 0:
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / math.exp(self.grid[i][j+1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) /  math.exp(self.grid[i][j+1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)
                actions['up'] = 0
                actions['left'] = 0
            else:
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k)
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k)
                actions['right']= math.exp(self.grid[i][j+1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i + 1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k)
                actions['up'] = 0

        elif i == self.size - 1:
            if j == self.size - 1:
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k)
                actions['up'] =   math.exp(self.grid[i-1][j].value/self.k) / math.exp(self.grid[i][j-1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k)
                actions['down'] =  0
                actions['right'] = 0

            elif j == 0:
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k)
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) / math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i-1][j].value/self.k)
                actions['down'] = 0
                actions['left'] = 0
            else:
                math.exp(self.grid[i][j+1].value/self.k) / math.exp(0/0.5) + math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k)
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k)
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) /   math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k)
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) /math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i][j+1].value/self.k)
                actions['down'] = 0
        else:
            if j == self.size - 1:
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) /   math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['right'] = 0
            elif j == 0:
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) /  math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) /    math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['left'] = 0
            else:
                actions['left'] = math.exp(self.grid[i][j-1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['up'] = math.exp(self.grid[i-1][j].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['right'] = math.exp(self.grid[i][j+1].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)
                actions['down'] = math.exp(self.grid[i+1][j].value/self.k) / math.exp(self.grid[i][j-1].value/self.k) + math.exp(self.grid[i-1][j].value/self.k) + math.exp(self.grid[i][j+1].value/self.k)  + math.exp(self.grid[i+1][j].value/self.k)

        actions = dict(sorted(actions.items(), key=lambda x: x[1], reverse=True))
        first = next(iter(actions))
        return first

    def runEpisode(self):
        
        # terminalReached = False
        green = False
        # episode = 1
        # print('Episode: ', episode)
        
        for i in range(100):
            
            print("Episode: ", i)
            # terminalReached = False
            # greenTerminal = False
            self.currentState = (0,0)
            x,y = self.currentState

            while not self.grid[x][y].isTerminal:
            # while(not(terminalReached)):
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

                # if self.grid[i][j].isTerminal:
                #     if self.grid[i][j].reward == 100:
                #         terminalReached = True
                #         greenTerminal = True
                #         break
                #     else:
                #         print("Red Terminal Reached")
                #         terminalReached = True
                #         # self.currentState = self.getStartPos()
                #         self.currentState = (0,0)
                #         break
                
                self.grid[self.currentState[0]][self.currentState[1]].value = self.grid[self.currentState[0]][self.currentState[1]].value + (self.alpha)*(self.grid[i][j].reward + (self.gamma)*(self.grid[i][j].value) - self.grid[self.currentState[0]][self.currentState[1]].value)
                self.currentState = (i,j)
                if self.currentState == (1,2):
                    green = True
                    break

                # if not(terminalReached):
                #     self.currentState = (i,j)    
                # else:
                #     self.currentState = (0,0)
                    # episode += 1
                    # print("Episode: ", episode)
            # self.currentState = (i,j)
                print('Action Selected: ', action)
                print(self.currentState)
                self.drawGrid()

            if green == True:
                print("Green Terminal Reached")
                break
            

            # print('Action Selected: ', action)
            # print(self.currentState)
            # self.currentState = (0,0)
            # if greenTerminal == True:
            #     print("Green state reached")
            #     break

                
            
        
        # print('Green Terminal Reached')

bruh = RL(5)
# print("Initial Grid: ")
# bruh.drawGrid()
bruh.runEpisode()
# bruh.drawGrid()