from RL import RL

def main():
    size = 10
    redTerminals = [(2, 4), (2, 5), (2, 6), (2, 7), (2, 9),
                          (6, 2), (7, 2), (8, 2), (9, 2), (7, 3),
                          (7, 6), (7, 6), (7, 8),(7,7),
                          (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)] 
    greenTerminals = [(9,9)]
    agent = RL(size, redTerminals, greenTerminals)
    # agent.drawGrid()
    agent.runEpisode()
    # agent.drawGrid()
    agent.visualizeGrid()

main()