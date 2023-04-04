import tkinter as tk


class TkinterGrid:
# Define function to create grid with red colored boxes
    def __init__(self , n:int, redBoxes, greenBox, arrowDic):
        self.size = n
        self.redBoxes = redBoxes
        self.greenBox = greenBox
        self.imagePath = {'up':'up_arrow.png', 'down':'down_arrow.png', 'left':'left_arrow.png','right':'right_arrow.png'}
        self.arrowDic = arrowDic

    def create_grid(self):
        # Create new window
        self.root = tk.Tk()
        # Set title
        self.root.title(f"{self.size} x {self.size} Grid")
        # Set background color
        self.root.configure(background="white")
        # Create n x n grid of labels
    
        # self.img = tk.PhotoImage(file="down_arrow.png")
    
        for i in range(self.size):
            for j in range(self.size):
                # If coordinates match red_boxes, set background to red
                if (i,j) in self.redBoxes:
                    label = tk.Label(self.root, width=4, height=2, bg="red", relief="solid")
                elif (i,j) == self.greenBox:
                    label = tk.Label(self.root, width=4, height=2, bg="green", relief="solid")
                else:
                    # label = tk.Label(self.root, width=4, height=2, bg="white", relief="solid")
                    if self.arrowDic.get((i,j)):
                        # print(self.imagePath[self.arrowDic[(i,j)]])
                        # self.img = tk.PhotoImage(file= self.imagePath[self.arrowDic[(i,j)]])
                        label = tk.Label(self.root, image= tk.PhotoImage(file= self.imagePath[self.arrowDic[(i,j)]]), relief='solid')
                    else:
                        label = tk.Label(self.root, width=4, height=2, bg="white", relief="solid")

                    # label.pack()
                label.grid(row=i, column=j)
        # Run main loop
        self.root.mainloop()

    # def create(self):
    #     self.root.mainloop()

# Get user input for size of grid
# n = int(input("Enter size of grid: "))
# Get user input for coordinates of red boxes
# coordinates = input("Enter coordinates of red boxes (separate each coordinate by comma and use no spaces): ").split(",")
# coordinates = [(2, 4), (2, 5), (2, 6), (2, 7), (2, 9),
#                           (6, 2), (7, 2), (8, 2), (9, 2), (7, 3),
#                           (7, 6), (7, 6), (7, 8),(7,7),
#                           (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)]
# red_boxes = [(int(c[0]), int(c[1])) for c in coordinates]
# Call create_grid function
# create_grid(n, red_boxes)

# grid = TkinterGrid(n, red_boxes, (9,9))
# grid.create_grid()
# grid.create()