from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

import os
import numpy as np
import pandas as pd

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_PATH, 'mapa.csv')

class Control:

    def __init__(self):

        self.path = []
        self.grid = []

        self.matrix = np.array(pd.io.parsers.read_csv(CSV_FILE, header=None)).astype("int")

        self.grid = Grid(matrix=self.matrix)

        self.finder = AStarFinder() 

        self.intersections = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 10, 5, 10, 2, 1, 10, 5, 10, 2],
                            [0, 8, 10, 9, 5, 7, 7, 5, 9, 10, 6],
                            [0, 3, 10, 6, 3, 2, 1, 4, 8, 10, 4],
                            [0, 0, 0, 11, 1, 7, 7, 2, 11, 0, 0],
                            [0, 0, 0, 8, 6, 0, 0, 8, 6, 0, 0],
                            [0, 0, 0, 11, 8, 10, 10, 6, 11, 0, 0], 
                            [0, 1, 10, 9, 7, 2, 1, 7, 9, 10, 2],
                            [0, 3, 2, 8, 5, 7, 7, 5, 6, 1, 4],
                            [0, 1, 7, 4, 3, 2, 1, 4, 3, 7, 2],
                            [0, 3, 10, 10, 10, 7, 7, 10, 10, 10, 4]]

        self.px_X = []

        for i in range(0, 547):
            self.px_X.append(-1)

        self.px_X[25] = 1
        self.px_X[65] = 2
        self.px_X[124] = 3
        self.px_X[184] = 4
        self.px_X[243] = 5
        self.px_X[303] = 6
        self.px_X[362] = 7
        self.px_X[422] = 8
        self.px_X[481] = 9
        self.px_X[521] = 10

        self.px_Y = []

        for i in range(0, 547):
            self.px_Y.append(-1)

        self.px_Y[25] = 1
        self.px_Y[96] = 2
        self.px_Y[149] = 3
        self.px_Y[202] = 4
        self.px_Y[255] = 5
        self.px_Y[308] = 6
        self.px_Y[361] = 7
        self.px_Y[414] = 8
        self.px_Y[467] = 9
        self.px_Y[520] = 10

        self.directions = [[], [-1, -2], [-1, 2], [1, -2], [1, 2], [-1, 2, -2], [1, -1, 2], [1, 2, -2], [1, -1, -2], [1, -1, 2, -2], [2, -2], [1, -1]]
        #  1: UP
        # -1: Down
        #  2: Left
        # -2: Rigth

    def finding(self, nstart, nend):

        self.grid.cleanup()
        
        start = self.grid.node(nstart[0], nstart[1])
        end = self.grid.node(nend[0], nend[1])
        path, runs = self.finder.find_path(start, end, self.grid)

        return path