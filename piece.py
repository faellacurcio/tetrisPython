class Piece:
    def __init__(self):
        self.loc = np.matrix([[0,0],[0,1],[1,0],[1,1]])

    def update(self):
        for i in range(self.loc.shape[0]):
            self.loc[i][1] = self.loc[i][1]+1
