import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class ChessPiece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type
    
class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'P')

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'K')

class HexagonalChessboard:
    max_width = 11
    pieces_config = [
        [None, None, None, None, None, ".", None, None, None, None, None],
        [None, None, None, None, ".", None, ".", None, None, None, None],
        [None, None, None, ".", None, ".", None, ".", None, None, None],
        [None, None, ".", None, ".", None, ".", None, ".", None, None],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],

        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."], 

        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [None, None, ".", None, ".", None, ".", None, ".", None, None],
        [None, None, None, ".", None, ".", None, ".", None, None, None],
        [None, None, None, None, ".", None, ".", None, None, None, None],
        [None, None, None, None, None, ".", None, None, None, None, None],
    ]
    pieces = None

    def __init__(self):
        self.pieces = np.empty((len(self.pieces_config), self.max_width), dtype=object)
        self.initialize_board()

    def initialize_board(self):
        for i in range(len(self.pieces_config)):
            for j in range(self.max_width):
                if self.pieces_config[i][j] == ".":
                    self.pieces[i, j] = "."
                else:
                    self.pieces[i, j] = self.pieces_config[i][j]

    def draw_hexagon(self, ax, center, size, color='black'):
        """Draw a hexagon."""
        angles = np.linspace(0, 2*np.pi, 7)
        x = center[0] + size * np.cos(angles)
        y = center[1] + size * np.sin(angles)
        ax.plot(x, y, color="black")
        ax.fill(x, y, color=color)

    def draw_board(self, ax, size):
        colors = ['#CD7F32', '#E5AA70', '#F5DEB3'] 
        row_offsets = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

        for i in range(len(self.pieces_config)):
            for j in range(len(self.pieces_config[0])):
                if isinstance(self.pieces_config[i][j], ChessPiece):
                    if isinstance(self.pieces[i][j], Pawn):
                        print("Pawn says hi")
                    elif isinstance(self.pieces[i][j], King):
                        print("King says hi")
                
                if self.pieces_config[i][j] is not None:
                    x = 3/2 * j * size
                    y = np.sqrt(3) * size * (len(self.pieces_config) - 1 - i)  # Base y-coordinate calculation
                    
                    if i % 2 == 0:  # 
                        y -= np.sqrt(3) * size / 2
                    
                    y += row_offsets[i] * np.sqrt(3) * size
                    
                    color = colors[i % len(colors)]  # Get alternating colors for rows
                    self.draw_hexagon(ax, (x, y), size, color=color)

    def print_board(self):
        for i in range(len(self.pieces_config)):
            for j in range(len(self.pieces_config[0])):
                print("." if self.pieces[i, j] is None else self.pieces[i, j], end=' ')
            print()

    def print_pieces(self):
        for i in range(len(self.pieces)):
            print(self.pieces[i])
if __name__ == "__main__":
    chessboard = HexagonalChessboard()
    chessboard.initialize_board()
    #chessboard.pieces[0, 0] = 'P'  # Example: Place a pawn at (0, 0)
    #chessboard.pieces[1, 1] = 'Q'  # Example: Place a queen at (1, 1)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    size = 1  # Size of each hexagon

    # Draw hexagonal grid and pieces
    chessboard.draw_board(ax, size)

    #chessboard.print_pieces()
    plt.show()

    idea2 = [
        [None, None, None, None, None, ".", None, None, None, None, None],
        [None, None, None, None, ".", None, ".", None, None, None, None],
        [None, None, None, ".", None, ".", None, ".", None, None, None],
        [None, None, ".", None, ".", None, ".", None, ".", None, None],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],

        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."],
        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [".", None, ".", None, ".", None, ".", None, ".", None, "."], 

        [None, ".", None, ".", None, ".", None, ".", None, ".", None],
        [None, None, ".", None, ".", None, ".", None, ".", None, None],
        [None, None, None, ".", None, ".", None, ".", None, None, None],
        [None, None, None, None, ".", None, ".", None, None, None, None],
        [None, None, None, None, None, ".", None, None, None, None, None],
        
    ]