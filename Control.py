class Control:

    def __init__(self):

        self.intersections = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 5, 0, 2, 1, 0, 5, 0, 2],
                            [0, 8, 0, 9, 5, 7, 7, 5, 9, 0, 6],
                            [0, 3, 0, 6, 3, 2, 1, 4, 8, 0, 4],
                            [0, 0, 0, 0, 1, 7, 7, 2, 0, 0, 0],
                            [0, 0, 0, 8, 6, 0, 0, 8, 6, 0, 0],
                            [0, 0, 0, 0, 8, 0, 0, 6, 0, 0, 0], 
                            [0, 1, 0, 9, 0, 2, 1, 0, 9, 0, 2],
                            [0, 3, 2, 8, 5, 7, 7, 5, 6, 1, 4],
                            [0, 1, 7, 4, 3, 2, 1, 4, 3, 7, 2],
                            [0, 3, 0, 0, 0, 7, 7, 0, 0, 0, 4]]

        self.px_X = []

        for i in range(0, 547):
            self.px_X.append(-1)

        self.px_X[1] = 1
        self.px_X[39] = 2
        self.px_X[99] = 3
        self.px_X[159] = 4
        self.px_X[217] = 5
        self.px_X[277] = 6
        self.px_X[337] = 7
        self.px_X[397] = 8
        self.px_X[456] = 9
        self.px_X[496] = 10

        self.px_Y = []

        for i in range(0, 547):
            self.px_Y.append(-1)

        self.px_Y[1] = 1
        self.px_Y[71] = 2
        self.px_Y[124] = 3
        self.px_Y[336] = 4
        self.px_Y[389] = 5
        self.px_Y[442] = 6
        self.px_Y[495] = 7

        self.directions = [[], [-1, -2], [-1, 2], [1, -2], [1, 2], [-1, 2, -2], [1, -1, 2], [1, 2, -2], [1, -1, -2], [1, -1, 2, -2]]
        #  1: UP
        # -1: Down
        #  2: Left
        # -2: Rigth